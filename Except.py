import unittest

my_var = 'Ciao'

try:
  my_var=float(my_var)
  
except ValueError:
  print('Non posso convertire my_var a valore numerico !')
  print('Ho auto un errore di VALORE. my_var valeva: {}'.format(my_var))
 
except TypeError:
  print('Non posso convertire my_var a valore numerico !')
  print('Ho avuto un errore di TIPO. my_var valeva: {}'.format(my_var))
  
except Exception as e:
  print('Non posso convertire my_var a valore numerico !')
  print('La variabile my_var valeva: {}'.format(my_var))
  print('Ed ho avuto questo errore: {}'.format(e))

class CSVFile():
 
  def __init__(self,nomefile):
        self.nomefile = nomefile
        

  def get_data(self):
    my_file = open(self.nomefile,'r')
    print(my_file.read())

my_file=CSVFile('shampoo_sales.csv')

my_file.get_data()
