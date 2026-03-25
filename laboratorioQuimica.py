import random
import argparse
from enum import Enum
class Equipamento:
    def __init__(self, nome, tempoMaximo,usosConsecutivos,limpeza):
        self.nome=  nome
        self.tempoMaximo = tempoMaximo
        self.usosConsecutivos = usosConsecutivos
        self.limpeza = limpeza


    def __repr__(self):
        return f"{self.nome} (Tempo: {self.tempoMaximo}h, Usos máx: {self.usosConsecutivos})"
    
class Equipamentos(Enum):
    BALANCA_ANALITICA = Equipamento("Balança Analítica", 6, 3,False)
    AGITADOR_MAGNETICO = Equipamento("Agitador Magnético", 4, 4,False),
    CROMATOGRAFO_LIQUIDO = Equipamento("Cromatógrafo Líquido", 8, 4,False),
    CROMATOGRAFO_GASOSO = Equipamento("Cromatógrafo Gasoso", 6, 3,False),
    ESPECTROFOTOMETRO_UV_VIS = Equipamento("Espectrofotômetro UV-VIS", 4, 2,False),
    ESPECTROMETRO_INFRAVERMELHO = Equipamento("Espectrômetro Infravermelho", 6, 3,False),
    ESPECTROMETRO_DE_MASSA = Equipamento("Espectrômetro de Massa", 4, 2,False),
    MICROSCOPIO = Equipamento("Microscópio", 6, 4,False),
    CENTRIFUGA = Equipamento("Centrífuga", 6, 3,False),
    FORNO_DE_MUFLA = Equipamento("Forno de Mufla", 4, 2,False)


analises = {
    1: [Equipamentos.ESPECTROFOTOMETRO_UV_VIS, Equipamentos.CROMATOGRAFO_GASOSO],
    2: [Equipamentos.CROMATOGRAFO_LIQUIDO, Equipamentos.ESPECTROMETRO_INFRAVERMELHO],
    3: [Equipamentos.MICROSCOPIO, Equipamentos.BALANCA_ANALITICA],
    4: [Equipamentos.ESPECTROMETRO_DE_MASSA],
    5: [Equipamentos.AGITADOR_MAGNETICO, Equipamentos.ESPECTROMETRO_INFRAVERMELHO],
    6: [Equipamentos.CROMATOGRAFO_LIQUIDO, Equipamentos.ESPECTROFOTOMETRO_UV_VIS],
    7: [Equipamentos.ESPECTROFOTOMETRO_UV_VIS, Equipamentos.MICROSCOPIO],
    8: [Equipamentos.CROMATOGRAFO_GASOSO],
    9: [Equipamentos.ESPECTROMETRO_INFRAVERMELHO, Equipamentos.BALANCA_ANALITICA],
    10: [Equipamentos.ESPECTROMETRO_DE_MASSA, Equipamentos.CROMATOGRAFO_GASOSO],
    11: [Equipamentos.CENTRIFUGA, Equipamentos.BALANCA_ANALITICA],
    12: [Equipamentos.AGITADOR_MAGNETICO, Equipamentos.CROMATOGRAFO_LIQUIDO],
    13: [Equipamentos.FORNO_DE_MUFLA, Equipamentos.ESPECTROMETRO_INFRAVERMELHO],
    14: [Equipamentos.ESPECTROFOTOMETRO_UV_VIS, Equipamentos.BALANCA_ANALITICA],
    15: [Equipamentos.CROMATOGRAFO_GASOSO, Equipamentos.ESPECTROMETRO_DE_MASSA],
    16: [Equipamentos.CENTRIFUGA, Equipamentos.CROMATOGRAFO_LIQUIDO],
    17: [Equipamentos.FORNO_DE_MUFLA, Equipamentos.MICROSCOPIO],
    18: [Equipamentos.BALANCA_ANALITICA, Equipamentos.AGITADOR_MAGNETICO, Equipamentos.ESPECTROFOTOMETRO_UV_VIS]
}

TOTAL_SLOTS = 50
dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]

def criar_paciente():
    paciente = {}

    for analise, etapas in analises.items():
        slot_anterior = -2

        for i in range(len(etapas)):
            slot = random.randint(slot_anterior + 2, TOTAL_SLOTS - 1)
            paciente[(analise, i)] = slot
            slot_anterior = slot

    return paciente

def fitness(paciente):
    penalidade = 0

    uso_equipamento = {}
    uso_analise = {}

    for (analise, etapa), slot in paciente.items():
        equipamento = analises[analise][etapa]

        # R1
        if (equipamento, slot) in uso_equipamento:
            penalidade += 100
        else:
            uso_equipamento[(equipamento, slot)] = analise

        # R2
        if (analise, slot) in uso_analise:
            penalidade += 100
        else:
            uso_analise[(analise, slot)] = True

    makespan = max(paciente.values())

    return 10000 - penalidade - makespan * 5 #função de fitness

#for eq in equipamentos:
#    print(eq)

class Laboratorio:
    def __init__(self, equipamentos_disponiveis):
        self.equipamentos_disponiveis = set(equipamentos_disponiveis)

    def tem(self, equipamento):
     return equipamento in self.equipamentos_disponiveis
    
    def encadeamento_frente(self):
        analises = [
        ("A01", self.tem(Equipamentos.ESPECTROFOTOMETRO_UV_VIS) and self.tem(Equipamentos.CROMATOGRAFO_GASOSO), "Análise 1"),
        ("A02", self.tem(Equipamentos.CROMATOGRAFO_LIQUIDO) and self.tem(Equipamentos.ESPECTROMETRO_INFRAVERMELHO), "Análise 2"),
        ("A03", self.tem(Equipamentos.MICROSCOPIO) and self.tem(Equipamentos.BALANCA_ANALITICA), "Análise 3"),
        ("A04", self.tem(Equipamentos.ESPECTROMETRO_DE_MASSA), "Análise 4"),
        ("A05", self.tem(Equipamentos.AGITADOR_MAGNETICO) and self.tem(Equipamentos.ESPECTROMETRO_INFRAVERMELHO), "Análise 5"),
        ("A06", self.tem(Equipamentos.CROMATOGRAFO_LIQUIDO) and self.tem(Equipamentos.ESPECTROFOTOMETRO_UV_VIS), "Análise 6"),
        ("A07", self.tem(Equipamentos.ESPECTROFOTOMETRO_UV_VIS) and self.tem(Equipamentos.MICROSCOPIO), "Análise 7"),
        ("A08", self.tem(Equipamentos.CROMATOGRAFO_GASOSO), "Análise 8"),
        ("A09", self.tem(Equipamentos.ESPECTROMETRO_INFRAVERMELHO) and self.tem(Equipamentos.BALANCA_ANALITICA), "Análise 9"),
        ("A10", self.tem(Equipamentos.ESPECTROMETRO_DE_MASSA) and self.tem(Equipamentos.CROMATOGRAFO_GASOSO), "Análise 10"),
        ("A11", self.tem(Equipamentos.CENTRIFUGA) and self.tem(Equipamentos.BALANCA_ANALITICA), "Análise 11"),
        ("A12", self.tem(Equipamentos.AGITADOR_MAGNETICO) and self.tem(Equipamentos.CROMATOGRAFO_LIQUIDO), "Análise 12"),
        ("A13", self.tem(Equipamentos.FORNO_DE_MUFLA) and self.tem(Equipamentos.ESPECTROMETRO_INFRAVERMELHO), "Análise 13"),
        ("A14", self.tem(Equipamentos.ESPECTROFOTOMETRO_UV_VIS) and self.tem(Equipamentos.BALANCA_ANALITICA), "Análise 14"),
        ("A15", self.tem(Equipamentos.CROMATOGRAFO_GASOSO) and self.tem(Equipamentos.ESPECTROMETRO_DE_MASSA), "Análise 15"),
        ("A16", self.tem(Equipamentos.CENTRIFUGA) and self.tem(Equipamentos.CROMATOGRAFO_LIQUIDO), "Análise 16"),
        ("A17", self.tem(Equipamentos.FORNO_DE_MUFLA) and self.tem(Equipamentos.MICROSCOPIO), "Análise 17"),
        ("A18", self.tem(Equipamentos.BALANCA_ANALITICA) and self.tem(Equipamentos.AGITADOR_MAGNETICO) and self.tem(Equipamentos.ESPECTROFOTOMETRO_UV_VIS), "Análise 18"),
    ]

        return [analise for analise in analises if analise[1]]


