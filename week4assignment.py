

def read_and_modify_file():
    """Challenge 1: Read a file and write a modified version"""
    print("=== File Read & Write Challenge ===")
    
    # Create a sample file first
    original_content = """Python is fun!
File handling is useful.
This is line three.
Learning programming rocks!"""
    
    with open("original.txt", "w") as file:
        file.write(original_content)
    print("Created 'original.txt' for testing")
    
    # Read the file and modify it
    with open("original.txt", "r") as input_file:
        lines = input_file.readlines()
    
    # Modify each line by adding line numbers
    with open("modified.txt", "w") as output_file:
        for i, line in enumerate(lines, 1):
            modified_line = f"Line {i}: {line}"
            output_file.write(modified_line)
    
    print("✅ Created 'modified.txt' with line numbers added!")
    
    # Show both files
    print("\nOriginal file:")
    with open("original.txt", "r") as file:
        print(file.read())
    
    print("\nModified file:")
    with open("modified.txt", "r") as file:
        print(file.read())

def safe_file_reader():
    """Challenge 2: Handle errors when reading files"""
    print("\n=== Error Handling Lab ===")
    
    filename = input("Enter a filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n✅ Successfully read '{filename}':")
            print("-" * 30)
            print(content)
            print("-" * 30)
            
    except FileNotFoundError:
        print(f"❌ Sorry! The file '{filename}' doesn't exist.")
        print("Try 'original.txt' or 'modified.txt' from the first challenge!")
        
    except PermissionError:
        print(f"❌ Permission denied! Can't read '{filename}'.")
        
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

# Main program
if __name__ == "__main__":
    print("🐍 Python File Handling Assignment\n")
    
    # Run both challenges
    read_and_modify_file()
    safe_file_reader()
    
    print("\n🎉 Assignment complete!")