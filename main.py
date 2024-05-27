import math
import pandas as pd
import numpy as np
from algorithms import dijsktra, bellman_ford, floyd_warshall
import utils.compile_path as utils
def prepare_data():

    nodes = pd.read_csv('data/nodes.csv')

    nodemap = {}
    for index, row in nodes.iterrows():
        # print(row['lat'], row['lon'], index)
        nodemap[str(round(row['id']))] = [row['lat'], row['lon']]

    edges = pd.read_csv('data/edges.csv')

    aM = np.zeros((len(nodemap)+2, len(nodemap)+2))
    for index, row in edges.iterrows():
        aM[row['from']][row['to']] = row['dis']
        aM[row['to']][row['from']] = row['dis']

    print('adjency matrix is ready')
    return aM, nodemap
import sys

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <arg1> <arg2>")
        return

    # Access arguments (they are strings by default)
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Convert arguments to integers (if needed)
    start = int(arg1)
    end = int(arg2)
    
    aM, nodemap = prepare_data()

    d_path = dijsktra.solve_dijsktra(aM, start, end)
    d_pathdf = utils.compile_rows(nodemap, d_path, start, end, 'dijsktra')

    b_path = bellman_ford.solve_bellman_ford(aM, start, end)
    b_pathdf = utils.compile_rows(nodemap, b_path, start, end, 'bellman_ford')

    f_path = floyd_warshall.solve_floyd_warshall(aM, start, end)
    f_pathdf = utils.compile_rows(nodemap, f_path, start, end, 'floyd_warshall')

    utils.compile_csv([d_pathdf, b_pathdf, f_pathdf], start, end)




if __name__ == "__main__":
    main()

