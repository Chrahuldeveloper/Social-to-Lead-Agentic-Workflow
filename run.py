def main():
    import main
from watchgod import run_process

def start_app():
    from main import start
    start()

if __name__ == "__main__":
    run_process(".", start_app)
