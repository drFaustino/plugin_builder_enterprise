import os
from ..core.utils import safe_mkdir

class FileWriter:
    def __init__(self, base_path, log):
        self.base_path = base_path
        self.log = log

    def full(self, *parts):
        return os.path.join(self.base_path, *parts)

    def write(self, rel_path, content):
        path = self.full(rel_path)
        safe_mkdir(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        self.log.append(f"Created file: {rel_path}")
