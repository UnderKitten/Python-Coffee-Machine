cost_espr = [250, 0, 16, 1, -4]
cost_latt = [350, 75, 20, 1, -7]
cost_capp = [200, 100, 12, 1, -6]
materials = ["water", "milk", "coffee beans", "disposable cups", "money"]

class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.cups = cups
        self.beans = beans
        self.money = money
        self.machine_content = [water, milk, beans, cups, money]

    def product_status(self):
        print(f'\nThe coffee machine has:\n{self.machine_content[0]} of water\n{self.machine_content[1]} of milk\n{self.machine_content[2]} of coffee beans\n{self.machine_content[3]} of disposable cups\n${self.machine_content[4]} of money\n')
        self.menu()

    def menu(self):
        action = input('Write action (buy, fill, take , remaining, exit) \n')
        if action == 'fill':
            return self.fill()
        elif action == 'buy':
            return self.buy()
        elif action == 'take':
            return self.take()
        elif action == 'remaining':
            return self.product_status()
        elif action == 'exit':
            exit()

    def buy(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n')
        if choice == '1':
            self.enough_for_coffee(cost_espr)
        elif choice == '2':
            self.enough_for_coffee(cost_latt)
        elif choice == '3':
            self.enough_for_coffee(cost_capp)
        elif choice == 'back':
            return self.menu()
        return self.menu()

    def fill(self):
        add_water = int(input('Write how many ml of water do you want to add: \n'))
        add_milk = int(input('Write how many ml of milk do you want to add: \n'))
        add_beans = int(input('Write how many grams of coffee beans do you want to add: \n'))
        add_cups = int(input('Write how many disposable cups of coffee do you want to add: \n'))
        add_items = [add_water, add_milk, add_beans, add_cups, 0]
        for item in range(len(self.machine_content)):
            self.machine_content[item] += add_items[item]
        return self.menu()

    def enough_for_coffee(self, drink):
        current = self.machine_content
        for i in range(len(current)):
            if current[i] < drink[i]:
                return print('Sorry, not enough {materials[i]}\n')
            current[i] -= drink[i]
        self.machine_content = current
        print('I have enough resources, making you a coffee!\n')

    def take(self):
        print(f'I gave you ${self.machine_content[-1]}')
        self.machine_content[-1] = 0
        return self.menu()

cust = CoffeeMachine(400, 540, 120, 9, 550)
cust.menu()