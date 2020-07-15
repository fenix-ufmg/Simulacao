#!/usr/bin/env python3
#created for BAIAO, Joao                                                                              and helped by miguel
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-

from math import pi
from math import sin
from math import cos
import numpy as np
import matplotlib.pyplot as plt
import Funcoes as f

variacaodetempo = 0.001
t = 0

#Todoss os valores no SI

coifacomprimento = 8*10**-2
coifadiametro = 6*10**-2
coifadensidade = 1240
coifavolume = pi*coifacomprimento/3*((coifadiametro/2)**2)
coifamassa = float(coifadensidade*coifavolume)

corpocomprimento = 20*10**-2
corpodiametro = coifadiametro
corpodensidade = 2550
corpoespessura = 0.1*10**-2
corpovolumeM = float(((corpodiametro/2)**2))*corpocomprimento*pi
corpovolumem = float(((corpodiametro/2-corpoespessura)**2))*corpocomprimento*pi
corpomassaM = float(corpodensidade*(corpovolumeM))
corpomassam = float(corpodensidade*(corpovolumem))
corpomassa = corpomassaM - corpomassam
corpoareamolhada = corpodiametro*corpocomprimento

transicaocomprimento = 8*10**-2
transicaodiametroinicial = corpodiametro
transicaodiametrofinal = 4*10**-2
transicaodensidade = 1240
transicaoespessura = 1*10**-2
transicaovolumeM = pi*transicaocomprimento*(transicaodiametroinicial**2 + transicaodiametroinicial*transicaodiametrofinal + transicaodiametrofinal**2)/12
transicaovolumem = pi*transicaocomprimento*((transicaodiametroinicial - 2*transicaoespessura)**2 + (transicaodiametroinicial - 2*transicaoespessura)*(transicaodiametrofinal - 2*transicaoespessura) + (transicaodiametrofinal-2*transicaoespessura)**2)/12
transicaomassaM = transicaovolumeM*transicaodensidade
transicaomassam = transicaovolumem*transicaodensidade
transicaomassa = transicaomassaM - transicaomassam
transicaoareamolhada = transicaocomprimento*(transicaodiametroinicial + transicaodiametrofinal)

corpo2comprimento = 20*10**-2
corpo2diametro = transicaodiametrofinal
corpo2densidade = 2550
corpo2espessura = 0.1*10**-2
corpo2volumeM = float(((corpo2diametro/2)**2))*corpo2comprimento*pi
corpo2volumem = float(((corpo2diametro/2-corpo2espessura)**2))*corpo2comprimento*pi
corpo2massaM = float(corpo2densidade*(corpo2volumeM))
corpo2massam = float(corpo2densidade*(corpo2volumem))
corpo2massa = corpo2massaM - corpo2massam
corpo2areamolhada = corpo2diametro*corpo2comprimento

aletacomprimentoraiz = 15*10**-2
aletacomprimentoponta = 5*10**-2
aletadesvio = 10*10**-2
aletalargura = 5*10**-2
aletaespessura = 0.1*10**-2
aletanumero = 4
aletadistanciadofundo = 0*10**-2
aletadensidade = 2700
aletamassa = float(aletadensidade*aletaespessura*((aletacomprimentoponta + aletacomprimentoraiz)*aletalargura/2))
aletaareamolhada = (aletacomprimentoponta + aletacomprimentoraiz)*aletalargura/2
AR = (2*aletalargura**2)/aletaareamolhada

comprimentodahaste = 2

componentemassa = 0.25

arearef = pi*(coifadiametro/2)**2
Rs = 200*10**-6

motorcomprimento = 20*10**-2
motordiametro = 3.8*10**-2
motormassa = 0.3
motorduracao = 0.3
empuxox = [0]
empuxoy = [120]
paraquedasCD = 0.78

#insira valores no SI
terramassa = 5.972*(10**24)
ardensidade = 1.225
viscosidadear = 1.8*10**-5
c = 340.29

posicaox = [0]
posicaoy = [0]

foguetemassa = motormassa + coifamassa + corpomassa + transicaomassa + corpo2massa + componentemassa + aletamassa*aletanumero
foguetecomprimento = coifacomprimento + corpocomprimento + transicaocomprimento + corpo2comprimento
foguetevolume = coifavolume + corpovolumeM + transicaovolumeM + corpo2volumeM + aletaareamolhada*aletaespessura*aletanumero
pesoy = [(-(5.972*(10**24)*foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2)]
momentodeinercia = pi*corpodensidade*foguetecomprimento/12*(3*(corpodiametro/2**4 - ((corpodiametro-corpoespessura)/2)**4) + foguetecomprimento**2*((corpodiametro/2)**2 - ((corpodiametro-corpoespessura)/2)**2))

Rcri = 51*(Rs/foguetecomprimento)**(-1.039)
fitnessratio = foguetecomprimento/corpodiametro

arrastox = [0]
arrastoy = [0]
arrasto = [arrastox[0],arrastoy[0]]

time = [0]

atitudex = [0]
atitudey = [1]
atitude = [atitudex[t],atitudey[t]]

momento = [0]

velocidadeangular = 0

vetorreferencia = [0,1]
modvetorreferencia = f.callmod(vetorreferencia[0],vetorreferencia[1])

velocidadex = [0]
velocidadey = [0]
velocidade = [velocidadex[t],velocidadey[t]]
modvelocidade = f.callmod(velocidadex[t],velocidadey[t])

velocidaderelativax = [0]
velocidaderelativay = [0]
velocidaderelativa = [velocidaderelativax[t],velocidaderelativay[t]]

aceleracaox = [0]
aceleracaoy = [0]
aceleracao = [aceleracaox[t],aceleracaoy[t]]

velocidadeangular = [0]
aceleracaoangular = [0]

windspeed = [0]

CD = [0]

q = 1/2*(ardensidade * modvelocidade**2)

CGcoifa = f.callCGcoifa(coifamassa, 0, coifacomprimento,0)
CGcorpo = coifacomprimento + corpocomprimento/2
CGtransicao = coifacomprimento + corpocomprimento + (transicaomassaM*f.callCGtransicao(transicaocomprimento, transicaodiametroinicial, transicaodiametrofinal, transicaodensidade) - transicaomassam*f.callCGtransicao(transicaocomprimento, transicaodiametroinicial - 2*transicaoespessura, transicaodiametrofinal - 2*transicaoespessura, transicaodensidade))/(transicaomassaM - transicaomassam)
CGcorpo2motor = coifacomprimento + corpocomprimento + transicaocomprimento + f.callCGcorpomotor(motormassa,corpo2massa,corpo2comprimento,motorcomprimento)
CGaleta = coifacomprimento + corpocomprimento + transicaocomprimento + corpo2comprimento - (aletadistanciadofundo + aletacomprimentoraiz) + f.callCGaleta(aletaespessura*aletadensidade, aletamassa, aletadesvio, aletalargura, aletacomprimentoraiz, aletacomprimentoponta, aletadistanciadofundo,coifacomprimento,corpocomprimento)

CG = (CGcoifa*coifamassa + CGcorpo*corpomassa + CGtransicao*transicaomassa + CGcorpo2motor*(corpo2massa + motormassa) + CGaleta*aletamassa*aletanumero)/(coifamassa + corpomassa + transicaomassa + (corpo2massa + motormassa) + aletamassa*aletanumero)

if np.cross(vetorreferencia,atitude) >= 0:
	angulo = [-f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1])]
else:
	angulo = [f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1])]
    
if np.cross(velocidade,atitude) >= 0:
	alpha = [-f.callalpha(atitudex[t],atitudey[t],velocidade[0],velocidade[1])]
else:
	alpha = [f.callalpha(atitudex[t],atitudey[t],velocidade[0],velocidade[1])]

CNalphacoifa = f.callCNalpha(arearef,coifadiametro,0,alpha[t])

CNalphacorpo = f.callCNalpha(arearef,corpodiametro,corpodiametro,alpha[t])

CNalphatransicao = f.callalpha(arearef,transicaodiametroinicial,transicaodiametrofinal,alpha[t])

CNalphacorpo2 = f.callCNalpha(arearef,corpo2diametro,corpo2diametro,alpha[t])

CNalphaumaaleta = (2*pi*AR*(aletaareamolhada/arearef))/(2+(4+(((((modvelocidade/c)**2 - 1)**2)**(1/4))*AR/cos(pi/6))**2))

CNalphaaleta = aletanumero*CNalphaumaaleta/2

CPcoifa = f.callCPbody (coifacomprimento,0,coifadiametro,coifavolume)

CPcorpo = f.callCPbody (corpocomprimento,corpodiametro,corpodiametro,corpovolumeM) + coifacomprimento

CPtransicao = f.callCPbody (transicaocomprimento, transicaodiametroinicial, transicaodiametrofinal, transicaovolumeM) + corpocomprimento + coifacomprimento

CPcorpo2 = f.callCPbody (corpo2comprimento,corpo2diametro,corpo2diametro,corpo2volumeM) + transicaocomprimento + corpocomprimento + coifacomprimento

CPaleta = f.callCPaleta (aletadesvio,aletacomprimentoraiz,aletacomprimentoponta)  + corpo2comprimento + transicaocomprimento + corpocomprimento + coifacomprimento - aletacomprimentoraiz

CP = (CNalphacoifa*CPcoifa + CNalphacorpo*CPcorpo + CNalphatransicao*CPtransicao + CNalphacorpo2*CPcorpo2 + CNalphaaleta*CPaleta)/(CNalphacoifa + CNalphacorpo + CNalphatransicao + CNalphacorpo2 + CNalphaaleta)

Cm = [f.callCm(alpha[t],coifadiametro,arearef,coifadiametro,foguetecomprimento,foguetevolume)]
CDdamping = [f.callCDdamping (CPaleta, CG, aletaareamolhada,arearef,coifadiametro,foguetecomprimento,corpodiametro/2,velocidadeangular,modvelocidade)]

reynoldsnumero = f.callRey(ardensidade,coifadiametro, viscosidadear,modvelocidade)

vooimpulsionado = True
cabotagem = True
quedalivre = True

#lancamento

lancamentoduracao = 0


while posicaoy[t] <= comprimentodahaste:
    
	print('a')
    
	windspeed.append(f.callwind(posicaoy[t]))
	reynoldsnumero = f.callRey(ardensidade,coifadiametro, viscosidadear,modvelocidade)
    
	modvelocidade = f.callmod(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modaceleracao = f.callmod(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modatitude = f.callmod(atitudex[t],atitudey[t])
	Mach = modvelocidade/c
    
	CD.append(f.callCDfriction(arearef,aletaareamolhada,Rcri,fitnessratio,corpoareamolhada,aletaespessura,reynoldsnumero,Rs,foguetecomprimento,Mach) + f.callCDcoifa(coifadiametro,coifacomprimento) + f.callCDtubeira(Mach))

	velocidaderelativax.append(velocidadex[t]-windspeed[t])
	velocidaderelativay.append(velocidadey[t])
	velocidaderelativa = [velocidaderelativax[t],velocidaderelativay[t]]

	modempuxo = f.callmod(empuxox[t],empuxoy[t])

	arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((-velocidadey[t]/modvelocidade)*arrastomodulo)

	except:
		arrastox.append(0)
		arrastoy.append(0)

	try:
		empuxox.append((velocidadex[t]/modvelocidade)*modempuxo)
		empuxoy.append((velocidadey[t]/modvelocidade)*modempuxo)
	except:
		empuxox.append(empuxox[t])
		empuxoy.append(empuxoy[t])
        
	foguetemassa -= motormassa/8000
	pesoy.append((-(terramassa*foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))
        
	q = 1/2*(ardensidade * modvelocidade**2)
    
	if np.cross(vetorreferencia,atitude) >= 0:
		angulo.append(f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))
	else:
		angulo.append(-f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))
        
	if np.cross(velocidaderelativa,atitude) >= 0:
		alpha.append(f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))
	else:
		alpha.append(-f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))
    
	momento.append(0)

	aceleracaoangular.append(momento[t]/momentodeinercia)
	velocidadeangular.append(variacaodetempo*aceleracaoangular[t] + velocidadeangular[t])
	angulo[t] += variacaodetempo*velocidadeangular[t]

	Cm.append(f.callCm(alpha[t],coifadiametro,arearef,coifadiametro,foguetecomprimento,foguetevolume))
	CDdamping.append(f.callCDdamping (CPaleta, CG, aletaareamolhada,arearef,coifadiametro,foguetecomprimento,corpodiametro/2,velocidadeangular,modvelocidade))
	
	atitudex.append(sin(angulo[t]))
	atitudey.append(cos(angulo[t]))
    
	lancamentoduracao += variacaodetempo
    
	aceleracaox.append((empuxox[t] + arrastox[t])/foguetemassa)
	aceleracaoy.append((empuxoy[t] + pesoy[t] + arrastoy[t])/foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)

	t += 1

motorduracao -= lancamentoduracao


time = time[:-1]
posicaox = posicaox[:-1]
posicaoy = posicaoy[:-1]
velocidadex = velocidadex[:-1]
velocidadey = velocidadey[:-1]
aceleracaox = aceleracaox[:-1]
aceleracaoy = aceleracaoy[:-1]
empuxox = empuxox[:-1]
empuxoy = empuxoy[:-1]
arrastox = arrastox[:-1]
arrastoy = arrastoy[:-1]
pesoy = pesoy[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CDdamping = CDdamping[:-1]
velocidadeangular = velocidadeangular[:-1]
aceleracaoangular = aceleracaoangular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
windspeed= windspeed[:-1]
velocidaderelativax = velocidaderelativax[:-1]
velocidaderelativay = velocidaderelativay[:-1]
t -= 1



#voo impulsionado


vooimpulsionadoduracao = 0


while motorduracao >= 0:
    
    
	if vooimpulsionado == False:
		break

	print('b')

	windspeed.append(f.callwind(posicaoy[t]))
    
	modvelocidade = f.callmod(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modaceleracao = f.callmod(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modatitude = f.callmod(atitudex[t],atitudey[t])
	Mach = modvelocidade/c

	CD.append(f.callCDfriction(arearef,aletaareamolhada,Rcri,fitnessratio,corpoareamolhada,aletaespessura,reynoldsnumero,Rs,foguetecomprimento,Mach) + f.callCDcoifa(coifadiametro,coifacomprimento) + f.callCDtubeira(Mach))

	velocidaderelativax.append(velocidadex[t]-windspeed[t])
	velocidaderelativay.append(velocidadey[t])
	velocidaderelativa = [velocidaderelativax[t],velocidaderelativay[t]]

	modempuxo = f.callmod(empuxox[t],empuxoy[t])

	empuxox[t] = -modempuxo*sin(angulo[t])
	empuxoy[t] = modempuxo*cos(angulo[t])

	arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((-velocidadey[t]/modvelocidade)*arrastomodulo)
	except:
		arrastox.append(0)
		arrastoy.append(0)
        
	try:
		empuxox.append((velocidadex[t]/modvelocidade)*modempuxo)
		empuxoy.append((velocidadey[t]/modvelocidade)*modempuxo)
	except:
		empuxox.append(0)
		empuxoy.append(0)

	foguetemassa -= motormassa/8000
	pesoy.append((-(terramassa*foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	q = 1/2*(ardensidade * modvelocidade**2)


	if np.cross(vetorreferencia,atitude) >= 0:
		angulo.append(f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))

	else:
		angulo.append(-f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))
        
	if np.cross(velocidaderelativa,atitude) >= 0:
		alpha.append(f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))
	else:
		alpha.append(-f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))

	momento.append((Cm[t] + CDdamping[t])*q*coifadiametro)

	aceleracaoangular.append(momento[t]/momentodeinercia)
	velocidadeangular.append(variacaodetempo*aceleracaoangular[t] + velocidadeangular[t])
	angulo[t] += variacaodetempo*velocidadeangular[t]

	Cm.append(f.callCm(alpha[t],coifadiametro,arearef,coifadiametro,foguetecomprimento,foguetevolume))
	CDdamping.append(f.callCDdamping (CPaleta, CG, aletaareamolhada,arearef,coifadiametro,foguetecomprimento,corpodiametro/2,velocidadeangular,modvelocidade))

	if np.cross(vetorreferencia,atitude) >= 0:
		atitudex.append(-sin(angulo[t]))
	else:
		atitudex.append(sin(angulo[t]))
	atitudey.append(cos(angulo[t]))

	vooimpulsionadoduracao += variacaodetempo

	aceleracaox.append((empuxox[t] + arrastox[t])/foguetemassa)
	aceleracaoy.append((empuxoy[t] + arrastoy[t]+pesoy[t])/foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)
	motorduracao -= variacaodetempo
   
	t += 1
    
    
time = time[:-1]
posicaox = posicaox[:-1]
posicaoy = posicaoy[:-1]
velocidadex = velocidadex[:-1]
velocidadey = velocidadey[:-1]
aceleracaox = aceleracaox[:-1]
aceleracaoy = aceleracaoy[:-1]
empuxox = empuxox[:-1]
empuxoy = empuxoy[:-1]
arrastox = arrastox[:-1]
arrastoy = arrastoy[:-1]
pesoy = pesoy[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CDdamping = CDdamping[:-1]
velocidadeangular = velocidadeangular[:-1]
aceleracaoangular = aceleracaoangular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
windspeed= windspeed[:-1]
velocidaderelativax = velocidaderelativax[:-1]
velocidaderelativay = velocidaderelativay[:-1]
t -= 1


   
    
#cabotagem


cabotagemduracao = 0


while velocidadey[t] >= 0:
    
	if vooimpulsionado == False or cabotagem == False:
		break
    
	print('c')

	windspeed.append(f.callwind(posicaoy[t]))

	modvelocidade = f.callmod(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modaceleracao = -f.callmod(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modatitude = f.callmod(atitudex[t],atitudey[t])
	Mach = modvelocidade/c

	pesoy.append((-(terramassa*foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	CD.append(f.callCDfriction(arearef,aletaareamolhada,Rcri,fitnessratio,corpoareamolhada,aletaespessura,reynoldsnumero,Rs,foguetecomprimento,Mach)+f.callCDcoifa (coifadiametro,coifacomprimento)+f.callCDtubeira(Mach))

	arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4

	velocidaderelativax.append(velocidadex[t]-windspeed[t])
	velocidaderelativay.append(velocidadey[t])
	velocidaderelativa = [velocidaderelativax[t],velocidaderelativay[t]]

	try:
		arrastox.append((-velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((-velocidadey[t]/modvelocidade)*arrastomodulo)
	except:
		arrastox.append(0)
		arrastoy.append(0)
        
	empuxox.append(0)
	empuxoy.append(0)

	q = 1/2*(ardensidade * modvelocidade**2)

	if np.cross(vetorreferencia,atitude) >= 0:
		angulo.append(f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))
        
	else:
		angulo.append(-f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))
        
	if np.cross(velocidaderelativa,atitude) >= 0:
		alpha.append(f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))
	else:
		alpha.append(-f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))

	momento.append((Cm[t] + CDdamping[t])*q*coifadiametro)

	aceleracaoangular.append(momento[t]/momentodeinercia)
	velocidadeangular.append(variacaodetempo*aceleracaoangular[t] + velocidadeangular[t])
	angulo[t+1] += variacaodetempo*velocidadeangular[t]

	Cm.append(f.callCm(alpha[t],coifadiametro,arearef,coifadiametro,foguetecomprimento,foguetevolume))
	CDdamping.append(f.callCDdamping(CPaleta, CG, aletaareamolhada, arearef , coifadiametro , foguetecomprimento , corpodiametro/2 , velocidadeangular[t] , modvelocidade))

	if np.cross(vetorreferencia,atitude) >= 0:
		atitudex.append(-sin(angulo[t]))
	else:
		atitudex.append(sin(angulo[t]))
	atitudey.append(cos(angulo[t]))

	cabotagemduracao += variacaodetempo
    
	aceleracaox.append((arrastox[t])/foguetemassa)
	aceleracaoy.append((arrastoy[t]+pesoy[t])/foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo) 
	t += 1



time = time[:-1]
posicaox = posicaox[:-1]
posicaoy = posicaoy[:-1]
velocidadex = velocidadex[:-1]
velocidadey = velocidadey[:-1]
aceleracaox = aceleracaox[:-1]
aceleracaoy = aceleracaoy[:-1]
empuxox = empuxox[:-1]
empuxoy = empuxoy[:-1]
arrastox = arrastox[:-1]
arrastoy = arrastoy[:-1]
pesoy = pesoy[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CDdamping = CDdamping[:-1]
velocidadeangular = velocidadeangular[:-1]
aceleracaoangular = aceleracaoangular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
windspeed= windspeed[:-1]
velocidaderelativax = velocidaderelativax[:-1]
velocidaderelativay = velocidaderelativay[:-1]
t -= 1





#queda livre

quedalivreduracao = 0


while posicaoy[t] >= 0:

	if vooimpulsionado == False or cabotagem == False or quedalivre == False:
		break
    
	print('d')
    
	windspeed.append(f.callwind(posicaoy[t]))    

	modvelocidade = -f.callmod(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modaceleracao = -f.callmod(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modatitude = f.callmod(atitudex[t],atitudey[t])
	Mach = modvelocidade/c

	pesoy.append((-(terramassa*foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	#CD.append(f.callCDfriction(arearef,aletaareamolhada,Rcri,fitnessratio,corpoareamolhada,aletaespessura,reynoldsnumero,Rs,foguetecomprimento,Mach)+f.callCDcoifa (coifadiametro,coifacomprimento)+f.callCDtubeira(Mach))
	CD.append(paraquedasCD)
    
    
	velocidaderelativax.append(velocidadex[t]-windspeed[t])
	velocidaderelativay.append(velocidadey[t])
	velocidaderelativa = [velocidaderelativax[t],velocidaderelativay[t]]
    
	arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4
    
	if modvelocidade == 0:
		arrasto = [0,0]
	else:
		arrasto = [(velocidadex[t]/modvelocidade)*arrastomodulo, (velocidadey[t]/modvelocidade)*arrastomodulo]

	try:
		arrastox.append((velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((velocidadey[t]/modvelocidade)*arrastomodulo)
	except:
		arrastox.append(0)
		arrastoy.append(0)
    
	empuxox.append(0)
	empuxoy.append(0)
        
	q = 1/2*(ardensidade * modvelocidade**2)

	if np.cross(vetorreferencia,atitude) >= 0:
		angulo.append(f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))

	else:
		angulo.append(-f.callalpha(atitudex[t],atitudey[t],vetorreferencia[0],vetorreferencia[1]))

     
	if np.cross(velocidaderelativa,atitude) >= 0:
		alpha.append(f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))
	else:
		alpha.append(-f.callalpha(atitudex[t],atitudey[t],velocidaderelativa[0],velocidaderelativa[1]))

	momento.append((Cm[t] + CDdamping[t])*q*coifadiametro) 

	aceleracaoangular.append(momento[t]/momentodeinercia)
	velocidadeangular.append(variacaodetempo*aceleracaoangular[t] + velocidadeangular[t])
	angulo[t+1] += variacaodetempo*velocidadeangular[t]

	Cm.append(f.callCm(alpha[t],coifadiametro,arearef,coifadiametro,foguetecomprimento,foguetevolume))
	CDdamping.append(f.callCDdamping (CPaleta, CG, aletaareamolhada,arearef,coifadiametro,foguetecomprimento,corpodiametro/2,velocidadeangular,modvelocidade))
	
	if np.cross(vetorreferencia,atitude) >= 0:
		atitudex.append(-sin(angulo[t]))
	else:
		atitudex.append(sin(angulo[t]))
	atitudey.append(cos(angulo[t]))

	quedalivreduracao += variacaodetempo

	aceleracaox.append((arrastox[t])/foguetemassa)
	aceleracaoy.append((arrastoy[t]+pesoy[t])/foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)
    
    
	t += 1




time = time[:-1]
posicaox = posicaox[:-1]
posicaoy = posicaoy[:-1]
velocidadex = velocidadex[:-1]
velocidadey = velocidadey[:-1]
aceleracaox = aceleracaox[:-1]
aceleracaoy = aceleracaoy[:-1]
empuxox = empuxox[:-1]
empuxoy = empuxoy[:-1]
arrastox = arrastox[:-1]
arrastoy = arrastoy[:-1]
pesoy = pesoy[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CDdamping = CDdamping[:-1]
velocidadeangular = velocidadeangular[:-1]
aceleracaoangular = aceleracaoangular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
windspeed = windspeed[:-1]
velocidaderelativax = velocidaderelativax[:-1]
velocidaderelativay = velocidaderelativay[:-1]
t -= 1








plt.figure()

plt.plot(time, posicaoy, label='Height')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Launch height x time')

plt.grid()




plt.figure()

plt.plot(time, posicaox, label='Distance')

plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.title('Distance x time')

plt.grid()




#plt.figure()

#plt.plot(time, velocidadex, label='Horizontal Velocity')

#plt.xlabel('Time (s)')
#plt.ylabel('Horizontal Velocity (m/s)')

#plt.title('Horizontal Velocity x time')

#plt.grid()




plt.figure()

plt.plot(time, velocidadey, label='Vertical Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Velocity (m/s)')

plt.title('Vertical Velocity x time')

plt.grid()




plt.figure()

plt.plot(time, aceleracaox, label='Horizontal Acceleration')

plt.xlabel('Time (s)')
plt.ylabel('Horizontal Acceleration (m/s²)')
plt.title('Horizontal Accelerationt x time')

plt.grid()




plt.figure()

plt.plot(time, aceleracaoy, label='Vertical Acceleration')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Acceleration (m/s²)')
plt.title('Vertical Accelerationt x time')

plt.grid()




plt.figure()

plt.plot(time, empuxox, label='Horizontal Thrust')

plt.xlabel('Time (s)')
plt.ylabel('Horizontal Thrust (N)')
plt.title('Horizontal Thrust x time')

plt.grid()




plt.figure()

plt.plot(time, empuxoy, label='Vertical Thrust')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Thrust (N)')
plt.title('Vertical Thrust x time')

plt.grid()




plt.figure()

plt.plot(time, arrastox, label='Horizontal Drag')

plt.xlabel('Time (s)')
plt.ylabel('Horizontal Drag (N)')
plt.title('Horizontal Drag x time')

plt.grid()




plt.figure()

plt.plot(time, arrastoy, label='Vertical Drag')

plt.plot(time, pesoy, label='Vertical Weight')

plt.plot(time, arrastox, label='Horizontal Drag')

plt.xlabel('Time (s)')
plt.ylabel('Force (N)')

plt.title('Forces x time')

plt.legend()

plt.grid()




plt.figure()

plt.plot(time, CD, label='Drag Coefficient')

plt.xlabel('Time (s)')
plt.ylabel('Drag Coefficient')
plt.title('Drag Coefficient x time')

plt.grid()




plt.figure()

plt.plot(time, momento, label='Moment')

plt.xlabel('Time (s)')
plt.ylabel('Moment')
plt.title('Moment x time')

plt.grid()




plt.figure()

plt.plot(time, alpha, label='Attack angle')

plt.xlabel('Time (s)')
plt.ylabel('Alpha (rad)')
plt.title('Attack angle x time')

plt.grid()




plt.figure()

plt.plot(time, angulo, label='Reference Angle')

plt.xlabel('Time (s)')
plt.ylabel('Reference Angle (rad)')
plt.title('Reference angle x time')

plt.grid()




plt.figure()

plt.plot(time, Cm, label='Moment coefficient')

plt.xlabel('Time (s)')
plt.ylabel('Moment coefficient')
plt.title('Moment coefficient x time')

plt.grid()




plt.figure()

plt.plot(time, CDdamping, label='Damping coefficient')

plt.xlabel('Time (s)')
plt.ylabel('Damping coefficient')
plt.title('Damping coefficient x time')

plt.grid()




plt.figure()

plt.plot(time, velocidadeangular, label='Angular Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity(1/s)')
plt.title('Angular Velocity x time')

plt.grid()




plt.figure()

plt.plot(time, aceleracaoangular, label='Angular Acceleration')

plt.xlabel('Time (s)')
plt.ylabel('Angular Acceleration(1/s²)')
plt.title('Angular Acceleration x time')

plt.grid()




plt.grid()

plt.figure()

plt.plot(time, atitudex, label='Horizontal Atitude')
plt.plot(time, atitudey, label='Vertical Atitude')

plt.xlabel('Time (s)')
plt.ylabel('Atitude')
plt.title('Atitude x time')

plt.grid()




plt.figure()

plt.plot(time, velocidaderelativax, label='Horizontal Relative Velocity')
plt.plot(time, velocidaderelativay, label='Vertical Relative Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Relative Velocity (m/s)')
plt.title('Relative Velocity x time')

plt.grid()




plt.figure()

plt.plot(posicaox, posicaoy, label='Horizontal Relative Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Relative Velocity (m/s)')
plt.title('Relative Velocity x time')

plt.grid()






plt.legend()

plt.show()

aceleracao = open('aceleracao.txt', 'w')
aceleracao.write(f'{aceleracaoy}')
aceleracao.close()

altura = open('altura.txt', 'w')
altura.write(f'{posicaoy}')
altura.close()




print((CP-CG)/coifadiametro)
print(foguetemassa)
print(lancamentoduracao, 's')
print(lancamentoduracao + vooimpulsionadoduracao, 's')
print(lancamentoduracao + vooimpulsionadoduracao + cabotagemduracao,'s')
print(lancamentoduracao + vooimpulsionadoduracao + cabotagemduracao + quedalivreduracao,'s')