#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi,sin,cos
import numpy as np
#import matplotlib.pyplot as plt
import funcoes as f

'''
Integração dos valores digitados na interface ao programa

Funcional para configuraçãoes com até dois corpos e apenas um de cada um dos outros componentes
'''

#abertura de arquivo e passagem de dados para lista "armazenamento"
armazenamento = []

with open("desenho.txt","r") as arquivo:
    for i in arquivo.readlines():
        armazenamento.append(i[:-1])

arquivo.close()

#método de identificar se os valores de corpo se referem ao primeiro ou segundo corpo do foguete
corpo_diametro = 0
corpo_comprimento = 0
corpo_espessura = 0
corpo_densidade = 0

componente_de_massa_massa = 0
componente_de_massa_distancia = 0

#transferência dos dados da lista "armazenamento" para declaração de variáveis
for i in armazenamento:
	if i == 'c0':
		coifa_tipo = float(armazenamento[armazenamento.index(i)+1] )*10**-2    
	elif i == 'c1':
		coifa_diametro = float(armazenamento[armazenamento.index(i)+1] )*10**-2
	elif i == 'c2':
		coifa_comprimento = float(armazenamento[armazenamento.index(i)+1] )*10**-2 
	elif i == 'c3':
		coifa_espessura = float(armazenamento[armazenamento.index(i)+1] )*10**-2
	elif i == 'c4':
		coifa_densidade = float(armazenamento[armazenamento.index(i)+1] ) 
	elif i == 'cp1':
		if corpo_diametro == 0:
			corpo_diametro = float(armazenamento[armazenamento.index(i)+1] )*10**-2 
		else:
			corpo2_diametro = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 'cp2':
		if corpo_comprimento == 0:
			corpo_comprimento = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
		else:
			corpo2_comprimento = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 'cp3':
		if corpo_espessura == 0:
			corpo_espessura = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
		else:
			corpo2_espessura = float(armazenamento[armazenamento.index(i)+1] )*10**-2 
	elif i == 'cp4':
		if corpo_densidade == 0:
			corpo_densidade = float(armazenamento[armazenamento.index(i)+1] )  
		else:
			corpo2_densidade = float(armazenamento[armazenamento.index(i)+1] ) 
	elif i == 'm1':
		componente_de_massa_massa = float(armazenamento[armazenamento.index(i)+1] )   
	elif i == 'm2':
		componente_de_massa_distancia = float(armazenamento[armazenamento.index(i)+1] )*10**-2   
	elif i == 'p1':
		paraquedas_massa = float(armazenamento[armazenamento.index(i)+1] )  
	elif i == 'p2':
		paraquedas_CD = float(armazenamento[armazenamento.index(i)+1] ) 
	elif i == 'mt1':
		motor_empuxo = float(armazenamento[armazenamento.index(i)+1] )       
	elif i == 'mt2':
		motor_massa = float(armazenamento[armazenamento.index(i)+1] ) 
	elif i == 'mt3':
		motor_duracao = float(armazenamento[armazenamento.index(i)+1] )    
	elif i == 'mt4':
		motor_comprimento = float(armazenamento[armazenamento.index(i)+1] )*10**-2    
	elif i == 'g1':
		guia_CD = float(armazenamento[armazenamento.index(i)+1] )     
	elif i == 't1':
		transicao_diametro_inicial = float(armazenamento[armazenamento.index(i)+1] )*10**-2    
	elif i == 't2':
		transicao_comprimento = float(armazenamento[armazenamento.index(i)+1] )*10**-2    
	elif i == 't3':
		transicao_diametro_final = float(armazenamento[armazenamento.index(i)+1] )*10**-2     
	elif i == 't4':
		transicao_espessura = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 't5':
		transicao_densidade = float(armazenamento[armazenamento.index(i)+1] )  
	elif i == 'a1':
		aleta_comprimento_raiz = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 'a2':
		aleta_comprimento_ponta = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 'a3':
		aleta_desvio = float(armazenamento[armazenamento.index(i)+1] )*10**-2
	elif i == 'a4':
		aleta_largura = float(armazenamento[armazenamento.index(i)+1] )*10**-2 
	elif i == 'a5':
		aleta_espessura = float(armazenamento[armazenamento.index(i)+1] )*10**-2
	elif i == 'a6':
		aleta_quantidade = float(armazenamento[armazenamento.index(i)+1] )  
	elif i == 'a7':
		aleta_distancia_do_fundo = float(armazenamento[armazenamento.index(i)+1] )*10**-2  
	elif i == 'a8':
		aleta_densidade = float(armazenamento[armazenamento.index(i)+1] )  

#variáveis auxiliares de passagem de tempo

variacao_de_tempo = 0.002
t = 0

#propriedades dos componentes calculadas em função do que foi recebido pelo arquivo

coifa_volume = pi*coifa_comprimento/3*((coifa_diametro/2)**2)
coifa_massa = float(coifa_densidade*coifa_volume)    

corpo_volume_maior = float(((corpo_diametro/2)**2))*corpo_comprimento*pi
corpo_volume_menor = float(((corpo_diametro/2-corpo_espessura)**2))*corpo_comprimento*pi
corpo_massa_maior = float(corpo_densidade*(corpo_volume_maior))
corpo_massa_menor = float(corpo_densidade*(corpo_volume_menor))
corpo_massa = corpo_massa_maior - corpo_massa_menor
corpo_area_molhada = corpo_diametro*corpo_comprimento

transicao_volume_maior = pi*transicao_comprimento*(transicao_diametro_inicial**2 + transicao_diametro_inicial*transicao_diametro_final + transicao_diametro_final**2)/12
transicao_volume_menor = pi*transicao_comprimento*((transicao_diametro_inicial - 2*transicao_espessura)**2 + (transicao_diametro_inicial - 2*transicao_espessura)*(transicao_diametro_final - 2*transicao_espessura) + (transicao_diametro_final-2*transicao_espessura)**2)/12
transicao_massa_maior = transicao_volume_maior*transicao_densidade
transicao_massa_menor = transicao_volume_menor*transicao_densidade
transicao_massa = transicao_massa_maior - transicao_massa_menor
transicao_area_molhada = transicao_comprimento*(transicao_diametro_inicial + transicao_diametro_final)

corpo2_volume_maior = float(((corpo2_diametro/2)**2))*corpo2_comprimento*pi
corpo2_volume_menor = float(((corpo2_diametro/2-corpo2_espessura)**2))*corpo2_comprimento*pi
corpo2_massa_maior = float(corpo2_densidade*(corpo2_volume_maior))
corpo2_massa_menor = float(corpo2_densidade*(corpo2_volume_menor))
corpo2_massa = corpo2_massa_maior - corpo2_massa_menor
corpo2_area_molhada = corpo2_diametro*corpo2_comprimento

aleta_massa = float(aleta_densidade*aleta_espessura*((aleta_comprimento_ponta + aleta_comprimento_raiz)*aleta_largura/2))
aleta_area_molhada = (aleta_comprimento_ponta + aleta_comprimento_raiz)*aleta_largura/2
AR = (2*aleta_largura**2)/aleta_area_molhada

area_de_referencia = pi*(coifa_diametro/2)**2

#normalização do empuxo inicial
empuxox = [0]
empuxoy = [0]
empuxoz = [motor_empuxo]
empuxo = np.arrat([empuxox[t],empuxoy[t],empuxoz[t]])

#constantes
Terra_massa = 5.972*(10**24)
Ar_densidade = 1.225
Ar_viscosidade = 1.8*10**-5
#velocidade do som
C = 340.29
#Altura média aproximada da rugosidade da superfície
Rs = 200*10**-6
#haste de lançamento
comprimento_da_haste = 2

posicaox = [0]
posicaoy = [0]
posicaoz = [0]
posicao = np.array([posicaox[t],posicaoy[t],posicaoz[t]])

#variáveis referentes ao foguete completo
foguete_massa = motor_massa + coifa_massa + corpo_massa + transicao_massa + corpo2_massa + componente_de_massa_massa + aleta_massa*aleta_quantidade
foguete_comprimento = coifa_comprimento + corpo_comprimento + transicao_comprimento + corpo2_comprimento
foguete_volume = coifa_volume + corpo_volume_maior + transicao_volume_maior + corpo2_volume_maior + aleta_area_molhada*aleta_espessura*aleta_quantidade
peso = [(-(5.972*(10**24)*foguete_massa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2)]
momento_de_inercia = pi*corpo_densidade*foguete_comprimento/12*(3*(corpo_diametro/2**4 - ((corpo_diametro-corpo_espessura)/2)**4) + foguete_comprimento**2*((corpo_diametro/2)**2 - ((corpo_diametro-corpo_espessura)/2)**2))
#Reynolds Crítico
Rcri = 51*(Rs/foguete_comprimento)**(-1.039)
fitnessratio = foguete_comprimento/corpo_diametro

#listas usadas para armazenamentos das variáveis em cada instante da trajetória, permite a criação dos gráficos
arrastox = [0]
arrastoy = [0]
arrastoz = [0]
arrasto = np.linalg.norm([arrastox[t],arrastoy[t],arrastoz[t]])

atitudex = [0]
atitudey = [0]
atitudez = [1]
atitude = np.array([atitudex[t],atitudey[t],atitudez[t]])

#vetor estático durante todo o voo 
vetor_de_referencia = [0,0,1]
modulo_vetor_de_referencia = np.linalg.norm(vetor_de_referencia[0],vetor_de_referencia[1])

velocidadex = [0]
velocidadey = [0]
velocidade = np.linalg.norm([velocidadex[t],velocidadey[t]])
modulo_da_velocidade = np.linalg.norm(velocidadex[t],velocidadey[t])

velocidade_relativax = [0]
velocidade_relativay = [0]
velocidade_relativa = np.array([velocidade_relativax[t],velocidade_relativay[t]])

aceleracaox = [0]
aceleracaoy = [0]
aceleracaoz = [0]
aceleracao = np.array([aceleracaox[t],aceleracaoy[t]])

velocidade_do_vento = [0]

CD = [0]

#componente repetida no cálculo de todos os coeficientes
q = 1/2*(Ar_densidade * modulo_da_velocidade**2)

#cálculo dos centros de gravidade de cada componente e do foguete completo
CG_coifa = f.callCGcoifa(coifa_massa, 0, coifa_comprimento,0)
CG_corpo = coifa_comprimento + corpo_comprimento/2
CG_transicao = coifa_comprimento + corpo_comprimento + (transicao_massa_menor*f.callCGtransicao(transicao_comprimento, transicao_diametro_inicial, transicao_diametro_final, transicao_densidade) - transicao_massa_menor*f.callCGtransicao(transicao_comprimento, transicao_diametro_inicial - 2*transicao_espessura, transicao_diametro_final - 2*transicao_espessura, transicao_densidade))/(transicao_massa_maior - transicao_massa_menor)
CG_corpo2_motor = coifa_comprimento + corpo_comprimento + transicao_comprimento + f.callCGcorpomotor(motor_massa,corpo2_massa,corpo2_comprimento,motor_comprimento)
CG_aleta = coifa_comprimento + corpo_comprimento + transicao_comprimento + corpo2_comprimento - (aleta_distancia_do_fundo + aleta_comprimento_raiz) + f.callCGaleta(aleta_espessura*aleta_densidade, aleta_massa, aleta_desvio, aleta_largura, aleta_comprimento_raiz, aleta_comprimento_ponta, aleta_distancia_do_fundo)

CG = f.callCG(CG_coifa,CG_corpo,CG_corpo2_motor,CG_transicao,CG_aleta,coifa_massa,corpo_massa,corpo2_massa,motor_massa,aleta_massa,aleta_quantidade,componente_de_massa_massa,componente_de_massa_distancia,transicao_massa)

#cálculo dos coeficientes normais para alpha = 0
CNalphacoifa = f.callCNalpha(area_de_referencia,coifa_diametro,0,0)

CNalphacorpo = f.callCNalpha(area_de_referencia,corpo_diametro,corpo_diametro,0)

CNalphatransicao = f.callalpha(area_de_referencia,transicao_diametro_inicial,transicao_diametro_final,0)

CNalphacorpo2 = f.callCNalpha(area_de_referencia,corpo2_diametro,corpo2_diametro,0)

CNalphaumaaleta = (2*pi*AR*(aleta_area_molhada/area_de_referencia))/(2+(4+(((((modulo_da_velocidade/C)**2 - 1)**2)**(1/4))*AR/cos(pi/6))**2))

CNalphaaleta = aleta_quantidade*CNalphaumaaleta/2

#cálculo dos centros de pressão de cada componente e do foguete completo
CPcoifa = f.callCPbody (coifa_comprimento,0,coifa_diametro,coifa_volume)

CPcorpo = f.callCPbody (corpo_comprimento,corpo_diametro,corpo_diametro,corpo_volume_maior) + coifa_comprimento

CPtransicao = f.callCPbody (transicao_comprimento, transicao_diametro_inicial, transicao_diametro_final, transicao_volume_maior) + corpo_comprimento + coifa_comprimento

CPcorpo2 = f.callCPbody (corpo2_comprimento,corpo2_diametro,corpo2_diametro,corpo2_volume_maior) + transicao_comprimento + corpo_comprimento + coifa_comprimento

CPaleta = f.callCPaleta (aleta_desvio,aleta_comprimento_raiz,aleta_comprimento_ponta)  + corpo2_comprimento + transicao_comprimento + corpo_comprimento + coifa_comprimento - aleta_comprimento_raiz

CP = (CNalphacoifa*CPcoifa + CNalphacorpo*CPcorpo + CNalphatransicao*CPtransicao + CNalphacorpo2*CPcorpo2 + CNalphaaleta*CPaleta)/(CNalphacoifa + CNalphacorpo + CNalphatransicao + CNalphacorpo2 + CNalphaaleta)

#coeficientes de momento e arrasto de amortecimento usados para cálculo da rotação
Cm = [f.callCm(alpha[t],coifa_diametro,area_de_referencia,coifa_diametro,foguete_comprimento,foguete_volume)]
CD_damping = [f.callCD_damping (CPaleta, CG, aleta_area_molhada,area_de_referencia,coifa_diametro,foguete_comprimento,corpo_diametro/2,velocidade_angular,modulo_da_velocidade)]

reynolds_numero = f.callRey(Ar_densidade,coifa_diametro, Ar_viscosidade,modulo_da_velocidade)

#facilitador de debug por selecionar até onde a simulação deve rodar
voo_impulsionado = True
cabotagem = True
queda_livre = True

#acumuladores de duração
lancamentoduracao = 0
voo_impulsionadoduracao = 0
cabotagemduracao = 0
queda_livre_duracao = 0


#Segue a execução do método de Euler para cada etapa do voo

#lancamento

while posicaoy[t] <= comprimento_da_haste:
    
	print('a')
    
    #cálculo de módulos das derivadas de posiçao e variáveis de estado
	velocidade_do_vento.append(f.callwind(posicaoy[t]))
	reynolds_numero = f.callRey(Ar_densidade,coifa_diametro, Ar_viscosidade, modulo_da_velocidade)
	modulo_da_velocidade = np.linalg.norm(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modulo_de_aceleracao = np.linalg.norm(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modulo_de_atitude = np.linalg.norm(atitudex[t],atitudey[t])
	Mach = modulo_da_velocidade/C
    
    
    #cálculo da velocidade do foguete em relação ao vento
	velocidade_relativax.append(velocidadex[t]-velocidade_do_vento[t])
	velocidade_relativay.append(velocidadey[t])
	velocidade_relativa = [velocidade_relativax[t],velocidade_relativay[t]]

    #calculo das forças
	modempuxo = np.linalg.norm(empuxox[t],empuxoy[t])

	CD.append(f.callCDfriction(area_de_referencia,aleta_area_molhada,Rcri,fitnessratio,corpo_area_molhada,aleta_espessura,reynolds_numero,Rs,foguete_comprimento,Mach) + f.callCDcoifa(coifa_diametro,coifa_comprimento) + f.callCDtubeira(Mach))

	modulo_do_arrasto = (CD[t])*q*pi*(coifa_diametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modulo_da_velocidade)*modulo_do_arrasto)
		arrastoy.append((-velocidadey[t]/modulo_da_velocidade)*modulo_do_arrasto)

	except:
		arrastox.append(0)
		arrastoy.append(0)

	try:
		empuxox.append((velocidadex[t]/modulo_da_velocidade)*modempuxo)
		empuxoy.append((velocidadey[t]/modulo_da_velocidade)*modempuxo)
	except:
		empuxox.append(empuxox[t])
		empuxoy.append(empuxoy[t])
        
	foguete_massa -= motor_massa/8000
	peso.append((-(Terra_massa*foguete_massa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))
        
	q = 1/2*(Ar_densidade * modulo_da_velocidade**2)
    
    #armazena duração total da etapa ao final do programa
	lancamentoduracao += variacao_de_tempo
    
    #cálculo das derivadas de posição
	aceleracaox.append((empuxox[t] + arrastox[t])/foguete_massa)
	aceleracaoy.append((empuxoy[t] + peso[t] + arrastoy[t])/foguete_massa)
	velocidadex.append(variacao_de_tempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacao_de_tempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacao_de_tempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacao_de_tempo*velocidadey[t] + posicaoy[t])

    #auxiliar de passagem de tempo
	t += 1

#retira o tempo de queima já gasto
motor_duracao -= lancamentoduracao

#solução deselegante para um bug que ocorria na impressão dos gráficos ao fim de casa etapa
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
peso = peso[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CD_damping = CD_damping[:-1]
velocidade_angular = velocidade_angular[:-1]
aceleracao_angular = aceleracao_angular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
velocidade_do_vento = velocidade_do_vento[:-1]
velocidade_relativax = velocidade_relativax[:-1]
velocidade_relativay = velocidade_relativay[:-1]
t -= 1


#voo impulsionado

while motor_duracao >= 0:
    
	if voo_impulsionado == False:
		break

	print('b')

    #cálculo de módulos das derivadas de posiçao e variáveis de estado
	velocidade_do_vento.append(f.callwind(posicaoy[t]))
	reynolds_numero = f.callRey(Ar_densidade,coifa_diametro, Ar_viscosidade, modulo_da_velocidade)
	modulo_da_velocidade = np.linalg.norm(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modulo_de_aceleracao = np.linalg.norm(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modulo_de_atitude = np.linalg.norm(atitudex[t],atitudey[t])
	Mach = modulo_da_velocidade/C

    #cálculo da velocidade do foguete em relação ao vento
	velocidade_relativax.append(velocidadex[t]-velocidade_do_vento[t])
	velocidade_relativay.append(velocidadey[t])
	velocidade_relativa = [velocidade_relativax[t],velocidade_relativay[t]]

    #calculo das forças
	modempuxo = np.linalg.norm(empuxox[t],empuxoy[t])

	empuxox[t] = -modempuxo*sin(angulo[t])
	empuxoy[t] = modempuxo*cos(angulo[t])

	CD.append(f.callCDfriction(area_de_referencia,aleta_area_molhada,Rcri,fitnessratio,corpo_area_molhada,aleta_espessura,reynolds_numero,Rs,foguete_comprimento,Mach) + f.callCDcoifa(coifa_diametro,coifa_comprimento) + f.callCDtubeira(Mach))


	modulo_do_arrasto = (CD[t])*q*pi*(coifa_diametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modulo_da_velocidade)*modulo_do_arrasto)
		arrastoy.append((-velocidadey[t]/modulo_da_velocidade)*modulo_do_arrasto)
	except:
		arrastox.append(0)
		arrastoy.append(0)
        
	try:
		empuxox.append((velocidadex[t]/modulo_da_velocidade)*modempuxo)
		empuxoy.append((velocidadey[t]/modulo_da_velocidade)*modempuxo)
	except:
		empuxox.append(0)
		empuxoy.append(0)

	foguete_massa -= motor_massa/8000
	peso.append((-(Terra_massa*foguete_massa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	q = 1/2*(Ar_densidade * modulo_da_velocidade**2)

    #armazena duração total da etapa ao final do programa
	voo_impulsionadoduracao += variacao_de_tempo

    #cálculo das derivadas de posição
	aceleracaox.append((empuxox[t] + arrastox[t])/foguete_massa)
	aceleracaoy.append((empuxoy[t] + arrastoy[t]+peso[t])/foguete_massa)
	velocidadex.append(variacao_de_tempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacao_de_tempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacao_de_tempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacao_de_tempo*velocidadey[t] + posicaoy[t])
	motor_duracao -= variacao_de_tempo
   
    #auxiliar de passagem de tempo
	t += 1
    
#solução deselegante para um bug que ocorria na impressão dos gráficos ao fim de casa etapa 
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
peso = peso[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CD_damping = CD_damping[:-1]
velocidade_angular = velocidade_angular[:-1]
aceleracao_angular = aceleracao_angular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
velocidade_do_vento= velocidade_do_vento[:-1]
velocidade_relativax = velocidade_relativax[:-1]
velocidade_relativay = velocidade_relativay[:-1]
t -= 1

   
#cabotagem

while velocidadey[t] >= 0:
    
	if voo_impulsionado == False or cabotagem == False:
		break
    
	print('c')
    
    #cálculo de módulos das derivadas de posiçao e variáveis de estado
	velocidade_do_vento.append(f.callwind(posicaoy[t]))
	reynolds_numero = f.callRey(Ar_densidade,coifa_diametro, Ar_viscosidade, modulo_da_velocidade)
	modulo_da_velocidade = np.linalg.norm(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modulo_de_aceleracao = -np.linalg.norm(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modulo_de_atitude = np.linalg.norm(atitudex[t],atitudey[t])
	Mach = modulo_da_velocidade/C

    #cálculo da velocidade do foguete em relação ao vento
	velocidade_relativax.append(velocidadex[t]-velocidade_do_vento[t])
	velocidade_relativay.append(velocidadey[t])
	velocidade_relativa = [velocidade_relativax[t],velocidade_relativay[t]]


    #calculo das forças
	CD.append(f.callCDfriction(area_de_referencia,aleta_area_molhada,Rcri,fitnessratio,corpo_area_molhada,aleta_espessura,reynolds_numero,Rs,foguete_comprimento,Mach)+f.callCDcoifa (coifa_diametro,coifa_comprimento)+f.callCDtubeira(Mach))

	modulo_do_arrasto = (CD[t])*q*pi*(coifa_diametro)**2/4

	try:
		arrastox.append((-velocidadex[t]/modulo_da_velocidade)*modulo_do_arrasto)
		arrastoy.append((-velocidadey[t]/modulo_da_velocidade)*modulo_do_arrasto)
	except:
		arrastox.append(0)
		arrastoy.append(0)
        
	empuxox.append(0)
	empuxoy.append(0)

	peso.append((-(Terra_massa*foguete_massa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))

	q = 1/2*(Ar_densidade * modulo_da_velocidade**2)

    #armazena duração total da etapa ao final do programa
	cabotagemduracao += variacao_de_tempo
    
    #cálculo das derivadas de posição
	aceleracaox.append((arrastox[t])/foguete_massa)
	aceleracaoy.append((arrastoy[t]+peso[t])/foguete_massa)
	velocidadex.append(variacao_de_tempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacao_de_tempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacao_de_tempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacao_de_tempo*velocidadey[t] + posicaoy[t])

    #auxiliar de passagem de tempo
	t += 1


#solução deselegante para um bug que ocorria na impressão dos gráficos ao fim de casa etapa
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
peso = peso[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CD_damping = CD_damping[:-1]
velocidade_angular = velocidade_angular[:-1]
aceleracao_angular = aceleracao_angular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
velocidade_do_vento= velocidade_do_vento[:-1]
velocidade_relativax = velocidade_relativax[:-1]
velocidade_relativay = velocidade_relativay[:-1]
t -= 1


#queda livre

while posicaoy[t] >= 0:

	if voo_impulsionado == False or cabotagem == False or queda_livre == False:
		break
    
	print('d')

    #cálculo de módulos das derivadas de posiçao e variáveis de estado
	velocidade_do_vento.append(f.callwind(posicaoy[t]))    
	reynolds_numero = f.callRey(Ar_densidade,coifa_diametro, Ar_viscosidade, modulo_da_velocidade)
	modulo_da_velocidade = -np.linalg.norm(velocidadex[t],velocidadey[t])
	velocidade = [velocidadex[t],velocidadey[t]]
	modulo_de_aceleracao = -np.linalg.norm(aceleracaox[t],aceleracaoy[t])
	aceleracao = [aceleracaox[t],aceleracaoy[t]]
	modulo_de_atitude = np.linalg.norm(atitudex[t],atitudey[t])
	Mach = modulo_da_velocidade/C

    #cálculo da velocidade do foguete em relação ao vento
	velocidade_relativax.append(velocidadex[t]-velocidade_do_vento[t])
	velocidade_relativay.append(velocidadey[t])
	velocidade_relativa = [velocidade_relativax[t],velocidade_relativay[t]]

	#cálculo das forças
	#CD.append(f.callCDfriction(area_de_referencia,aleta_area_molhada,Rcri,fitnessratio,corpo_area_molhada,aleta_espessura,reynolds_numero,Rs,foguete_comprimento,Mach)+f.callCDcoifa (coifa_diametro,coifa_comprimento)+f.callCDtubeira(Mach))
	CD.append(paraquedas_CD)
        
	modulo_do_arrasto = (CD[t])*q*pi*(coifa_diametro)**2/4
    
	if modulo_da_velocidade == 0:
		arrasto = [0,0]
	else:
		arrasto = [(velocidadex[t]/modulo_da_velocidade)*modulo_do_arrasto, (velocidadey[t]/modulo_da_velocidade)*modulo_do_arrasto]

	try:
		arrastox.append((velocidadex[t]/modulo_da_velocidade)*modulo_do_arrasto)
		arrastoy.append((velocidadey[t]/modulo_da_velocidade)*modulo_do_arrasto)
	except:
		arrastox.append(0)
		arrastoy.append(0)
    
	empuxox.append(0)
	empuxoy.append(0)
    
	peso.append((-(Terra_massa*foguete_massa*6.67408*10**-11)/(posicaoy[t] + 6.371*10**6)**2))
        
	q = 1/2*(Ar_densidade * modulo_da_velocidade**2)

    #armazena duração total da etapa ao final do programa
	queda_livre_duracao += variacao_de_tempo

    #cálculo das derivadas de posição
	aceleracaox.append((arrastox[t])/foguete_massa)
	aceleracaoy.append((arrastoy[t]+peso[t])/foguete_massa)
	velocidadex.append(variacao_de_tempo*aceleracaox[t] + velocidadex[t])
	velocidadey.append(variacao_de_tempo*aceleracaoy[t] + velocidadey[t])
	posicaox.append(variacao_de_tempo*velocidadex[t] + posicaox[t])
	posicaoy.append(variacao_de_tempo*velocidadey[t] + posicaoy[t])
    
    #auxiliar de passagem de tempo
	t += 1
    

#solução deselegante para um bug que ocorria na impressão dos gráficos ao fim de casa etapa
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
peso = peso[:-1]
CD = CD[:-1]
momento = momento[:-1]
alpha = alpha[:-1]
angulo = angulo[:-1]
Cm = Cm[:-1]
CD_damping = CD_damping[:-1]
velocidade_angular = velocidade_angular[:-1]
aceleracao_angular = aceleracao_angular[:-1]
atitudex = atitudex[:-1]
atitudey = atitudey[:-1]
velocidade_do_vento = velocidade_do_vento[:-1]
velocidade_relativax = velocidade_relativax[:-1]
velocidade_relativay = velocidade_relativay[:-1]
t -= 1

print(lancamentoduracao, 's')
print(lancamentoduracao + voo_impulsionadoduracao, 's')
print(lancamentoduracao + voo_impulsionadoduracao + cabotagemduracao,'s')
print(lancamentoduracao + voo_impulsionadoduracao + cabotagemduracao + queda_livre_duracao,'s')
