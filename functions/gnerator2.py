
#wap to generate a list of acronyms from a list of words using generator & *args
def acro(*names):
   for word in names:

    items=word.split()
    yield ''.join (i[0].upper() for i in word.split())

for i in acro('Project Manager','Software Enginer','Data Analyst'):
    print(i)
print(list(acro('Project Manager','Software Enginer','Data Analyst')))

# print('&'.join(name))