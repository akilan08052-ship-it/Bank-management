
import json

class Transaction:
    def __init__(self,title,amount,type,note):
        self.title=title
        self.amount=amount
        self.type=type
        self.note=note
    def display_info(self):
        return f"Transaction:\n Expense:{self.title}\n Amount:{self.amount}\n Type:{self.type}\n Note:{self.note}"
    

class Bank:
    def __init__(self):
        self.wallet=[] 
    
    def add_trancation(self,transaction):
        self.wallet.append(transaction)

    def delete_transaction(self,title):
        for trans in self.wallet:
            if trans.title==title:
                self.wallet.remove(trans)
                return f"{title} has been removed"
        return f"{title} not found "
    
    def display(self):
        if not self.add_trancation:
            return f"No Transaction id available in your wallet"
        
        return f"\n".join([transaction.display_info() for transaction in self.wallet])
    
    def search_wallet(self,query):
        found=[trans for trans  in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        
        if not found:
            return f"no Transactions"
        return f"\n".join([transaction.display_info() for transaction in found])
    def save_file(self,filename="wallet.json"):
        data=[{'title':transaction.title, 'amount':transaction.amount, 'type':transaction.type, 'note':transaction.note} for transaction in self.wallet]
        with open(filename,"w") as file:
            json.dump(data,file)
            
    
    def load_file(self,filename="wallet.json"):
        try:
            with open(filename,"r") as file:
                data= json.load(file)
                self.wallet= [Transaction(trans['title'], trans['amount'], trans['type'], trans['note']) for trans in data]
                
        except FileNotFoundError:
            print("WE don't have this file")

def main():
    wallet=Bank()

    while True:
        print("\n ======Personal BankSystem")
        print("1. Add a Transaction")
        print("2. Remove a Transaction")
        print("3 .Display all transation")
        print("4.Search a Transaction")
        print("5. Save a Transaction  to file")
        print("6.load a Transaction in file")
        print("7.exit")

        choice=input("Enter a Choice")

        if choice=="1":
            title=input("Enter the title")
            amount= float(input("Enter amount:"))
            type=input("Expense or Deposite:")
            note=input("Details")
            transaction=Transaction(title,amount,type,note)
            wallet.add_trancation(transaction)
            print(f"{title} added successfully")
        elif choice=="2":
            title=input("Enter a Title")
            print(wallet.delete_transaction(title))
            
        elif choice=="3":
            print(wallet.display())

        elif choice=="4":
            query=input("Enter a query")
            print(wallet.search_wallet(query))

        elif choice=="5":
            wallet.save_file()
            print("Sved as json")
        elif choice=="6":
            wallet.load_file()
            print("Load file")
        elif choice=="7":
            print("Ending the program")
            break
        else:
            print(" Invalid choice ,Reenter the choice")
if __name__== "__main__":
    main()

        
        