import requests
import re
import glob

myFiles = glob.glob('*.txt')
for file in myFiles:
    f = open(file, 'r')
    payload = {"action":"ajax_hash", "text":"%s" % f.read(), "algo":"md2"}
    r = requests.post("https://www.tools4noobs.com/", data=payload)
    m = re.search('</b> (.+?)</div>', r.text)
    if m:
        found = m.group(1)
    f.close()
    h = open("../hashes.txt", "r")
    hashes = h.read().split('\n')
    if found not in hashes:
        print("Alterado --> ", file)
