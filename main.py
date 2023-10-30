import get_input
from models.GA import KnapsackGA

if __name__ == "__main__":
    boxes, end_condition_choice, end_condition_setting = get_input.run()

    knapsack_solver = KnapsackGA(boxes, 250, 10, end_condition_choice, end_condition_setting)
    best_fit = knapsack_solver.run()

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


