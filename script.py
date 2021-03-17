import requests
import re
import glob
import sys

try:
    hashes = sys.argv[1]
    pastaDosArquivos = sys.argv[2]
    if list(pastaDosArquivos)[-1] != "/":
        pastaDosArquivos += "/"

    myFiles = glob.glob('%s*.txt' % pastaDosArquivos)
    for file in myFiles:
        with open(file, 'r') as f:
            payload = {"action":"ajax_hash", "text":"%s" % f.read(), "algo":"md2"}
            r = requests.post("https://www.tools4noobs.com/", data=payload)
            m = re.search('</b> (.+?)</div>', r.text)
            if m:
                found = m.group(1)
            with open(hashes, 'r') as h:
                hsh = h.read().split('\n')
                if found not in hsh:
                    print("Alterado --> ", file)
except:
    print("""Uso: python script.py <hash> <pasta>

    Onde: <hash> - um arquivo .txt contendo os valores de hash separados por quebra de linha

          <pasta> - pasta/diretório contendo os arquivos a serem verificados a integridade, também em .txt\n""")
