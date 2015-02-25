__author__ = 'artem'

nodes = {}
files = []

for filenum in range(100):
    filename = 'file_00' + str(filenum)
    files.append(filename)

for node in range(10):
    subset = files[0:10]
    nodes[node] = subset
    files[0:10] = []

for node in nodes:
    print(node, nodes[node])
