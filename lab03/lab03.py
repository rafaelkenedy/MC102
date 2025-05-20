fridge_type = "SIMPLES"
residents = 3
motor_power = 200

if fridge_type == "SIMPLES":
    if residents <= 2:
        if motor_power <= 70:
            print("Gel-S")
        elif motor_power <= 130:
            print("Gel-SPlus")
        else:
            print("Frost++")
    elif residents == 3:
        if motor_power <= 100:
            print("DeluxFF")
        else:
            print("Frost++")
    elif residents >= 4:
        if motor_power <= 100:
            print("IceCold")
        elif motor_power <= 130:
            print("DeluxFF")
        else:
            print("Frost++")

else: #DUPLEX
    if residents == 1:
        print("Gel-D")
    elif residents == 2 and motor_power <= 150:
        print("Gel-DPlus")
    elif residents == 2 and motor_power > 150:
        print("DupCold")
    elif residents <= 3 and motor_power <= 100:
        print("Gel-DPlus")
    elif residents <=3 and motor_power > 100:
        print("DupCold")
    elif residents >= 4 and motor_power <= 100:
        print("IceCold")
    else:
        print("Frost++")



