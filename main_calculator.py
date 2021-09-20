

class Calculator:
    def __init__(self):
        self._number1=0
        self._number2=0
        self._result =0

    def number1(self):
        self._number1 = int(input('Please enter a number: '))

    def number2(self):
        self._number2 = int(input('Please enter another number: '))

    def test(self):
        print(self._number1)
        print(self._number2)

    def printer(self):
        print(self._result)

    def operation(self):
        pass

class Addition(Calculator):
    def operation(self):
        self._result=self._number1+self._number2

class Substraction(Calculator):
    def operation(self):
        self._result=self._number1-self._number2

class Division(Calculator):
    def operation(self):
        self._result=self._number1/self._number2

class Multiplication(Calculator):
    def operation(self):
        self._result=self._number1*self._number2

result=Addition()
result.number1()
result.number2()
result.operation()
result.printer()
result.test()

result2=Multiplication()
#result2.number1()
#result2.number2()
result2.operation()
result2.printer()
result2.test()
    
