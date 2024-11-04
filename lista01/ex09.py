# gender = character(input())
# age = int(input())
# t_contribution = int(input())

gender = 'M'.upper()
age = 65
t_contribution = 10

if (gender == 'M' and ((age >= 65 and t_contribution >= 10) or (age >= 63 and t_contribution >= 15))) or \
   (gender == 'F' and ((age >= 63 and t_contribution >= 10) or (age >= 61 and t_contribution >= 15))):
    print("Aposentável!")
else:
    print("Não Aposentável!")
