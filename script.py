import tkinter as tk
from tkinter import filedialog
from colorama import Fore, init
import time
import os

# Inicializa a colorama
init(autoreset=True)

def load_usernames(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

def compare_followers(old_file, new_file):
    old_followers = load_usernames(old_file)
    new_followers = load_usernames(new_file)

    unfollowed = old_followers - new_followers
    new_followers_added = new_followers - old_followers

    print(f"\n{Fore.RED}[ - ] Deixaram de seguir ou mudaram de nome:")
    for user in unfollowed:
        print(f"{Fore.RED}[ - ] {user}")

    print(f"\n{Fore.GREEN}[ + ] Começaram a seguir ou mudaram de nome:")
    for user in new_followers_added:
        print(f"{Fore.GREEN}[ + ] {user}")

    # Perguntar se deseja salvar em um arquivo .txt
    save = input("\nDeseja salvar a lista em um arquivo .txt? (s/n): ").strip().lower()
    if save == 's':
        save_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_file:
            with open(save_file, "w", encoding="utf-8") as file:
                file.write(f"[ - ] Deixaram de seguir ou mudaram de nome:\n")
                for user in unfollowed:
                    file.write(f"[ - ] {user}\n")
                
                file.write(f"\n[ + ] Começaram a seguir ou mudaram de nome:\n")
                for user in new_followers_added:
                    file.write(f"[ + ] {user}\n")
            print(f"\nLista salva em: {save_file}")
        else:
            print("\nArquivo não foi salvo.")

def get_file_path(prompt):
    root = tk.Tk()
    root.withdraw()  # Não exibe a janela principal
    file_path = filedialog.askopenfilename(title=prompt)
    return file_path

def clear_screen():
    # Limpa a tela, dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":

    print("Por favor, siga as instruções abaixo para selecionar os arquivos.")
    
    print(f"\n{Fore.GREEN}Primeiro, selecione o arquivo com a lista antiga")
    
    time.sleep(3)
    old_txt = get_file_path("Selecione o arquivo de seguidores ATUAIS")
    
    clear_screen()  # Limpa a tela após a seleção do primeiro arquivo

    print(f"\n{Fore.GREEN}Agora, selecione o arquivo com a lista mais recente")
    
    time.sleep(3)
    new_txt = get_file_path("Selecione o arquivo de seguidores MAIS RECENTES")

    clear_screen()  # Limpa a tela após a seleção do segundo arquivo

    # Comparando as listas
    compare_followers(old_txt, new_txt)
