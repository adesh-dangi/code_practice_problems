class Solution:
    def gcd(self, num1, num2):
        while num2!=0:
            num1,num2 = num2, num1%num2
        return num1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        lenght = self.gcd(len(str1), len(str2))
        return str1[0:lenght]