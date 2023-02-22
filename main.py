import math

print('Hello, world !')

number_list = [13,12,34,4,51,8,27,18]

for item in number_list:
  if item <5:
    print(item)

my_dict = {'Trieste':34100,'Padova':35100}
print('CAP di Trieste: {}'.format(my_dict['Trieste']))



def mia_funzione(arg1,arg2,arg3):
    print("Argomenti: {} e {}".format(arg1,arg2))
    return arg3*arg3


result=mia_funzione("Pippo","Pluto",3)
print(result)
print(math.sqrt(result))

my_file = open('shampoo_sales.csv','r')
#print(my_file.read())
print(my_file.read()[0:50])
my_file.close()

values = []
my_file = open('shampoo_sales.csv','r')
for line in my_file:
  elements=line.split(',')
  if elements[0] != 'Date':
    date = elements[0]
    value=elements[1]

    values.append(value)
print(values)

