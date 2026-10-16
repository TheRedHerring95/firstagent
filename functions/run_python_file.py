import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif target_file[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        else: 
            command = ["python", working_dir_abs+"/"+file_path]
            if args != None:
                command.extend(args)
            process = subprocess.run(command, timeout=30, text=True, capture_output=True)
            if process.returncode != 0:
                return f"Process exited with code {process.returncode}"
            else:
                if process.stdout == None and process.stderr == None:
                    return f"No output produed"
                else: return f"STDOUT: {process.stdout}\nSTDERR: {process.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"