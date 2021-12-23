#Author: Arshveer Gahir


def federal_income_Tax(income):

    #Income Tax Brackets (implemented in v2)
    tax_brackets = {0 : 0, 49020 : 7353, 98040 : 17402, 151978 : 31425.98, 216511 : 50140.55} #tax bracket minimum : max Total Tax for previous ranges
    

    #Calculate Canadian Federal Tax

    global tax_fed 
    tax_fed= 0

    if income in range(0,49020):
        tax_fed = income * 0.15
    elif income in range(49020,98040):
        tax_fed = 7353 + (income - 49019) * 0.205  
    elif income in range(98040,151978):
        tax_fed = 17402.10 + (income - 98039) * 0.26
    elif income in range(151978,216511):
        tax_fed = 31425.98 + (income - 151977) * 0.29
    else:
        tax_fed = 50140.55 + (income - 216510) * 0.33

    print("Your Federal Income Tax is {:.2f}".format(tax_fed))

def ontario_income_tax(income):
    #Calculate Ontario Provincial Tax

    global tax_prov
    tax_prov = 0

    if income in range(0,45142):
        tax_prov = income * 0.0505
    elif income in range(45142,90287):
        tax_prov = 2280 + (income - 45141) * 0.0915  
    elif income in range(90287,150000):
        tax_prov = 6411 + (income - 90286) * 0.1116
    elif income in range(150000,220000):
        tax_prov = 13075 + (income - 149999) * 0.1216
    else:
        tax_prov = 21587 + (income - 219999) * 0.1316

    print("Your Ontario Income Tax is {:.2f}".format(tax_prov))

def main():
    income = int(input("Enter your Annual Income: "))

    federal_income_Tax(income)
    ontario_income_tax(income)

    #Sum total income tax

    total_tax = tax_fed + tax_prov
    print('Your Total Income tax is {:.2f}'.format(total_tax))

if __name__ == "__main__":
    main()