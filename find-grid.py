wordlist = 'words-en.txt'

words = [line.strip() for line in open(wordlist)]

words = filter(lambda x: len(x) == 5, words)

rev = lambda w: "".join(reversed(list(w)))

words = set(words)
rev = lambda w: "".join(reversed(list(w)))
reversible = [w for w in words if rev(w) in words]

squares = []
for w1 in reversible:
    w2_match = lambda x: x[0] == w1[1] and x[-1] == w1[-2]
    for w2 in filter(w2_match, reversible):
        w3_match = lambda x: x[0] == w1[2] and x[1] == w2[2]
        for w3 in filter(w3_match, reversible):
            if w3 == rev(w3):
                square = [w1, w2, w3, rev(w2), rev(w1)]
                squares.append(square)

for x in squares:
    print("%s\n%s\n%s\n%s\n%s\n\n" % tuple(x))
