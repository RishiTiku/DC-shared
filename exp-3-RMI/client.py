# client.py

import Pyro4

# Connect to the Pyro4 server
uri = input("Enter the server URI: (Starts with Pyro) \n")
remote_object = Pyro4.Proxy(uri)

# Call the remote method

source = input('Enter Source\n')
pwd = input(f'Enter Source Password for {source}\n')
dest = input('Enter Destination.\n')
money = float(input('Enter Money to be transferred.\n'))

result = remote_object.Transfer(source, pwd, dest, money)

print("Result:", result)