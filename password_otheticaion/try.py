def pass_autintication(username:  str): 
    ds= {'naxim': 12312, 'azim':23424}
    
    for  i in ds : 
        if ds.keys() == i : 
            print('username matched : ')
            print('enter your password : ')
            b= int(input('enter your password: '))
            for j in ds: 
                if ds.values() == j : 
                    print( 'log in complete : ')
                    print( 'account autinticated : ')
                else: 
                    print( 'wrong passcode : ')
                    print('try another  time  ')
            break 
        print('  wrong username try another time : ')
usr_name= str(input('enter your username : '))

pass_autintication(usr_name )
