import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = 'json'
    BYTE = 'byte'

class SerializeManager:
    def __init__(self, filename: str, filetype: FileType):
        self.filename = filename
        self.filetype = filetype

    def __enter__(self):
        if self.filetype == FileType.BYTE:
            self.file = open(self.filename, 'wb')
        elif self.filetype == FileType.JSON:
            self.file = open(self.filename, 'w', encoding='utf-8')
        else:
            raise ValueError("Unsupported file type")
        return self

    def serialize(self, obj):
        if self.filetype == FileType.JSON:
            json.dump(obj, self.file, ensure_ascii=False, separators=(', ', ': '))
        elif self.filetype == FileType.BYTE:
            pickle.dump(obj, self.file)
        else:
            raise ValueError("Unsupported file type")

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

def serialize(object, filename, filetype):
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(object)