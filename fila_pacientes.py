nomes = input('Digite o nomes dos pacientes')
pacientes = nomes.split(',')
atendido = 0
comando = input('Digite o comando (ADICIONAR,PRIORIDADE,GRUPO,CHAMAR,fim)')
while comando != 'fim':
    partes = comando.split(' ')
    palavra1 = partes [0] 

    if palavra1 == 'ADICIONAR':
        nome_paciente = partes[1]
        pacientes.append(nome_paciente)
    elif palavra1 == 'PRIORIDADE' :
        nome_paciente = partes[1]
        pacientes.insert(0, nome_paciente)
    elif palavra1 == 'CHAMAR':
        paciente_chamados = pacientes.pop(0)
        print(f'Chamando o paciente:{paciente_chamados}')
        atendidos = atendido + 1
    elif palavra1 == 'GRUPO':
        lista_grupo = partes[1].split(',')
        pacientes.extend(lista_grupo)

    print(pacientes)
    comando = input('Digite o próximo comando (ou fim):')

print(f'Total de pacientes atendidos durante a sessão: {atendidos}')
 
