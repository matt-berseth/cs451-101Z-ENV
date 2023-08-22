# cs451-101Z-ENV
Follow the instructions to ensure you have the computing environment configured properly.

## Windows 10/11 Steps
1. Clone the repo: https://github.com/matt-berseth/cs451-101Z-ENV.git using GitHub Desktop (as shown in Environment Set Up - Windows.docx)
1. Open powershell terminal with the current directory the cs451-101Z-ENV folder
1. From a powershell command line, run the following commands
```powershell
# confirm version is 3.10
python3.10 -v

# create a virtual environment
python3.10 -m venv .venv

# activate virtual environment
.\.venv\Scripts\activate.ps1

# upgrade pip
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt

# launch vscode
code .
```

## Ubuntu 22.04.2 Steps
1. Install Ubuntu 22.04.2 LTS (WSL)
2. Clone the repo: https://github.com/matt-berseth/cs451-101Z-ENV.git from the wsl command line
1. Open wsl terminal with the current directory the cs451-101Z-ENV folder
2. From the wsl terminal, run the following commands
```bash
# launch a WSL window
sudo apt update
sudo apt -y upgrade

# confirm python 3.10
python3 -V

# install python dev tools
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

# create and enter virtual environment
python3 -m venv .venv
source ./.venv/bin/activate

# install requirements
pip install --upgrade pip
pip install -r requirements.txt

# launch vscode
code .
```
1. Install the following vscode packages (Python, Pylance)
1. Launch the 'main' entry.
