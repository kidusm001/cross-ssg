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