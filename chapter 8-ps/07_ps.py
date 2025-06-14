def rem(l,word):
    for item in l:
        l.remove(word)
        return l
l=["moni","piya","an","bn"]

print(rem(l,"an"))