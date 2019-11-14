class CompressedGene:
    def __init__(self, gene:str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1