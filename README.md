# Knapsack problem with genetic algorithm

## Assumptions

- The max weight that the bag can carry is 250.
- We're going to sample only 10 random individuals, meaning that the size of the population is going to be 10 individuals.
- Each individual is going to have a randomly selected genes.
- Each gene is going to be whether a box at the given index is selected or not (1 indicated yes, and 0 indicate no)
- The chromosome is going to be the list of all the boxes.
- The fitness function is going to prioritize maximizing the total value of all the selected boxes.
- The fitness function is going to return 0 for any selection of boxes that result in total weight over the set limit as a penalty.
- The selection process is going to rank all the individuals based on the fitness value and randomly select after culling.
- The culling rate is 50% of the population meaning the next generation consists of 50% of the top performer of the last generation.
- The data is going to be read in a json format and any updates to the values is going to modify this file.
- The program termination is going to be determined by the user.
- The program can be terminated when the average fitness of the population is converge for the past 10 generations and can be bypass to run for the period of time or generations.
- The program can be terminated after a certain period of time.
- The program can be terminated after a certain generations.
- The mutation rate is going to be 1% of the time.
- The mutation can happen for any number of genes but not all and is randomly selected.
- The reproduction is going to be a one-point crossover strategy.

## Usage

You can run the program using `python main.py` with the following options:

```
usage: main.py [-h] [-d DATA] [-g GENERATIONS] [-t TIME] [--bypass-convergence]

options:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  The path to boxes JSON file for testing
  -g GENERATIONS, --generations GENERATIONS
                        The number of generation to run the algorithm for
  -t TIME, --time TIME  The running period of the algorithm in SECONDS
  --bypass-convergence  Bypass the convergence check
```

Examples:

Default runs:
```
python main.py
```

To run for a period of time:
```
python main.py --bypass-convergence -t 10
```

To run for specific number of generations:
```
python main.py --bypass-convergence -g 10
```

To run for custom boxes:
```
python main.py -d test_data.json
```
