class interprinter:
    def __init__(self):
        self.ns = {}
        self.code = []
        self.condition = 0
    def interpret_pro(self,code):
        self.code = [code]
        for c in self.code:
            self.interpret_func(c)

    def interpret_ns(self):
        return self.ns

    def interpret_func(self,subcode):
        div = subcode[0]
        if div == "while":
            logic = subcode[1][1]
            body = subcode[2]
            print(logic)
            while(self.interpret_login(logic) != True):
                self.interpret_func(body)
                
        elif div == "print":
            var = subcode[1]
            if var in self.ns:
                ans = self.ns[var]
                print("print execute : "+str(ans))
            else:
                print("value is not define := print")
        elif div == "=":
            var = subcode[1]
            expr = self.interpret_expr(subcode[2])
            self.ns[var] = expr
        elif div == "if":
            logic = self.interpret_login(subcode[1][1])
            if logic == True:
                body = self.interpret_func(subcode[2])
                print("if - execute")
            else:
                self.condition = 1
                print("if - not execute")
        elif div == "else" and self.condition == 1:
            body = self.interpret_func(subcode[1])
            print("else Enter - execute body")
            self.condition = 0



    def interpret_login(self,subcode):
        op = subcode[0]

        ident = self.interpret_expr(subcode[1])
        value = self.interpret_expr(subcode[2])
        

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
