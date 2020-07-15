#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-

from math import pi
from math import acos
from math import sin
from math import cos
from math import log1p
from math import fabs
import numpy as np
import matplotlib.pyplot as plt


class Foguete:

	def __init__(self,t,motormassa,coifamassa,corpomassa,corpoespessura,corpodensidade,aletamassa,aletanumero,coifacomprimento,corpodiametro,coifavolumeM,corpovolumeM,posicaoy):
		self.foguetemassa = motormassa + coifamassa + corpomassa + aletamassa*aletanumero
		self.foguetecomprimento = coifacomprimento + corpocomprimento
		self.foguetevolume = coifavolumeM + corpovolumeM
		self.pesoy = [(-(5.972*(10**24)*self.foguetemassa*6.67408*10**-11)/(posicaoy + 6.371*10**6)**2)]
		self.momentodeinercia = pi*corpodensidade*self.foguetecomprimento/12*(3*(corpodiametro/2**4 - ((corpodiametro-corpoespessura)/2)**4) + self.foguetecomprimento**2*((corpodiametro/2)**2 - ((corpodiametro-corpoespessura)/2)**2))

def callmod (vetorx,vetory):
	mod = (vetorx**2 + vetory**2)**0.5
	return mod

#COEFICIENTE DE GRAVIDADE

def callCGcoifa (coifamassaM,coifamassam,coifacomprimento,coifacomprimentomenor):

	CGcoifa = [0,(coifacomprimento*2/3*coifamassaM - coifamassam*(coifacomprimento - coifacomprimentomenor/3))/(coifamassaM + coifamassam)]
	return CGcoifa

def callCGcorpomotor (massamotor,massacorpo,corpocomprimento,coifacomprimento,motorcomprimento):

	CGcorpo = [0 , corpocomprimento/2 + coifacomprimento]
	CGmotor = [0 , coifacomprimento + corpocomprimento - motorcomprimento/2]
	CGcorpomotor = [0 , (CGcorpo[1]*massacorpo + CGmotor[1]*massamotor)/(massacorpo + massamotor)] 
	return CGcorpomotor

def callCGaleta (aletamassa,aletadesvio,aletalargura,aletacomprimentoraiz,aletacomprimentoponta
	,aletadistanciadofundo,coifacomprimento,corpocomprimento):

	CGumaaleta = [0,((aletadesvio*aletalargura/2*param*(2*aletadesvio/3) + 
		aletalargura*(aletacomprimentoraiz - aletadesvio)*param*(aletadesvio+(aletacomprimentoraiz-aletadesvio)/2) + 
		aletalargura*((aletacomprimentoponta + aletadesvio)-aletacomprimentoraiz)/2*param*(aletacomprimentoraiz+(aletacomprimentoponta+aletadesvio-aletacomprimentoraiz)/3))/aletamassa) + 
		coifacomprimento + corpocomprimento - (aletadistanciadofundo + aletacomprimentoraiz)]
	return CGumaaleta

def callCG (CGcoifa,CGcorpomotor,CGaleta,coifamassa,corpomassa,motormassa,aletamassa,
	aletanumero,componentemassa,componentedistancia):
	CG = [0, (CGcoifa*coifamassa + CGcorpomotor*(corpomassa+motormassa) + 
		CGaleta*aletamassa*aletanumero + componentemassa*componentedistancia)/(coifamassa +
		 corpomassa + motormassa + aletamassa*aletanumero + componentemassa)]
	return CG

#COEFICIENTE DE MOMENTO

def callCm (alpha,coifadiametro,foguetecomprimento,foguetevolume):
	try:
		Cm = 2*sin(alpha)/(pi*coifadiametro/2**2)*(foguetecomprimento*(pi*coifadiametro**2/4) - foguetevolume)
	except:
		Cm = 0
	return Cm

#COEFICIENTES DE ARRASTO

def callCDdamping (comprimento,raiomedio,velocidadeangular,velocidade):
	try:
		CDdamping = (0.55*(comprimento**4)*raiomedio*(velocidadeangular*fabs(velocidadeangular)))/(arearef*(coifadiametro/2)*(velocidade**2))
	except:
		CDdamping = 0
	return CDdamping

def callCDfriction (reynoldsnumero,Rs,foguetecomprimento,Mach):
	if reynoldsnumero < 10**4:
		Cf = 1.48*10**-2
	elif 10**4 <= reynoldsnumero <= Rcri:
		Cf = 1/(1.5*log1p(reynoldsnumero) - 5.6)**2
	else:
		Cf = 0.032*(Rs/foguete.foguetecomprimento)**0.2

	Cfc = Cf*(1 - 0.1*Mach**2)

	CDfriction = Cfc*((1 + 1/(2*fitnessratio))*corpoareamolhada*2 + (1 + (2*aletaespessura)/1.5)*aletaareamolhada)/arearef

	return CDfriction

def callCDcoifa (coifadiametro,coifacomprimento):
	CDcoifa = 0.8*(coifadiametro/2)/(coifacomprimento**2 + (coifadiametro/2)**2)**0.5
	return CDcoifa

def callCDtubeira(Mach):
	if Mach < 1:
		CDtubeira = 0.12+0.13*Mach**2
	else:
		CDtubeira = 0.25/Mach
	return CDtubeira

#COEFICIENTE DE FORCA NORMAL

def callCNalpha (arearef,diametrobase,diametrotip,alpha):
	if alpha != 0:
		CNalpha = ((2/arearef)*(pi*(diametrobase/2)**2-pi*(diametrotip/2)**2)*sin(alpha))/alpha
	else:
		CNalpha = (2/arearef)*(pi*(diametrobase/2)**2-pi*(diametrotip/2)**2)
	return CNalpha

#COEFICIENTE DE CENTRO DE PRESSAO

def callCPbody (bodycomprimento,bodydiametroinicial,bodydiametrofinal,bodyvolumeaparente):
	try:
		CPbody = (bodycomprimento*(pi*(bodydiametrofinal/2)**2) - bodyvolumeaparente)/(pi*(bodydiametrofinal/2)**2 - pi*(bodydiametroinicial/2)**2)
	except:
		CPbody = 0
	return CPbody

def callCPaleta (aletadesvio,aletacomprimentoraiz,aletacomprimentoponta):
	CPaleta = aletadesvio/3*(aletacomprimentoraiz + 2*aletacomprimentoponta)/(aletacomprimentoraiz + aletacomprimentoponta) + 1/6*(aletacomprimentoraiz**2 + aletacomprimentoponta**2 + aletacomprimentoraiz*aletacomprimentoponta)/(aletacomprimentoraiz + aletacomprimentoponta)
	return CPaleta

def callCP (CPcoifa,CNalphacoifa,CPcorpo,CNalphacorpo,CPaleta,CNalphaaleta,aletanumero):
	CP = [0,(CPcoifa*CNalphacoifa + CPcorpo*CNalphacorpo + CPaleta*CNalphaaleta*aletanumero)/(CNalphacoifa + CNalphacorpo + aletanumero*CNalphaaleta)]
	return CP

#ANGULO ENTRE DOIS VETORES

def callalpha (vetor10,vetor11,vetor20,vetor21):
	try:
		alpha = (acos(((vetor10*vetor20 + vetor11*vetor21))/
			(((vetor10**2 + vetor11**2)**0.5)*(vetor20**2 + vetor21**2)**0.5)))
	except:
		alpha = 0
	return alpha

#NUMERO DE REYNOLDS

def callRey (velocidademodulo):
	numerodereynolds = ardensidade*velocidademodulo*coifadiametro/viscosidadear
	return numerodereynolds


variacaodetempo = 0.001
t = 0


coifacomprimento = 4*10**-2
#float(input('Insira o comprimento da coifa (cm) '))
coifadiametro = 3*10**-2
#float(input('Insira o dimetro da coifa (cm) '))
coifadensidade = 2700
#float(input('Insira densidade da coifa (Kg/m) '))
coifaespessura = 0.5*10**-2
#float(input('Insira a espessura da coifa (cm) '))
coifacomprimentomenor = (2*coifacomprimento*(coifadiametro/2 - coifaespessura)/coifadiametro)
coifavolumeM = pi*coifacomprimento/3*((coifadiametro/2)**2)
coifavolumem = pi*coifacomprimentomenor/3*((coifadiametro/2 - coifaespessura)**2)
coifamassaM = float(coifadensidade*coifavolumeM)
coifamassam = float(coifadensidade*coifavolumem)
coifamassa = coifamassaM - coifamassam

corpocomprimento = 10*10**-2
#float(input('Insira o comprimento do corpo (cm) '))
corpodiametro = coifadiametro
#corpodensidade = 338
corpodensidade = 2700
#float(input('Insira densidade do corpo (Kg/m) '))
corpoespessura = 0.5*10**-2
#float(input('Insira a espessura do corpo (cm) '))
corpovolumeM = float(((corpodiametro/2)**2))*corpocomprimento*pi
corpovolumem = float(((corpodiametro/2-corpoespessura)**2))*corpocomprimento*pi
corpomassaM = float(corpodensidade*(corpovolumeM))
corpomassam = float(corpodensidade*(corpovolumem))
corpomassa = corpomassaM - corpomassam
corpoareamolhada = corpodiametro*corpocomprimento

aletacomprimentoraiz = 2*10**-2
#float(input('Insira o comprimento das raiz da aletas (cm) '))
aletacomprimentoponta = 1*10**-2
#float(input('Insira o comprimento das ponta da aletas (cm) '))
aletadesvio = 1*10**-2
#float(input('Insira o desvio vertical entre a ponta e a raiz das aletas (cm) '))
aletalargura = 1*10**-2
#float(input('Insira a largura das aletas (cm) '))
aletaespessura = 0.1*10**-2
#float(input('Insira a espessura das aletas (cm) '))
aletanumero = 3
#float(input('Insira a quantidade de aletas '))
aletadistanciadofundo = 0*10**-2 
#float(input('Insira a distancia do fundo das aletas para o fundo do foguete (cm) '))
aletadensidade = 2700
#float(input('Insira densidade das aletas (Kg/m) '))
aletamassa = float(aletadensidade*aletaespessura*((aletacomprimentoponta + aletacomprimentoraiz)*aletalargura/2))
param = aletaespessura*aletadensidade
aletaareamolhada = (aletacomprimentoponta + aletacomprimentoraiz)*aletalargura/2
AR = 2*(aletalargura**(2))/aletaareamolhada

componentemassa = 1
componentedistancia = coifadiametro

arearef = pi*(coifadiametro/2)**2
Rs = 200*10**-6

motorcomprimento = 4*10**-2
motordiametro = 2*10**-2
motormassa = 0.5
motorduracao = 0.5
empuxox = [0]
empuxoy = [90]

#insira valores no SI
terramassa = 5.972*(10**24)
ardensidade = 1.225
viscosidadear = 1.8*10**-5
c = 340.29

posicaox = [0]
posicaoy = [0]

foguete = Foguete(t,motormassa,coifamassa,corpomassa,corpoespessura,corpodensidade,aletamassa,aletanumero,coifacomprimento,corpodiametro,coifavolumeM,corpovolumeM,posicaoy[t])

Rcri = 51*(Rs/foguete.foguetecomprimento)**(-1.039)
fitnessratio = foguete.foguetecomprimento/corpodiametro

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
modvetorreferencia = callmod(vetorreferencia[0],vetorreferencia[1])

velocidadex = [0]
velocidadey = [0]
velocidade = [velocidadex[t],velocidadey[t]]
modvelocidade = callmod(velocidadex[t],velocidadey[t])

aceleracaox = [0]
aceleracaoy = [0]
aceleracao = [aceleracaox[t],aceleracaoy[t]]

CD = [0]

comprimentodahaste = 2
q = 1/2*(ardensidade * modvelocidade**2)

CGcoifa = callCGcoifa(coifamassaM, coifamassam, coifacomprimento,coifacomprimentomenor)
CGcorpomotor = callCGcorpomotor(motormassa,corpomassa,corpocomprimento, coifacomprimento,motorcomprimento)
CGaleta = callCGaleta(aletamassa, aletadesvio, aletalargura, aletacomprimentoraiz, aletacomprimentoponta, aletadistanciadofundo,coifacomprimento,corpocomprimento)

CG = callCG(CGcoifa[1],CGcorpomotor[1],CGaleta[1],coifamassa,corpomassa,motormassa,aletamassa,aletanumero,componentemassa,componentedistancia)

if np.cross(vetorreferencia,atitude) >= 0:
	angulo = [callalpha(atitude[0],atitude[1],vetorreferencia[0],vetorreferencia[1])]
else:
	angulo = [-callalpha(atitude[0],atitude[1],vetorreferencia[0],vetorreferencia[1])]
    
if np.cross(velocidade,atitude) >= 0:
	alpha = [callalpha(atitude[0],atitude[1],velocidade[0],velocidade[1])]
else:
	alpha = [-callalpha(atitude[0],atitude[1],velocidade[0],velocidade[1])]

CNalphacoifa = callCNalpha(arearef,coifadiametro,0,alpha[t])

CNalphacorpo = callCNalpha(arearef,corpodiametro,corpodiametro,alpha[t])


CPcoifa = callCPbody (coifacomprimento,0,coifadiametro,coifavolumeM - coifavolumem)

CPcorpo = callCPbody (corpocomprimento,corpodiametro,corpodiametro,corpovolumeM - corpovolumem) + coifacomprimento

CPaleta = callCPaleta(aletadesvio,aletacomprimentoraiz,aletacomprimentoponta) + corpocomprimento + coifacomprimento - aletacomprimentoraiz

CNalphaaleta = (2*pi*AR*(aletaareamolhada/arearef))/(2+(4+(((((modvelocidade/c)**2 - 1)**2)**(1/4))*AR/cos(pi/6))**2))

CP = callCP(CPcoifa,CNalphacoifa,CPcorpo,CNalphacorpo,CPaleta,CNalphaaleta,aletanumero)

if CP[1] < CG[1]:
	print('Configuracao instavel')
else:
	print('Configuracao estavel')

Cm = [callCm(alpha[t],coifadiametro,foguete.foguetecomprimento,foguete.foguetevolume)]
CDdamping = [callCDdamping(foguete.foguetecomprimento,corpodiametro/2,velocidadeangular,modvelocidade)]

reynoldsnumero = callRey(modvelocidade)





#lancamento




while posicaoy[t] <= comprimentodahaste:

	print('a')
    
	modvelocidade = callmod(velocidadex[t],velocidadey[t])
	modempuxo = callmod(empuxox[t],empuxoy[t])

	Mach = modvelocidade/c

	CD.append(callCDfriction (reynoldsnumero,Rs,foguete.foguetecomprimento,Mach)+callCDcoifa (coifadiametro,coifacomprimento)+callCDtubeira(Mach))

	if modvelocidade == 0:
		arrastomodulo = 0
	else:
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

	foguete.pesoy.append((-(terramassa*foguete.foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))
        
	aceleracaox.append((empuxox[t] + arrastox[t])/foguete.foguetemassa)
	aceleracaoy.append((empuxoy[t] + foguete.pesoy[t] + arrastoy[t])/foguete.foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	lancamentoduracao = t*variacaodetempo
	time.append(t*variacaodetempo)
	t += 1

motorduracao -= lancamentoduracao







#voo impulsionado






while motorduracao >= 0:

	print('b')
    
	modvelocidade = callmod(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modaceleracao = callmod(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	Mach = modvelocidade/c

	CD.append(callCDfriction (reynoldsnumero,Rs,foguete.foguetecomprimento,Mach)+callCDcoifa (coifadiametro,coifacomprimento)+callCDtubeira(Mach))

	if modvelocidade == 0:
		arrastomodulo = 0
	else:
		arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4
    
	modempuxo = callmod(empuxox[t],empuxoy[t])

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

	foguete.pesoy.append((-(terramassa*foguete.foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	q = 1/2*(ardensidade * modvelocidade**2)


	vooimpulsionadoduracao = t*variacaodetempo

	aceleracaox.append((empuxox[t] + arrastox[t])/foguete.foguetemassa)
	aceleracaoy.append((empuxoy[t] + arrastoy[t]+foguete.pesoy[t])/foguete.foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)
	motorduracao -=  variacaodetempo
	t += 1
    
    
    
#cabotagem






while velocidadey[t] >= 0:

	print('c')
    
	modvelocidade = callmod(velocidadex[t],velocidadey[t])
	modatitude = callmod(atitude[0],atitude[1])
	Mach = modvelocidade/c

	foguete.pesoy.append((-(terramassa*foguete.foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	CD.append(callCDfriction (reynoldsnumero,Rs,foguete.foguetecomprimento,Mach)+callCDcoifa (coifadiametro,coifacomprimento)+callCDtubeira(Mach))

	if modvelocidade == 0:
		arrastomodulo = 0
	else:
		arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((-velocidadey[t]/modvelocidade)*arrastomodulo)
	except:
		arrastox.append(0)
		arrastoy.append(0)
        
	empuxox.append(0)
	empuxoy.append(0)

	q = 1/2*(ardensidade * modvelocidade**2)

	aceleracaox.append((arrastox[t])/foguete.foguetemassa)
	aceleracaoy.append((arrastoy[t]+foguete.pesoy[t])/foguete.foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)
	cabotagemduracao = t*variacaodetempo
	t += 1




#queda livre




while posicaoy[t] >= 0:

	print('d')
    
	modvelocidade = callmod(velocidadex[t],velocidadey[t])
	modatitude = callmod(atitude[0],atitude[1])
	Mach = modvelocidade/c

	foguete.pesoy.append((-(terramassa*foguete.foguetemassa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	CD.append(callCDfriction (reynoldsnumero,Rs,foguete.foguetecomprimento,Mach)+callCDcoifa (coifadiametro,coifacomprimento)+callCDtubeira(Mach))

	if modvelocidade == 0:
		arrastomodulo = 0
	else:
		arrastomodulo = (CD[t])*q*pi*(coifadiametro)**2/4
    
	if modvelocidade == 0:
		arrasto = [0,0]
	else:
		arrasto = [(-velocidadex[t]/modvelocidade)*arrastomodulo, (-velocidadey[t]/modvelocidade)*arrastomodulo]

	try:
		arrastox.append((-velocidadex[t]/modvelocidade)*arrastomodulo)
		arrastoy.append((-velocidadey[t]/modvelocidade)*arrastomodulo)
	except:
		arrastox.append(0)
		arrastoy.append(0)

    
	empuxox.append(0)
	empuxoy.append(0)
        
	q = 1/2*(ardensidade * modvelocidade**2)


	quedalivreduracao = t*variacaodetempo

	aceleracaox.append((arrastox[t])/foguete.foguetemassa)
	aceleracaoy.append((arrastoy[t]+foguete.pesoy[t])/foguete.foguetemassa)
	velocidadex.append(variacaodetempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacaodetempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacaodetempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacaodetempo*velocidadey[t] + posicaoy[t])
	time.append(t*variacaodetempo)
	t += 1


plt.figure()

plt.plot(time, posicaoy, label='Height')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Launch height x time')

plt.grid()




plt.figure()

plt.plot(time, velocidadey, label='Vertical Velocity ')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Velocity (m/s)')
plt.title('Vertical Velocity x time')

plt.grid()






plt.figure()

plt.plot(time, velocidadex, label='Horizontal Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Horizontal Velocity (m/s)')

plt.title('Horizontal Velocity x time')

plt.grid()




plt.figure()

plt.plot(time, arrastoy, label='Vertical Drag')

plt.plot(time, foguete.pesoy, label='Vertical Weight')

plt.plot(time, arrastox, label='Horizontal Drag')

plt.xlabel('Time (s)')
plt.ylabel('Force (N)')


plt.title('Forces x time')

plt.legend()

plt.grid()





plt.figure()

plt.plot(time, empuxoy, label='Vertical Thrust')

plt.plot(time, empuxox, label='Horizontal Thrust')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Thrust (N)')
plt.title('Vertical Thrust x time')

plt.grid()



plt.figure()

plt.plot(time, CD, label='Drag Coefficient')

plt.xlabel('Time (s)')
plt.ylabel('Drag Coefficient')
plt.title('Drag Coefficient x time')

plt.grid()


plt.figure()

plt.plot(time, aceleracaox, label='Horizontal Acceleration')

plt.xlabel('Time (s)')
plt.ylabel('Horizontal Acceleration')
plt.title('Horizontal Accelerationt x time')

plt.grid()






plt.figure()

plt.plot(time, aceleracaoy, label='Vertical Acceleration')

plt.xlabel('Time (s)')
plt.ylabel('Vertical Acceleration')
plt.title('Vertical Accelerationt x time')

plt.grid()




plt.show()
