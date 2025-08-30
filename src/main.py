from textnode import TextNode, TextNodeType

def main():
    node = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
