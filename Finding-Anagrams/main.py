# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
    # [assignment] Add your code here
from collections import Counter
def check(s1, s2):
    
    if(Counter(s1) == Counter(s2)):
        print("True")
    else:
        print("False")


s1 = "listen"
s2 = "silent"
check(s1, s2)

    

