




def process(node, result=None):
    if result is None:
        result = []
    for dep in node.deps:
        process(dep, result)
    result.append(node)
    return result