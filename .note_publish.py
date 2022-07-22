"""Extract .md files matching certain criteria into a folder for publishing

Required packages:
- frontmatter
- python-frontmatter
"""
import os
from pathlib import Path

import frontmatter as fm

# All paths assume our current working directory is at the root of the obsidian project
SOURCE_FILES = Path("TryHackMe/")
DESTINATION_FOLDER = Path(".publish/content/post/")


def get_published_notes():
    """Generator yielding paths and content of notes that are marked as published"""
    for item in SOURCE_FILES.rglob("*"):
        if item.is_file():
            with open(item) as f:
                note = fm.load(f)
                if note.metadata.get("published", False):
                    print(f"Publishing {item}")
                    # Find the h1 and remove it from the file
                    content_list = note.content.splitlines()
                    title = ""
                    item_to_remove = None
                    for index, line in enumerate(content_list):
                        if line.startswith("# "):
                            title = line.replace("# ", "")
                            item_to_remove = line
                            break
                    if item_to_remove:
                        content_list.remove(item_to_remove)
                    # If no title has been set so we take the h1 from earlier and set it as title
                    if not note.metadata.get("title"):
                        note.metadata["title"] = title
                    note.content = "\n".join(content_list)

                    yield item, note


def run():
    """Run the script"""
    # Ensure our destination folder exists
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    for source_path, note in get_published_notes():
        # Construct the final location for the file in the destination
        destination_file = DESTINATION_FOLDER / str(source_path)

        # Create the destination folder recursively if it is missing
        destination_folder = "/".join(str(destination_file).split("/")[:-1])
        os.makedirs(destination_folder, exist_ok=True)

        # Dump the processed note to the destination
        with open(destination_file, "w+") as destination:
            destination.write(fm.dumps(note))


if __name__ == "__main__":
    run()
