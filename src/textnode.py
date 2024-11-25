from enum import Enum

class TextType(Enum):
	TEXT = 'text'
	BOLD = 'bold'
	ITALIC = 'italic'
	CODE = 'code'
	LINK = 'link'
	IMAGE = 'image'

class TextNode():
	
	def __init__(self, content, text_type, url = None):
		self.text = content
		self.text_type = text_type
		self.url = url
		
	def __eq__(self, textnode_object):
		if self.text == textnode_object.text:
			if self.text_type == textnode_object.text_type:
				if self.url == textnode_object.url:
					return True
		return False

	def __repr__(self):
		return f'TextNode({self.text}, {self.text_type.value}, {self.url})'