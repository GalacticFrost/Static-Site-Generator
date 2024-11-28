import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode(value='This is just plain text').__repr__()
        node1 = HTMLNode('b', 'This is bold text').__repr__()
        node2 = HTMLNode('a', 'This is a link', None, {'href':'www.boerseunwife.co.za'}).__repr__()

        self.assertEqual(node, 'HTMLNode(None, This is just plain text, children: None, props: None)')
        self.assertEqual(node1, 'HTMLNode(b, This is bold text, children: None, props: None)')
        self.assertEqual(node2, 'HTMLNode(a, This is a link, children: None, props:  href=www.boerseunwife.co.za)')

    def test_props_str(self):
        node = HTMLNode(props={'href':'www.faggot.com', 'target':'bottom'}).props_to_html()
        node1 = HTMLNode(props={'href':'www.faggot.com'}).props_to_html()
        node2 = HTMLNode(props={'href':'www.faggot.com', 'target':'bottom', 'require':'top'}).props_to_html()

        self.assertEqual(node, ' href=www.faggot.com target=bottom')
        self.assertEqual(node1, ' href=www.faggot.com')
        self.assertEqual(node2, ' href=www.faggot.com target=bottom require=top')