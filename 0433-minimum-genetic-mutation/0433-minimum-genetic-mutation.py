class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Start from the endGene 
        # Try all posssible ways to get to the startGene
            # for each mutation try to find valid mutations within the bank
                # there are valid mutations
                    # for each valid mutation
                    # if there are valid mutations after it 
                        # explore more until you get to the startGene
                    # else:
                        # backtrack and explore other valid mutations
                # there are none 
                    # return -1

        startGene = list(startGene)
        endGene = list(endGene)
        st = set()
        st.add("".join(endGene))
        valids = [[endGene,0]]

        if "".join(endGene) not in bank:
            return -1


        MUTATIONS = ["A","C","G","T"]
        solutions = []

        while True:
            current_gene,steps = valids.pop()

            for i in range(8):
                for x in MUTATIONS:
                    if x != current_gene[i]:
                        new = current_gene[:]
                        new[i] = x
                        s_new = "".join(new)
                        if s_new in bank and s_new not in st:
                            valids.append([new,steps + 1])
                            st.add(s_new)
                            
                        if new == startGene:
                            solutions.append(steps + 1)
            if not valids:
                break

        if solutions:
            return min(solutions)

        return -1
