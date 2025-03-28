from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("not implemented")

    def props_to_html(self):
        return reduce(lambda acc, prop: acc + f' {prop[0]}="{prop[1]}"', self.props.items(),"")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"       
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("all leafs must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    
class ParentNode(HTMLNode):
    def __init__(self, tag,  children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("parents require tag")
        if not self.children:
            raise ValueError("parents requrie children")
        content = ""
        for child in self.children:
            content += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"

