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


