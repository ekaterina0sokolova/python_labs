import re


def function(string):
    pattern = r'\b[A-ZА-Я]{2,}\b'
    words = re.findall(pattern, string)
    return len(words)


print(function(" А курс информатики в вузе соответствует ФГОС и ПООП, что подтверждено ФГУ"))
print(function(" СССР и США"))