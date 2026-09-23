class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = "".join(char for char in s if char.isalnum()).lower()


        print(clean_string[::-1])
        return clean_string == clean_string[::-1]