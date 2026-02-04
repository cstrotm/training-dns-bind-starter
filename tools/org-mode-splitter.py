import os
import argparse

def sanitize_filename(title):
    # Keep only alphanumeric chars, replace others with underscore
    chars = [c if c.isalnum() else '_' for c in title]
    # Join and clean up consecutive/trailing underscores
    clean_name = ''.join(chars)
    while '__' in clean_name:
        clean_name = clean_name.replace('__', '_')
    return clean_name.strip('_')

def split_org_file(input_filename):
    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} not found.")
        return

    current_filename = None
    current_content = []

    with open(input_filename, 'r', encoding='utf-8') as f:
        for line in f:
            # Detect top-level heading: line starts with '* '
            if line.startswith('* '):
                # Save previous section if it exists
                if current_filename and current_content:
                    with open(current_filename, 'w', encoding='utf-8') as out:
                        out.writelines(current_content)

                # Setup new section
                heading_text = line[2:].strip()
                current_filename = f"{sanitize_filename(heading_text)}.TXT"
                current_content = [line]
                print(f"Processing: {current_filename}")
            else:
                # Accumulate content for the current section
                if current_filename is not None:
                    current_content.append(line)

        # Write the final section after the loop ends
        if current_filename and current_content:
            with open(current_filename, 'w', encoding='utf-8') as out:
                out.writelines(current_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split Org file using basic string operations.")
    parser.add_argument("filename", help="Path to the .org file")
    args = parser.parse_args()
    split_org_file(args.filename)
