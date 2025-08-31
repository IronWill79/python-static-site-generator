class HTMLNode():
    def __init__(self, tag = None, val = None, children = None, props = None):
        self.tag = tag
        self.value = val
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, val, props = None):
        super().__init__(tag, val, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        result = f'<{self.tag}>'
        for child in self.children:
            result += child.to_html()
        result += f'</{self.tag}>'
        return result
