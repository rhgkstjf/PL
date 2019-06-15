class interprinter:
    def __init__(self,code,ns):
        self.ns = ns
        self.code = code

    def interpret_pro(self):
        for c in self.code:
            print(c)
            self.interpret_func(c)
        print("final")
        print(self.ns)
    
    def interpret_func(self,subcode):
        div = subcode[0]
        if div == "while":
            logic = subcode[1]
            body = subcode[2]
            while(self.interpret_login(logic) != True):
                self.interpret_func(body)
                
        elif div == "print":
            var = subcode[1]
            if var in self.ns:
                ans = self.ns[var]
                print(ans)
            else:
                print("value is not define := print")
        elif div == "=":
            var = subcode[1]
            expr = self.interpret_expr(subcode[2])
            self.ns[var] = expr
        elif div == "if":
            logic = subcode[1][1]
            if logic == True:
                body = subcode[2]
                print("if - execute")
            else:
                print("if - not execute")
        elif div == "else":
            body = subcode[1]
            print("else Enter - execute body")



    def interpret_login(self,subcode):
        op = subcode[0]
        
        ident = 0
        value = 0
        if isinstance(subcode[1],int):
            ident = subcode[1]
        else:
            ident = self.ns[subcode[1]]

        if isinstance(subcode[2],int):
            
            value = subcode[2]
        else:
            value = self.ns[subcode[2]]

        if op == ">":
            if ident > value:
                return True
            else:
                return False
        elif op == "<":
            if ident < value:
                return True
            else:
                return False
        elif op == "equals":
            if ident == value:
                return True
            else:
                return False

            

    def interpret_expr(self,subcode):
        if isinstance(subcode,str) and subcode.isdigit():
            ans = int(subcode)
            return ans
        elif isinstance(subcode,str) and len(subcode) > 0 and subcode[0].isalpha():
            if subcode in self.ns:
                ans = self.ns[subcode]
                return ans
            else:
                print("value not define --")
        else: 
            op = subcode[0]
            v1 = self.interpret_expr(subcode[1])
            v2 = self.interpret_expr(subcode[2])
            ans = 0
            if op == "+":
                ans = v1 + v2
            elif op == "-":
                ans = v1 - v2
            elif op == "*":
                ans = v1 * v2
            elif op == "/":
                ans = v1 / v2
            elif op == "%":
                ans = v1 % v2
            else:
                print("expr error")
            return ans
