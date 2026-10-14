total=float(input ("enter total purchase amount:"))
if total >=1000:
    discount = total*0.10
    final_amount = total-discount
    print("Discount applied =",discount)
    print("final amount to pay:",final_amount)
else:
    print("no discount applied")
    print("total amount:",total)