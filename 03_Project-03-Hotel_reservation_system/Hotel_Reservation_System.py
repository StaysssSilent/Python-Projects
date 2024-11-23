# Hotel reservation system 

from datetime import datetime
import random 

Hotel_Name = "MAHARAJA HOTEL"
Hotel_location = "Western Express Highway in Borivali East area of 'MUMBAI'"

class CustomerDetails:
    def __init__(self, name, contact_no, email_id, payment_type):
        self.name = name
        self.contact_no = contact_no
        self.email_id = email_id
        self.payment_type = payment_type

        print(f"Customer Name : {self.name}, Mobile No. : {self.contact_no}, Email-ID : {self.email_id}, Payment Method : {self.payment_type}")

# Customer Name input validation
CustomerName = ""
while not CustomerName.replace(" ", "").isalpha():  # Check if name contains only alphabets and spaces
    CustomerName = input("Enter your name here: ")
    if not CustomerName.replace(" ", "").isalpha():
        print("Please enter a valid name with alphabets only.")

# Mobile number input validation
MobileNo = ""
while not MobileNo.isdigit() or len(MobileNo) != 10:  # Ensure it has only digits and exactly 10 characters
    MobileNo = input("Enter your contact number (+91): ")
    if not MobileNo.isdigit() or len(MobileNo) != 10:
        print("Please enter a valid 10-digit mobile number.")

# Email validation (simple check)
Email = input("Enter your e-mail address : ")

# Payment Type validation
PaymentType = ""
validPayment_Types = ["UPI", "Bank Transfer", "Credit Card", "AmazonPay"]
while PaymentType not in validPayment_Types:
    PaymentType = input("Enter how will you proceed your payment (UPI, Bank Transfer, Credit Card, AmazonPay): ")
    if PaymentType not in validPayment_Types:
        print("Please enter a valid payment type.")

print()
print(f"Welcome to {Hotel_Name}")
print()


# Room Charges
print("Please read the room charges below carefully before check-in")
print()
label_width = 15
RoomPrices = {
    "Preferences- AC & Non-Smoking" : {"Single" : "Rs 4,000/-night", "Double" : "Rs 7,000/-night", "Suite" : " Rs 10,000/-night"},
    "Preferences- AC & Smoking" : {"Single" : "Rs 4,500/-night", "Double" : "Rs 6,000/-night", "Suite" : " Rs 8,500/-night"},
    "Preferences- Non-AC & Non-Smoking" : {"Single" : "Rs 2,500/-night", "Double" : "Rs 3,900/-night", "Suite" : " Rs 6,500/-night"},
    "Preferences- Non-AC & Smoking" : {"Single" : "Rs 2,000/-night", "Double" : "Rs 4,500/-night", "Suite" : " Rs 7,000/-night"}
}
for room_preferences, room_type in RoomPrices.items():
    print(f"{room_preferences}:")
    for option, price in room_type.items():
        print(f"  {option:<{label_width}}: {price}")
print()
print()

# User input for the number of days
def get_days():
    # Prompt the user for the number of days needed for the room.
    while True:
        try:
            days = int(input("Enter the number of days you will need the room: "))
            if days <= 0:
                print("Please enter a positive number for the days.")
                continue
            return days
        except ValueError:
            print("Please enter a valid number for the days.")

# Helper function to validate and parse dates
def get_date_input(prompt):
    # Prompt the user for a date and validate it.
    while True:
        date_str = input(prompt)
        try:
            # Parse the date in DD/MM/YYYY format
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("Please enter a valid date in DD/MM/YYYY format.")

# Get the number of days from the user
days = get_days()

# Get check-in and check-out dates from the user
while True:
    check_in_date = get_date_input("Enter your check-in date (DD/MM/YYYY) : ")
    check_out_date = get_date_input("Enter your check-out date (DD/MM/YYYY): ")

    # Calculate the duration of the stay
    duration = (check_out_date - check_in_date).days

    # Check if dates are valid and match the number of days
    if check_out_date <= check_in_date:
        print("Check-out date must be after the check-in date. Please re-enter the dates.")
    elif duration != days:
        print(f"The dates entered do not match your stay duration of {days} days. Please re-enter the dates.")
    else:
        print(f"The duration of your stay is {duration} days.")
        break


# RoomChoice logic
class RoomChoice:
    # Room prices dictionary
    RoomPrices = {
        "AC & Non-Smoking": {"Single": 4000, "Double": 7000, "Suite": 10000},
        "AC & Smoking": {"Single": 4500, "Double": 6000, "Suite": 8500},
        "Non-AC & Non-Smoking": {"Single": 2500, "Double": 3900, "Suite": 6500},
        "Non-AC & Smoking": {"Single": 2000, "Double": 4500, "Suite": 7000},
    }

    def __init__(self, room_type, has_ac, is_non_smoking, days):
        self.room_type = room_type
        self.has_ac = has_ac
        self.is_non_smoking = is_non_smoking
        self.days = days  # Number of days room is required

    def get_price_category(self):
        # Determine the price category based on AC and smoking preference
        ac_status = "AC" if self.has_ac == 1 else "Non-AC"
        smoking_status = "Non-Smoking" if self.is_non_smoking == 1 else "Smoking"
        return f"{ac_status} & {smoking_status}"

    def calculate_total_cost(self):
        # Calculate total cost based on room type, preferences, and days.
        price_category = self.get_price_category()
        daily_rate = self.RoomPrices[price_category][self.room_type]
        return daily_rate * self.days

    def display_choice(self):
        #Display selected room details and calculate total price.
        ac_status = "AC" if self.has_ac == 1 else "Non-AC"
        smoking_status = "Non-Smoking" if self.is_non_smoking == 1 else "Smoking"
        
        print(f"Room choice: {self.room_type} room, {ac_status}, {smoking_status}")
        
        # Calculate and display total cost
        total_room_cost = self.calculate_total_cost()
        print(f"Total cost of room for {self.days} days: {total_room_cost} Rupees")

# User input for room type with validation
def get_room_type():
    RoomType = ""
    valid_room_types = ["Single", "Double", "Suite"]
    while RoomType not in valid_room_types:
        RoomType = input("Please enter which room you would like to prefer (Single/Double/Suite): ")
        if RoomType not in valid_room_types:
            print("Please enter a valid room type (Single, Double, Suite).")
    return RoomType

# User input for AC and smoking preferences with validation
def get_preference(prompt, valid_options):
    while True:
        try:
            choice = int(input(prompt))
            if choice not in valid_options:
                raise ValueError("Invalid input.")
            return choice
        except ValueError:
            print(f"Please enter a valid option: {valid_options}")


# Collecting user inputs
RoomType = get_room_type()
AC = get_preference("Do you prefer A.C. (1 for yes & 0 for no): ", [0, 1])
Smoking = get_preference("Do you prefer a non-smoking room (1 for yes & 0 for no): ", [0, 1])
print()

# Room data organized in a dictionary
label_width = 20
rooms_data = {
    ("Single", 1, 1): {
        "Room 1": "Single AC Non-Smoking - Available",
        "Room 2": "Single AC Non-Smoking - Available",
        "Room 6": "Single AC Non-Smoking - Available",
        "Room 9": "Single AC Non-Smoking - Available",
    },
    ("Single", 0, 1): {
        "Room 5": "Single Non-AC Non-Smoking - Available",
        "Room 8": "Single Non-AC Non-Smoking - Available",
        "Room 7": "Single Non-AC Non-Smoking - Available",
    },
    ("Double", 1, 1): {
        "Room 101": "Double AC Non-Smoking - Available",
        "Room 113": "Double AC Non-Smoking - Available",
        "Room 105": "Double AC Non-Smoking - Available",
    },
    ("Double", 1, 0): {
        "Room 106": "Double AC Smoking - Available",
        "Room 120": "Double AC Smoking - Available",
        "Room 107": "Double AC Smoking - Available",
        "Room 114": "Double AC Smoking - Available",
    },
    ("Double", 0, 1): {
        "Room 109": "Double Non-AC Non-Smoking - Available",
        "Room 102": "Double Non-AC Non-Smoking - Available",
    },
    ("Double", 0, 0): {
        "Room 111": "Double Non-AC Smoking - Available",
        "Room 115": "Double Non-AC Smoking - Available",
    },
    ("Suite", 1, 1): {
        "Room 201": "Suite AC Non-Smoking - Available",
        "Room 210": "Suite AC Non-Smoking - Available",
        "Room 219": "Suite AC Non-Smoking - Available",
    },
    ("Suite", 1, 0): {
        "Room 202": "Suite AC Smoking - Available",
        "Room 203": "Suite AC Smoking - Available",
    },
    ("Suite", 0, 1): {
        "Room 204": "Suite Non-AC Non-Smoking - Available",
        "Room 205": "Suite Non-AC Non-Smoking - Available",
        "Room 207": "Suite Non-AC Non-Smoking - Available",
        "Room 208": "Suite Non-AC Non-Smoking - Available",
    },
    ("Suite", 0, 0): {
        "Room 206": "Suite Non-AC Smoking - Available",
        "Room 209": "Suite Non-AC Smoking - Available",
        "Room 211": "Suite Non-AC Smoking - Available",
        "Room 212": "Suite Non-AC Smoking - Available",
    },
}

# Fix the show_available_rooms logic
def show_available_rooms(preferred_type, has_ac, is_non_smoking):
    # Search for rooms matching preferences
    key = (preferred_type, has_ac, is_non_smoking)
    available_rooms = rooms_data.get(key, {})
    
    if available_rooms:
        print("Available rooms matching your preferences:")
        for room_number, description in available_rooms.items():
            print(f"  {room_number:<{label_width}}: {description}")
        return available_rooms
    else:
        print("Sorry, no rooms match your preferences.")
        return None

# Display available rooms or offer alternatives
available_rooms = show_available_rooms(RoomType, AC, Smoking)

while not available_rooms:
    print("\nNo rooms available with your current preferences.")
    print("You can adjust your preferences and try again.")
    
    # Allow user to change their preferences
    RoomType = get_room_type()
    AC = get_preference("Do you prefer A.C. (1 for yes & 0 for no): ", [0, 1])
    Smoking = get_preference("Do you prefer a non-smoking room (1 for yes & 0 for no): ", [0, 1])
    
    # Recheck available rooms
    available_rooms = show_available_rooms(RoomType, AC, Smoking)

# Validate room choice
while True:
    CustomerRoomChoice = input("Enter the room number you would like to prefer: ")
    if CustomerRoomChoice in available_rooms:
        print(f"You have selected {CustomerRoomChoice}: {available_rooms[CustomerRoomChoice]}")
        break
    else:
        print("Please enter a valid room number from the available rooms.")


print()
print(f"You have selected {CustomerRoomChoice}: {available_rooms[CustomerRoomChoice]}")
print()

# Meal Prices 
print("See the meal charges before selecting your meals -")
print()
label_width = 15 
MealsPrices = {
    "Breakfast Prices": {"Veg": "Rs. 50/-day", "Non-Veg": "Rs. 150/-day"},
    "Lunch Prices": {"Veg": "Rs. 150/-day", "Non-Veg": "Rs. 300/-day"},
    "Dinner Prices": {"Veg": "Rs. 250/-day", "Non-Veg": "Rs. 480/-day"}
}
for meal_type, options in MealsPrices.items():
    print(f"{meal_type}:")
    for option, price in options.items():
        print(f"  {option:<{label_width - 2}}: {price}")


class Meals:
    # Prices for meals (in whatever currency you prefer)
    MEAL_PRICES = {
        "Veg": {"breakfast": 50, "lunch": 150, "dinner": 250},
        "Non-veg": {"breakfast": 100, "lunch": 300, "dinner": 480},
        "None": 0
    }

    def __init__(self, breakfast, lunch, dinner, days):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.days = days  # Number of days meals are required

    def get_meal_status(self, meal_choice):
        #Helper function to return meal type based on user choice.
        return "Veg" if meal_choice == 1 else "Non-veg" if meal_choice == 2 else "None"

    def calculate_total_cost(self):
        #Calculate the total cost based on selected meal choices and days.
        total_meal_cost = 0
        meal_types = {
            "breakfast": self.get_meal_status(self.breakfast),
            "lunch": self.get_meal_status(self.lunch),
            "dinner": self.get_meal_status(self.dinner)
        }

        for meal, meal_type in meal_types.items():
            if meal_type != "None":
                total_meal_cost += self.MEAL_PRICES[meal_type][meal] * self.days
        
        return total_meal_cost

    def display_choice(self):
        #Display selected meal types and calculate total price.
        breakfast_status = self.get_meal_status(self.breakfast)
        lunch_status = self.get_meal_status(self.lunch)
        dinner_status = self.get_meal_status(self.dinner)
        
        print(f"Your meals : Breakfast: {breakfast_status}, Lunch: {lunch_status}, Dinner: {dinner_status}")
        
        # Calculate and display total cost
        total_meal_cost = self.calculate_total_cost()
        print(f"Total cost of selected meals for {self.days} days: {total_meal_cost} Rupees")

# User input for meal choices with validation
def get_meal_choice(meal_name):
    while True:
        try:
            choice = int(input(f"Do you prefer {meal_name} (1 for veg, 2 for non-veg & 0 for no): "))
            if choice not in [0, 1, 2]:
                raise ValueError(f"Invalid input for {meal_name} preference.")
            return choice
        except ValueError:
            print(f"Please enter a valid option for {meal_name} meal (1 for veg, 2 for non-veg & 0 for no).")

print()

# User input for the number of days for meals
while True:
    try:
        meal_days = int(input("Enter the number of days you will need the meals: "))
        if meal_days <= 0:
            print("Please enter a positive number for the days.")
            continue
        if meal_days > days:  # Compare with the stay duration
            print(f"Meal days cannot exceed the duration of stay ({days} days).")
            continue
        break
    except ValueError:
        print("Please enter a valid number for the days.")


Breakfast = get_meal_choice("Breakfast")
Lunch = get_meal_choice("Lunch")
Dinner = get_meal_choice("Dinner")


print()
print()
print("Your reservation is successfull")
print()

RegisID = random.randint(1, 5000)
print("Registration ID : ", RegisID)
# Create the CustomerDetails object after all inputs
customer = CustomerDetails(CustomerName, MobileNo, Email, PaymentType)

# Create RoomChoice object and display choices with total price
room_choice = RoomChoice(RoomType, AC, Smoking, days)
room_choice.display_choice()

# Create Meals object and display choices with total price
CustomerMeals = Meals(Breakfast, Lunch, Dinner, days)
CustomerMeals.display_choice()

print()
print()
print()

def generate_bill(customer, room_choice, CustomerRoomChoice, CustomerMeals, RegisID, check_in_date, check_out_date, duration):
    # Generate and display the final bill.

    # Greeting based on time of day
    current_time = datetime.now()
    if current_time.hour < 12:
        time_of_day = "morning"
    elif 12 <= current_time.hour < 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    # Calculate costs
    room_cost = room_choice.calculate_total_cost()
    meal_cost = CustomerMeals.calculate_total_cost()
    total_cost = room_cost + meal_cost

    # Define label width
    label_width = 40

    # Display the bill
    print("\n************ Final Bill ************")
    print(f"{'Hotel Name':<{label_width}}: {Hotel_Name}")
    print(f"{'Hotel Location':<{label_width}}: {Hotel_location}")
    print("-" * 60)
    print(f"{'Customer Name':<{label_width}}: {customer.name}")
    print(f"{'Contact No':<{label_width}}: {customer.contact_no}")
    print(f"{'Email':<{label_width}}: {customer.email_id}")
    print(f"{'Payment Method':<{label_width}}: {customer.payment_type}")
    print(f"{'Registration ID':<{label_width}}: {RegisID}")
    print(f"{'Check-in Date':<{label_width}}: {check_in_date.strftime('%d/%m/%Y')}")
    print(f"{'Check-out Date':<{label_width}}: {check_out_date.strftime('%d/%m/%Y')}")
    print(f"{'Duration of stay':<{label_width}}: {duration} days")
    print("-" * 60)
    print(f"{'Room Details':<{label_width}}: {room_choice.room_type} room, {room_choice.get_price_category()}")
    print(f"{'Room Number':<{label_width}}: {CustomerRoomChoice}")
    print(f"{'Room Cost':<{label_width}}: {room_cost} Rupees")
    print("-" * 60)
    print("Meal Preferences:")
    print(f"{'  Breakfast':<{label_width}}: {CustomerMeals.get_meal_status(CustomerMeals.breakfast)}")
    print(f"{'  Lunch':<{label_width}}: {CustomerMeals.get_meal_status(CustomerMeals.lunch)}")
    print(f"{'  Dinner':<{label_width}}: {CustomerMeals.get_meal_status(CustomerMeals.dinner)}")
    print(f"{'Meal Cost':<{label_width}}: {meal_cost} Rupees")
    print("-" * 60)
    print(f"{'Total Amount Payable':<{label_width}}: {total_cost} Rupees")
    print("************************************")
    print(f"Good {time_of_day}, {customer.name}!")
    print("Thank you for staying with us! We hope you had a pleasant experience.")
    print("Safe travels and we look forward to welcoming you back soon!")
    print("Good Bye!")



Bill = generate_bill(customer, room_choice, CustomerRoomChoice, CustomerMeals, RegisID, check_in_date, check_out_date, duration)
