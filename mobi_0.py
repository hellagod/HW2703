

d = dict()
for word in open('moby_clean.txt').read().split('\n'):
    word = word.strip().lower()
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

d.pop('')
sorted_keys = sorted(d, key=d.get)
print(sorted_keys[:5])


