def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modify the content and write to a new file
        with open(output_filename, 'w') as outfile:
            for line in lines:
                modified_line = line.strip() + " - Modified\n"  # Modify the line
                outfile.write(modified_line)

        print(f"Content has been modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")

# Example usage
input_file = "CV.V.rtf"
output_file = "OUTPUT.rtf"
modify_file(input_file, output_file)
