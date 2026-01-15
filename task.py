import argparse
parser = argparse.ArgumentParser() # objeto parser: lê argumentos da linha de comando, valida e gera mensagens de help
parser.add_argument("echo", help="echo the string you use here. ",type=str) #nome argumento, mensagem help, tipo
parser.add_argument("square", help="display a square of a given number. ",type=int) 
args = parser.parse_args() # lê argumentos do terminal, valida os tipos, cria um objeto args com os valores
print(args.echo) # imprime. parser.add_argumento("echo") -> args.echo (compilador lê o nome do argumento e transnforma nisso)
print(args.square**2) 


