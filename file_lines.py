import os, sys

def walk(dir_path, ext):
    for root, _, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith(ext):
                full_path = os.path.join(root, file_name)
                print(f"{file_name} contains " + str(lines_count(full_path)) + " lines")

def lines_count(file_path):
    with open(file_path) as f:
        for i, _ in enumerate(f):
            pass
    f.close()
    return i + 1

if __name__ == '__main__':
    dir_path = sys.argv[1]
    extension = sys.argv[2]
    walk(dir_path, extension)