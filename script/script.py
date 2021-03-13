import requests
import re
import glob

# cria uma lista com os nomes dos arquivos, no caso são .txt
myFiles = glob.glob('*.txt')
for file in myFiles:
    f = open(file, 'r')
    payload = {"action":"ajax_hash", "text":"%s" % f.read(), "algo":"md2"}
    r = requests.post("https://www.tools4noobs.com/", data=payload)
    # captura o valor de hash dentro do response do site
    m = re.search('</b> (.+?)</div>', r.text)
    if m:
        found = m.group(1)
    f.close()
    h = open("../hashes.txt", "r")
    hashes = h.read().split('\n')
    if found not in hashes:
        print("Alterado --> ", file)
    h.close()
