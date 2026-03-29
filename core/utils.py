import os
import re

def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def write_file(path, content, encoding="utf-8"):
    folder = os.path.dirname(path)
    if folder:
        safe_mkdir(folder)
    with open(path, "w", encoding=encoding) as f:
        f.write(content)


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9_]+", "_", s)
    s = re.sub(r"_+", "_", s)
    return s.strip("_") or "plugin"
