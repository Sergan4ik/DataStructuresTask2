class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def decode(node, code):
    res = ""
    cur_node = node
    for c in code:
        if type(cur_node) is str:
            res += cur_node
            cur_node = node

        if c == '0':
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right

    return res


# Calculating frequency
freq = {
    "A": 8,
    "O": 26,
    "Y": 24,
    "B": 12,
    "V": 26,
    "D": 26,
    "M": 11,
    "N": 12,
    "P": 30,
    "T": 28,
}

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

text = "DOBPOBYTDOMA"
code = ""
for c in text:
    code += huffmanCode[c]

to_decode = "010111001001101100111110110"

print(f'Code for {text}')
print(code)

print(f'Decode for {to_decode}')
print(decode(nodes[0][0], to_decode))



