from stack import module

if __name__ == '__main__':
    stack = module.Stack(4)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print_stack()