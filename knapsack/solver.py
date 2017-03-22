#!/usr/bin/python
# -*- coding: utf-8 -*-


#curentbest
#k1 - smallFirst (7)
#k2 - mostValuedFirst (10)
#k3 - valueDensity (7)
#k4 - mostValuedFirst (7)
#k5 - valueDensity (7)
#k6 - valueDensity (7)


from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
from solverTypes import *
import numpy as np


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()#
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full


    #print(len(items))
    #pred = DefaultOrder(item_count, capacity, items)
    #pred = SmallestWeightFirst(item_count, capacity, items)
    #pred = MostValuedFirst(item_count, capacity, items)
    #pred = WeightValueRation(item_count, capacity, items)
    pred = BranchAndBound(item_count, capacity, items)
    value, weight, taken = pred.solve()


    #print(capacity,  np.sum(np.array(taken)*np.array([x.value for x in items])))
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

