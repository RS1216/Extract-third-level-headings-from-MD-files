import re

class MarkdownProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headings = []
        self.no_heading_flag = True  # Flag to check if any level-3 headings are found

    def read_file(self):
        """Reads the content of the Markdown file."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def process_lines(self, lines):
        """Processes the lines to extract level-3 headings and their corresponding text blocks."""
        i = 0
        while i < len(lines):
            line = lines[i]
            level3_heading_match = re.match(r'###\s*(.*)', line)

            if level3_heading_match:
                self.no_heading_flag = False  # Set the flag to False if a level-3 heading is found
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

                # Combine short paragraphs
                heading_text = self.merge_short_paragraphs(text_lines).strip()
                if not heading_text:
                    heading_text = "No content under this heading."
                self.headings.append((heading, heading_text))
            else:
                i += 1

        if self.no_heading_flag:
            print("No level-3 headings found in the document.")

    def merge_short_paragraphs(self, text_lines, min_length=50):
        """Merges paragraphs if individual segments are too short."""
        combined_text = []
        temp_paragraph = []

        for line in text_lines:
            if line.strip():
                temp_paragraph.append(line)
            else:
                if sum(len(p) for p in temp_paragraph) < min_length:
                    combined_text.append(' '.join(temp_paragraph))
                else:
                    combined_text.append('\n'.join(temp_paragraph))
                temp_paragraph = []

        if temp_paragraph:
            if sum(len(p) for p in temp_paragraph) < min_length:
                combined_text.append(' '.join(temp_paragraph))
            else:
                combined_text.append('\n'.join(temp_paragraph))

        return '\n'.join(combined_text)

    def display_results(self):
        """Displays the extracted headings and their text."""
        if self.headings:
            for heading, text in self.headings:
                print(f"Third level heading: {heading}")
                print("Text:")
                print(f"{text}\n")
        else:
            print("No level-3 headings or content to display.")

# Usage example
if __name__ == "__main__":
    file_path = "path/to/your/file.md"  # Please replace this path with your actual file path
    processor = MarkdownProcessor(file_path)
    lines = processor.read_file()
    processor.process_lines(lines)
    processor.display_results()
