import random, string
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
        self.namename = self.ScientistName.split()[1][0]
        self.namesred = self.ScientistName.split()[2][0]
'''
класс Scientist, содержащий в себе данные о:
ScientistName = ФИО учёного
preparation - препарат
date - дата создания препарата
date2 - формат даты создания препарата для сортировки
components - компоненты для создания препарата
namesurname - фамилия учёного
namename - литера имени
namesred - литера отчества
'''
password = string.ascii_letters+string.digits
file = open('scientist.txt','r',encoding='UTF-8')
info = file.readlines()
header = f"{info[0].strip()}#login#password\n"
info.pop(0)
scientists = list(map(Scientist,info))
file2 = open('scientist_password.csv','w',encoding='UTF-8')
file2.write(header)
for scientist in scientists:
    login = f"{scientist.namesurname}_{scientist.namename}{scientist.namesred}"
    password = ''.join(random.choice(password) for x in range(8))
    '''
    Создание логина посредством f строки
    создание пароля посредством генератора
    '''
    file2.write(f'{scientist.ScientistName}#{scientist.preparation}#{scientist.date}#{scientist.components}#{login}#{password}\n')
