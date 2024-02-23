import subprocess

from gui import GUI

def install_reqs():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

def main():
    gui = GUI()


if __name__ == '__main__':
    install_reqs()
    main()
