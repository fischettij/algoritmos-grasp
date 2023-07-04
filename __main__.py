from fileinput import filename
import random
from grasp import selection, grasp
from utils import read_graph
import sys

# To execute the code do:
# python3 __main__.py input_files/test_graph_10.txt
# python3 __main__.py test_graph_100.txt 
# python3 __main__.py test_graph_200.txt 
# python3 __main__.py test_graph_1000.txt

if __name__ == "__main__":
    filename = sys.argv[1]
    graph = read_graph(filename)

    # if you want you can change any of the parameters

    # Minimum amount of asixs to take
    min_adjacents = 4
    # Target amount of asixs to take
    target_percent_of_adjacents = 7
    selection_strategy = selection(min_adjacents, target_percent_of_adjacents)
    local_search_time_out = 50

    print(
        f"Parameters: selection(min={min_adjacents}, target % = {target_percent_of_adjacents}), local search time out: {local_search_time_out} ")

"""
    This loop executes grasp multiple times with different number of iterations.
The idea is to compare the results and evaluate the number of iterations necessary to reach a good result.
"""
# executes grasp the summation from 0 to 300 times
for iterations in range(300):
    solution = grasp(graph[0], graph[1], iterations,
                      selection_strategy, local_search_time_out)
    print(iterations, solution.cost)
