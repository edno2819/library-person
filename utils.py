from datetime import datetime
import csv
import shutil, os
from dateutil import tz
import time



# ARQUIVOS DE CONFIGS ------------------------------------------------------------------------------------------------------
def consult_csv():
    configs={}
    gnore = [' ', '[', '#']
    with open('configs.txt', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n')
        for row in spamreader:
            if row!=[]:
                if row[0][0] not in gnore:
                    dic = row[0].split('=')
                    value = dic[1].strip().split(',')
                    configs[dic[0].strip()] = '' if len(dic)<2 else value
    return configs

def salve_csv(ask, space=True):
    file=open('historico.txt', mode='a')
    if space:
        file.write(f'\n{ask}:')
    else:
        file.write(f'{ask}:')
    file.close()  

# SET ENVIROMENT ------------------------------------------------------------------------------------------------------

def set_folder(folder_path, rewrite=False):
    if os.path.exists(folder_path) and rewrite:
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)

def remove_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))

def check_folder(folder_name):
    return os.path.isdir(folder_name)

# FUNÇÕES EXTRAS

def retrys(function, *args, timeout=60*5):
    break_loop = time.time() + timeout
    while time.time() < break_loop:
        try:
            result = function(*args)
            if result is not None:
                return result
        except:
            pass
    raise Exception('Bot loop breaked by reaching timeout!')

def retry(func, loops, erro, **kwargs):
    for _ in range(loops):
        try:
            result=func(kwargs)
            if result!=erro: return result
        except: 
            pass
    return False


# FUNÇÕES DE TEMPO ------------------------------------------------------------------------------------------------------

def time_now(formato):
    return datetime.now().strftime(formato)

def timestamp_converter(x): 
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))
	return str(hora)[:-6]  
