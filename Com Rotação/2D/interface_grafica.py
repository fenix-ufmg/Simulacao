#!/usr/bin/env python3
# -*- coding: utf-8 -*-

scene.autoscale= False

#Céu
sphere(pos=vector(0,0,0),
    texture="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQeyBdjnaFh2sKtxQtJ1da76heXCxCiSSf-1w&usqp=CAU",
    radius=1002,
    shininess=0)
#Chão   
cylinder(pos=vector(0,0,0),
          axis=vector(0,1,0),
          size=vector(.1,2000,2000),
          texture=textures.stucco)

#a1 aleta comprimento raiz 15
#a2 aleta comprimento ponta 5
#a3 aletadesvio 10
#a4 aletalargura 5
#a5 aletaespessura 0.1
#a6 aletanumero 4
#a7 aletadistanciadofundo 0

#pega dados de composição do foguete e de trajetória
with open("desenho.txt", "r") as arquivo:
    for i in arquivo.readlines():
        desenho.append(i[:-1])

with open("altura.txt", "r") as arquivo:
    for i in arquivo.readlines():
        posicaoy.append(i[:-1])

with open("deslocamento.txt", "r") as arquivo:
    for i in arquivo.readlines():
        posicaox.append(i[:-1])

with open("atitudex.txt", "r") as arquivo:
    for i in arquivo.readlines():
        atitudex.append(i[:-1])

with open("atitudey.txt", "r") as arquivo:
    for i in arquivo.readlines():
        atitudey.append(i[:-1])

corpo1_diametro = 0
corpo1_comprimento = 0

#aplica dados de composição do foguete
for i in desenho:
    if i == "c1":
        coifa_diametro = float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
    elif i == "c2":
        coifa_comprimento = float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
    elif i == "cp1":
        if corpo1_diametro == 0:
            corpo1_diametro = float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
        else:
            corpo2_diametro = (
                float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
            )
    elif i == "cp2":
        if corpo1_comprimento == 0:
            corpo1_comprimento = (
                float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
            )
        else:
            corpo2_comprimento = (
                float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
            )
    elif i == "t1":
        transicao_diametro_inicial = (
            float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
        )
    elif i == "t2":
        transicao_comprimento = (
            float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
        )
    elif i == "t3":
        transicao_diametro_final = (
            float(armazenamento[armazenamento.index(i) + 1]) * 10 ** -2
        )

#CG do Fawkes
CG = 33

foguete_comprimento = transicao_comprimento + corpo1_comprimento + corpo2_comprimento +coifa_comprimento


#Eixos
cylinder( pos=vector(0,0,0),
          axis=vector(1,0,0), # x-axis
          size=vector(50,1,1),
          color=color.black,
          opacity=0.5 )
cylinder( pos=vector(0,0,0),
          axis=vector(0,1,0), # y-axis
          size=vector(50,1,1),
          color=color.black,
          opacity=0.5 )
cylinder( pos=vector(0,0,0),
          axis=vector(0,0,1), # z-axis
          size=vector(50,1,1),
          color=color.black,
          opacity=0.5 )



#base para todos os outros componentes, inicia-se no ponto (10,0,10)
corpo2 = cylinder( pos=vector(10,0,10), axis=vector(0,1,0),
        size=vector(corpo2_comprimento,corpo2_diametro,corpo2_diametro), color=color.red )
        
#seguinte à base é um cone invertido posicionado com base nos comprimentos anteriores
transicao = cone(pos=vector(10,corpo2_comprimento+transicao_comprimento,10), axis=vector(0,-1,0), 
        size=vector(transicao_comprimento*transicao_diametro_inicial/(transicao_diametro_inicial-transicao_diametro_final),
        transicao_diametro_inicial,transicao_diametro_inicial), color=color.white, make_trail=True, trail_type="points",
              interval=5, retain=500)
        
#seguinte à transição é um cilindro posicionado com base nos comprimentos anteriores
corpo1 = cylinder( pos=vector(10,corpo2_comprimento+transicao_comprimento,10), axis=vector(0,1,0),
        size=vector(corpo1_comprimento,corpo1_diametro,corpo1_diametro), color=color.red )

#último elemento, trata-se de um cone no topo do foguete
coifa = cone(pos=vector(10,corpo1_comprimento+corpo2_comprimento+transicao_comprimento,10), axis=vector(0,1,0), 
        size=vector(coifa_comprimento,coifa_diametro,coifa_diametro), color=color.blue)

l=mag(coifa.pos-vector(10,foguete_comprimento-coifa_comprimento,10))
#scene.camera.pos = vector(10,10,31.5552)
#scene.camera.axis = vector(5, -20, -31.5552)

t = 0

scene.camera.follow(transicao)
scene.camera.pos += vector(0,0,10)

while t < len(atitudex):
    rate(6)
    scene.camera.pos += vector(0,0,10)
    coifa.pos=vector(10 + (CG-coifa_comprimento)*atitudex[t],(foguete_comprimento-CG)+(CG-coifa_comprimento)*atitudey[t],10) 
    coifa.axis=vector(coifa_comprimento*atitudex[t],coifa_comprimento*atitudey[t],0)
    
    corpo1.pos=vector(10 + ((CG-coifa_comprimento-corpo1_comprimento))*atitudex[t],(foguete_comprimento-CG)+(CG-coifa_comprimento-corpo1_comprimento)*atitudey[t],10) 
    corpo1.axis=vector(corpo1_comprimento*atitudex[t],corpo1_comprimento*atitudey[t],0)
    
    transicao.pos=vector(10 + ((CG-coifa_comprimento-corpo1_comprimento))*atitudex[t],(foguete_comprimento-CG)+((CG-coifa_comprimento-corpo1_comprimento))*atitudey[t],10)
    transicao.axis=vector(-(transicao_comprimento*transicao_diametro_inicial/(transicao_diametro_inicial-transicao_diametro_final))*atitudex[t],
    -(transicao_comprimento*transicao_diametro_inicial/(transicao_diametro_inicial-transicao_diametro_final))*atitudey[t],0)
    
    corpo2.pos=vector(10 - (foguete_comprimento-CG)*atitudex[t],(foguete_comprimento-CG)*(1-atitudey[t]),10)
    corpo2.axis=vector(corpo2_comprimento*atitudex[t],corpo2_comprimento*atitudey[t],0)
    
    coifa.pos=coifa.pos+vector(posicaox[t]*5,posicaoy[t]*5,0)
    corpo1.pos=corpo1.pos+vector(posicaox[t]*5,posicaoy[t]*5,0)
    transicao.pos=transicao.pos+vector(posicaox[t]*5,posicaoy[t]*5,0)
    corpo2.pos=corpo2.pos+vector(posicaox[t]*5,posicaoy[t]*5,0)

    t = t + 1