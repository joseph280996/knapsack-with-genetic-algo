from _typeshed import Self
from .Chromosome import Chromosome


class Phenotype():
    def __init__(self, chromosome: Chromosome):
        self.chromosome = chromosome

    def reproduce(self, y_entity: Self) -> Self:
        """
        The reproduction functionality of an individual with another individual using cross-over

        Args:
            y_entity: another individual

        Returns:
            A new individual
        """
        raise NotImplemented()

