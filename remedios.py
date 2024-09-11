class Remédio:
    nome = ''
    genero = ''
    grupo = ''
    ativo = False

remedio_dipirona = Remédio()
remedio_rivotril = Remédio()
remedio_buscopan = Remédio()

remedio_dipirona.nome  = 'dipirona'
remedio_dipirona.nome_cientifico = 'metamizol sódico'

remedios = [remedio_dipirona, remedio_rivotril, remedio_buscopan]

for remedio in remedios:
print(remedio, \n)
print(remedio_dipirona, \n)
print(dir(remedio_dipirona))