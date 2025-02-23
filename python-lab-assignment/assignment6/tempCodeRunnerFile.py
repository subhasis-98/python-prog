s = input()
d = {}
for ch in s:
    d[ch] = s.count(ch)
print(d)