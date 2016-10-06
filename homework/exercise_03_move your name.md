# exercise 03
## 下列程序给出了平移名字的一个初步的实现方法
    #-*-coding:UTF-8-*-
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

## 关于动画，初步代码如下
    #-*-coding:UTF-8-*-
    import os
    import time
    def printimg(img):
        for i in range(0,9):
            for j in range(0,9):
                print img[i][j],
            print
    img=[]
    for i in range(0,9):
        img.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    img[8] = [' ',' ',' ',' ','#',' ',' ',' ',' ']
    printimg(img)
    for k in range(1,5):
        img[8-k] = img[9-k]
        img[9-k] = img[0]
        printimg(img)
        k=os.system('cls')
        time.sleep(0.5)
    for l in range(1,5):
        for k in range(0,l+1):
            img[4+l-k][4-k] = '#'
            img[4-l+k][4+k] = '#'
            img[4+l-k][4+k] = '#'
            img[4-l+k][4-k] = '#'
        for k in range(0,l):
            img[3+l-k][4-k] = ' '
            img[5+k-l][4+k] = ' '
            img[5+k-l][4-k] = ' '
            img[3+l-k][4+k] = ' '      
        printimg(img)
        print

## 输出结果出现谜之BUG。。
## 修改后
    #-*-coding:UTF-8-*-
    import os
    import time
    def printimg(img):
        for i in range(0,9):
            for j in range(0,9):
                print img[i][j],
            print
    img = []
    for i in range(0,9):
        img.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    img[8] = [' ',' ',' ',' ','#',' ',' ',' ',' ']
    printimg(img)
    for k in range(1,5):
        img[8-k][4] = img[9-k][4]
        img[9-k][4] = img[0][4]
        printimg(img)
        time.sleep(1)
        os.system('cls')
    for l in range(1,5):
        for k in range(0,l+1):
            img[4+l-k][4-k] = '#'
            img[4-l+k][4+k] = '#'
            img[4+l-k][4+k] = '#'
            img[4-l+k][4-k] = '#'
        for k in range(0,l):
            img[3+l-k][4-k] = ' '
            img[5+k-l][4+k] = ' '
            img[5+k-l][4-k] = ' '
            img[3+l-k][4+k] = ' '
        printimg(img)
        print
        time.sleep(1)
        os.system('cls')

## 对比前后代码，发现`img[8-k][4] = img[9-k][4] img[9-k][4] = img[0][4]`在后半段产生了截然不同的效果。若将代码改为
    #-*-coding:UTF-8-*-
    import os
    import time
    import numpy as np
    def printimg(img):
        for i in range(0,9):
            for j in range(0,9):
                print img[i][j],
            print
    img=[]
    for i in range(0,9):
        img.append([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    img[8]=[' ',' ',' ',' ','#',' ',' ',' ',' ']
    printimg(img)
    Img = np.array(img)
    for k in range(1,5):
        Img[8-k]=Img[9-k]
        Img[9-k]=Img[0]
        printimg(Img)
        k=os.system('cls')
        time.sleep(0.5)
    for l in range(1,5):
        for k in range(0,l+1):
            Img[4+l-k][4-k]='#'
            Img[4-l+k][4+k]='#'
            Img[4+l-k][4+k]='#'
            Img[4-l+k][4-k]='#'
        for k in range(0,l):
            Img[3+l-k][4-k] = ' '
            Img[5+k-l][4+k] = ' '
            Img[5+k-l][4-k] = ' '
            Img[3+l-k][4+k] = ' '
        printimg(Img)
## 在将img的类由list类改为numpy库中的array类后，输出正常，可以认为该BUG由python中的list类引起，具体原因是list的数据保存类型为数据的存放地址。进行`img[8-k] = img[9-k]`的操作时相当于将img[9-k]的指针赋给了img[8-k]，从而导致了后续的问题。由于python中对list的操作大多基于指针，再次遇到相似问题时，尽量使用array或许会更好。
