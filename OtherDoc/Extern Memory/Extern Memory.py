    # Disco magnético
    #     subtrato de material magnetizável
    #     Tradicionalmente tem sido alumínio ou material de liga de alumínio
    #     Atualmente tem sido usado meterial
    #
    # A bobina condutora de recuperação é chamada cabeça
    # Em muitos sistemas existem duas cabeças uma de leitura e outra de gravação
    #
    # A cabeça é um dispositivo pequeno capaz de ler e escrever em uma parte do prato girando por debaixo
    #
    # Trilha: conjunto concentrico de aneis
    # Existem lacunas entre as trilhas e entre os setores: diminuem o erro de precisão
    # Setores: espeaços de gravação dos dados
    #
    # CAV --> velocidade angular constante
    #     Vantagem o endereçamento pode ser realizado por trilah e setore
    #     desvantagem : a desvatagem é que a quantidade dedados armazenada nas trilhas lngas é
    #             a mesma que nas trilhas curtas
    #
    #     Densidade de trilha é a quantidade de bits por polegada quadrada
    #
    # TÉCNINCA DE PERFORMANCE
    #
    # Gravação em multiplas zonas : uma superficie pode ser dividida em multiplas zonas
    # Dentro de uma zona há um número de bits por trilha é constante

    # ++++As zonas mais distantes do centro contêm mais bits (mais setores)
    #     do que as zonas próximas do centro.
    #
    # O byte SYNCH é um padrão de bits especial, que delimita o início do campo.

    # CARACTERÍSTICAS FÍSICAS
    #
    #     FIX HEAD:
    #        # There are a head of read and write for trail
    #             There aren't more
    #     FIX MOBILE
    #             There are head for head and read for write
    #
        #
        # # Em geral quando não é possível ganhar desempenho com projeto utilizam-se
        # arquiteturas paralelas
        #
        # RAID é um conjunto de unidades de discos físicos, vistas pelo sistema operacional como uma única unidade
        #         lógica.
        # STRIPING --> intercalação de dados: Dados são distribuidos por pelos vários discos físicos


        # RAID 0 -->  STRIPING
        #         Os dados são divididos em tiras(Strip) e compartilhado pelos diversos discos disponíveis
        #
        #         Os dados são armazenados em padrão round robin
        #
        #         2 Requisitos de performance
        #                 +grande capacidade de transferência ao longo do caminho inteiro
        #                         ++i.e barramentos (internos;I.O;First  memory)
        #                 +As solicitações de entrada e saída devem ser eficazes
        #         x1 + x2 +x3 = 1x


        # RAID 1
        #
        #         +Nos Raids de 2 a 6 sempre há alguma forma de paridade
        #         +Um espelhamento de dados é realizado
        #         + O ritmo de gravação é ditado pelo disco mais lento
        #         + A recuperação de falha simples é realizada de maneira simples
        #         +Em um ambiente orientado à transação, RAID 1 pode alcançar altas taxas de solicitação de E/S
        #         x1=x2


        # RAID 2
        #
        #         + acesso paralelo ao disco
        #         + É utilizado um nível extra de redundância de dados(disco de paridade)
        #         +RAID 2 só seria uma escolha efi caz em um ambiente em que ocorrem muitos erros de disco.
        #         +Dada a alta confi abilidade dos discos individuais e unidades de disco, RAID 2 é um exagero, e normalmente não é implementado.
        #         x1 + x2 =x3 + x4
        # #

        # RAID 3
        #
        #         + acesso paralelo ao disco
        #         + bit de paridade é calculado para um mesmo conjunto de bit na mesmo posição em todos os discos
        #         + faz a paridade para todos os discos ao mesmo tempo
        #         e.g = x4 =x1+x2

        #
        # RAID 5
        #         +semelhante ao RAID 4
        #         + distribui os strip de paridades por todos os discos
        #







