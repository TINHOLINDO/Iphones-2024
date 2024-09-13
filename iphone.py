class iPhone:
    iphones = []

    def __init__(self, modelo, ano_lancamento, características, sistema_operacional):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.características = características
        self.sistema_operacional = sistema_operacional
        iPhone.iphones.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.ano_lancamento} | {self.características} | {self.sistema_operacional}'
    
    def listar_iPhone():
        for iphone in iPhone.iphones:
            print(f'{iphone.modelo} | {iphone.ano_lancamento} | {iphone.características} | {iphone.sistema_operacional}')

iphone_13 = iPhone('iPhone 13', 2021, 'Câmera dupla, Chip A15 Bionic, 5G', 'iOS 15')
iphone_14 = iPhone('iPhone 14', 2022, 'Melhorias na câmera, Chip A16 Bionic, 5G', 'iOS 16')
iphone_15 = iPhone('iPhone 15', 2023, 'Design atualizado, Chip A17 Bionic, 5G', 'iOS 17')

iPhone.listar_iPhone()