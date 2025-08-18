### **Repository 6: Markdown to HTML Converter**
```python
# Repository: python-markdown-to-html
# Description: Convert Markdown files to HTML.

import markdown

def convert_markdown_to_html(file_path, template=None):
    with open(file_path, 'r') as file:
        text = file.read()
        html = markdown.markdown(text)
        if template:
            with open(template, 'r') as tpl:
                html = tpl.read().replace('{{content}}', html)
        output_path = file_path.replace('.md', '.html')
        with open(output_path, 'w') as output_file:
            output_file.write(html)
        print(f"HTML file saved to {output_path}")

def batch_convert(directory, template=None):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            convert_markdown_to_html(os.path.join(directory, filename), template)
# Example usage
convert_markdown_to_html("example.md")
