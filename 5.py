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
        self.namesurname = self.ScientistName.split()[0]
        self.namename = self.ScientistName.split()[1]
        self.namesred = self.ScientistName.split()[2]

asciir = [int(x) for x in range(1024)]
perest = asciir[-225:] + asciir[:-225]

file = open('scientist.txt','r',encoding='UTF-8')
info = file.readlines()
header = f"{info[0].strip()}#login#password\n"
info.pop(0)
scientists = list(map(Scientist,info))
file2 = open('scientist_password.csv','w',encoding='UTF-8')
file2.write(header)