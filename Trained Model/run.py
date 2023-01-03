import model

b = True

while(b):
    customer_id = input("Enter Customer ID: \n")
    lst = model.predict(customer_id)
    print("Embifi's Repayment Score of the Customer is: ", lst[0])
    print("Probability of Default: ", lst[1])
    value = input(" More Input : Press 1 to continue and 0 to exit \n")
    if(value=='0'):
        b = False
    
