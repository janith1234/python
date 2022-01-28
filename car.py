class Car (object):
    def __init__(self,model,company,speedlimit):
        self.company=company
        self.model=model
        self.speedlimit=speedlimit
        
    def start (self):
     print("started")

jon= Car ("sxo","hundai",240)      
print(jon.company)