def decision_tree(age, income):

    if income >= 50000:
        if age >= 30:
            return "Loan Approved"
        else:
            return "Loan Approved"

    else:
        return "Loan Rejected"


age = int(input("Enter Age: "))
income = int(input("Enter Income: "))

result = decision_tree(age, income)

print(result)
