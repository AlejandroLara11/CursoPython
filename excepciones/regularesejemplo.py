import re
text = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$", text)  #el * significa 0 coincidencias o mas del operador anterior

if x:
    print("SI")
else:
    print("NO")