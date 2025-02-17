import os
import subprocess
import sys

def run_yaml_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check for both .yaml and .yml extensions
        if filename.endswith((".yaml", ".yml")):
            filepath = os.path.join(directory, filename)
            print(f"Running: qrun {filepath}")
            
            # Execute the qrun command with the YAML file as argument
            result = subprocess.run(["qrun", filepath], capture_output=True, text=True)
            
            # Print stdout and stderr from the command
            if result.stdout:
                print("Output:", result.stdout)
            if result.stderr:
                print("Error:", result.stderr)

if __name__ == "__main__":
    # If no directory is provided, default to the current directory
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    run_yaml_files(directory)
