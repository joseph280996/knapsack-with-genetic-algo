from .Chromosome import Chromosome


class Phenotype():
    def __init__(self, chromosome: list[int]):
        self.chromosome = chromosome

    def reproduce(self, y_entity: Phenotype):
        """
        The reproduction functionality of an individual
        """
        raise NotImplemented()
