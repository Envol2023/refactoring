import subprocess
import sys
from pathlib import Path

def get_asciidoc_list(location: Path) -> list[Path]:
    with open(location, 'r') as file:
        return  [Path(line.strip()) for line in file.readlines()]

def convert_asciidocs_to_html(paths: list[Path]):
    for doc in paths:
        if not doc.exists():
            print(f"{doc}doesn't not exist", file=sys.stderr )

        name = doc.stem
        path = doc.parent
        subprocess.Popen(f"bin/asciidoctor-revealjs {doc} -o {name}.html -v", shell=True)
        #subprocess.Popen(f"bin/asciidoctor {doc} -a data-uri -b html5 -o book_{name}.html -v", shell=True)

convert_asciidocs_to_html(get_asciidoc_list(Path('./documents.txt')))