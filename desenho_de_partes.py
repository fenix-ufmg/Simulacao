# -*- coding: utf-8 -*-

from time import sleep

"""
Será utilizada a seguinte relação na lista de armazenamento de forma a permitir o uso externo:
c0 coifa tipo
c1 coifa diametro
c2 coifa comprimento
c3 coifa espessura
c4 coifa densidade
cp1 corpo diametro
cp2 corpo comprimento
cp3 corpo espessura
cp4 corpo densidade
m1 componente de massa massa
m2 componente de massa distância do nariz
p1 paraquedas massa
p2 paraquedas CD
mt1 motor empuxo médio
mt2 motor massa
mt3 motor duração
g1 guia CD
t1 transição diametro inicial
t2 transição comprimento
t3 transição diametro final
t4 transição espessura 
t4 transição densidade
a1 aletacomprimentoponta
a2 aletadesvio
a3 aletalargura
a4 aletaespessura
a5 aletanumero
a6 aletadistanciadofundo
a7 aletadensidade
"""

# lista que permite o acompanhamento do usuário durante o processo
exibicao = []
# lista utilizada para armazenar e transmitir valores
armazenamento = []

# coifa
print("\n" * 3, "#" * 40, "\n" * 3)
# O desenho sempre inicia-se pela coifa
coifatipo = int(
    input("Indique o tipo de coifa:\n1 - Cônica\n2 - Ogival Parabólica\n3 - Ogival\n\n")
)
if coifatipo == 1:
    auxcoifatipo = "cônica"
elif coifatipo == 2:
    auxcoifatipo = "ogival parabólica"
elif coifatipo == 3:
    auxcoifatipo = "ogival"
else:
    print("\nOpção inválida. Será considerado Ogival parabólica.\n")
    auxcoifatipo = "Ogival Parabólica"
    coifatipo = 2

coifacomprimento = float(input("Insira o comprimento da coifa (cm) "))
coifadiametro = float(input("Insira o diâmetro da coifa (cm) "))
coifaespessura = float(input("Insira a espessura da coifa (cm)"))
coifadensidade = float(input("Insira a densidade da coifa (Kg/m³)"))

exibicao.append(
    f"Coifa {auxcoifatipo} de comprimento {coifacomprimento}cm, diâmetro {coifadiametro}cm, espessura de {coifaespessura}cm e densidade de {coifadensidade}Kg/m³."
)

armazenamento.append("c0")
armazenamento.append(coifatipo)
armazenamento.append("c1")
armazenamento.append(coifadiametro)
armazenamento.append("c2")
armazenamento.append(coifacomprimento)
armazenamento.append("c3")
armazenamento.append(coifaespessura)
armazenamento.append("c4")
armazenamento.append(coifadensidade)

while True:

    print("\n" * 3, "#" * 40, "\n" * 3)
    print("O seu foguete está assim: \n")
    for i in exibicao:
        print(i)

    opcao = float(
        input(
            f"""Indique qual parte você deseja em seguida:\ncorpo (1)\ntransição (2)\nacréscimos (3)\naletas (4)\nfoguete completo (5)\n"""
        )
    )

    if opcao == 1:
        # corpo
        print("\n" * 3, "#" * 40, "\n" * 3)
        corpocomprimento = float(input("Insira o comprimento do corpo (cm) "))
        corpoespessura = float(input("Insira a espessura do corpo (cm) "))
        corpodensidade = float(input("Insira a densidade do corpo (kg/m³) "))

        try:
            corpodiametro = float(armazenamento[armazenamento.index("t3") + 1])
        except:
            corpodiametro = float(armazenamento[armazenamento.index("c1") + 1])

        exibicao.append("+")
        exibicao.append(
            f"Corpo de comprimento {corpocomprimento}cm, diâmetro {corpodiametro}cm, espessura {corpoespessura}cm e densidade de {corpodensidade}Kg/m³."
        )

        armazenamento.append("cp1")
        armazenamento.append(corpodiametro)
        armazenamento.append("cp2")
        armazenamento.append(corpocomprimento)
        armazenamento.append("cp3")
        armazenamento.append(corpoespessura)
        armazenamento.append("cp4")
        armazenamento.append(corpodensidade)

    elif opcao == 2:
        # transicao

        print("\n" * 3, "#" * 40, "\n" * 3)
        transicaocomprimento = float(input("Insira o comprimento da transição (cm) "))
        transicaoespessura = float(input("Insira a espessura da transição (cm) "))
        transicaodensidade = float(input("Insira a densidade da transição (kg/m³) "))

        try:
            transicaodiametroinicial = armazenamento[armazenamento.index("cp1") + 1]
        except:
            transicaodiametroinicial = armazenamento[armazenamento.index("c1") + 1]

        transicaodiametrofinal = float(
            input("Insira o diâmetro final da transição (cm) ")
        )

        exibicao.append("+")
        exibicao.append(
            f"Transição de comprimento {transicaocomprimento}cm, diâmetro inicial {transicaodiametroinicial}cm, diâmetro final {transicaodiametrofinal}cm, espessura {transicaoespessura}cm e densidade {transicaodensidade}Kg/m³."
        )

        armazenamento.append("t1")
        armazenamento.append(transicaodiametroinicial)
        armazenamento.append("t2")
        armazenamento.append(transicaocomprimento)
        armazenamento.append("t3")
        armazenamento.append(transicaodiametrofinal)
        armazenamento.append("t4")
        armazenamento.append(transicaoespessura)
        armazenamento.append("t5")
        armazenamento.append(transicaodensidade)

    elif opcao == 3:
        # acréscimos

        print("\n" * 3, "#" * 40, "\n" * 3)
        opcaoacrescimo = float(
            input(
                """Indique o acrescimo desejado:
            Componente de massa (1)
            Paraquedas (2)
            Motor (3)
            Guia (4)
            """
            )
        )
        if opcaoacrescimo == 1:
            componentedemassadistancia = float(
                input(
                    "Insira a distância do componente de massa do nariz do foguete (cm) "
                )
            )
            componentedemassamassa = float(input("Insira a massa do componente (Kg) "))

            exibicao.append("e")
            exibicao.append(
                f"Componente de massa de {componentedemassamassa}Kg a uma distância de {componentedemassadistancia}cm do nariz do foguete."
            )

            armazenamento.append("m1")
            armazenamento.append(componentedemassadistancia)
            armazenamento.append("m2")
            armazenamento.append(componentedemassamassa)

        elif opcaoacrescimo == 2:
            CDparaquedas = float(input("Insira o CD do paraquedas "))
            massaparaquedas = float(input("Insira a massa do paraquedas (Kg) "))

            exibicao.append("e")
            exibicao.append(
                f"Paraquedas de {massaparaquedas}Kg e CD de {CDparaquedas}."
            )

            armazenamento.append("p1")
            armazenamento.append(CDparaquedas)
            armazenamento.append("p2")
            armazenamento.append(massaparaquedas)

        elif opcaoacrescimo == 3:
            motorempuxo = float(input("Insira o empuxo médio do motor (N) "))
            motormassa = float(input("Insira a massa do motor (Kg) "))
            motorduracao = float(input("Insira o período de queima do motor (s) "))
            motorcomprimento = float(input("Insira o comprimento do motor (cm) "))

            exibicao.append("e")
            exibicao.append(
                f"Motor de massa {motormassa}Kg, empuxo médio {motorempuxo}N, período de queima de {motorduracao}s e comprimento do motor {motorcomprimento}cm."
            )

            armazenamento.append("mt1")
            armazenamento.append(motorempuxo)
            armazenamento.append("mt2")
            armazenamento.append(motormassa)
            armazenamento.append("mt3")
            armazenamento.append(motorduracao)
            armazenamento.append("mt4")
            armazenamento.append(motorcomprimento)

        elif opcaoacrescimo == 4:
            CDguia = float(input("Insira o CD gerado pela guia "))

            exibicao.append("e")
            exibicao.append(f"Guia de CD de {CDguia}.")

            armazenamento.append("g1")
            armazenamento.append(CDguia)

        else:
            print("Comando inválido. Tente novamente")

    elif opcao == 4:
        # aletas
        print("\n" * 3, "#" * 40, "\n" * 3)

        aletacomprimentoraiz = float(
            input("Indique o comprimento da raiz de cada aleta (cm) ")
        )
        aletacomprimentoponta = float(
            input("Indique o comprimento da ponta de cada aleta (cm) ")
        )
        aletadesvio = float(
            input(
                "Indique a distância vertical entre a raiz e a ponta de cada aleta (cm) "
            )
        )
        aletalargura = float(input("Indique a largura de cada aleta (cm) "))
        aletaespessura = float(input("Indique a espessura de cada aleta (cm) "))
        aletanumero = float(input("Indique a quantidade de aletas "))
        aletadistanciadofundo = float(
            input("Indique a distância do fundo do foguete de cada aleta (cm) ")
        )
        aletadensidade = float(input("Indique a densidade das aletas (Kg/m³) "))

        exibicao.append("e")
        exibicao.append(
            f"Aletas de comprimento de raiz {aletacomprimentoraiz}cm, comprimento de ponta {aletacomprimentoponta}cm, desvio {aletadesvio}cm, largura {aletalargura}cm, espessura {aletaespessura}cm, quantidade {aletanumero}, distância do fundo {aletadistanciadofundo}cm e densidade {aletadensidade}Kg/m³"
        )
        armazenamento += [
            "a1",
            aletacomprimentoraiz,
            "a2",
            aletacomprimentoponta,
            "a3",
            aletadesvio,
            "a4",
            aletalargura,
            "a5",
            aletaespessura,
            "a6",
            aletanumero,
            "a7",
            aletadistanciadofundo,
            "a8",
            aletadensidade,
        ]

    elif opcao == 5:
        break

    else:

        print("Comando inválido. Tente novamente")

file = open("desenho.txt", "w+")

for i in armazenamento:
    file.write(str(i) + "\n")

file.close

sleep(1)
print("Espero que tenha gostado!")
sleep(1)


from math import pi


class Foguete:
    def __init__(
        self,
        t,
        motormassa,
        coifamassa,
        corpomassa,
        corpoespessura,
        corpodensidade,
        aletamassa,
        aletanumero,
        coifacomprimento,
        corpodiametro,
        coifavolumeM,
        corpovolumeM,
        posicaoy,
    ):

        self.foguetemassa = (
            motormassa + coifamassa + corpomassa + aletamassa * aletanumero
        )
        self.foguetecomprimento = coifacomprimento + corpocomprimento
        self.foguetevolume = coifavolumeM + corpovolumeM
        self.pesoy = [
            (
                -(5.972 * (10 ** 24) * self.foguetemassa * 6.67408 * 10 ** -11)
                / (posicaoy + 6.371 * 10 ** 6) ** 2
            )
        ]
        self.momentodeinercia = (
            pi
            * corpodensidade
            * self.foguetecomprimento
            / 12
            * (
                3
                * (corpodiametro / 2 ** 4 - ((corpodiametro - corpoespessura) / 2) ** 4)
                + self.foguetecomprimento ** 2
                * (
                    (corpodiametro / 2) ** 2
                    - ((corpodiametro - corpoespessura) / 2) ** 2
                )
            )
        )
