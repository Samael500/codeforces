import re
import math
import sys


class Convert(object):

    base = 26
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    splitter = re.compile(r'(\d+)')
    bases = (
        1, 26, 676, 17576, 456976, 11881376, 308915776, 8031810176, 208827064576,
        5429503678976, 141167095653376, 3670344486987776, 95428956661682176, 2481152873203736576, )

    def to_(self, value):
        res, digits = '', 0
        for i in xrange(10):
            if value > self.bases[i]:
                value -= self.bases[i]
                digits += 1
        res = ''
        i = 1
        while value > 0:
            res += self.alpha[value % self.base]
            value /= self.base
            i += 1
        if digits - len(res) > 0:
            res += 'A' * (digits - len(res))
        # prefix zeros
        return res[::-1]

    def from_(self, value):
        res, x = 0, 0
        for char in value[::-1]:
            res += self.bases[x] * (ord(char) - 64)
            x += 1
        return res

    def __call__(self, row):
        x_row = self.splitter.split(row)
        if len(x_row) == 5:
            _, r, _, c, _ = x_row
            return '%s%s\n' % (self.to_(int(c)), r)
        c, r, _ = x_row
        return 'R%sC%d\n' % (r, self.from_(c))


c = Convert()
n = int(sys.stdin.readline())
while n:
    row = sys.stdin.readline()
    sys.stdout.write(c(row))
    n -= 1
