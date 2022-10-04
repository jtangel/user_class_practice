class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")

    def enroll(self):
        self.gold_card_points = 200
        if self.is_rewards_member == True:
            print('User is already member')
        else: self.is_rewards_member = True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('Not enough points for this purchase')
        else: self.gold_card_points -= amount



Jack = User('Jack', 'Tangel', 'jackmtangel@gmail.com', 24)
Jack.spend_points(50)
Jack.display_info()

Bernie = User('Bernie', 'Sanders', 'bernieShouldBePres@bernie.com', 78)
Bernie.enroll()
Bernie.spend_points(80)
Bernie.display_info()


Ben = User('Ben', 'Brown', 'iWishYouWereHere@ripBen.com', 25)
Ben.display_info()