from textnode import *

def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)

main()
