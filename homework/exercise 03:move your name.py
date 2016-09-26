import os
import time
def printname(name):
   for line in name:
      print(line)
ASCIIIMG=['','','','','']
Z=['#####','   # ','  #  ',' #   ','#####']
H=['#   #','#   #','#####','#   #','#   #']
A=['  #  ',' # # ',' ### ','#   #','#   #']
N=['#   #','##  #','# # #','#  ##','#   #']
G=['#####','#    ','## ##','#  ##','##  #']
R=['#### ','#   #','###  ','# #  ','#  ##']
space=['  ','  ','  ','  ','  ']
for i in range(5):
   ASCIIIMG[i]+=(Z[i]+space[i]+H[i]+space[i]+A[i]+space[i]+N[i]+space[i]+G[i]+space[i]+R[i]+space[i]+A[i]+space[i]+N[i])
for j in range(10):
    for i in range(5):
        ASCIIIMG[i]=space[i]+ASCIIIMG[i]
    printname(ASCIIIMG)
    j=os.system('cls')
    time.sleep(0.5)
