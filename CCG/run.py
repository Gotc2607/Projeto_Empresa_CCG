#rodando todos os sites ao mesmo tempo
import subprocess

subprocess.Popen(['python', 'Pagina_inicial/routes.py'])
subprocess.Popen(['python', 'Led_gamers/routes.py'])
subprocess.Popen(['python', 'Sushalu/routes.py'])
subprocess.Popen(['python', 'LedGamer/run.py'])

print('Todos os sites foram iniciados!')
