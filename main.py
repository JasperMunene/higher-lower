# IMPORT NECESSARY PACKAGES
import art
from game_data import data
import random

POINTS = 0
# Function to select a random person and return their values
def select_person():
    person = random.choice(data)
    name = person['name']
    follower_count = person['follower_count']
    description = person['description']
    country = person['country']
    return name, follower_count, description, country


# Function to check which person has more followers
def check_highest(first_person, second_person):
    return first_person > second_person


# Function to check if the user's choice is correct
def check_answer(choice, person1, person2):
    highest = check_highest(person1[1], person2[1])
    if highest and choice == "A":
        return True
    elif not highest and choice == "B":
        return True
    return False


print(art.logo)

# Initial comparison
person1 = select_person()
person2 = select_person()

# Ensure person2 is different from person1
while person1 == person2:
    person2 = select_person()

# Display the comparison
print(f"Compare A: {person1[0]}, {person1[2]}, from {person1[3]}")
print(art.vs)
print(f"Compare B: {person2[0]}, {person2[2]}, from {person2[3]}")

# Show follower counts (for debugging purposes)
print(person1[1], person2[1])

# Take the user's choice
choice = input("Who has more followers? 'A' or 'B': ").upper()

# Check if the user's answer is correct
is_correct = check_answer(choice, person1, person2)
if is_correct:
    POINTS += 1
    print(f"Points: {POINTS}")

# Continue the game if the answer is correct
while is_correct:
    # Determine which person has more followers
    if check_highest(person1[1], person2[1]):
        person1 = person1  # person1 already has the higher count
    else:
        person1 = person2  # person2 becomes person1 because they have the higher count

    # Select a new person for person2
    person2 = select_person()

    # Ensure person2 is different from person1
    while person1 == person2:
        person2 = select_person()

    # Display the next comparison
    print(f"Compare A: {person1[0]}, {person1[2]}, from {person1[3]}")
    print(art.vs)
    print(f"Compare B: {person2[0]}, {person2[2]}, from {person2[3]}")


    # Take the next choice
    choice = input("Who has more followers? 'A' or 'B': ").upper()

    # Check if the answer is correct
    is_correct = check_answer(choice, person1, person2)
    POINTS += 1
    print(f"Points: {POINTS}")

print("Game Over!")
print(f"Final Points: {POINTS}")

