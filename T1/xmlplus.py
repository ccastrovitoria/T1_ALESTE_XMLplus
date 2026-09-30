class Node:
    def __init__(self):
        self.children = []
        self.values = []


def parse(data):
    it = iter(data)
    return parse_node(it)


def parse_node(it):
    f = next(it)
    n = next(it)

    node = Node()

    for _ in range(f):
        child = parse_node(it)
        node.children.append(child)

    for _ in range(n):
        v = next(it)
        node.values.append(v)

    return node

def count_nodes(node):
    total = 1 

    for child in node.children:
        total = total + count_nodes(child)

    return total

def height (node):
    if not node.children:
        return 1

    max_height = 0
    for child in node.children:
        if max_height < height(child):
            max_height = height(child)

    return 1 + max_height

def sum_values(node):
    total = sum(node.values)

    for child in node.children:
        total = total + sum_values(child)

    return total

def generate_dot(root, filename):
    lines = ["digraph G {"]
    counter = [0]

    def visit(node):
        node_id = counter[0]
        counter[0] += 1

        values = ", ".join(map(str, node.values))
        lines.append(f'    n{node_id} [label="{values}"];')

        for child in node.children:
            child_id = visit(child)
            lines.append(f"    n{node_id} -> n{child_id};")

        return node_id

    visit(root)

    lines.append("}")

    with open(filename, "w") as f:
        f.write("\n".join(lines))