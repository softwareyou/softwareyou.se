import glob
import os
from sys import argv

for l10n_path in glob.glob('**/*.' + argv[1], recursive=True):
    html_path, _ = os.path.splitext(l10n_path)
    if os.path.isfile(html_path):
        with open(html_path, 'r+') as html_file:
            html_text = html_file.read()
            with open(l10n_path, 'r') as l10n_file:
                for line in l10n_file.readlines():
                    values = line.strip().split('=', maxsplit=1)
                    if len(values) == 2:
                        html_text = html_text.replace("{%s}" % values[0], values[1])
            html_file.seek(0)
            html_file.write(html_text)
            html_file.truncate()
