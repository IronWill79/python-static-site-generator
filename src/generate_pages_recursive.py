import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        if os.path.isdir(os.path.join(dir_path_content, file)):
            generate_pages_recursive(
                os.path.join(dir_path_content, file),
                template_path,
                os.path.join(dest_dir_path, file)
            )
        else:
            generate_page(
                os.path.join(dir_path_content, file),
                template_path,
                os.path.join(dest_dir_path, file.replace(".md", ".html"))
            )
