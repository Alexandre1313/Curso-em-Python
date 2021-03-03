import re

##################################
# Trabalhando com regex do Python
##################################

a = re.match('Pr', 'Programe fácil')  # existe 'Pr' na string 'Programe Fácil' ?
print(a.group())
b = re.match('[Pp]y', 'Python')  # tem 'Pp' seguido de 'y' nessa string 'Python'?
c = re.match('[a-zA-Z]y', 'Python')
d = re.findall('[a-zA-Z]y', 'Python jython Programe fácil')
e = re.findall('[a-zA-Z][a-zA-Z]', 'Python jython 10')
f = re.findall('[a-zA-Z][a-zA-Z]+', 'Python jython')
g = re.findall(r'\w+', 'python jython')

end = 'www.site.com/clientes/17'

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

print(re.split(r'(clientes)/(?P<id>\d+)', end))
