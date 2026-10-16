import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if valid_file_path == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_file) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            path_list = file_path.split("/")
            folders_list = []
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            with open(target_file, mode='wt') as f:
                f.write(content)
            return f'Sucessfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"