

def MBI():
    weight = int(input('Please Enter Your Weight : '))
    height = float(input('Please Enter Your Height(In Meter) : ' ))


    bmi = weight / (height * height)
    print('Your BMI is ' ,round (bmi, 2))
    if bmi <= 18.5:
        print (' You are UNDERWEIGHT...')

    elif bmi > 18.5 and bmi <=24.9:
        print('You are Normal Weight ...')
    elif bmi > 24.9 and bmi <=29.9:
        print('You are Over Weight ...')
    else :
        print('You Are Obesity')
    


MBI()

    

