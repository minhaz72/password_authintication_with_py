import getpass 
ds={'naxim ': '12312312', 'azim': '253453'}
username= str(input(' enter your username : '))
password=getpass.getpass('enter your password : ')
for i in ds.keys(): 
    if username== i : 
        while password !=   ds.get(i)  :
            password=  getpass.getpass('enter your password againe : ')
        break 
print('varifiyed : ')

