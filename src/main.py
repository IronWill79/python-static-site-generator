import os
import shutil

from generate_pages_recursive import generate_pages_recursive


def main():
    source = './static'
    dest = './public'
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
