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

    nodes_amount = graph[2]
    grasp_time_out = 300
    print(
        f"Parameters: Nodes: {nodes_amount}, selection(min={min_adjacents}, target % = {target_percent_of_adjacents}), grasp time out: {grasp_time_out}, local search time out: {local_search_time_out}")

    grasp(graph[0], graph[1], grasp_time_out,selection_strategy, local_search_time_out)