from fileinput import filename
import random
from grasp import LocalSearchParameters, selection, grasp
from utils import read_graph
import sys

# To execute the code do:
# python3 __main__.py input_files/test_graph_10.txt 
# python3 __main__.py input_files/test_graph_100.txt >> result.txt 
# python3 __main__.py input_files/test_graph_200.txt >> result.txt

if __name__ == "__main__":
    filename = sys.argv[1]
    graph = read_graph(filename)

    # if you want you can change any of the parameters

    # Minimum amount of asixs to take
    min_adjacents = 4
    # Target amount of asixs to take
    target_percent_of_adjacents = 10
    selection_strategy = selection(min_adjacents, target_percent_of_adjacents)
    nodes_amount = graph[2]
    neighbors_time_out = nodes_amount
    neighborhood_time_out = 100
    neighborhood_witout_improvement_time_out = 20
    grasp_time_out = 2000
    print(
        f"Parameters: Nodes: {nodes_amount}, selection(min={min_adjacents}, target % = {target_percent_of_adjacents}), ls vecinos time out: {neighbors_time_out}, ls vecindario time out: {neighborhood_time_out}, tolerancia de vecindarios sin mejora{neighborhood_witout_improvement_time_out} ")
    
    ls_parameters = LocalSearchParameters(neighbors_time_out, neighborhood_time_out, neighborhood_witout_improvement_time_out)

    grasp(graph[0], graph[1], grasp_time_out,ls_parameters, selection_strategy)