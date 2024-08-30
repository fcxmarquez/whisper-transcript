import subprocess
import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_command(command, timeout=60):
    print(f"Running command: {' '.join(command)}")
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            print(f"{command[0]} found issues:")
            print(result.stdout)
            print(result.stderr)
            return False
        print(f"{command[0]} completed successfully.")
        return True
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds: {' '.join(command)}")
        return False
    except Exception as e:
        print(f"An error occurred while running {command[0]}: {str(e)}")
        return False


def run_linters():
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")

    # Run Black to format the code
    run_command([sys.executable, "-m", "black", "."])

    # Run Pylint on individual Python files
    python_files = [f for f in os.listdir(".") if f.endswith(".py")]
    for file in python_files:
        run_command([sys.executable, "-m", "pylint", file], timeout=120)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Flask app with optional linting")
    parser.add_argument("--skip-lint", action="store_true", help="Skip linting")
    args = parser.parse_args()

    if not args.skip_lint:
        run_linters()

    print("Starting the Flask application...")
    from app import create_app

    app = create_app()
    app.run(debug=True)
