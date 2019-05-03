# Dir

  # diretorio raiz : normal em diretórios

# Sistemas de diretório hierárquico


# caminho absoluto: contém o nome do diretório raiz até o o aqrquivo

#     caminho relativo: todos os caminho são presumidos atraves do diretorio atual, denominado diretorio de
#       trabalho
#
#     rotinas de biblioeta sempre voltam para o lugar onde estavam
#
#
#     entradas especiais
#         --> . que indica  que o diretorio de utilização é o diretorio atual
#         --> .. indica o diretorio anterior

# Operações com diretorios
#
# Create: cria um diretorio
# Delete: remoção de diretorio
#
#     Diretorio que contém apenas ponto e pontoponto é vazio
#
# OpenDir: abre um diretorio para a leitura
#
# CloseDir: fecha um diretorio
# readDir: retorna uma entrada em formato padrão diferente de read que retorna a estrutura do diretorio
#
# Rename : renomação do diretorio
#
# Link: Uma maneira de especificar que um arquivo está ou pode aparecer em vários diretórios
# i-node: ligação que monitora o número de entradas de diretório que contém o arquivo, chamdo de ligação estrita
# (hard link)
#
# Ulink: remover uma entrada de diretorio: se ele estiver em varios diretorios apenas o nome do
# caminho é removido, caso contrário ele é removido por completo do sistema de arquivo

# ligação simbolica: um nome que aponte para um