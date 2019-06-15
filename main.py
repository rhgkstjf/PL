from paser import lex_basic
from inte import interprinter



lastcode = "y = 5; k = 2; a = 1; while (y equals 1) : y = y-1 finish ; a = k + 2; if(y < 1) y = a finish; else y = k finish; print a;"

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
