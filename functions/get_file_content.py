import os
from config import MAX_CHARS_READ

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file path relative to the working directory, providing contents contained",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path for the file to be read, there is no default so a file must be provided",
                },
            },
        },
    },
}

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if valid_file_path == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(target_file, "r") as f:
                content = f.read(MAX_CHARS_READ)
                if f.read(1):
                    content += f'\n[...File "{file_path}" truncated at {MAX_CHARS_READ} characters]'
                return content

    except Exception as e:
        return f"Error: {e}"