import os
import fileinput
import re

def parse(f, dir):
    lineCount = 0
    result = '\\begin{minipage}{\\textwidth}\n'
    path = './sources/' + dir + '/' + f
    for line in fileinput.input(files=path):
        line = re.sub(r'\+(.*)\+', r'\section{\1}', line.rstrip(), flags=re.I)
        line = re.sub(r'#', r'\#', line, flags=re.I)
        line = re.sub(r'([abcdefghijklmnopqrstunwxyzàèìòù]*)\[(.*?)\]', r'\stackon{\1}{\2}', line, flags=re.I)
        line = re.sub(r'à', r"a'", line)
        line = re.sub(r'è', r"e'", line)
        line = re.sub(r'ì', r"i'", line)
        line = re.sub(r'ò', r"o'", line)
        line = re.sub(r'ù', r"u'", line)

        # Ignore the first two lines
        if (lineCount >= 2):
            line += '\\\\'
        line += '\n'
        result += line
        lineCount += 1
    result += '\end{minipage}'
    print(result)

files = {}
for (dirpath, dirnames, filenames) in os.walk("./sources/"):
    for dir in dirnames:
        for (dirpath, dirnames, filenames) in os.walk("./sources/" + dir):
            if (dir in files) and (len(filenames) > 0):
                files[dir].extend(filenames)
            else:
                files[dir] = filenames
    break

for dir in files:
    for f in files[dir]:
        parse(f, dir)
