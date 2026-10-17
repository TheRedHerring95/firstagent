import os
    
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        dir = ""
        if directory == ".":
            dir = "current directory"
        else: dir = directory
        pre = f"Result for {dir}:"
        if valid_target_dir == False:
            return f'{pre}\nError: Cannot list "{directory}" as it is outside the permitted working directory'
        #elif os.path.isdir(target_dir) == False:
        #    return f'{pre}\nError: "{directory}" is not a directory'
        #elif valid_target_dir == True:
        #    return f'Success: "{directory}" is within the working directory'
        else:
            list_dir = os.listdir(target_dir)
            item_list = []
            items_string = ""
            for item in list_dir:
                size = ""
                is_dir = False
                if os.path.isdir(target_dir+"/"+item):
                    is_dir = True
                size = os.path.getsize(target_dir+"/"+item)
                item_list.append(f"  - {item}: file_size={size}, is_dir={is_dir}")
            for item in item_list:
                items_string = "\n".join(item_list)
            return f"{pre}\n{items_string}"
    except Exception as e:
        return f"Error: {e}"

