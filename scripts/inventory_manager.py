#!/usr/bin/env python3
"""
Utility to manage inventory.json and SKU generation for DSD3D Print Ordering system.
"""

import json
from pathlib import Path

INVENTORY_FILE = Path(__file__).parent.parent / "Inventory" / "inventory.json"

class PrintInventory:
    def __init__(self, inventory_path=INVENTORY_FILE):
        self.inventory_path = inventory_path
        self.data = self._load()
    
    def _load(self):
        """Load inventory from JSON file."""
        if self.inventory_path.exists():
            with open(self.inventory_path, 'r') as f:
                return json.load(f)
        return {"projects": [], "next_prt_number": 1, "metadata": {}}
    
    def save(self):
        """Save inventory to JSON file."""
        self.inventory_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.inventory_path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_next_sku(self, categories):
        """
        Generate the next SKU based on categories.
        
        Args:
            categories: List of category strings (e.g., ["visual impairments", "occupational therapy"])
        
        Returns:
            str: SKU in format PRT-XXXXX-SUFFIX1-SUFFIX2...
        """
        category_suffixes = {
            "visual impairments": "VIS",
            "occupational therapy": "OT",
            "physical therapy": "PT",
            "speech language pathology": "SLP",
            "orientation and mobility": "OM",
            "miscellaneous": "MISC"
        }
        
        next_number = self.data.get("next_prt_number", 1)
        prt_base = f"PRT-{next_number:05d}"
        
        # Add category suffixes in order
        suffixes = []
        for cat in categories:
            if cat in category_suffixes:
                suffixes.append(category_suffixes[cat])
        
        if suffixes:
            sku = f"{prt_base}-{'-'.join(suffixes)}"
        else:
            sku = prt_base
        
        return sku
    
    def add_project(self, title, sku, categories, tags):
        """
        Add a new project to inventory.
        
        Args:
            title: Project title
            sku: Generated SKU
            categories: List of categories
            tags: List of tags
        """
        prt_number = self.data.get("next_prt_number", 1)
        
        project = {
            "prt_number": prt_number,
            "title": title,
            "sku": sku,
            "categories": categories,
            "tags": tags
        }
        
        self.data["projects"].append(project)
        self.data["next_prt_number"] = prt_number + 1
        self.data["metadata"]["total_projects"] = len(self.data["projects"])
        
        self.save()
        return project
    
    def get_project_by_sku(self, sku):
        """Lookup project by SKU."""
        for proj in self.data.get("projects", []):
            if proj["sku"] == sku:
                return proj
        return None
    
    def list_projects(self):
        """Return all projects."""
        return self.data.get("projects", [])


if __name__ == "__main__":
    # Example usage
    inv = PrintInventory()
    print(f"Inventory has {len(inv.list_projects())} projects")
    print(f"Next PRT number: {inv.data.get('next_prt_number')}")
    
    # Example: Generate SKU for new project
    example_categories = ["visual impairments", "occupational therapy"]
    example_sku = inv.get_next_sku(example_categories)
    print(f"\nExample SKU for {example_categories}: {example_sku}")
