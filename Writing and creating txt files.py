#Exercicio python Brasil

#funcao para arrendodar, substituir ponto por virgula e converter bytes para megabytes
def bytes_to_mb(qntbytes):   
    return str(round(qntbytes/1048576, 2)).replace(".", ",")

#funcao para calcular a porcentagem de cada usuario, total, arredondar e substituir ponto por virgula
def porcentagem(espaco_usado, total):    
    return str(round(espaco_usado*100/total, 2)).replace(".", ",")

#abre o arquivo com usuarios, e coloca as linhas separadas na variavel usuarios_espacos
usuario_txt = open("usuarios.txt", "r")
usuarios_espacos = usuario_txt.read().split("\n")

#aqui e criado o relatorio.txt, e feito o indice, com recuos e alinhamento do cabecalho e titulos
arquivo_relatorio = open("relatorio.txt", "wt")
arquivo_relatorio.write("ACME Inc.    Uso do espaco em disco pelos usuarios\n")
arquivo_relatorio.write("-"*72 + "\n")
arquivo_relatorio.write("Nr.".ljust(5))
arquivo_relatorio.write("Usuario".ljust(15))
arquivo_relatorio.write("Espaco utilizado".ljust(21))
arquivo_relatorio.write("% do uso".ljust(9) + "\n\n")

#agora e feito a soma do espaco da memoria de acordo com a soma toda do grupo
espaco_total = 0
for usuarios_espaco in usuarios_espacos:
    espaco_total += int(usuarios_espaco.split()[1])

#e criado o indice da tabela, de acordo com a quantidade de linhas com o comando len
for indice_usuario_espaco in range(len(usuarios_espacos)):
    usuario_espaco = usuarios_espacos[indice_usuario_espaco].split()

    usuario = usuario_espaco[0]
    espaco = usuario_espaco[1]

    arquivo_relatorio.write(str(indice_usuario_espaco+1).ljust(5))
    arquivo_relatorio.write(usuario.ljust(15))
    arquivo_relatorio.write(bytes_to_mb(int(espaco)).rjust(7)+" MB         ")
    arquivo_relatorio.write(porcentagem(int(espaco), espaco_total).rjust(7)+"%\n")

arquivo_relatorio.write("\nEspaco total ocupado: " +bytes_to_mb(espaco_total) + " MB\n")
arquivo_relatorio.write("Espaco medio ocupado: " +bytes_to_mb(espaco_total/len(usuarios_espacos))+" MB")
