#rodando todos os sites ao mesmo tempo
import subprocess

subprocess.Popen(['python', 'Pagina_inicial/routes.py'])
subprocess.Popen(['python', 'Loja_gamer/routes.py'])
subprocess.Popen(['python', 'Sushalu/routes.py'])

print('Todos os sites foram iniciados!')
