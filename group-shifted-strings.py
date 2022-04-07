class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # O(n*m) time O(n*m) space
        # Hashing
        
        # Hash hashFn to list of strings
        charMap = defaultdict(list)
        
        # Step 2: shiftString helper 
        def shiftString(letter, shift):
            shiftDist = ord(letter) - shift
            # Because z links to a, mod by 26
            shiftDist = shiftDist % 26
            # Add shiftDist to ord(a) because we want to get the character after applying shiftDist to a
            shiftDist += ord('a')
            # Return that char
            return chr(shiftDist)
        
        # Step 1: Iterate over strings
        for string in strings:
            # Get the shift distance based on 0th char
            shift = ord(string[0])
            # Call shift string helper for each char in string
            hashFn = ''
            for c in string:
                res = shiftString(c, shift)
                hashFn += res
            
            charMap[hashFn].append(string)
            
        return list(charMap.values())
