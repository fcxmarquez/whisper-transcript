from app import create_app
import subprocess
import sys

app = create_app()

if __name__ == '__main__':
    # Run Flake8 before starting the app
    result = subprocess.run(['flake8'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Flake8 found issues:")
        print(result.stdout)
        sys.exit(1)

    app.run(debug=True)
