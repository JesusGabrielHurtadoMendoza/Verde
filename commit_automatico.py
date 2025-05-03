import os
import time
import subprocess
from datetime import datetime

# Directorio donde está tu repositorio Git
repo_dir = r'C:\Users\mm\Downloads'  # Cambia esto por el path de tu repositorio

# Configura Git con tu nombre y correo
def configurar_git():
    subprocess.run(['git', 'config', '--global', 'user.name', 'JesusGabrielHurtadoMendoza'])
    subprocess.run(['git', 'config', '--global', 'user.email', 'jesusgabo2002@gmail.com'])

# Hacer commit diario (100 commits)
def hacer_commits():
    os.chdir(repo_dir)
    for i in range(100):  # Realiza 100 commits
        # Crea un archivo temporal para simular el commit
        archivo_temp = f"commit_{i}.txt"
        with open(archivo_temp, 'w') as f:
            f.write(f"Commit {i} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Añadir el archivo y hacer commit
        subprocess.run(['git', 'add', archivo_temp])
        subprocess.run(['git', 'commit', '-m', f'Commit automático {i}'])
        
        # Elimina el archivo después de hacer commit
        os.remove(archivo_temp)

# Función principal
def main():
    configurar_git()  # Asegúrate de configurar Git antes de hacer commits
    hacer_commits()  # Realiza los 100 commits

if __name__ == "__main__":
    main()
