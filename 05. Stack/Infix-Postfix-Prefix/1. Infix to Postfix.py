


# First store the priority of the elements 
def prec(c):
    if c == '^':
        return 3
    elif c in ['/', '*']:
        return 2
    elif c in ['+', '-']:
        return 1
    else:
        return -1


def infix_to_postfix(s):
    st = []  # Using a list as a stack
    result = ""

    for c in s:
        # If the scanned character is an operand, add it to the output string
        # if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')):
        if c.isalnum():
            result += c
        # If the scanned character is an '(', push it to the stack
        elif c == '(':
            st.append(c)
        # If the scanned character is an ')', pop and add to output string from the stack
        # until an '(' is encountered
        elif c == ')':
            while st and st[-1] != '(':
                result += st.pop()
            if st and st[-1] == '(':
                st.pop()
        # If an operator is scanned
        else:
            # if the current operator is char and the value of it is 
            while st and prec(c) <= prec(st[-1]):
                result += st.pop()
            st.append(c)

    # Pop all the remaining elements from the stack
    while st:
        result += st.pop()

    print("Postfix expression:", result)

if __name__ == "__main__":
    exp = "(p+q)*(m-n)"
    print("Infix expression:", exp)
    infix_to_postfix(exp)