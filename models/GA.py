import random
from models.Chromosome import Chromosome
from models.Population import Population
from models.Box import Box
import time


class KnapsackGA:
    def __init__(self, boxes: list[Box], bag_max_weight:int, initial_population_len: int, end_condition: int, end_condition_settings):
        self.boxes = boxes
        self.bag_max_weight = bag_max_weight
        self._seen_individual_fitness = {}
        self.population = Population.generate_random(initial_population_len, len(boxes), self.fitness)
        self.end_condition = end_condition
        self.end_condition_settings = end_condition_settings
        self._generation_average_fitness = [self._calculate_generation_average_fitness()]

    def evaluate_current_population(self) -> bool:
        match(self.end_condition):
            case 1: 
                self.end_condition_settings["generations"] -= 1
                return self.end_condition_settings["generations"] > 0
            case 2:
                return time.time() - self._start_time < self.end_condition_settings["run_period_in_ms"]
            case _:
                return not self._has_values_converged()


    def fitness(self, individual: Chromosome):
        genotypes_tuple = tuple(individual.genotypes)

        if genotypes_tuple in self._seen_individual_fitness:
            return self._seen_individual_fitness[genotypes_tuple]

        total_weight = sum([individual.genotypes[i] * self.boxes[i].weight for i in range(len(self.boxes))])
        if total_weight > self.bag_max_weight:
            return 0

        fitness_val = sum([individual.genotypes[i] * self.boxes[i].value for i in range(len(self.boxes))])

        self._seen_individual_fitness[genotypes_tuple] = fitness_val
        return fitness_val

    def run(self):
        best_individual = None
        self._start_time = time.time()

        while self.evaluate_current_population():
            # rank individuals based on fitness value and record best fit individuals
            self.population.rank_individual()
            candidate = self.population.individuals[0]
            
            if not best_individual or candidate.fitness > best_individual.fitness:
                best_individual = candidate

            # Cull 50% of the population + select randomly 2 individuals + reproduce a child
            self.population.cull()
            culled_population_size = len(self.population.individuals)

            while culled_population_size > 0:
                x, y= random.sample(self.population.individuals, 2)

                child = x.reproduce(y)
                child.fitness = self.fitness(child)
                self.population.individuals.append(child)

                culled_population_size -= 1

            # Calculate the average fitness of the new population
            self._generation_average_fitness.append(self._calculate_generation_average_fitness())
            if len(self._generation_average_fitness) > 10:
                self._generation_average_fitness.pop(0)

        return best_individual

    def _calculate_generation_average_fitness(self):
        return sum(individual.fitness for individual in self.population.individuals) / len(self.population.individuals)


    def _has_values_converged(self) -> bool:
        if len(self._generation_average_fitness) == 1:
            return False

        return abs(self._generation_average_fitness[-1] - self._generation_average_fitness[0]) < 0.1
