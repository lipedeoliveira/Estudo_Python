

# def double(x):
#     return x*2

# def apply_to_one(f):
#     return f(1)


# my_double = double
# x = apply_to_one(my_double)
# print(x)
# #
# #
# #Também é fácil criar pequenas funções anônimas, lambdas
# y = apply_to_one(lambda x: x+4)
# print(y)


#Os parâmetros das funçoes, também podem possuir, argumentos padrão
#que também deve ser especificado para se obter um valor diferente do padrão

def my_message( message = "Mensagem padrão "):
    print(message)

my_message()
my_message("Mensagem fora do padrão")

#As vezes, é útil especificar argumentos pelo nome

def full_name(first = "Qual é o o nome dele", last = "Algo"):
    return first+"  "+last

print(full_name("Felipe","Vieira"))
print(full_name("Vieira","Felipe"))
print(full_name(last="Vieira",first="Felipe"))

multi_line_string = """

Primeira Linha
Segunda Linha
Terceira Linha

"""

print(multi_line_string)


integer_list = [1,2,3]
#sum(), pega todos os itens da lista, e soma da esquerda pra direita
#sum(iteravel, /, start = 0)
print(sum(integer_list))


##Fatiamento


