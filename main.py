import re

# Step 1: Read the content of the Markdown file
file_path = "path/to/your/file.md"  # Please replace this path with your actual file path
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # Read the file content line by line

# Step 2: Process line by line to extract level-3 headings and their corresponding text blocks
headings = []
i = 0
while i < len(lines):
    line = lines[i]
    level3_heading_match = re.match(r'###\s*(.*)', line)
    if level3_heading_match:
        heading = level3_heading_match.group(1).strip()
        text_lines = []
        i += 1
        while i < len(lines):
            next_line = lines[i]
            # Check if the next line is any level of heading
            if re.match(r'#{1,6}\s', next_line):
                break
            else:
                text_lines.append(next_line.rstrip())
                i += 1
        heading_text = '\n'.join(text_lines).strip()
        print(f"Third level heading: {heading}")
        print("Text:")
        print(f"{heading_text}\n")
    else:
        i += 1
