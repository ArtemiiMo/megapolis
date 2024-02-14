import sys,threading


class Scientist:
    def __init__(self, info: str):
        self.raw = info.strip('\n')
        data = self.raw.split('#')
        self.ScientistName = data[0]
        self.preparation = data[1]
        self.date = data[2]
        y, m, d = self.date.split('-')
        self.date2 = int(y) * 3600 + int(m) * 60 + int(d)
        self.components = data[3]
        self.namesurname = self.ScientistName.split()[0]
        self.namename = self.ScientistName.split()[1][0]
        self.namesred = self.ScientistName.split()[2][0]


def binsearch(s, maxi):
    m = 0
    if s < maxi:
        maxi = maxi // 2
    elif s > maxi:
        maxi = maxi + maxi // 2
    elif s == maxi:
        return True
    return binsearch(s, maxi)


sys.setrecursionlimit(9999999)
file = open('scientist.txt', 'r', encoding='UTF-8')
info = file.readlines()
header = f"{info[0].strip()}#login#password\n"
info.pop(0)
scientists = list(map(Scientist, info))
user = input("Введите дату")
while user != 'эксперимент':
    u1, u2, u3 = user.split('-')
    userdate = int(u1) * 3600 + int(u2) * 60 + int(u3)
    for scientist in scientists:
        if binsearch(userdate, 1048576):
            print(
                f'Ученый {scientist.namesurname} {scientist.namename}. {scientist.namesred}. создал препарат: {scientist.preparation} - {scientist.date}')
