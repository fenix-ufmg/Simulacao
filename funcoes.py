#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, acos, sin, log, fabs, sqrt

# calcula módulo entre dois vetores
def call_mod(vetorx, vetory):
    mod = sqrt(vetorx ** 2 + vetory ** 2)
    return mod


# COEFICIENTE DE GRAVIDADE


def callCGcoifa(coifamassaM, coifamassam, coifacomprimento, coifacomprimentomenor):

    CGcoifa = (
        coifacomprimento * 2 / 3 * coifamassaM
        - coifamassam * (coifacomprimento - coifacomprimentomenor / 3)
    ) / (coifamassaM + coifamassam)
    return CGcoifa


def callCGcorpomotor(massamotor, massacorpo, corpocomprimento, motorcomprimento):

    CGcorpo = corpocomprimento / 2
    CGmotor = corpocomprimento - motorcomprimento / 2
    CGcorpomotor = (CGcorpo * massacorpo + CGmotor * massamotor) / (
        massacorpo + massamotor
    )
    return CGcorpomotor


def callCGaleta(
    param,
    aletamassa,
    aletadesvio,
    aletalargura,
    aletacomprimentoraiz,
    aletacomprimentoponta,
    aletadistanciadofundo,
):

    CGumaaleta = (
        aletadesvio * aletalargura / 2 * param * (2 * aletadesvio / 3)
        + aletalargura
        * (aletacomprimentoraiz - aletadesvio)
        * param
        * (aletadesvio + (aletacomprimentoraiz - aletadesvio) / 2)
        + aletalargura
        * ((aletacomprimentoponta + aletadesvio) - aletacomprimentoraiz)
        / 2
        * param
        * (
            aletacomprimentoraiz
            + (aletacomprimentoponta + aletadesvio - aletacomprimentoraiz) / 3
        )
    ) / aletamassa

    return CGumaaleta


def callCGtransicao(
    transicaocomprimento,
    transicaodiametroinicial,
    transicaodiametrofinal,
    transicaodensidade,
):
    H = fabs(
        transicaocomprimento
        * transicaodiametroinicial
        / (transicaodiametroinicial - transicaodiametrofinal)
    )
    h = fabs(
        transicaocomprimento
        * transicaodiametrofinal
        / (transicaodiametroinicial - transicaodiametrofinal)
    )
    M = pi * H * transicaodensidade / 3 * (transicaodiametroinicial / 2) ** 2
    m = pi * h * transicaodensidade / 3 * (transicaodiametrofinal / 2) ** 2
    CG = (H * M / 4 - (H - 3 * h / 4) * m) / (M - m)
    return CG


def callCG(
    CGcoifa,
    CG_corpo,
    CGcorpomotor,
    CGtransicao,
    CGaleta,
    coifamassa,
    corpo1massa,
    corpo2massa,
    motormassa,
    aletamassa,
    aletanumero,
    componentemassa,
    componentedistancia,
    transicaomassa
):
    CG = (
            CGcoifa * coifamassa
            + CGtransicao*transicaomassa
            + CGcorpomotor * (corpomassa + motormassa)
            + CGaleta * aletamassa * aletanumero
            + componentemassa * componentedistancia
        )
        / (
            coifamassa
            + corpo1massa
            + corpo2massa
            + transicaomassa
            + motormassa
            + aletamassa * aletanumero
            + componentemassa
        )
        
    return CG


# COEFICIENTE DE MOMENTO


def callCm(alpha, coifadiametro, A, d, foguetecomprimento, foguetevolume):
    try:
        Cm = (
            -2
            * sin(alpha)
            / (A)
            * d
            * (foguetecomprimento * (pi * coifadiametro ** 2 / 4) - foguetevolume)
        )
    except:
        Cm = 0
    return Cm


# COEFICIENTES DE ARRASTO

# coeficiente de arrasto de amortecimento
def callCD_damping(
    CPaleta,
    CG,
    aletaarea,
    arearef,
    coifadiametro,
    comprimento,
    raiomedio,
    velocidadeangular,
    velocidade,
):
    try:
        CDdamping = (
            0.55
            * (comprimento ** 4)
            * raiomedio
            * (velocidadeangular * fabs(velocidadeangular))
        ) / (
            arearef * (coifadiametro / 2) * (velocidade ** 2)
            + (
                (0.6 * 4 * aletaarea * (CPaleta - CG) ** 3 * velocidadeangular ** 2)
                / (arearef * coifadiametro * velocidade)
            )
        )
    except:
        CDdamping = 0
    return CDdamping


# coeficiente de arrasto de fricção
def callCDfriction(
    arearef,
    aletaareamolhada,
    Rcri,
    fitnessratio,
    corpoareamolhada,
    aletaespessura,
    reynoldsnumero,
    Rs,
    foguetecomprimento,
    Mach,
):
    if reynoldsnumero < 10 ** 4:
        Cf = 1.48 * 10 ** -2
    elif 10 ** 4 <= reynoldsnumero <= Rcri:
        Cf = 1 / (1.5 * log(reynoldsnumero) - 5.6) ** 2
    else:
        Cf = 0.032 * (Rs / foguetecomprimento) ** 0.2

    Cfc = Cf * (1 - 0.1 * Mach ** 2)

    CDfriction = (
        Cfc
        * (
            (1 + 1 / (2 * fitnessratio)) * corpoareamolhada * 2
            + (1 + (2 * aletaespessura) / 1.5) * aletaareamolhada
        )
        / arearef
    )

    return CDfriction


# calcula coeficiente de arrasto de pressão da coifa
def callCDcoifa(coifadiametro, coifacomprimento):
    CDcoifa = (
        0.8
        * ((coifadiametro / 2)
        / sqrt(coifacomprimento ** 2 + (coifadiametro / 2) ** 2))**2
    )
    return CDcoifa


# calcula coeficiente de arrasto de base da tubeira
def callCDtubeira(Mach):
    if Mach < 1:
        CDtubeira = 0.12 + 0.13 * Mach ** 2
    else:
        CDtubeira = 0.25 / Mach
    return CDtubeira


# COEFICIENTE DE FORCA NORMAL


def callCNalpha(arearef, diametrobase, diametrotip, alpha):
    if alpha != 0:
        CNalpha = (
            (2 / arearef)
            * (pi * (diametrobase / 2) ** 2 - pi * (diametrotip / 2) ** 2)
            * sin(alpha)
        ) / alpha
    else:
        CNalpha = (2 / arearef) * (
            pi * (diametrobase / 2) ** 2 - pi * (diametrotip / 2) ** 2
        )
    return CNalpha


# CENTRO DE PRESSAO

# calcula CP de transições e corpos
def callCPbody(
    bodycomprimento, bodydiametroinicial, bodydiametrofinal, bodyvolumeaparente
):
    try:
        CPbody = (
            bodycomprimento * (pi * (bodydiametrofinal / 2) ** 2) - bodyvolumeaparente
        ) / (pi * (bodydiametrofinal / 2) ** 2 - pi * (bodydiametroinicial / 2) ** 2)
    except:
        CPbody = bodycomprimento / 2
    return CPbody


# calcula CP da aleta
def callCPaleta(aletadesvio, aletacomprimentoraiz, aletacomprimentoponta):
    CPaleta = aletadesvio / 3 * (aletacomprimentoraiz + 2 * aletacomprimentoponta) / (
        aletacomprimentoraiz + aletacomprimentoponta
    ) + 1 / 6 * (
        aletacomprimentoraiz ** 2
        + aletacomprimentoponta ** 2
        + aletacomprimentoraiz * aletacomprimentoponta
    ) / (
        aletacomprimentoraiz + aletacomprimentoponta
    )
    return CPaleta


# calcula CP do foguete inteiro com base nas partes individuais
def callCP(
    CPcoifa, CNalphacoifa, CPcorpo, CNalphacorpo, CPaleta, CNalphaaleta, aletanumero
):
    CP = [
        0,
        (
            CPcoifa * CNalphacoifa
            + CPcorpo * CNalphacorpo
            + CPaleta * CNalphaaleta * aletanumero
        )
        / (CNalphacoifa + CNalphacorpo + aletanumero * CNalphaaleta),
    ]
    return CP


# ANGULO ENTRE DOIS VETORES


def callalpha(vetor10, vetor11, vetor20, vetor21):
    try:
        alpha = acos(
            ((vetor10 * vetor20 + vetor11 * vetor21))
            / ((sqrt(vetor10 ** 2 + vetor11 ** 2)) * sqrt(vetor20 ** 2 + vetor21 ** 2))
        )
    except:
        alpha = 0
    return alpha


# NUMERO DE REYNOLDS


def callRey(ardensidade, coifadiametro, viscosidadear, velocidademodulo):
    numerodereynolds = ardensidade * velocidademodulo * coifadiametro / viscosidadear
    return numerodereynolds


# WIND


def callwind(altura):
    return 30 * (4 / 1.225) ** 0.5 * (2.5) * log(1 / 2) * (altura) ** 0.25
