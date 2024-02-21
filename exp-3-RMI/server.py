# server.py

import Pyro4

# Define a class whose methods will be remotely invocable
class MyObject(object):
    # def add(self, x, y):
    #     return x + y
    def __init__(self):
        self.Accounts = {'A':10000, 'B':10000, 'C':10000}
        self.IDs = {'A':'1', 'B':'2', 'C':'3'}
        self.ErrorCodes = {0:'ID not Found', 1:'Wrong Password', 2:'Invalid Transaction', 3:'Successful Transaction'}

    # Define the function to be called remotely
    def add(self, id, money):
        if id in self.IDs:
            self.Accounts[id] += money
            return (3, f'{id} has balance: {self.Accounts[id]}.')
        else:
            return (0, f'ID not Found for {id}')

    def remove(self, id, pwd, money):
        if id in self.IDs:
            if pwd == self.IDs[id]:
                if self.Accounts[id] >= money:
                    self.Accounts[id] -= money
                    return (3, f'{id} has balance: {self.Accounts[id]}.')
                else:
                    return (2, f'{id} has balance: {self.Accounts[id]}, which is less than {money}. Invalid Transaction.')
            else:
                return (1, f'Wrong Password for {id}')
        else:
            return (0, f'ID not Found for {id}')
    @Pyro4.expose
    def Transfer(self, source, pwd, destination, money):
        print(f'Trying transaction from {source} to {destination} of {money} Rupees.')
        
        if source == destination:
            return (2, 'Source cannot be same as destination. Invalid Transaction.')

        i, result1 = self.remove(source, pwd, money)
        
        if i < 3:
            return (i, result1)
        
        j, result2 = self.add(destination, money)

        if j < 3:
            result1 = self.add(source, money)
            return (j, result2, result1)
        
        if i == 3 and j == 3:
            return (3, 'Transaction successful', result1, result2)
        

# Create a Pyro4 Daemon
daemon = Pyro4.Daemon()

# Register the class with Pyro4
uri = daemon.register(MyObject)

print("Ready. Object uri =", uri)

# Start the Pyro4 server
daemon.requestLoop()