def copy_unique_content(input_filename, output_filename):
    """
    Reads a file, removes duplicate lines, and saves to a new file.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            
            # Use a set to automatically handle unique lines
            unique_lines = sorted(list(set(lines)))
            
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)
            
        print(f"Content from '{input_filename}' with duplicates removed has been saved to '{output_filename}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")

# Example usage:
# Create a dummy file with duplicate lines
with open('sample.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 1\n")
    f.write("Line 3\n")
    f.write("Line 2\n")
    
copy_unique_content('sample.txt', 'unique_data.txt')
