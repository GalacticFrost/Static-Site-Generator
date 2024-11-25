from textnode import *

def main():

    TestNode = TextNode('This is a test', TextType.BOLD)
    TestNode1 = TextNode('Nother test', TextType.LINK, 'http//:www.helpmekaar.co.za')
    TestNode2 = TextNode('This is a test', TextType.BOLD)
    print(TestNode.__eq__(TestNode1))
    print(TestNode.__eq__(TestNode2))
    print(TestNode1)

main()