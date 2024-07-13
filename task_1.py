import argparse
import shutil
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(description="Image sorting script")
    parser.add_argument("-S", "--source", type=Path, required=True, help="Images directory")
    parser.add_argument("-O", "--output", type=Path, default=Path("output"), help="Sorted images directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    return parser.parse_args()

def sort_images(src: Path, dst: Path, verbose: bool):
    for item in src.iterdir():
        if item.is_dir():
            sort_images(item, dst / item.name, verbose)
        else:
            file_extension = item.suffix.lower()[1:]
            folder = dst / file_extension
            folder.mkdir(parents=True, exist_ok=True)
            if verbose:
                print(f"Copying {item} to {folder}")
            shutil.copy2(item, folder)

def main():
    args = get_args()
    sort_images(args.source, args.output, args.verbose)

if __name__ == "__main__":
    main()