class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # O(n) time O(n) space
        # Brute force

        currSum = 0
        lastDigit = digits[-1] + 1
        exp = 0

        for i in range(len(digits)-1, -1, -1):
            currSum += (lastDigit * (10 ** exp))
            exp+=1
            lastDigit = digits[i-1] if i-1 >= 0 else 0

        ret = [0] * (len(digits) + 1)
        i = len(ret)-1

        while currSum > 0:
            ret[i] = (currSum % 10)
            currSum = currSum//10
            i-=1

        if i == 0:
            ret = ret[1:]

        return ret

        # Lets optimize this 

        # Base case: digits[-1] + 1 < 9
        lastDigit = digits[-1]
        if lastDigit + 1 < 10:
            digits[-1] = lastDigit+1
            return digits

        digits[-1] = 0
        carry = 1

        for i in range(len(digits)-2, -1, -1):
            lastDigit = digits[i]
            if lastDigit + carry < 10:
                digits[i] = lastDigit + carry
                return digits
            digits[i] = 0

        digits.insert(0, carry)
        return digits

        # Another approach is to just reverse the array

        # O(n) time O(1) space since reverse() doesnt take extra space

        digits.reverse()
        plusOne, i = 1, 0

        while plusOne:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + plusOne
                    plusOne = 0
            else:
                digits.append(1)
                plusOne = 0
            i+=1

        digits.reverse()
        return digits


