import os
import shutil

from generate_page import generate_page

def main():
    source = './static'
    dest = './public'
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


if __name__ == "__main__":
    main()
