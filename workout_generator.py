import random

# Define exercise categories with sets, reps, and rest times
exercises = {
    'push': [
        {'name': 'Push-ups', 'sets': 3, 'reps': 12, 'rest': 60},
        {'name': 'Chest Press', 'sets': 4, 'reps': 10, 'rest': 90},
        {'name': 'Overhead Press', 'sets': 4, 'reps': 8, 'rest': 90},
        {'name': 'Triceps Dips', 'sets': 3, 'reps': 12, 'rest': 60}
    ],
    'pull': [
        {'name': 'Pull-ups', 'sets': 3, 'reps': 6, 'rest': 90},
        {'name': 'Rows', 'sets': 4, 'reps': 10, 'rest': 90},
        {'name': 'Deadlifts', 'sets': 4, 'reps': 8, 'rest': 120},
        {'name': 'Lat Pulldown', 'sets': 4, 'reps': 10, 'rest': 90}
    ],
    'legs': [
        {'name': 'Squats', 'sets': 4, 'reps': 12, 'rest': 90},
        {'name': 'Lunges', 'sets': 3, 'reps': 12, 'rest': 60},
        {'name': 'Leg Press', 'sets': 4, 'reps': 10, 'rest': 90},
        {'name': 'Glute Bridges', 'sets': 3, 'reps': 12, 'rest': 60}
    ],
    'core': [
        {'name': 'Planks', 'sets': 3, 'reps': '30s', 'rest': 60},
        {'name': 'Russian Twists', 'sets': 3, 'reps': 20, 'rest': 60},
        {'name': 'Leg Raises', 'sets': 3, 'reps': 12, 'rest': 60},
        {'name': 'Bicycle Crunches', 'sets': 3, 'reps': 20, 'rest': 60}
    ],
    'cardio': [
        {'name': 'Jump Rope', 'sets': 5, 'reps': '30s', 'rest': 60},
        {'name': 'Running', 'sets': 5, 'reps': '5 mins', 'rest': 90},
        {'name': 'Cycling', 'sets': 5, 'reps': '5 mins', 'rest': 90},
        {'name': 'Burpees', 'sets': 4, 'reps': 20, 'rest': 60}
    ],
    'full_body': [
        {'name': 'Burpees', 'sets': 3, 'reps': 15, 'rest': 60},
        {'name': 'Kettlebell Swings', 'sets': 4, 'reps': 15, 'rest': 90},
        {'name': 'Thrusters', 'sets': 4, 'reps': 12, 'rest': 90},
        {'name': 'Push-ups', 'sets': 3, 'reps': 12, 'rest': 60}
    ]
}

# Meal plans based on fitness goal
meal_plans = {
    'muscle_gain': ['Protein Pancakes', 'Chicken & Quinoa Bowl', 'Steak & Sweet Potatoes'],
    'fat_loss': ['Salmon Salad', 'Veggie Stir Fry', 'Chicken & Broccoli'],
    'endurance': ['Pasta & Chicken', 'Oatmeal & Berries', 'Smoothie with Protein'],
    'strength': ['Protein Pancakes', 'Chicken & Quinoa Bowl', 'Steak & Sweet Potatoes']
}

# Functions for specific goal-based workout routines
def strength_workout(level):
    if level == 'beginner':
        return exercises['push'][:2] + exercises['pull'][:2] + exercises['legs'][:2]
    elif level == 'intermediate':
        return exercises['push'][:3] + exercises['pull'][:3] + exercises['legs'][:3]
    elif level == 'advanced':
        return exercises['push'][:4] + exercises['pull'][:4] + exercises['legs'][:4]

def endurance_workout(level):
    if level == 'beginner':
        return exercises['cardio'][:2] + exercises['core'][:2]
    elif level == 'intermediate':
        return exercises['cardio'][:3] + exercises['core'][:3]
    elif level == 'advanced':
        return exercises['cardio'][:4] + exercises['core'][:4]

def weight_loss_workout(level):
    if level == 'beginner':
        return exercises['cardio'][:2] + exercises['legs'][:2]
    elif level == 'intermediate':
        return exercises['cardio'][:3] + exercises['legs'][:3]
    elif level == 'advanced':
        return exercises['cardio'][:4] + exercises['legs'][:4]

def general_fitness_workout(level):
    if level == 'beginner':
        return exercises['push'][:2] + exercises['pull'][:2] + exercises['core'][:2]
    elif level == 'intermediate':
        return exercises['push'][:3] + exercises['pull'][:3] + exercises['core'][:3]
    elif level == 'advanced':
        return exercises['push'][:4] + exercises['pull'][:4] + exercises['core'][:4]

# Function to generate workout based on goal and level
def generate_workout(goal, level, days_per_week):
    workout_plan = []
    
    if goal == 'strength':
        workout_plan = strength_workout(level)
    elif goal == 'endurance':
        workout_plan = endurance_workout(level)
    elif goal == 'weight_loss':
        workout_plan = weight_loss_workout(level)
    elif goal == 'general_fitness':
        workout_plan = general_fitness_workout(level)
    
    final_plan = []
    for i in range(days_per_week):
        daily_workout = random.sample(workout_plan, k=3)  # Select 3 exercises for the day
        final_plan.append(daily_workout)
    
    return final_plan

# Function to format and display workout
def display_workout(workout_plan):
    workout_text = ""
    for day, exercises in enumerate(workout_plan, start=1):
        workout_text += f"Day {day}: "
        for exercise in exercises:
            workout_text += f"{exercise['name']} (Sets: {exercise['sets']}, Reps: {exercise['reps']}, Rest: {exercise['rest']}s) | "
        workout_text = workout_text.rstrip(" | ")  # Remove trailing separator
        workout_text += "\n"
    return workout_text

# Function to format and display meal plan
def display_meal_plan(goal):
    # Make sure goal is valid
    if goal not in meal_plans:
        return "No meal plan available for this goal."

    meal_text = f"Suggested meal plan for {goal}:\n"
    for meal in meal_plans.get(goal, []):
        meal_text += f"  - {meal}\n"
    return meal_text

# Function to allow user input for goal, level, and days per week
def get_user_input():
    print("Please enter your fitness goal (muscle_gain, fat_loss, endurance, strength):")
    goal = input().strip().lower()

    print("Please enter your fitness level (beginner, intermediate, advanced):")
    level = input().strip().lower()

    print("Please enter the number of days per week you want to workout (1-7):")
    days_per_week = int(input().strip())

    return goal, level, days_per_week

# Main function to get user input and generate workout and meal plans
def main():
    goal, level, days_per_week = get_user_input()

    # Generate workout plan
    workout_plan = generate_workout(goal, level, days_per_week)
    workout_output = display_workout(workout_plan)
    
    # Generate meal plan
    meal_output = display_meal_plan(goal)
    
    # Display the results
    print("\nWorkout Plan:\n")
    print(workout_output)
    print("\nMeal Plan:\n")
    print(meal_output)

# Run the program
if __name__ == "__main__":
    main()
