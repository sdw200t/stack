class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]

 
def check(myStr):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = Stack()
    for i in myStr:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((stack.size() > 0) and (open_list[pos] == stack.peek())):
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
  
# Пример сбалансированных последовательностей скобок:  
string = '(((([{}]))))'
print(string,"-", check(string))
  
string = '[([])((([[[]]])))]{()}'
print(string,"-", check(string))
  
string = '{{[()]}}'
print(string,"-",check(string))

# Несбалансированные последовательности:
string = '}{}'
print(string,"-", check(string))
  
string = '{{[(])]}}'
print(string,"-", check(string))
  
string = '[[{())}]'
print(string,"-",check(string))