import random
from models.Chromosome import Chromosome
from models.Population import Population
from models.Box import Box
import time


class KnapsackGA:
    """
    This class represent the Genetic Algorithm used to solve knapsack problem.

    Attributes:
        boxes: The list of boxes of the knapsack problem.
        bag_max_weight: The maximum weight that can be put into the knapsack.
        population: The list of inidividuals in the genetic algorithm.
        run_duration_ms: The time in miliseconds to run the algorithm for.
        generation_count: The total amount of generation that the algorithm should run for.
        should_bypass_convergence: The flag to tell the algorithm to skip checking for best fit convergence and run until end of run duration or end of generation count.
    """

    def __init__(
        self,
        boxes: list[Box],
        bag_max_weight: int,
        initial_population_len: int,
        run_duration_ms: int,
        generation_count: int,
        should_bypass_convergence: bool,
    ):
        # Algorithm attributes
        self.boxes = boxes
        self.bag_max_weight = bag_max_weight
        self._seen_individual_fitness = {}
        self.population = Population.generate_random(
            initial_population_len, len(boxes), self.fitness
        )

        # Algorithm config
        self.run_duration_ms = run_duration_ms
        self.generation_count = generation_count
        self._generation_average_fitness = [
            self._calculate_generation_average_fitness()
        ]
        self.should_bypass_convergence = should_bypass_convergence

    def should_stop(self) -> bool:
        """
        Checking function to validate whether to stop running the algorithm or not.

        Returns:
            The boolean indicating whether we've reached the goal or not.
        """
        self.generation_count -= 1
        running_period = time.time() - self._start_time
        return (
            self._has_values_converged()
            or running_period >= self.run_duration_ms
            or self.generation_count == 0
        )

    def fitness(self, individual: Chromosome) -> int:
        """
        The fitness function used to calculate the fitness value of each individuals in the population.
        This function will cache the fitness value of any seen individuals.

        Arguments:
            individual: The individual in the population to calculate the fitness function for.

        Returns:
            The fitness value of the current individual with the set of chromosome.
        """
        genotypes_tuple = tuple(individual.genotypes)

        if genotypes_tuple in self._seen_individual_fitness:
            return self._seen_individual_fitness[genotypes_tuple]

        total_weight = sum(
            [
                individual.genotypes[i] * self.boxes[i].weight
                for i in range(len(self.boxes))
            ]
        )
        if total_weight > self.bag_max_weight:
            return 0

        fitness_val = sum(
            [
                individual.genotypes[i] * self.boxes[i].value
                for i in range(len(self.boxes))
            ]
        )

        self._seen_individual_fitness[genotypes_tuple] = fitness_val
        return fitness_val

    def run(self):
        """
        This function will run the algorithm and record best fit individuals.
        """
        best_individual = None
        self._start_time = time.time()

        while not self.should_stop():
            # rank individuals based on fitness value and record best fit individuals
            self.population.rank_individual()
            candidate = self.population.individuals[0]

            if not best_individual or candidate.fitness > best_individual.fitness:
                best_individual = candidate

            # Cull 50% of the population + select randomly 2 individuals + reproduce a child + calculate fitness for child
            self.population.cull()
            culled_population_size = len(self.population.individuals)

            while culled_population_size > 0:
                x, y = random.sample(self.population.individuals, 2)

                child = x.reproduce(y)
                child.fitness = self.fitness(child)
                self.population.individuals.append(child)

                culled_population_size -= 1

            # Calculate the average fitness of the new population
            self._generation_average_fitness.append(
                self._calculate_generation_average_fitness()
            )
            if len(self._generation_average_fitness) > 10:
                self._generation_average_fitness.pop(0)

        return best_individual

    def _calculate_generation_average_fitness(self):
        return sum(
            individual.fitness for individual in self.population.individuals
        ) / len(self.population.individuals)

    def _has_values_converged(self) -> bool:
        if self.should_bypass_convergence:
            return False

        if len(self._generation_average_fitness) == 1:
            return False

        return (
            abs(
                self._generation_average_fitness[-1]
                - self._generation_average_fitness[0]
            )
            < 0.1
        )
