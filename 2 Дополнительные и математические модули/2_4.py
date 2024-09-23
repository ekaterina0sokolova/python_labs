import re


def function(string):
    return re.sub(r'([A-Z])', lambda x: '_' + x.group(0).lower(), string).lstrip('_')


print(function("camelCaseVar"))
print(function("myWonderfulVar"))