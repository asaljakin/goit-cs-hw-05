import os
import shutil
import asyncio
import argparse

async def read_folder(source):
    files = []
    for root, _, filenames in os.walk(source):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

async def copy_file(source_file, output):
    try:
        extension = os.path.splitext(source_file)[1]
        destination_folder = os.path.join(output, extension[1:])
        os.makedirs(destination_folder, exist_ok=True)
        shutil.copy(source_file, destination_folder)
        print(f"Successfully copied {source_file} to {destination_folder}")
    except Exception as e:
        print(f"Error copying {source_file}: {str(e)}")

async def main(source_folder, output_folder):
    files = await read_folder(source_folder)
    tasks = [copy_file(file, output_folder) for file in files]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async file sorting script")
    parser.add_argument("--source", type=str, default="./source", help="Source folder path")
    parser.add_argument("--output", type=str, default="./output", help="Output folder path")
    args = parser.parse_args()

    asyncio.run(main(args.source, args.output))