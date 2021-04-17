# steps
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
#  These objects should allow for:
#  1.Depositing funds to each of the categories
#  2.Withdrawing funds from each category
#  3.Computing category balances
#  4.Transferring balance amounts between categories
class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount

        return f"your new balance is ₤{self.balance} in {self.name} budget"

    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance = self.balance - amount

            feedback = "==========================\n"
            feedback += "Transaction was successful\n"
            feedback += f"Your new balance is ₤{self.balance} in {self.name} budget "

            return feedback

    def get_balance(self):
        feedback = f"Your balance for {self.name} is ₤{self.balance}"

        return feedback

    def transfer(self, amount, category):
        if self.name == category.name:
            feedback = "Error\n"
            feedback += "You can't transfer within this same category"
            feedback += " You can only deposit within a category and transfer within different categories"

            return feedback

        if self.balance < amount:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            category.balance += amount

            feedback = "=======================\n"
            feedback += "Transfer was successful \n"
            feedback += f"The balance for {self.name} is ₤{self.balance}\n"
            feedback += f"The balance for {category.name} is ₤{category.balance}"

            return feedback


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")
print(food.deposit(2000))
print("=======================")
print(clothing.deposit(5000))
print("=======================")
print(entertainment.deposit(7000))

print("=======================")

print(food.withdraw(3000))
print(clothing.withdraw(2000))
print(entertainment.withdraw(2500))

print("=======================")

print(food.get_balance())
print("=======================")
print(clothing.get_balance())
print("=======================")
print(entertainment.get_balance())

print(clothing.transfer(1500, food))
print("=======================")
print(entertainment.transfer(1500, clothing))
print("=======================")
print(food.transfer(1500, food))