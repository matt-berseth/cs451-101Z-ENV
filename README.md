# cs451-101Z-ENV
Follow the instructions to ensure you have the computing environment configured properly.

## Steps
1. Install Ubuntu 22.04.2 LTS (WSL)
1. Configure python 3.10
```bash
# launch a WSL window
sudo apt update
sudo apt -y upgrade

# confirm python 3.10
python3 -V

# install python dev tools
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
1. Clone this repo.
```bash
git clone https://github.com/matt-berseth/cs451-101Z-ENV.git
```
1. Create the virtual environment and launch vscode
```bash
python3 -m venv .venv
source ./.venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

code .
```
1. Install the following vscode packages (Python, Pylance)
1. Launch the 'main' entry.
