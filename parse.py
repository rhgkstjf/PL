
#letter -> 0
#digit -> 1
#int -> 10
#assign 20 -> =
#add 21 -> +
#sub 22 -> -
#mul 23 -> *
#div 24 -> /
#( -> 25
#) -> 26
#comp_left 27 -> <
#comp_right 28 -> >
#remain 29 -> %
#separator_left 30 -> {
#separator_right 31 -> }
#separator 40 -> ~
#complex separator 41 -> ;
#while -> 80
#while finish -> 81
#ident -> 99 
#EOF -> 100
#print -> 141
#conditioner 200 -> if
#conditioner 201 -> else
#equal -> 222
#array_left -> 300
#array_right -> 301
#equal -> 400
class lex_basic:
    def __init__(self,txt):
        self.txt = txt
        self.index = -1
        self.nextChar = ""
        self.charClass = 0
        self.nextToken = 0
        self.lexLen = 0
        self.lexeme = ""
        self.parse = []
        self.impo = []
        
        self.inter = []
        self.tmp =[]
    def getChar(self):
        self.index += 1
        if self.index != len(self.txt):
            self.nextChar = self.txt[self.index]
            if self.nextChar.isalpha():
                self.charClass = 0
            elif self.nextChar.isdigit():
                self.charClass = 1
            else:
                self.charClass = 99
        else:
            self.charClass = 100
    
            
    def addChar(self):
        if self.lexLen <= len(self.txt):
            self.lexLen += 1
            self.lexeme+= self.nextChar
        else:
            print("Error - lexeme is too long")

    def getNonBlank(self):
        self.lexeme = ""
        while self.nextChar.isspace() == True:
            self.getChar()


    def lex(self):
        self.lexLen = 0
        self.getNonBlank()

        if self.charClass == 0:
            self.addChar()
            self.getChar()
            while self.charClass == 0 or self.charClass == 1:
                self.addChar()
                self.getChar()
            self.nextToken = 99
        elif self.charClass == 1:
            self.addChar()
            self.getChar()
            while self.charClass == 1:
                self.addChar()
                self.getChar()
            self.nextToken = 10
        elif self.charClass == 99:
            self.lookup(self.nextChar)
            self.getChar()
        else:
            self.nextToken = 100
        
        
        if self.lexeme == "while":
            self.nextToken = 80
        elif self.lexeme == "if":
            self.nextToken = 200
        elif self.lexeme == "else":
            self.nextToken = 201
        elif self.lexeme == "equals":
            self.nextToken = 222
        elif self.lexeme == "finish":
            self.nextToken = 81
        elif self.lexeme == "print":
            self.nextToken = 141
        
        
        print("Next token is:"+str(self.nextToken)+"Next lexeme is "+str(self.lexeme))
        self.parse.append(str(self.lexeme))
        List = [self.nextToken,str(self.lexeme)]
        self.impo.append(List)
        return self.nextToken

    def lookup(self,ch):
        if ch == '(':
            self.addChar()
            self.nextToken = 25
        elif ch == ')':
            self.addChar()
            self.nextToken = 26
        elif ch == '+':
            self.addChar()
            self.nextToken = 21
        elif ch == '-':
            self.addChar()
            self.nextToken = 22
        elif ch == '*':
            self.addChar()
            nextToken = 23
        elif ch == '/':
            self.addChar()
            self.nextToken = 24
        elif ch == '=':
            self.addChar()
            self.nextToken = 20
        elif ch == '<':
            self.addChar()
            self.nextToken = 27
        elif ch == '>':
            self.addChar()
            self.nextToken = 28
        elif ch == '%':
            self.addChar()
            self.nextToken = 29
        elif ch == '{':
            self.addChar()
            self.nextToken = 30
        elif ch == '}':
            self.addChar()
            self.nextToken = 31
        elif ch == '~':
            self.addChar()
            self.nextToken = 40
        elif ch == ';':
            self.addChar()
            self.nextToken = 41
        elif ch == ':':
            self.addChar()
            self.nextToken = 65
        elif ch == '[':
            self.addChar()
            self.nextToken == 300
        elif ch == ']':
            self.addChar()
            self.nextToken == 301
        else:
            self.addChar()
            self.nextToken = 100
        return self.nextToken

    def main_lex(self):
        self.getChar()
        while True:
            self.lex()
            if self.nextToken == 100:
                print("읽기끝")
                break;
        print(self.parse)
        return self.impo
    

    def return_inter(self):
        return self.inter

    def start(self):
        self.lex()
        tree = self.pro()
        return tree
    
    def pro(self):
        dev = self.func()
        while self.nextToken == 41:
            w = self.lexeme
            self.lex()
            self.inter.append(dev)
            if self.nextToken == 100:
                print("EOF")
            else:
                dev = self.func()
                
        return dev
    
    def func(self):
        if self.nextToken == 99:
            sub = self.declaration()
            return sub
        elif self.nextToken == 80:
            exp = self.expr()
            if self.nextToken == 65:
                self.lex()
            else:
                print("while - is not ':'")
            pro = self.pro()
            if self.nextToken == 81:
                self.lex()
                sub = ["while",exp,pro,"finish"]
                return sub
            else:
                print("while - error is not")
        elif self.nextToken == 30:
            self.lex()
            #sub = ["{",self.pro()]
            sp = self.pro()
            return sp
        elif self.nextToken == 141:
            s = self.hprint()
            self.lex()
            return s
        elif self.nextToken == 200:
            sub = self.conditioner()
            if self.nextToken == 81:
                self.lex()
                sub.append("finish")
                return sub
            else:
                print("condition is not exist 'finish'")
        elif self.nextToken == 201:
            sub = self.conditioner()
            if self.nextToken == 81:
                self.lex()
                sub.append("finish")
                return sub
            else:
                print("condition is not exist 'finish'")
        else:
            print(self.lexeme)
            print("error is not garmmer")
        
            
    def declaration(self):
        ident = self.lexeme
        self.lex()
        sub = ["=",ident,self.expr()]
        return sub
    
    def conditioner(self):
        ident = self.lexeme
        if self.nextToken == 200:
            self.lex()
            if self.nextToken == 25:
                tp = self.expr()
                if self.nextToken == 26:
                    self.lex()
                    exe = self.func()
                    semi = ["(",tp,")"]
                    last = [ident,semi,exe]
                    return last;
                else:
                    print("conditioner ')' not exist")
            else:
                print("conditioner if '(' not exist")
        elif self.nextToken == 201:
            self.lex()
            pro = self.pro()
            return [ident,pro]
        else:
            print("is error - recieve : it's not conditoner")
        
        
    def hprint(self):
        self.lex()
        if self.nextToken == 99 or self.nextToken == 10:
            sub = ["print",self.lexeme]
            return sub


    def expr(self):
        self.lex()
        v = self.lexeme
        if self.nextToken == 10 or self.nextToken == 99:
            self.lex()
            if self.nextToken == 21:
                sub = ["+",v,self.expr()]
                return sub
            elif self.nextToken == 22:
                sub = ["-",v,self.expr()]
                return sub
            elif self.nextToken == 23:
                sub = ["*",v,self.expr()]
                return sub
            elif self.nextToken == 24:
                sub = ["/",v,self.expr()]
                return sub
            elif self.nextToken == 29:
                sub = ["%",v,self.expr()]
                return sub
            elif self.nextToken == 27:
                sub = ["<",v,self.expr()]
                return sub
            elif self.nextToken == 28:
                sub = [">",v,self.expr()]
                return sub
            elif self.nextToken == 222:
                sub = ["equals",v,self.expr()]
                return sub
            else:
                #print("expr return value : " + str(v))
                return v
        else:
            print("Grammer - error")

p = lex_basic("while k equals 0 : a= a + 1 finish ;  k = k + 1; a = k; if(k equals 0) a = a +1 finish; else k = k+1 finish; print a;")
k = p.start()
k = p.return_inter()
print(k)
#print(k[0])
#print(k[1])
#print(k[2])
#print(k[3])
#print(k[4])
#print(k[5])
