def main():
    # Ask the user for the filename to read
    input_filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nFile read successfully!")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
        return

    except IOError:
        print(f"❌ Error: Could not read the file '{input_filename}'.")
        return

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Define the output filename
    output_filename = "modified_" + input_filename

    try:
        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"\n✅ Modified content written to '{output_filename}'.")

    except IOError:
        print(f"❌ Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()
