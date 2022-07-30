def sortSentence(s: str) -> str:
    def last(n):                            
        return n[-1]

    return " ".join([ x[:-1] for x in sorted(s.split(" "),key = last)])


print(sortSentence(s = "is2 sentence4 This1 a3"))