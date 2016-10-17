# -*-coding:UTF-8-*-
import math
import numpy as mp
import matplotlib.pyplot as plt
import time
import os

class shells(object): #用于计算简单的中距离火炮弹道
    def __init__(self):
        self.adc = 0.00004 #初始化空气阻力系数(air drag coefficient)，默认为0.00004
        self.intro = "This is a simple program for concluting the trajectories of shells ,like mortar,which ignore the influence of altitude and corolis force\nAll units follow the International System of Units\nThe unit of angle is degress rather radian\n"
        self.g = 9.8 #重力加速度
        self.sl = 0.01 #step length 步长
        self.h = 0.0 #初始海拔
    def print_intro(self):
        print(self.intro)
    def initial(self,s=None,a=None): #初始化初始虚度与发射角度
        try:
            s= float(raw_input('now input the initial speed for your shells\n'))
            a = math.pi*float(raw_input('now input the angle\n'))/180.0
            if not(isinstance(s,float) and 0<a<90):
                raise ValueError
        except ValueError as e:
                print('You must input the right value of speed and angle, angle shoule be less than 90 but more than 0\n')
        self.speed = s
        self.angle = a
    def judge(self,jadc=None,jg=None,js=None): #判断(judge)是否引入各种影响
            try:
                jadc = raw_input("Do you want to take air drag into consideration?\n\'yes\' or \'no\'?\n")
                if jadc == 'yes':
                    self.adc = float(raw_input('now input the coefficient\n'))
                    if not isinstance(self.adc,float):
                        raise TypeError
                elif (jadc != 'no'):
                    raise ValueError

                jg = raw_input("Do you want to take gravity changing into consideration?\n\'yes\' or \'no?\'\n")
                if jg == 'yes':
                    self.g = float(raw_input('now input the acceleration of gravity \n'))
                    self.h = float(raw_input('now input the altitude of you\n'))
                    if not isinstance(self.g,float):
                        raise TypeError
                elif (jg != 'no'):
                    raise ValueError

                jad = raw_input("Do you want to take air density changing into consideration?\n\'yes\' or \'no?\'\n")
                if jad == 'yes':
                        self.ad = float(raw_input('now input the  air density changing coeddicient of y\n'))
                        if not isinstance(self.ad,float):
                            raise TypeError
                elif (jad != 'no'):
                    raise ValueError
                js = raw_input("Do you want to change the path length of calculating?(default:0.01)\n\'yes\' or \'no?\'\n")
                if js == 'yes':
                    self.sl = float(raw_input("now input the step length\n"))
                    if not isinstance(self.sl,float):
                        raise TypeError
                elif (js != 'no'):
                    raise ValueError

            except ValueError as e:
                print('You must input \'yse\' or \'no\'\n')
                time.sleep(5)
                i=5
                while i!=0:
                    print 'THis program will end in',i,'seconds'
                    time.sleep(1)
                    i-=1
                os._exit(1)
            except TypeError as e:
                print('Please input the right number\n')
                time.sleep(5)
                i=5
                while i!=0:
                    print 'THis program will end in',i,'seconds'
                    time.sleep(1)
                    i-=1
                os._exit(1)

            self.jadc = jadc   #判断完成，将结果写入对象
            self.jg =  jg
            self.js = js
            self.jad = jad
    def calculate(self): #采用Euler法计算弹道
        self.x = [0.0]
        self.y = [0.0]
        self.xv = 0.0
        self.yv = 0.0
        self.vx = self.speed*math.cos(self.angle)
        self.g0 = self.g
        self.adc0 = self.adc
        self.vy = self.speed*math.sin(self.angle)
        while not(self.yv<0):
            if self.jadc == 'no': #判断是否引入参数
                self.adc = 0
            if self.jg == 'no':
                self.g0 = 0
            if self.jad == 'no':
                self.ad = 0
            self.nvx = self.vx-self.adc*self.vx*math.hypot(self.vx,self.vy)*self.sl
            self.nvy = self.vy-self.g*self.sl-self.adc*self.vy*math.hypot(self.vx,self.vy)*self.sl
            self.vx = self.nvx
            self.vy = self.nvy
            self.xv += self.vx*self.sl
            self.yv += self.vy*self.sl
            self.x.append(self.xv)
            self.y.append(self.yv)
            if self.g0 !=0: #不考虑重力加速度变化
                self.g = self.g0*math.pow((6371393+self.h)/(6371393+self.h+self.yv),2)
            if self.ad !=0: #不考虑空气阻力系数变化
                self.adc = self.adc0*math.exp(-self.ad*self.yv)
    def img(self): #作图
        plt.figure()
        plt.plot(self.x, self.y,label="x-y curves")
        plt.xlabel("Distance(meters)")
        plt.ylabel("Height(meters)")
        plt.legend()

class missiles(shells): #挖个坑，待填
    pass

A=shells()
A.print_intro()
time.sleep(2)
A.initial()
A.judge()
A.calculate()
A.img()
