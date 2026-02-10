# Copyright 2026 Michael Ryan Hunsaker, M.Ed., Ph.D.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import re
from pathlib import Path

# Define projects with metadata
projects = {
    "Customizable-Braille-Print-Keyring": {
        "title": "Customizable Braille Print Keyring",
        "short_description": "Portable braille identification keyring for personalization",
        "long_description": "A customizable keyring with braille labeling that allows users to identify keys and personal items by touch. Perfect for organizing keys with tactile feedback.",
        "categories": ["visual impairments"],
        "tags": ["braille", "daily-living", "adaptive-tools", "identification"],
        "images": ["Customizable-Braille0Print-Keyring.jpg"]
    },
    "Laptop-Stand-2": {
        "title": "Laptop Stand 2",
        "short_description": "Ergonomic adjustable laptop stand for enhanced viewing",
        "long_description": "An improved ergonomic laptop stand with adjustable angles for comfortable laptop positioning and better accessibility for extended use.",
        "categories": ["visual impairments"],
        "tags": ["ergonomics", "daily-living", "low-vision", "adaptive-tools"],
        "images": ["Laptop-Stand-2.jpeg", "Laptop-Stand-2-1.jpeg"]
    },
    "Orientation-Mobility-Intercestions": {
        "title": "Orientation and Mobility Intersections",
        "short_description": "Tactile intersection model for O&M training",
        "long_description": "A 3D tactile model representing street intersections for orientation and mobility training. Helps users understand traffic patterns and navigation through touch.",
        "categories": ["orientation and mobility"],
        "tags": ["orientation-mobility", "navigation", "tactile", "training"],
        "images": ["Orientation-Mobility-Intersections.jpeg"]
    },
    "Orientation-Mobility-Route-Shapes": {
        "title": "Orientation and Mobility Route Shapes",
        "short_description": "Tactile route shape models for O&M instruction",
        "long_description": "Educational tactile models of various route shapes and patterns for orientation and mobility instruction. Helps students understand different navigation routes through touch.",
        "categories": ["orientation and mobility"],
        "tags": ["orientation-mobility", "navigation", "tactile", "education"],
        "images": ["Orientation-Mobility-Route-Shapes.jpeg"]
    },
    "Project-Core-3D-Symbols": {
        "title": "Project Core 3D Symbols",
        "short_description": "3D tactile symbols for core curriculum concepts",
        "long_description": "A set of 3D tactile symbols representing core educational concepts and ideas. Provides visual-tactile learning aids for science and language arts curriculum.",
        "categories": ["visual impairments"],
        "tags": ["education", "symbols", "tactile", "curriculum"],
        "images": ["Project_Core-3D-Symbols.jpeg"]
    },
    "TODOList-1": {
        "title": "TODO List 1",
        "short_description": "Adaptive task organization and tracking tool",
        "long_description": "An organizational tool for managing daily tasks and to-do items with tactile feedback for organization and planning.",
        "categories": ["occupational therapy"],
        "tags": ["organization", "daily-living", "adaptive-tools", "planning"],
        "images": ["IMG_0062.jpeg"]
    },
    "TODOList-2": {
        "title": "TODO List 2",
        "short_description": "Enhanced task tracking and management system",
        "long_description": "An improved task management system with better tactile organization and labeling for daily task planning.",
        "categories": ["occupational therapy"],
        "tags": ["organization", "daily-living", "adaptive-tools", "planning"],
        "images": ["IMG_0061.jpeg"]
    },
    "Traditional-Soroban": {
        "title": "Traditional Soroban",
        "short_description": "Japanese abacus for mathematical calculations",
        "long_description": "A traditional Soroban (Japanese abacus) adapted for tactile learning. Excellent for teaching arithmetic and mathematical concepts through touch.",
        "categories": ["visual impairments"],
        "tags": ["braille", "math", "abacus", "arithmetic"],
        "images": ["IMG_0044.jpeg"]
    }
}

staging_root = "Staging"

# Process each project
for project_name, metadata in projects.items():
    project_path = Path(staging_root) / project_name
    template_file = project_path / "template.md"
    
    if not template_file.exists():
        print(f"⚠ {project_name}: template.md not found")
        continue
    
    # Generate slug for filename
    slug = project_name.lower().replace(" ", "-")
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    
    # Generate SKU with category suffixes
    category_suffixes = {
        "visual impairments": "-VIS",
        "occupational therapy": "-OT",
        "physical therapy": "-PT",
        "speech language pathology": "-SLP",
        "orientation and mobility": "-OM",
        "miscellaneous": "-MISC"
    }
    
    sku_parts = [slug]
    for cat in metadata["categories"]:
        sku_parts.append(category_suffixes.get(cat, ""))
    sku = "".join(sku_parts).upper()
    
    # Read template
    with open(template_file, 'r') as f:
        template_content = f.read()
    
    # Replace placeholders
    new_content = template_content
    new_content = new_content.replace("$Template", metadata["title"])
    new_content = new_content.replace("$SKU", sku)
    new_content = new_content.replace("$Short_Description", metadata["short_description"])
    new_content = new_content.replace("$Long_Description", metadata["long_description"])
    
    # Handle images - replace first image reference and add others
    first_image = metadata["images"][0]
    new_content = new_content.replace("$Photo", first_image)
    new_content = new_content.replace("$Photo_Title", metadata["title"])
    
    # Add additional images if they exist
    if len(metadata["images"]) > 1:
        image_lines = [f'![]({img.replace("assets/images/prints/", "")}):' for img in metadata["images"]]
        image_markdown = "\n".join([f'![{metadata["title"]}](/assets/images/prints/{img}):' .full style="max-width: 600px;"}' for img in metadata["images"]])
        # Find the first image line and replace
        first_image_pattern = rf'!\[{re.escape(metadata["title"])}\]\(/assets/images/prints/{re.escape(first_image)}\):' .full style="max-width: 600px;"}' 
        # Insert additional images after first
        insertion_point = new_content.find(f'![{metadata["title"]}](/assets/images/prints/{first_image})')
        if insertion_point != -1:
            end_of_first_image = new_content.find('"}', insertion_point) + 2
            additional_images = "\n".join([f'![{metadata["title"]}](/assets/images/prints/{img}):' .full style="max-width: 600px;"}' for img in metadata["images"][1:]])
            new_content = new_content[:end_of_first_image] + "\n\n" + additional_images + new_content[end_of_first_image:]
    
    # Replace categories
    categories_yaml = "categories:\n"
    for cat in metadata["categories"]:
        categories_yaml += f"  - {cat}\n"
    
    new_content = re.sub(r'categories:\s*- accessibility', categories_yaml.rstrip(), new_content)
    
    # Replace tags
    tags_yaml = "tags:\n"
    for tag in metadata["tags"]:
        tags_yaml += f"  - {tag}\n"
    
    old_tags = re.search(r'tags:.*?(?=\n[a-z])', new_content, re.DOTALL)
    if old_tags:
        new_content = new_content[:old_tags.start()] + tags_yaml.rstrip() + new_content[old_tags.end():]
    
    # Write to _prints
    output_file = Path("_prints") / f"{slug}.md"
    with open(output_file, 'w') as f:
        f.write(new_content)
    
    print(f"✓ {project_name} → {output_file.name} (SKU: {sku})")
    
    # Copy images
    for img_file in metadata["images"]:
        src = project_path / img_file
        dst = Path("assets/images/prints") / img_file
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            import shutil
            shutil.copy2(src, dst)
            print(f"  ✓ Copied image: {img_file}")

print("\n✓ All projects processed!")