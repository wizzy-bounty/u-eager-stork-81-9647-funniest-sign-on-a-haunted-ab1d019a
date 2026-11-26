import os

def main():
    line = "WARNING: DO NOT GIVE THE GHOST ROOT ACCESS. IT REBOOTS RACK 4 FOR ATTENTION."
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "entry.txt"), "wb") as entry_file:
        entry_file.write(line.encode("utf-8"))


if __name__ == "__main__":
    main()
