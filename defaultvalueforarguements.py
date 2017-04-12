def get_gender(sex='unknown'):
    if sex is 'M':
        sex="male"
    elif sex is 'F':
        sex="female"
    print(sex)

get_gender('M')
get_gender('F')
get_gender()


