try:
    # Ask user for the file to read
    infile = input("Enter the name of the file to read: ")

    # Open and read content
    with open(infile, "r") as f:
        content = f.readlines()

    # Modify: add line numbers
    modified = [f"{i+1}: {line}" for i, line in enumerate(content)]

    # Write to new file
    outfile = "modified_" + infile
    with open(outfile, "w") as f:
        f.writelines(modified)

    print(f"🎉 File successfully modified and saved as '{outfile}'")

except FileNotFoundError:
    print("⚠️ The file you entered does not exist. Please check and try again.")
except PermissionError:
    print("⚠️ You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ Something went wrong: {e}")
