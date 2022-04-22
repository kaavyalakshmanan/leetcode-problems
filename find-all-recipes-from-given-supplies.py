class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        adj = defaultdict(list)
        suppliesDict = defaultdict(bool)
        
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                adj[recipe].append(ingredient)
                
        for supply in supplies:
            suppliesDict[supply] = True
            
        res = []
        
        def dfs(recipe, visit):
            
            visit.add(recipe)
            if recipe in suppliesDict:
                return suppliesDict[recipe]
            
            res = True
            for ing in adj[recipe]:
                if ing in suppliesDict:
                    if suppliesDict[ing]:
                        continue
                    else:
                        res = False
                        break
                elif ing in adj and ing not in visit:
                    res = res and dfs(ing, visit)
                else:
                    res = False
                    break
            
            suppliesDict[recipe] = res
            return res
            
        
        for recipe in recipes:
            if (recipe in suppliesDict and suppliesDict[recipe]) or dfs(recipe, set()):
                res.append(recipe)
        
        
        return res
