import unittest
from block_converter import markdown_to_blocks
from block_func import block_to_block_type
from blocknode import BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_empty(self):
        md = """
            """
        blocks= markdown_to_blocks(md)
        self.assertEqual([],blocks)
    

    def test_markdown_to_blocks_oneline(self):
        md = """
        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
        )

    def test_block_to_blocktype(self):
        block = "- This is a list\n- with items"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)
        
    def test_block_to_blocktype_heading(self):
        block = "### This is a Heading"        
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)


    def test_block_to_blocktype_code(self):
        block = "```let message = 'Hello world';\nalert(message);```"        
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)
        

    def test_block_to_blocktype_orderedlist(self):
        block = "1. This is a list\n2. with items"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_block_to_blocktype_quote(self):
        block = ">This is a list\n>with items"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)
    
    def test_block_to_blocktype_paragraph(self):
        block = "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)


    def test_block_to_blocktype_empty(self):
        block = ""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

if __name__ == "__main__":
    unittest.main()