# server.py

from xmlrpc.server import SimpleXMLRPCServer

Accounts = {'A':10000, 'B':10000, 'C':10000}
IDs = {'A':'1', 'B':'2', 'C':'3'}
ErrorCodes = {0:'ID not Found', 1:'Wrong Password', 2:'Invalid Transaction', 3:'Successful Transaction'}

# Define the function to be called remotely
def add(id, money):
    if id in IDs:
        Accounts[id] += money
        return (3, f'{id} has balance: {Accounts[id]}.')
    else:
        return (0, f'ID not Found for {id}')

def remove(id, pwd, money):
    if id in IDs:
        if pwd == IDs[id]:
            if Accounts[id] >= money:
                Accounts[id] -= money
                return (3, f'{id} has balance: {Accounts[id]}.')
            else:
                return (2, f'{id} has balance: {Accounts[id]}, which is less than {money}. Invalid Transaction.')
        else:
            return (1, f'Wrong Password for {id}')
    else:
        return (0, f'ID not Found for {id}')

# Create a SimpleXMLRPCServer
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Register the function so it can be called remotely
server.register_function(add, "add")
server.register_function(remove, "remove")

# Run the server
server.serve_forever()