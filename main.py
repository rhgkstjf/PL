from paser import lex_basic
from inte import interprinter



lastcode = "k = 1; a = 1; while (k equals 0) : k= k-1 finish ; a = k + 2; if(k equals 0) k = k - 1 finish; else k = k+1 finish; print a;"

code = "while a equals 0 : a = a -1 finish;"
p = lex_basic(lastcode)
k = p.start()
k = p.return_inter()
print(k)

a = interprinter()
for c in k:
    a.interpret_pro(c)
ns = a.interpret_ns()

print(ns)
