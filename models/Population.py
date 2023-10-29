from models.Chromosome import Chromosome
from .Phenotype import Phenotype


class Population():
    """
    This class represent a whole population

    Properties:
        individuals: The list of all individuals with phenotypes in the population
    """
    def __init__(self, individuals: list[Phenotype]):
        self._individuals = individuals

    @staticmethod
    def generate_random(population_len: int, chromosome_len: int) -> list[Chromosome]:
        """
        This function is for generating a random initial population for the genetic algorithm

        Args:
            length: the length of the population

        Returns:
            The list of Chromosome
        """
        new_population = []
        for _ in range(population_len):
            new_population.append(Phenotype(Chromosome.generate_random(chromosome_len)))

        return new_population

