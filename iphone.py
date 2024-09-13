class iPhone:
    iphones = []

    def __init__(self, modelo, ano_lancamento, características, sistema_operacional):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.características = características
        self._sistema_operacional = sistema_operacional
        iPhone.iphones.append(self)

    @property
    def sistema_operacional(self):
        return '🍎 Sistema operacional' if self._sistema_operacional else '🍏 Sistema operacional'

    @classmethod
    def listar_iPhone(cls):
        print('')
        print('''...''') 
        print(f'{"Modelo do iphone".ljust(25)} | {"Ano de lançamento".ljust(22)} | {"Característica".ljust(22)} | {"Sistema operacional".ljust(22)}')
        for iphone in cls.iphones:
            print(f'{iphone.modelo.ljust(25)} | {str(iphone.ano_lancamento).ljust(22)} | {iphone.características.ljust(22)} | {iphone.sistema_operacional}')

iphone_13 = iPhone('iPhone 13', 2021, 'Câmera dupla, Chip A15 Bionic, 5G', 'iOS 15')
iphone_14 = iPhone('iPhone 14', 2022, 'Melhorias na câmera, Chip A16 Bionic, 5G', 'iOS 16')
iphone_15 = iPhone('iPhone 15', 2023, 'Design atualizado, Chip A17 Bionic, 5G', 'iOS 17')

iPhone.listar_iPhone()
