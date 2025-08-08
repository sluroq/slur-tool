import os
import sys
import time
import subprocess
import threading
import platform
import shutil
import zipfile
try:
    import requests
    from pystyle import Colorate, Colors, Write
    from packaging import version
except ModuleNotFoundError:
    def install_libraries():
        libs = ["requests", "pystyle", "packaging"]
        for lib in libs:
            try:
                subprocess.run(["python", "-m", "pip", "install", lib], check=True)
            except subprocess.CalledProcessError as error:
                print(f"Error installing libraries: {error}")
                time.sleep(2.5)
                sys.exit(1)

        print("All required libraries installed successfully.")
        print("Restarting program...")
        time.sleep(1)
        subprocess.Popen([sys.executable, __file__])
        time.sleep(1)
        sys.exit(0)

    install_libraries()

def return_version():
    v1 = None
    v2 = None
    try:
        with open("version.txt", "r", encoding="utf-8") as file:
            try:
                v1 = version.parse(file.read().strip())
            except:
                v1 = version.parse("0.0.0")
    except FileNotFoundError:
        with open("version.txt", "w", encoding="utf-8") as file:
            file.write("1.0.0")
        v1 = version.parse("1.0.0")
    try:
        v2 = version.parse(requests.get("https://raw.githubusercontent.com/sluroq/slur-tool/refs/heads/main/version.txt").text.strip())
    except requests.exceptions.RequestException:
        v2 = version.parse("1.0.0")

    return v1, v2

def update_software():
    try:
        v1, v2 = return_version()

        if v1 != v2:
            print(f"Update available! Your version: {v1}, Newest version: {v2}")

            download_url = "https://github.com/sluroq/slur-tool/archive/refs/heads/main.zip"
            download_path = "slur-tool.zip"

            print("Downloading the latest version...")
            response = requests.get(download_url)

            if response.status_code == 200:
                with open(download_path, "wb") as f:
                    f.write(response.content)
                print("Download complete.")

                print("Extracting files...")
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall("slur-tool-new")

                print("Files extracted to 'slur-tool-new'.")

                if os.path.exists("slur-tool"):
                    print("Deleting old files...")
                    shutil.rmtree("slur-tool")

                os.rename("slur-tool-new", "slur-tool")

                print("Files updated successfully!")

                os.remove(download_path)
            else:
                print(f"Failed to download the latest version. Status code: {response.status_code}")
                time.sleep(2.5)
                sys.exit(1)
        else:
            pass

    except Exception as e:
        print(f"An error occurred while updating the software: {e}")
        time.sleep(2.5)
        sys.exit(1)

class LoadModules():
    pass

def main():
    v1, _ = return_version()

    os.system("cls" if os.name == 'nt' else "clear")
    if os.name == 'nt':
        os.system(f"mode con: cols=100 lines=23")
        os.system(f"title Slur v{v1}")
    else:
        os.system(f"printf '\033[8;23;100t'")
        os.system(f"printf '\033]0;Slur v{v1}\033\\'")

    banner_modules = rf"""
                          ______   _____  _____  _____  _______     
                        .' ____ \ |_   _||_   _||_   _||_   __ \    
                        | (___ \_|  | |    | |    | |    | |__) |   
                         _.____`.   | |   _| '    ' |    |  __ /    
                        | \____) | _| |__/ |\ \__/ /    _| |  \ \_  
                         \______.'|________| `.__.'    |____| |___|  
                  
                          ══╦═════════════════════════════════╦══
                            ║    https://github.com/sluroq    ║
                  ╔═════════╩═════════════════════════════════╩═════════╗  
                  ║ [ 1 ] OSINT                                         ║
                  ║ [ 2 ]                                               ║
                  ║ [ 3 ]                                               ║
                  ║ [ 4 ]                                               ║
                  ║ [ 5 ]                                               ║
                  ║ [ 6 ]                                               ║
                  ║ [ 7 ]                                               ║
                  ║ [ 8 ] Useful websites                               ║
                  ║ [ 9 ]                                               ║
                  ╚═════════════════════════════════════════════════════╝
    """
    colored = Colorate.Vertical(Colors.red_to_purple, banner_modules)
    print(colored)

    while True:
        user_input = Write.Input(f"\n{os.getlogin()}$slur-> ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
        break
        
        
if __name__ == "__main__":
    updater_thread = threading.Thread(target=update_software, daemon=True)
    updater_thread.start()
    main()
