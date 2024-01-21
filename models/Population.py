from typing import Callable
from constants import CULL_RATE
from models.Chromosome import Chromosome


class Population():
    """
    This class represent a whole population

    Properties:
        individuals: The list of all individuals with phenotypes in the population
    """

    def __init__(self, individuals: list[Chromosome]):
        self._individuals = individuals

    def rank_individual(self):
        """
        This function will rank the individuals in the population by their fitness value.
        """
        self._individuals = sorted(self._individuals, key=lambda x: x.fitness, reverse=True)

    @property
    def individuals(self):
        """
        This function is a getter to get all the individuals of the current population.
        Returns:
            The list of individuals in the population
        """
        return self._individuals

    def cull(self):
        """
        This function will cull the population by the given rate.
        """
        cull_idx = int(len(self._individuals) * CULL_RATE)
        self._individuals = self._individuals[:cull_idx]

    @staticmethod
    def generate_random(population_len: int, chromosome_len: int, fitness_func: Callable) -> "Population":
        """
        This function is for generating a random initial population for the genetic algorithm

        Args:
            population_len: The length of the population.
            chromosome_len: The length of the chromosome for each individuals.
            fitness_func: The fitness function to calculate the initial fitness value of each individuals.

        Returns:
            The Population with list of individuals with random Chromosome.
        """
        new_population = []
        for _ in range(population_len):
            new_individual = Chromosome.generate_random(chromosome_len)
            new_individual.fitness = fitness_func(new_individual)
            new_population.append(new_individual)

        return Population(new_population)

