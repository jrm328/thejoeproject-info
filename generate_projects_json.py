import os
import glob
import yaml
import json

PROJECTS_DIR = 'docs/projects'
OUTPUT_JSON = 'docs/assets/projects.json'
SITE_URL = 'https://thejoeproject.info/projects/'

projects = []

for filepath in glob.glob(os.path.join(PROJECTS_DIR, '*.md')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        parts = content.split('---')
        frontmatter = yaml.safe_load(parts[1])
        filename = os.path.basename(filepath).replace('.md', '')
        
        project = {
            'title': frontmatter.get('title', filename),
            'summary': frontmatter.get('summary', ''),
            'thumbnail': frontmatter.get('thumbnail', 'https://placehold.co/400x200'),
            'slug': filename,
            'url': f"{SITE_URL}{filename}/"
        }
        projects.append(project)

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(projects, f, indent=2)

print(f"Generated {OUTPUT_JSON} with {len(projects)} projects.")
