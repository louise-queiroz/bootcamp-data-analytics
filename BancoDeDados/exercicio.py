import sqlite3

conexao = sqlite3.connect('bd') 
cursor = conexao.cursor()  

#1) Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(256))')

#2) Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Louise", 21, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Maria Júlia", 20, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Bianca", 22, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Gabriel", 21, "Farmácia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Cauan", 19, "Matemática")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Emerson", 25, "Engenharia")')


#3) Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')

#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for usuario in dados:
    #print(usuario)

#4. Atualização e Remoção

#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=23 WHERE nome="Emerson" ')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 3')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(256), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Flavia", 35, 930)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Jorge", 24, 1368.97)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Louise", 21, 322.6)')

# 6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')

#b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) FROM clientes')

#c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

#d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
#for usuario in dados:
    #print(usuario)

# 7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 700 WHERE nome = "Louise"')

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id =1')

# 8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(256), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes (id));')

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2, "Porta", "120")')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 3, "Notebook", "4000")')
dados = cursor.execute('SELECT c.nome, co.produto, co.valor FROM compras co INNER JOIN clientes c ON co.cliente_id = c.id')
for usuario in dados:
    print(usuario)


conexao.commit() 
conexao.close 
