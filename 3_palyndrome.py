# https://leetcode.com/problems/valid-palindrome/submissions/1441142622/

def isPalyndrome(s):
    # time: O(n) space O(1)
    L = 0
    R = len(s) - 1
    s = s.lower()
    while (L < R):
        while not(s[L].isalnum()) and L < R:
            L += 1
        while not(s[R].isalnum()) and L < R:
            R -= 1
        if s[L] == s[R]:
            L += 1
            R -= 1
        else:
            return False
    return True    

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
s4 = ".,"
print(s4.lower())
print(not(s4[0].isalnum()))


if (isPalyndrome(s1)):
    print("ok")
else:
    print("not ok")

if (isPalyndrome(s2)):
    print("ok")
else:
    print("not ok")

if (isPalyndrome(s3)):
    print("ok")
else:
    print("not ok")

if (isPalyndrome(s4)):
    print("ok")
else:
    print("not ok")
