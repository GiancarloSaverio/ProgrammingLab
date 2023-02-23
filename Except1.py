
class ExamException(Exception):
    pass

#raise DemoException('Eccezione')
class Prova():
  Ex=ExamException()
  def __init__(self,name):
      self.name=name 
      if (name=='errore'):
         raise ExamException('errore')
      else:
         print('corretto')

my_prova=Prova('errore')
  