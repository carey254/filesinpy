def read_file_with_error_handling():
    filename = input("Please enter the filename to read:")

    try:
       
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: The file {filename} could not be read due to an IO issue.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_file_with_error_handling()
