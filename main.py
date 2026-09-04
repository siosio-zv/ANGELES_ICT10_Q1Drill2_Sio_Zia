from pyscript import document

def compute(event):

    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)

    operation = document.querySelector("#operation").value

# If the operation is addition
    if operation == "+":
        answer = num1+num2

# If the operation is subtraction
    elif operation == "-":
        answer = num1-num2

# If the operation is multiplication
    elif operation == "x":
        answer = num1*num2

# If the operation is division
    elif operation == "/":

        # Used if the user inputs the number zero
        if num2 == 0:
            document.querySelector("#result").innerText = "Cannot Be Divide by Zero"
            return
        answer = num1/num2

# Answer will be provided here
    document.querySelector("#result").innerText = "Result" + str(answer)