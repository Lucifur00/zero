print(""" 
\033[0;33m  111111  111111  111111  111    111  111111 
\033[0;32m  11  11  11  11    11    11 1111 11  11
\033[0;36m  111111  1111      11    11  11  11  111111
\033[1;33m  11      11 11     11    11  11  11  11
\033[0;31m  11      11  11  1111111 11  11  11  111111 """)
print("")
print(" \033[0;32m ")
user=str(input("Enter Tool Name : "))
password=str(input("\033[0;35m Enter Tool Password : "))
if user=="prime" and password=="prime":
  print( "\033[0;36m ")
  def load():
   import time as t
   t.spleep(0.3)
  for x in range(0,10,1):
   import time as a
   a.sleep(0.3)
   print(" loading..")
   x+=1
else:
  print(" \033[0;31m Password Wrong")