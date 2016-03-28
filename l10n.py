import glob
import os
from sys import argv

for l10n_path in glob.glob('**/*.' + argv[1], recursive=True):
    path, _ = os.path.splitext(l10n_path)
    if os.path.isfile(path):
        with open(path, 'r+') as file:
            text = file.read()
            with open(l10n_path, 'r') as l10n_file:
                for line in l10n_file.readlines():
                    values = line.strip().split('=', maxsplit=1)
                    if len(values) == 2:
                        text = text.replace("{%s}" % values[0], values[1])
            file.seek(0)
            file.write(text)
            file.truncate()
