import re
regex=re.compile((r'Batman|Tina Fey'))
mo=regex.search('Batman and Tina Fey.')
print(mo)
print(mo.group(0))

pyregex=re.compile(r'^\d+$')
mo=pyregex.search('2222')
print(mo)
