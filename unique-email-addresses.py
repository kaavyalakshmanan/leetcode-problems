class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        # O(n*m) time O(n*m) space

        emailSet = set()

        for email in emails:
            filteredEmail = self.parseEmail(email)
            emailSet.add(filteredEmail)

        return len(emailSet)


    def parseEmail(self, email: str) -> str:

        end = len(email) - 5
        start = 0
        filteredEmail = ""
        afterDomain = False

        # case 1: not '.' or '+'
            # include that in filteredEmail
        # case 2: '+' before '@'
            # skip over everything that comes after '+' (including '.') until we get to '@'
        # case 3: '.' before '@' 
            # just skip over '.' and add the rest
        # case 4: '.' or '+' after '@'
            # include that
        while start <= end:

            if email[start] == '+' and not afterDomain:
                curr = start
                while curr < end and email[curr] != '@':
                    curr+=1
                start = curr
            # case 3
            elif email[start] == '.' and not afterDomain:
                start+=1
            # case 1 & case 4
            else:
                if email[start] == '@':
                    afterDomain = True
                filteredEmail += email[start]
                start+=1

        return filteredEmail


            
        


