#  https://leetcode.com/problems/reverse-words-in-a-string/description/
#todo what is the time and space complexity 
#todo follow up questions

def reverseList(l):
    reversedList = []
    for i in range(len(l)-1,-1,-1):
        reversedList.append(l[i])
    return reversedList

def list_to_string(l):
    s = ""
    s += l[0]
    for i in range(1, len(l)):
        s = s + " " + l[i] 
    return s

def reverseWords(s):
    l = s.split()
    l = reverseList(l)
    s = list_to_string(l)
    return s


s = "  the sky is blue"
print(reverseWords(s))

s = "  hello world  "
print(reverseWords(s))

s = "a good   example"
print(reverseWords(s))


