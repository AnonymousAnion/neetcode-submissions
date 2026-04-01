from sortedcontainers import SortedDict

class FreqStack:

    def __init__(self):

        self.stacks_on_stacks = [[]]
        self.freqs = Counter()
        
    def push(self, val: int) -> None:

        print("pushing: ", val)

        self.freqs[val] += 1

        if self.freqs[val] >= len(self.stacks_on_stacks):

            self.stacks_on_stacks.append([val])

        else:

            self.stacks_on_stacks[self.freqs[val]].append(val)

        print("Frequencies: ", self.freqs)
        print(self.stacks_on_stacks)
        
    def pop(self) -> int:
        
        removed_element = self.stacks_on_stacks[-1].pop()

        print("Removing: ", removed_element)

        if not self.stacks_on_stacks[-1]:

            self.stacks_on_stacks.pop()

        self.freqs[removed_element] -= 1

        print("Frequencies: ", self.freqs)
        print(self.stacks_on_stacks)

        return removed_element

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()