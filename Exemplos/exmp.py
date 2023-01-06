ordemDeNascimento = ['primeira filha', 'segunda filha']
primeiroNome = ['Tiffany','Débora']

for nome_filha, ordem  in zip(primeiroNome, ordemDeNascimento):
    mensagem = f'Nome {nome_filha} é minha {ordem}'
    print(mensagem)