
numero_tipo_float = 10.10
numero_tipo_string = "1998"

print(f"Primeiro exemplo convertendo o número: {numero_tipo_float}, inicialmente o seu tipo:{type(numero_tipo_float)}" )

#esse f dentro do print no antes da menssagem serve para que seja possível  concatenar texto com variavel
numero_tipo_float_convertido = int(numero_tipo_float)
print(f"Utilizando a função int() convertemos ele para inteiro {numero_tipo_float_convertido} o seu tipo:{type(numero_tipo_float_convertido)}")

print("==============================================================================================================")

print(f"Segundo exemplo convertendo um texto: {numero_tipo_string}, inicialmente o seu tipo:{type(numero_tipo_string)}" )

#esse f dentro do print no antes da menssagem serve para que seja possível  concatenar texto com variavel
string_convertida_inteiro = int(numero_tipo_string)
print(f"Utilizando a função int() convertemos ele para inteiro {string_convertida_inteiro} o seu tipo:{type(string_convertida_inteiro)}")
