import subprocess
import sys

def install_requirements():
    requirements = ['sippy', 'flask', 'twisted']
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    print("Setting up Custom SIP Server for Windows...")
    try:
        install_requirements()
        print("Setup complete! You can now run main.py")
    except Exception as e:
        print(f"An error occurred: {e}")
