import re


def function(string):
    pattern = r'\b[о|О|э|Э]'
    words = re.findall(pattern, string)
    return len(words)

print(function("""Он --- серо-буро-малиновый слон!!>>>:->А не кот."""))