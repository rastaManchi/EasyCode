from pygame import *
import os,sys
width=500
height=500
fps=60
screen=display.set_mode((width,height))
clock=time.Clock()
class Wall:
    def __init__(self,rect,image):
        self.rect=Rect(rect[0],rect[1],20,20)
        self.image=transform.scale(image,(20,20))
    def draw(self):
        screen.blit(self.image,self.rect)
class Player:
    def __init__(self,rect,speed,image):
        self.rect=Rect(rect[0],rect[1],20,20)
        self.speed_w=speed[0]
        self.speed_a=speed[1]
        self.speed_s=speed[2]
        self.speed_d=speed[3]
        self.image=transform.scale(image,(20,20))
    def move(self):
        self.rect.y+=self.speed_w+self.speed_s
        self.rect.x+=self.speed_a+self.speed_d
    def draw(self):
        screen.blit(self.image,self.rect)
    def collide(self,object):
        if self.rect.colliderect(object.rect):
            if 0<object.rect.right-self.rect.left<=5:
                self.rect.x-=(self.speed_a+self.speed_d)*2
                return
            elif 0<self.rect.right-object.rect.left<=5:
                self.rect.x-=(self.speed_a+self.speed_d)*2
                return
            if 0<self.rect.bottom-object.rect.top<=5:
                self.rect.y-=(self.speed_w+self.speed_s)*2
                return
            elif 0<object.rect.bottom-self.rect.top<=5:
                self.rect.y-=(self.speed_w+self.speed_s)*2
                return
lvl1_map=[]
file=open('lvl_1.txt','r')
M=file.read().split('\n')
row=0
col=0
for line in M:
    col=0
    for symbol in line:
        if symbol=='1' or symbol=='2':
            lvl1_map.append(Wall((col*20,row*20),image.load('bedrock.png')))
        col+=1
    row+=1
player=Player((20,20),(0,0,0,0),image.load('player.png'))
while 1:
    screen.fill((0,0,0))
    for e in event.get():
        if e.type==QUIT:
            sys.exit()
            quit()
        if e.type==KEYDOWN:
            if e.key==K_w:
                player.speed_w=-5
            if e.key==K_a:
                player.speed_a=-5
            if e.key==K_s:
                player.speed_s=5
            if e.key==K_d:
                player.speed_d=5
        if e.type==KEYUP:
            if e.key==K_w:
                player.speed_w=0
            if e.key==K_a:
                player.speed_a=0
            if e.key==K_s:
                player.speed_s=0
            if e.key==K_d:
                player.speed_d=0
    player.move()
    for block in lvl1_map:
        player.collide(block)
    for block in lvl1_map:
        block.draw()
    player.draw()
    display.update()
    clock.tick(fps)