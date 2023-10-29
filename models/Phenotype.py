from .Chromosome import Chromosome
import random


class Phenotype():
    """
    This class represent a Phenotype, can be thought of as an individual in the population
    Properties:
        chromosome: The chromosome instance that has the characteristics
    """
    def __init__(self, chromosome: Chromosome):
        self.chromosome = chromosome

    def reproduce(self, y_entity: "Phenotype") -> list["Phenotype"]:
        """
        The reproduction functionality of an individual with another individual using cross-over

        Args:
            y_entity: The y entity for reproduction

        Returns:
            A new individual
        """
        return self._crossover(y_entity)

    def _crossover(self, y_entity: "Phenotype") -> list["Phenotype"]:
        """
        The crossover functionality which is the core of reproduction to generate new individuals

        Args:
            y_entity: The y entity for reproduction

        Returns:
            A new individuals
        """
        rand_idx_for_gene_swap = random.randint(0, len(self.chromosome.genotypes))
        new_individuals = [
                Phenotype (
                    Chromosome (self.chromosome.genotypes[:rand_idx_for_gene_swap] + y_entity.chromosome.genotypes[rand_idx_for_gene_swap:])
                ),
                Phenotype (Chromosome(self.chromosome.genotypes[:rand_idx_for_gene_swap] + y_entity.chromosome.genotypes[rand_idx_for_gene_swap:]))
        ]

        return new_individuals


