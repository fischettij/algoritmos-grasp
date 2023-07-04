import random
from re import A
from typing import List, Callable, Tuple

class Solution:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

    def __str__(self):
        return f"{self.road}, {self.cost}"

class IterationInfo:
    def __init__(self):
        self.iteration = 0
        self. greedy_result = 0
        self.local_sarch_result = 0

    def __str__(self):
        return f"{self.iteration}, {self.greedy_result}, {self.local_sarch_result}"

Asix = Tuple[int, int, int]

def selection(minimum, max_percent):
    def funcion_interna(some_list):
        size = len(some_list)
        max_elements = int(size * (max_percent / 100))
        if size < minimum or size < max_elements:
            return some_list
        if max_elements > minimum:
            return some_list[0:max_elements]
        return some_list[0:minimum]

    return funcion_interna


def grasp(matrix: List[List[int]], cost_of_tasks: List[int], iterations: int, selection_strategy: Callable = selection(4, 10), local_search_time_out=10):
    """
    Calculate the Hamiltonian circuit and its cost on the "matrix" graph by adding the cost of "cost_of_tasks"
    Args:
        matrix List[List[int]]: is the adjacency matrix.
        cost_of_tasks List[int]: every position represent the cost of cross that node
        iterations int: is the number of iterations
        selection_strategy : es la funcion que determina cuantos adyacentes al nodo actual tomar para hacer la selección random

    Returns:
        Solution: is the hamiltonian path with its cost
    """
    print(f"grasp_iteration, best_solution_cost")
    best_solution = _greedy(matrix, selection(4, 5))
    best_solution = _local_search(matrix, best_solution, local_search_time_out)
    print(f"0, {best_solution.cost}")
    for i in range(1,iterations):
        solution = _greedy(matrix, selection_strategy)
        solution = _local_search(matrix, solution, local_search_time_out)
        if best_solution.cost > solution.cost:
            best_solution = solution
        print(f"{i}, {best_solution.cost}")
    best_solution.cost = best_solution.cost + sum(cost_of_tasks)
    return best_solution


def _greedy(matrix: List[List[int]], selection_strategy: Callable):
    """
    Creates an hamiltonian path
    Args:
        matrix List[List[int]]: is the adjacency matrix.
        selection_strategy : is the function that determines how many adjacent to the current node to take to make the random selection

    Returns:
        Solution: is the hamiltonian path with its cost
    """
    n = len(matrix)
    cost = 0
    path = []
    visited = [False for i in range(n)]  # Array filled with False of length n
    start_node = 0
    current_node = start_node
    visited[current_node] = True
    path.append(current_node
                )
    for i in range(n-1):
        asixs = _get_adyecents_not_visited(matrix, current_node, visited)
        asix = random.choice(selection_strategy(asixs))
        current_node = asix[1]
        path.append(current_node)
        cost += asix[2]
        visited[current_node] = True

    # add the cost of going from the last element of the list to the first
    cost += matrix[current_node][start_node]

    return Solution(path, cost)


def _get_adyecents_not_visited(matrix, node, visiteds):
    asixs = []
    for i in range(len(matrix)):
        if i != node and (not visiteds[i]):
            asix: Asix = (node, i, matrix[node][i])
            insert_sorted_list(asixs, asix)
    return asixs


def _local_search(m, solution, time_out):
    iterations = 0
    new_solution = solution
    path_length = len(solution.path)
    while iterations < time_out:
        # I switch nodes b and c
        # the path [a, b, c ,d] change to [a, c, b, d] if the lastone is more efficient
        # Considering the example in the comment, I think it's easier to follow the code with those variable names.
        a = solution.path[mod_index(iterations, path_length, -1)]
        b_index = mod_index(iterations, path_length, 0)
        b = solution.path[b_index]
        c_index = mod_index(iterations, path_length, 1)
        c = solution.path[c_index]
        d = solution.path[mod_index(iterations, path_length, 2)]

        # cost of the edges to delete
        previous_cost = m[a][b] + m[c][d]

        # cost of the new edges
        new_cost = m[a][c] + m[b][d]

        # if the new are better, change de road
        if previous_cost > new_cost:
            new_solution.path[c_index] = b
            new_solution.path[b_index] = c
            new_solution.cost = solution.cost - previous_cost + new_cost

        iterations += 1
    return new_solution


def mod_index(index, limit, offset):
    return (index + offset) % limit

# usando divide and conquer
def insert_sorted_list(lst: List[Asix], element: Asix):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid][2] == element[2]:
            lst.insert(mid, element)
            return
        elif lst[mid][2] < element[2]:
            left = mid + 1
        else:
            right = mid - 1
    lst.insert(left, element)
