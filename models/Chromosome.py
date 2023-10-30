import random

class Chromosome:
    """
    Class representation of the Chromosome. In our use case it is the list of all the boxes and whether it was picked or not
    """
    mutation_rate = 0.1
    fitness = 0

    def __init__(self, genotypes: list[int]):
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
            new_population.append(random.choice([0, 1]))

        return Chromosome(new_population)


    def modify_gene(self, idx: int):
        """
        Flip the gene at a given location in the chromosome

        Args:
            idx: The idx of the gene to modify
        """
        self.genotypes[idx] = self.genotypes[idx] ^ 1

    def reproduce(self, y_entity: "Chromosome") -> "Chromosome":
        """
        The reproduction functionality of an individual with another individual using cross-over

        Args:
            y_entity: The y entity for reproduction

        Returns:
            A new individual
        """
        return self._crossover(y_entity)

    def mutate(self):
        should_mutation_occurs = random.choices([True, False], [self.mutation_rate, 1 - self.mutation_rate])[0]
        if should_mutation_occurs:
            self._single_point_mutation()
                
    def _crossover(self, y_entity: "Chromosome") -> "Chromosome":
        """
        The crossover functionality which is the core of reproduction to generate new individuals

        Args:
            y_entity: The y entity for reproduction

        Returns:
            A new individuals
        """
        rand_idx_for_gene_swap = random.randint(1, len(self.genotypes) - 1)
        child = Chromosome(self.genotypes[:rand_idx_for_gene_swap] + y_entity.genotypes[rand_idx_for_gene_swap:])
        child.mutate()

        return child

    def _single_point_mutation(self):
        gene_len = len(self.genotypes)
        rand_gene_count_mutate = random.randint(1, gene_len - 1)
        modified_gene = set()
        while rand_gene_count_mutate > 0:
            rand_gene_idx_to_mutate = random.randint(0, gene_len - 1)
            if rand_gene_idx_to_mutate not in modified_gene:
                modified_gene.add(rand_gene_idx_to_mutate)
                self.modify_gene(rand_gene_idx_to_mutate)
                rand_gene_count_mutate -= 1
