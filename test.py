import sys,threading
# import string
# s = [int(x) for x in range(1024)]
# a = s[-225:] + s[:-225]
# print(a)
#
# print(string.ascii_letters)
# str.isascii()
# print()
threading.stack_size()
sys.setrecursionlimit(9999)
def binsearch(s,maxi):
    m = 0
    if s < maxi:
        maxi = maxi // 2
    elif s > maxi:
        maxi = maxi + maxi // 2
    elif s == maxi:
        return True
    return binsearch(s,maxi)
print(binsearch(1943,2048))
