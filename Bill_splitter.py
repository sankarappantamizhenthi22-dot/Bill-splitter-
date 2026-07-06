total_bill = float(input("enter the total bill:"))
number_of_ppl = int(input("how many ppl?:"))

tip = total_bill * 0.10
final_bill = total_bill + tip
amount_per_person = final_bill / number_of_ppl

print("each person owes: " + str(amount_per_person))
