import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
	def test_eq(self):

		node = TextNode("This is a text node", TextType.BOLD)
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode('Url Node', TextType.LINK, 'https://www.cocksucker.com')
		node3 = TextNode('Url Node', TextType.LINK, 'https://www.cocksucker.com')

		self.assertEqual(node, node1)
		self.assertEqual(node2, node3)

	def test_ineq(self):

		node1 = TextNode('TextNode 1', TextType.ITALIC)
		node2 = TextNode('TextNode 2', TextType.ITALIC)
		node3 = TextNode('TextNode 1', TextType.TEXT)
		node4 = TextNode('Textnode 3', TextType.ITALIC)
		node5 = TextNode('Url Node', TextType.LINK, 'https://www.cocksucker.com')
		node6 = TextNode('URL Node', TextType.LINK, 'https://www.cocksucker.com')

		self.assertNotEqual(node1, node2)
		self.assertNotEqual(node1, node3)
		self.assertNotEqual(node2, node4)
		self.assertNotEqual(node5, node6)

	def test_url_ineq(self):

		node = TextNode('Url Node', TextType.LINK)
		node1 = TextNode('Url Node', TextType.LINK, 'https://www.cocksucker.com')

		self.assertNotEqual(node, node1)



if __name__ == "__main__":
    unittest.main()
