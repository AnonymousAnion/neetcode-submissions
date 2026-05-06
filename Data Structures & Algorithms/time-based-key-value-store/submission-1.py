class TimeMap:

    def __init__(self):
        
        # Create a dict of lists.
        # We can take advantage of the fact that
        # for all calls to set, the timestamps are in strictly
        # increasing order.
        self.timestamps: Dict[str, List[Tuple[int, str]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.timestamps:

            self.timestamps.update({key: []})

        self.timestamps[key].append((timestamp, value))

        # print("New Entry: ")
        # print(self.timestamps[key])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timestamps:

            return ""
        
        entries = self.timestamps[key]

        if len(entries) <= 0:

            return ""

        l = 0
        r = len(entries) - 1

        # Search for insert position, basically.
        # If there's an exact match then return that value.
        # If not, then return the insert position - 1 with
        # a minimum value of 0, e.g. max(0, insert position - 1).

        while l <= r:

            m = (r - l) // 2 + l

            # print("Before")
            # print("l: ", l)
            # print("r: ", r)
            # print("m: ", m)

            if entries[m][0] > timestamp:

                r = m - 1

            elif entries[m][0] == timestamp:

                return entries[m][1]
            
            else:

                l = m + 1

            # print("After")
            # print("l: ", l)
            # print("r: ", r)
            # print("m: ", m)

        # print("Final")
        # print("l: ", l)
        # print("r: ", r)

        if entries[r][0] <= timestamp:

            return entries[r][1]

        return ""
