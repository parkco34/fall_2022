#!/usr/bin/env python
#Truth Table Generator - www.101computing.net/truth-table-generator/

def truthTable(expression,inputs=2):
    """
    MY CONTRIBUTION:
        ============================================================
        - If the expression has "if" and "then" in the string, then it's a
        CONDITIONAL STATEMENT: p -> q
        - Convert the conditional to [~p v q] form
        - The letter that follows the "if" statement will plucked from the
        expression where it'll be given a "~" infront of it, followed by an OR
        statement between that and the letter that follows "then", which will
        replace the EXPRESSION.
        ============================================================
    """
    print("Boolean Expression:")
    print("  X = " + expression.upper() + "\n")
    expression = expression.lower()
    expression_list = expression.split();

    # If "if" and "then" is in the string, change the expression to something
    # we can use bit-wise operators on...
    if any(item in ["if", "then"] for item in expression_list):
        for el in range(len(expression_list)):
            if expression_list[el] == "if":
                proper = ''.join(" not " + expression_list[el+1] + " " + "or ")

            elif expression_list[el] == "then":
                proper = proper + ''.join(expression_list[el+1])

    expression = proper

    #replace Boolean Operators with bitwise operators
    expression = expression.replace("and","&")
    expression = expression.replace("xor","^")
    expression = expression.replace("or","|")
    expression = expression.replace("not","~")

    print("\nTruth Table:")
    if inputs==2:
        print("  -------------")
        print("  | p | q | X |")
        print("  -------------")

        for a in range(0,2):
            for b in range(0,2):
                breakpoint()
                x = eval(expression)
                print("  | " + str(a) + " | " + str(b) + " | " + str(x) + " |" )
                print("  -------------")

    elif inputs==3:
        print("  -----------------")
        print("  | p | q | r | X |")
        print("  -----------------")

        for a in range(0,2):
          for b in range(0,2):
            for c in range(0,2):
              x = eval(expression)
              print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" )
              print("  -----------------")

    elif inputs==4:
        print("  ---------------------")
        print("  | p | q | r | s | X |")
        print("  ---------------------")

        for a in range(0,2):
          for b in range(0,2):
            for c in range(0,2):
              for d in range(0,2):
                x = eval(expression)
                print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(x) + " |" )
                print("  ---------------------")

##############################################

expression = input("Enter your proposition:\n")
truthTable(expression,int(input("\nHow many parameters?\n")))

