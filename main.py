from constants import BAG_MAX_WEIGHT, INITIAL_POPULATION_SIZE
from models.GA import KnapsackGA
import argparse
import math
from utils import json_data_parser

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", default="data.json", help="The path to boxes JSON file for testing")
parser.add_argument("-g", "--generations", default=math.inf, type=int, help="The number of generation to run the algorithm for")
parser.add_argument("-t", "--time", default=math.inf, type=int, help="The running period of the algorithm in SECONDS")
parser.add_argument("--bypass-convergence", action='store_true', help="Bypass the convergence check")


if __name__ == "__main__":
    args = parser.parse_args()
    file_data = getattr(args, 'data')
    generations_to_end = getattr(args, 'generations')
    bypass_convergence = getattr(args, 'bypass_convergence')
    run_duration = getattr(args, 'time')


    boxes = json_data_parser.parse(file_data)

    knapsack_solver = KnapsackGA(boxes, BAG_MAX_WEIGHT, INITIAL_POPULATION_SIZE, run_duration, generations_to_end, bypass_convergence)
    best_fit = knapsack_solver.run()
    
    if best_fit:
        print("Best fit found!")
        total_weight = 0
        total_value = 0
        for idx, box_selected in enumerate(best_fit.genotypes):
            if box_selected == 1:
                chosen_box = boxes[idx]
                print(f"Add Box{chosen_box.id} Weight [{chosen_box.weight}] Value [{chosen_box.value}]")
                total_weight += chosen_box.weight
                total_value += chosen_box.value
        
        print(f"Total Bag Weight: {total_weight}")
        print(f"Total Bag Value: {total_value}")
    else:
        print("Something gone wrong with your end condition settings. Please run the program again and try different input.")


