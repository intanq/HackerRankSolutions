def isPalindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True

def palindromeIndex(s):
    # Write your code here
    low = 0
    high = len(s) - 1 
    if isPalindrome(s,low,high):
        return -1
    else:
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                if isPalindrome(s, low+1, high):
                    return low
                elif isPalindrome(s,low,high-1):
                    return high
                return -1

              
print(palindromeIndex("goog"))
