from .Genotype import Genotype
import random

class Chromosome:
    def __init__(self, genotypes: list[Genotype]):
        self.genotypes = genotypes

    @staticmethod
    def generate_random(length = 12) -> "Chromosome":
        """
        Generate a chromosome of random gene

        Args:
            length: The length of chromosome that would like to generate

        Returns:
            A new Chromosome with random gene
        """
        new_population = []
        for _ in range(length):
            new_population.append(Genotype(random.choice([0, 1])))

        return Chromosome(new_population)
