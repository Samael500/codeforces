def toi(value):
    return ord(value) - ord('a') + 1

def distance(a, b):
    a = toi(a)
    b = toi(b)
    return min((26 + a - b) % 26, (26 + b - a) % 26)

row = 'a' + raw_input()
res = 0

for i in xrange(1, len(row)):
    res += distance(row[i - 1], row[i])

print res
