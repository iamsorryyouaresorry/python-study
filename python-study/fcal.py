class Fcalc:
    def fadd(self, a ,b):
        self.a = a
        self.b = b
        return self.a + self.b
        
    def fsub(self, a ,b):
        self.a = a
        self.b = b
        return self.a - self.b

    def fmul(self, a ,b):
        self.a = a
        self.b = b
        return self.a * self.b

    def fdiv(self, a ,b):
        self.a = a
        self.b = b
        return self.a / self.b

class Fcala: 
    def fsqrt(self, a, b):
        self.a = a
        self.b = b
        return self.a ** self.b

if __name__ == "__main__":
    cal1 = Fcalc()
    print(cal1.fadd(10, 20))
    print(cal1.fsub(10, 20))
    print(cal1.fmul(10, 20))
    print(cal1.fdiv(10, 20))