import os
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

def copy_file(from_, to_):
    try:
        if not os.path.exists(to_):
            os.makedirs(to_)
        shutil.copy2(from_, to_)
    except Exception as e:
        print(f"Failed copiyng from {from_} to {to_}")

def processing_file(from_, to_):
    tasks = []
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        for root, folders, files in os.walk(to_):
            for file in files:
                file_path = os.path.join(root, file)
                extension = file.split('.')[-1]
                dest_path = os.path.join(to_, extension)
                tasks.append((file_path, dest_path))

    future_tasks = {executor.submit(copy_file, task): task for task in tasks}

    for future in as_completed(future_tasks):
        try:
            future.result()
        except Exception as e:
            from_, to_ = future_tasks[future]
            print(f"Error processing {from_} to {to_}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python folders.py <source_directory> [<destination_directory>]")
        sys.exit(1)

    from_ = sys.argv[1]
    to_ = sys.argv[2] if len(sys.argv) > 2 else "new_folder"

    if not os.path.exists(from_):
        print(f"Source directory '{from_}' does not exist.")
        sys.exit(1)

    processing_file(from_, to_)
    print(f"Files have been copied and sorted by extensions in '{to_}'")






