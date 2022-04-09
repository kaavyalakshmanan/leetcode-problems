class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # O(nm log nm) time O(nm) space
        
        output = []
        adj = defaultdict(list)
        visit = set()
        
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                adj[email].append(i)
                
        def dfs(i, temp):
            if i in visit:
                return
            
            visit.add(i)
            for email in accounts[i][1:]:
                temp.add(email)
                for record in adj[email]:
                    dfs(record, temp)
                    
            return 
                
        for i, acct in enumerate(accounts):
            temp = set()
            dfs(i, temp)
            if temp:
                output.append([acct[0]] + list(sorted(temp)))
        
        return output 
