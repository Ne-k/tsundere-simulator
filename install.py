import os
import platform
import subprocess
import sys
import requests


def download_installer(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

def install_windows():
    installer_url = "https://installers.lmstudio.ai/win32/x64/0.3.8-4/LM-Studio-0.3.8-4-x64.exe"
    installer_path = os.path.join(os.getcwd(), "lmstudio_installer.exe")
    download_installer(installer_url, installer_path)
    subprocess.check_call([installer_path])

def install_mac():
    installer_url = "https://installers.lmstudio.ai/darwin/arm64/0.3.8-4/LM-Studio-0.3.8-4-arm64.dmg"
    installer_path = os.path.join(os.getcwd(), "lmstudio_installer.dmg")
    download_installer(installer_url, installer_path)
    subprocess.check_call(["hdiutil", "attach", installer_path])
    subprocess.check_call(["sudo", "cp", "-r", "/Volumes/LMStudio/LMStudio.app", "/Applications"])
    subprocess.check_call(["hdiutil", "detach", "/Volumes/LMStudio"])

if __name__ == "__main__":
    current_os = platform.system()
    print(f"Installing LMStudio for {current_os}")
    if current_os == "Windows":
        install_windows()
    elif current_os == "Darwin":
        print("Go and execute the downloaded installer for LMStudio manually, I wrote code to run the installer but I "
              "can't test it, and don't want to be liable for system damages if it causes any :3")
        # install_mac()
    else:
        print(f"Unsupported operating system: {current_os}")
