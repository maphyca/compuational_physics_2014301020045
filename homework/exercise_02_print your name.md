# Exercise 02
## 下列程序给出了打印人名的一种实现方法
    def printname(name):
       for line in name:
          print(line)
    ASCIIIMG=['','','','','']
    Z=['#####','   # ','  #  ',' #   ','#####']
    H=['#   #','#   #','#####','#   #','#   #']
    A=['  #  ',' # # ',' ### ','#   #','#   #']
    N=['#   #','##  #','# # #','#  ##','#   #']
    G=['#####','#    ','## ##','#  ##','##  #']
    R=['#### ','#  ##','###  ','# #  ','#  ##']
    space=['  ','  ','  ','  ','  ']
    for i in range(5):
       ASCIIIMG[i]+=(Z[i]+space[i]+H[i]+space[i]+A[i]+space[i]+N[i]+space[i]+G[i]+space[i]+R[i]+space[i]+A[i]+space[i]+N[i])
    printname(ASCIIIMG)
