class Scientist:
    def __init__(self,info:str):
        self.raw = info.strip('\n')
        data = self.raw.split('#')
        self.ScientistName = data[0]
        self.preparation = data[1]
        self.date = data[2]
        y,m,d = self.date.split('-')
        self.date2 = int(y)*3600 + int(m)*60 + int(d)
        self.components = data[3]
def insort(s):
    for i in range(len(s)):
        s2 = s[i]
        j = i-1
        while j >= 0 and s[j].date2 > s2.date2:
            s[j+1] = s
            j -= 1

file = open('scientist.txt','r',encoding='UTF-8')
info = file.readlines()
header = info[0]
info.pop(0)
scientists = list(map(Scientist,info))
preparation_list = []
file2 = open('scientist_origin.txt','w',encoding='UTF-8')
file2.write(f'{header}')
for scientist in scientists:
    if scientist.preparation not in preparation_list:
        preparation_list.append(scientist.preparation)
file2.write(f'{scientist.ScientistName}#{scientist.preparation}#{scientist.date}#{scientist.components}\n')