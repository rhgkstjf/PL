from paser import lex_basic
from inte import interprinter



lastcode = "while k equals 0 : k= k-1 finish ;  k = k + 1; a = k; if(a equals 0) a = a - 1 finish; else k = k+1 finish; print a;"

code = "while a equals 0 : a = a -1 finish;"
p = lex_basic(code)
k = p.start()
k = p.return_inter()
print(k)

ns = {'a':1,'k':2}
a = interprinter(k,ns)
a.interpret_pro()

