
from textnode import TextType, TextNode



def main():
    dummyTextNode = TextNode("This is some anchor text", TextType.LINK, "url.com")

    print(dummyTextNode)


if __name__ == "__main__":
    main()