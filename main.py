import requests
import re
import sys
import os

try:
    hashes = sys.argv[1]
    pastaDosArquivos = sys.argv[2]
    if os.path.isfile(hashes) and os.path.isdir(pastaDosArquivos):
        try:
            if list(pastaDosArquivos)[-1] != "\":
                CamAbsoluto = os.getcwd() + "\" + pastaDosArquivos + "\"
            else:
                CamAbsoluto = os.getcwd() + "\" + pastaDosArquivos

            myFiles = [file for file in os.listdir(CamAbsoluto) if re.search('\.txt', file)]
            
            for file in myFiles:
                with open(CamAbsoluto + file, 'r') as f:
                    text = list(f.read())
                if text[-1] == "\n":
                    text.pop()
                payload = {"action":"ajax_hash", "text":"{}".format("".join(text)), "algo":"md2"}
                r = requests.get("https://www.tools4noobs.com/", params=payload)
                m = re.search('</b> (.+?)</div>', r.text)
                if m:
                    found = m.group(1)
                with open(hashes, 'r') as h:
                    hsh = h.read().split('\n')
                    if found not in hsh:
                        print("Alterado --> ", file)
        except IOError:
            print("Arquivo não acessivel")
    else:
        print("Bad Input: o primeiro argumento deve ser um arquivo .txt e o segundo um diretório.")        
except:
    print("""Uso: python script.py <hash> <pasta>

    Onde: <hash> - um arquivo .txt contendo os valores de hash separados por quebra de linha

          <pasta> - pasta/diretório contendo os arquivos a serem verificados a integridade, também em .txt\n""")
