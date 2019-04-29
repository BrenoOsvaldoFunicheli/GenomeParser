class Conta:

    # x ==> attr de classe

    def __init__(self,	numero,	titular,saldo,	limite):

        # variaveis de classe
        self.numero	= numero
        self.limite = limite
        self.titular = titular
        self.saldo = saldo

    # metodo da classe
    def	deposita(self,	valor):
        # self referencia do attr da instancia da clsse
        self.saldo += valor

    def	saca(self,	valor):
        self.saldo -= valor

    def	extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.numero,	self.saldo))


    # init n'ao cria o objeto, na realidade ele apenas inicializa-o
    # new cria o objeto na memoria
    # operador ==  compara a refenecia do objeto
    # a passagem de parametros copia o valor do objketo para o argumento
    # o metood dir mostra todos os metodosd do objeto
    # metodos que possuem dois underscore s'ao metodo magicos
    # vars() chama dict de um objeto

    #print(Conta.__dict__)

    # decorators sao uma maneira de implementar um comportamento diferente para um attr ou method
    # exe sao a maneira de atribuicao de getters e setters a classe
    # a maneira pythonica de realizar o encapsulamento e atraves de decorators

    # e.g
    #   @proprety
    #   get_saldo()


    # e.g
    #   @function_name.setter
    #   def function_name()
    #   condict1
    #   ...

    #   garante que a operacao de atribuicao ira seguir a s condicoes do method

    # @classMethod --> metodo de classe e possui attr cls
    #   -->pode ser reescrito em uma classe filha
    # @ staticmethod --> decorator de method static
    #   -->nao pode ser reescrito em uma classe filha

    # Métodos	 de	 classe	 servem	 para	 definir	 um	 método	 que
    # opera	 na	 classe,	 e	 não	 em	 instâncias.	 Já	 os
    # métodos	estáticos	utilizamos	quando	não	precisamos	receber	a
    # referência	de	um	objeto	especial	(seja	da
    # classe	ou	de	uma	instância)	e	funciona	como	uma	função
    # comum,	sem	relação


    #__slot__ =[lista_attr] --> faz com que as variaveis sejam mais economicas e ainda
    # implementa o encapsulamento