class UnionFind:

    def __init__(self, n):

        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x: int) -> int:

        if x != self.parent[x]: # Not root

            # Path Compression
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:

        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:

            return False

        if self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]

        else:

            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        ds = UnionFind(len(accounts))

        account_lookup = dict()

        # Track emails for each account
        # Union accounts that share emails
        for i, account in enumerate(accounts):

            emails = account[1:]
            
            for email in emails:

                if email in account_lookup:

                    ds.union(i, account_lookup[email])

                else:
                    
                    account_lookup.update({email: i})

        print(account_lookup)

        print(ds.parent)
        print(ds.rank)

        # From the disjoint set we now create
        # the final list of lists.
        # 1.) Create maps of lists of emails for each account #
        account_emails = defaultdict(list)

        for email, account in account_lookup.items():

            account_emails[ds.find(account)].append(email)

        print(account_emails)

        merged_accounts = []

        for account in account_emails:

            merged_accounts.append([accounts[account][0]])
            merged_accounts[-1].extend(account_emails[account])

        return merged_accounts
        