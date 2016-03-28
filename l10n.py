'''
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

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
