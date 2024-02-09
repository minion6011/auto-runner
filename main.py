import requests
import subprocess
import os

#config - main.py

repo_url_m = 'https://github.com/profilename/reposity'
file_path_m = 'startfilemain.py'

#config - requirement

repo_url_re = 'https://github.com/profilename/reposity'
file_path_re = 'requirementsfilename.txt'







#code

#requirements - code

def install_packages_from_text(repo_url_r,file_path_r):
    raw_url = repo_url_r.replace('github.com', 'raw.githubusercontent.com').rstrip('/') + '/main/' + file_path_r
    
    # Fare una richiesta GET all'URL raw per ottenere il contenuto del file
    response = requests.get(raw_url)
    
    # Verificare se la richiesta ha avuto successo
    if response.status_code == 200:
        # Eseguire il contenuto
        packages_text = response.text
        packages_list = packages_text.split('\n')
        for package_name in packages_list:
            package_name = package_name.strip()
            if package_name:  # Assicura che non si stia cercando di installare una riga vuota
                try:
                    os.system("pip install " + package_name)
                    #subprocess.check_call(['pip', 'install', package_name])
                    print(f"Package '{package_name}' has been successfully installed.")
                except Exception as e:
                    print(f"Error installing package '{package_name}': {e}")
    else:
        print(f"Errore {response.status_code}: Impossibile ottenere il file.")







#main.py - code

def get_github_code(repo_url, file_path):
    # Ottenere l'URL raw del file sul repository GitHub
    raw_url = repo_url.replace('github.com', 'raw.githubusercontent.com').rstrip('/') + '/main/' + file_path
    
    # Fare una richiesta GET all'URL raw per ottenere il contenuto del file
    response = requests.get(raw_url)
    
    # Verificare se la richiesta ha avuto successo
    if response.status_code == 200:
        # Eseguire il contenuto
        codice = response.text
        code = compile(codice, "", "exec")
        exec(code)
    else:
        print(f"Errore {response.status_code}: Impossibile ottenere il file.")




install_packages_from_text(repo_url_re,file_path_re)
print("istallazione pacchetti completata")
get_github_code(repo_url_m,file_path_m)
