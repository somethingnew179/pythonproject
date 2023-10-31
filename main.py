import argparse
from commands import show_python_version, create_directory, list_files_and_folders

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command", type=int)
    parser.add_argument("directory_name", nargs="?")

    args = parser.parse_args()

    if args.command == 1:
        show_python_version()
    elif args.command == 2:
        create_directory(args.directory_name)
    elif args.command == 3:
        list_files_and_folders()

if __name__ == "__main__":
    main()
