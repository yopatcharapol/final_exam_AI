from pathlib import Path

# Change this to the folder you want to process
folder = Path(r".")

# Rename files recursively
for file_path in folder.rglob("lab*"):
    if file_path.is_file() and file_path.suffix.lower() == ".txt" and file_path.suffix.lower() != ".xlsx":
        new_path = file_path.with_suffix(".py")

        # Avoid renaming if it's already .txt
        if file_path.suffix.lower() != ".py":
            try:
                print(f"{file_path}  ->  {new_path}")
                file_path.rename(new_path)
            except OSError as e:
                print(f"Error occurred while renaming {file_path}: {e}")        

print("Done!")