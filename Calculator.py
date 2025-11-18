def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def to_rpn(expression):
    output = []
    stack = []
    i = 0
    while i < len(expression):
        token = expression[i]

        if token.isdigit() or (token == '.' and i + 1 < len(expression) and
                               expression[i + 1].isdigit()):
            num = token
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or
                                               expression[i + 1] == '.'):
                i += 1
                num += expression[i]
            output.append(num)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

        i += 1

    while stack:
        output.append(stack.pop())

    return output


def eval_rpn(rpn):
    stack = []
    for token in rpn:
        if token not in '+-*/^':
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack[0]


def calculate(expression):
    expression = expression.replace(' ', '')
    rpn = to_rpn(expression)
    print(rpn)
    result = eval_rpn(rpn)
    return result


if __name__ == "__main__":
    expr = input("Введите выражение: ")
    try:
        res = calculate(expr)
        print("Результат:", res)
        print("-")
    except Exception as e:
        print("Ошибка в выражении:", e)
