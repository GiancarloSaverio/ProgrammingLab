import math
import random

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

my_string='a,b,c'
print(my_string)
print(my_string.split(','))
print(my_string)

my_list=[1,2,3,4]
print(my_list)
print(my_list.reverse())
print(my_list)


class Person():
    def __init__(self,nome,surname):
        self.nome = nome
        self.surname = surname
    def __str__(self):
        return('Person "{} {}"'.format(self.nome, self.surname))

    def say_hi(self):
      random_number= random.randint(0,2)

      if random_number==0:
        print('Hello, I am {} {}'.format(self.nome, self.surname))
      elif random_number == 1:
        print('Hi, I am {}'.format(self.nome))
      elif random_number ==2:
        print('Yo bro, {} here !'.format(self.nome))
        
person=Person('Mario','Rossi')
person.say_hi()

print(person)
print(person.nome)
print(person.surname)


