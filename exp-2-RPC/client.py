# client.py

import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote function
def Transfer(source, pwd, destination, money):
    print(f'Trying transaction from {source} to {destination} of {money} Rupees.')
    
    if source == destination:
        return (2, 'Source cannot be same as destination. Invalid Transaction.')


    i, result1 = proxy.remove(source, pwd, money)
    

    if i < 3:
        return (i, result1)
    
    j, result2 = proxy.add(destination, money)

    if j < 3:
        result1 = proxy.add(source, money)
        return (j, result2, result1)
    
    if i == 3 and j == 3:
        return (3, 'Transaction successful', result1, result2)

source = input('Enter Source')
pwd = input(f'Enter Source Password for {source}')
dest = input('Enter Destination.')
money = float(input('Enter Money to be transferred.'))

print("Result:", Transfer(source, pwd, dest, money))