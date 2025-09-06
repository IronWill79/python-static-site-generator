import os
import shutil
import sys

from generate_pages_recursive import generate_pages_recursive


def main():
    basepath = "/"
    if sys.argv[1]:
        basepath = sys.argv[1]
    source = './static'
    dest = './docs'
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    generate_pages_recursive("./content", "./template.html", dest, basepath)


if __name__ == "__main__":
    main()
