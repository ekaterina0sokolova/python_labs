import re


def function(string):
    pattern = r'\b\w+(-\w+)*\b'
    words = re.findall(pattern, string)
    return len(words)


print(function("""Он --- серо-буро-малиновый слон!!>>>:->А не кот."""))
print(function("""Он - человек!!>>>:->А не кот."""))