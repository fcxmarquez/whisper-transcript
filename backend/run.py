import subprocess
import sys

from app import create_app

app = create_app()


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"{command[0]} found issues:")
        print(result.stdout)
        return False
    return True


if __name__ == "__main__":
    # Run Black to format the code
    if not run_command(["black", "."]):
        sys.exit(1)

    # Run Pylint
    if not run_command(["pylint", "**/*.py"]):
        sys.exit(1)

    app.run(debug=True)
