import os
import shutil
import sys
from pathlib import Path

def copy_files_recursively(source_dir, dest_dir='dist'):
    try:
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)
        
        if not source_path.exists():
            print(f"Error: Source directory '{source_dir}' does not exist!")
            return
        
        if not source_path.is_dir():
            print(f"Error: '{source_dir}' is not a directory!")
            return
        
        dest_path. mkdir(parents=True, exist_ok=True)
        
        process_directory(source_path, dest_path)
        
        print(f"\nSuccess! Files copied from '{source_dir}' to '{dest_dir}'")
        print(f"Files organized by extension in '{dest_dir}'")
        
    except Exception as e: 
        print(f"An error occurred: {e}")

def process_directory(source_dir, dest_dir):
    try:
        # Iterate via all the items in the directory
        for item in source_dir.iterdir():
            try:
                if item.is_dir():
                    print(f"Processing directory: {item}")
                    process_directory(item, dest_dir)
                    
                elif item.is_file():
                    copy_file(item, dest_dir)
                    
            except PermissionError:
                print(f"Permission denied: {item}")
            except Exception as e:
                print(f"Error processing {item}:  {e}")
                
    except PermissionError:
        print(f"Permission denied: Cannot access {source_dir}")
    except Exception as e:
        print(f"Error reading directory {source_dir}: {e}")

def copy_file(file_path, dest_dir):
    try: 
        extension = file_path.suffix[1:] if file_path. suffix else 'no_extension'
        
        extension_dir = dest_dir / extension
        extension_dir.mkdir(parents=True, exist_ok=True)
        
        dest_file = extension_dir / file_path. name
        
        shutil.copy2(file_path, dest_file)
        print(f"Copied: {file_path} → {dest_file}")
        
    except PermissionError:
        print(f"Permission denied: Cannot copy {file_path}")
    except Exception as e:
        print(f"Error copying {file_path}: {e}")

def main():

    if len(sys.argv) < 2:
        print("Usage: python task1.py <source_directory> [destination_directory]")
        print("Example: python task1.py ./test_folder ./dist")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'
    
    print(f"Source directory: {source_dir}")
    print(f"Destination directory: {dest_dir}")
    print("-" * 50)
    
    copy_files_recursively(source_dir, dest_dir)

if __name__ == "__main__": 
    main()