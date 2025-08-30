from textnode import TextNode, TextNodeTypes

def main():
    node = TextNode("This is some anchor text", TextNodeTypes.LINK, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
