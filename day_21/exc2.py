class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []    # [{'amount': 1000, 'description': 'salary'}]
        self.expenses = []   # [{'amount': 500,  'description': 'rent'}]

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})
        print(f"Income added: {description} - ${amount}")

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})
        print(f"Expense added: {description} - ${amount}")

    def total_income(self):
        return sum(i['amount'] for i in self.incomes)

    def total_expense(self):
        return sum(e['amount'] for e in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"\n--- Account Info: {self.firstname} {self.lastname} ---")
        print("\nIncomes:")
        for i in self.incomes:
            print(f"  {i['description']}: ${i['amount']}")
        print("\nExpenses:")
        for e in self.expenses:
            print(f"  {e['description']}: ${e['amount']}")
        print(f"\nTotal Income:  ${self.total_income()}")
        print(f"Total Expense: ${self.total_expense()}")
        print(f"Balance:       ${self.account_balance()}")


# Testing
person = PersonAccount('Anar', 'Hasanov')

person.add_income(3000, 'Salary')
person.add_income(500,  'Freelance')
person.add_income(200,  'Investment')

person.add_expense(1200, 'Rent')
person.add_expense(300,  'Food')
person.add_expense(150,  'Transport')
person.add_expense(100,  'Utilities')

person.account_info()
