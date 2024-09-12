class iPhone:
    def __init__(self, modelo, ano_lancamento, características, sistema_operacional):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.características = características
        self.sistema_operacional = sistema_operacional
    def __str__(self):
        return f'{self.modelo} | {self.ano_lancamento} | {self.características} | {self.sistema_operacional}'

iphone_13 = iPhone('iPhone 13', 2021, 'Câmera dupla, Chip A15 Bionic, 5G', 'iOS 15')
iphone_14 = iPhone('iPhone 14', 2022, 'Melhorias na câmera, Chip A16 Bionic, 5G', 'iOS 16')
iphone_15 = iPhone('iPhone 15', 2023, 'Design atualizado, Chip A17 Bionic, 5G', 'iOS 17')

iphones = [iphone_13, iphone_14, iphone_15]

print(iphone_13)
print(iphone_14)
print(iphone_15)