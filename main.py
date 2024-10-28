import re

# Step 1: Read the content of the Markdown file
file_path = "path/to/your/file.md"  # Path to the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()  # Read the entire file content

# Step 2: Use regular expressions to extract all level-3 headings
headings = re.findall(r'^###\s*(.*)', content, re.MULTILINE)  # Find all lines starting with "### "

# Step 3: Check if any level-3 headings were found
if not headings:
    print("No level-3 headings found.")
else:
    print("Extracted level-3 headings:", headings)
