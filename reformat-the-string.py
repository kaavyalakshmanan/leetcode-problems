class Solution:
    def reformat(self, s: str) -> str:

        numDigits, numLetters = 0, 0
        for c in s:
            if c.isdigit():
                numDigits+=1
            elif c.isalpha():
                numLetters+=1

        digitPtr, letterPtr = 0, 0
        startWithDigit = False
        if numDigits > numLetters:
            startWithDigit = True

        res = ""

        while digitPtr < len(s) or letterPtr < len(s):
            while digitPtr < len(s) and not s[digitPtr].isdigit():
                digitPtr+=1
            while letterPtr < len(s) and not s[letterPtr].isalpha():
                letterPtr+=1 
            if startWithDigit:
                if digitPtr == len(s):
                    return ""
                res += s[digitPtr]
                digitPtr+=1
            else:
                if letterPtr == len(s):
                    return ""
                res += s[letterPtr]
                letterPtr+=1
            startWithDigit = not startWithDigit

            if len(res) == len(s):
                return res

        return res if len(res) == len(s) else ""
