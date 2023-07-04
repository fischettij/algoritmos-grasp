
import random
from typing import List

def read_graph(filename):
    with open(filename) as f:
        matrix = []         #Lista que contiene cada fila
        num_rows = int(f.readline())
        for row_index in range(num_rows):
            line = f.readline()
            row = [int(x) for x in line.split()] # Split en whitespace y castear cada elemento a int
            matrix.append(row)
        tasks = f.readline()
        tasks = [int(x) for x in tasks.split()]
    return (matrix,tasks,num_rows)

def write_graph(filename, nodes):
    matrix = [[str(0) for x in range(nodes)] for y in range(nodes)]
    for i in range(0, nodes):
        for j in range (i+1, nodes):
            value = str(random.randint(1, 1000)) 
            matrix[i][j] = value
            matrix[j][i] = value

    matrix = map(lambda row: ' '.join(row), matrix)

    tasks = [str(random.randint(1, 100)) for y in range(nodes)]
    tasks = ' '.join(tasks)

    graph_file = open(filename,"w")
    graph_file.write(str(nodes) + "\n")
    for row in matrix:
        graph_file.write(row + "\n")
    graph_file.write(tasks)
    graph_file.close()

write_graph("./input_files/test_graph_500.txt",500)

def create_matrix(n: int) -> List[List[int]]:
# create_matrix returns a simetric matrix of n x n with diagonal with 0
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            elif i < j:
                elemento = random.randint(1, 100)
                row.append(elemento)
            else:
                row.append(matrix[j][i])
        matrix.append(row)
    return matrix