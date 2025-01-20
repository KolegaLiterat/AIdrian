import yaml

class PromptReader():
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    def read_file(self) -> dict:
        try:
            with open(self.file_path, "r") as yaml_file:
                return yaml.safe_load(yaml_file)
        
        except FileNotFoundError as e:
            raise ValueError("Missing prompt file!")

class File():
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    def save(self, data: any) -> None:
        with open(self.file_path, "w") as file:
            file.write(str(data))