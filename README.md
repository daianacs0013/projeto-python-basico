# projeto-python-basico
# 🏥 Gerenciador de Fila de Pacientes

Exercícios e projetos práticos de Python desenvolvidos durante a faculdade no Infnet.

## 📝 Descrição da Tarefa
Desenvolva um programa que gerencie uma fila de atendimento a partir de comandos lidos da entrada padrão, obrigatoriamente utilizando os métodos append, insert, extend e pop. O programa deve exibir o estado atual da fila após cada comando e, ao final, o número total de pacientes atendidos durante a sessão.

### ⚙️ Os comandos possíveis são:
* ADICIONAR <nome> — adiciona ao final da fila
* PRIORIDADE <nome> — insere na posição 0
* GRUPO <nome1>,<nome2>,... — adiciona múltiplos nomes ao final
* CHAMAR — remove e exibe o primeiro da fila

### 📥 Entrada
A primeira linha contém os nomes dos pacientes da fila inicial separados por vírgula. As linhas seguintes contêm os comandos, até que seja digitado fim.

**Exemplo de entrada:**
Carlos,Maria,João
PRIORIDADE Beatriz
GRUPO Fátima,Rodrigo
CHAMAR
ADICIONAR Pedro
CHAMAR
fim

### 📤 Saída
Para cada comando recebido, o programa deve exibir o estado atualizado da fila. Quando o comando for CHAMAR, deve indicar o nome do paciente chamado. Ao final, deve exibir o total de pacientes atendidos durante a sessão. O formato de exibição fica a critério do aluno, desde que seja claro e consistente ao longo de toda a execução.
