import pandas as pd
import numpy as np
def array():
  a=np.random.randint(100,size=5)
  return a
def data():
  data={'Cars':['BMW','FORD','TATA','Bugatti','TESLA'],'Price':['$2,00,000','$05,00,000','$3,00,000','$10,00,000','$20,00,000']}
  display=pd.DataFrame(data)
  return display
list_number=array()
table_list=data()
print(list_number)
print(table_list)
print(list_number)
