def isAnagram (s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagram","nagaram"))


