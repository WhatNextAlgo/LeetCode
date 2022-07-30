def uniqueMorseRepresentations(words):
    lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return len(set(["".join([lst[ord(w)-ord('a')]  for w in word ]) for word in words]))

    

print(uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))



