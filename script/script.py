import requests
import re
import glob
import sys

hashes = sys.argv[1]
pastaDosArquivos = sys.argv[2]
if list(pastaDosArquivos)[-1] != "/":
    pastaDosArquivos += "/"

# cria uma lista com os nomes dos arquivos, no caso são .txt
myFiles = glob.glob('%s*.txt' % pastaDosArquivos)
for file in myFiles:
    with open(file, 'r') as f:
        payload = {"action":"ajax_hash", "text":"%s" % f.read(), "algo":"md2"}
        r = requests.post("https://www.tools4noobs.com/", data=payload)
        # captura o valor de hash dentro do response do site
        m = re.search('</b> (.+?)</div>', r.text)
        if m:
            found = m.group(1)
        with open(hashes, 'r') as h:
            hsh = h.read().split('\n')
            if found not in hsh:
                print("Alterado --> ", file)
