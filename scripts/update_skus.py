#!/usr/bin/env python3
"""
Update all SKUs in _prints files to match the new PRT-XXXXX-SUFFIX format.
Reads from Inventory/inventory.json to get the correct SKUs.
"""

import json
import re
from pathlib import Path

INVENTORY_FILE = Path(__file__).parent.parent / "Inventory" / "inventory.json"
PRINTS_DIR = Path(__file__).parent.parent / "_prints"

def load_inventory():
    """Load inventory from JSON."""
    with open(INVENTORY_FILE, 'r') as f:
        return json.load(f)

def get_sku_map():
    """Create a mapping of file titles to SKUs from inventory."""
    inventory = load_inventory()
    sku_map = {}
    for project in inventory.get("projects", []):
        title = project.get("title", "").lower()
        sku_map[title] = project.get("sku")
    return sku_map

def slugify(text):
    """Convert text to slug format."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text

def update_file_sku(file_path, sku_map):
    """Update SKU in a single markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if not title_match:
        return False, "No title found"
    
    title = title_match.group(1).strip()
    title_lower = title.lower()
    
    # Find matching SKU
    sku = sku_map.get(title_lower)
    if not sku:
        # Try to find by filename
        filename_slug = file_path.stem
        for t, s in sku_map.items():
            if slugify(t) == filename_slug:
                sku = s
                break
    
    if not sku:
        return False, f"No SKU found for title: {title}"
    
    # Replace SKU in file
    old_sku_pattern = r'^sku:\s*["\']?[^"\'\n]+["\']?'
    new_sku_line = f'sku: "{sku}"'
    
    updated_content = re.sub(old_sku_pattern, new_sku_line, content, flags=re.MULTILINE)
    
    if updated_content != content:
        with open(file_path, 'w') as f:
            f.write(updated_content)
        return True, f"Updated: {sku}"
    else:
        return False, "No changes needed"

def main():
    """Update all SKUs in _prints files."""
    if not INVENTORY_FILE.exists():
        print("❌ Inventory file not found!")
        return
    
    if not PRINTS_DIR.exists():
        print("❌ _prints directory not found!")
        return
    
    sku_map = get_sku_map()
    print(f"Loaded {len(sku_map)} SKUs from inventory\n")
    
    md_files = sorted(PRINTS_DIR.glob("*.md"))
    success_count = 0
    
    for md_file in md_files:
        success, message = update_file_sku(md_file, sku_map)
        status = "✓" if success else "⚠"
        print(f"{status} {md_file.name}: {message}")
        if success:
            success_count += 1
    
    print(f"\n✓ Updated {success_count}/{len(md_files)} files")

if __name__ == "__main__":
    main()
