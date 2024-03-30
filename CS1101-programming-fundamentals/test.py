try:
    file = open("example.txt", "r")
except FileNotFoundError:
    # If the file is not found
    print("Error: File not found.")
except PermissionError:
    # If there are issues with permissions
    print("Error: Permission denied.")
except Exception as e:
    # Handle any other unexpected errors
    print("An error occurred:", str(e))
# finally:
#     # Close the file regardless of whether an exception occurred or not
#     file.close()
