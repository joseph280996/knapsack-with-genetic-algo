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
       self._individuals = sorted(self._individuals, key=lambda x: x.fitness, reverse=True)

    @property
    def individuals(self):
        return self._individuals

    def cull(self):
        cull_idx = int(len(self._individuals) * CULL_RATE)
        self._individuals = self._individuals[:cull_idx]

    @staticmethod
    def generate_random(population_len: int, chromosome_len: int, fitness_func: Callable) -> "Population":
        """
        This function is for generating a random initial population for the genetic algorithm

        Args:
            length: the length of the population

        Returns:
            The list of Chromosome
        """
        new_population = []
        for _ in range(population_len):
            new_individual = Chromosome.generate_random(chromosome_len)
            new_individual.fitness = fitness_func(new_individual)
            new_population.append(new_individual)

        return Population(new_population)

