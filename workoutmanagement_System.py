from datetime import datetime

class Workout:
    def __init__(self, exercise_name, duration, calories):
        self.exercise_name = exercise_name
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.duration = duration
        self.calories = calories
    
    def __str__(self):
        return f"Exercise: {self.exercise_name}\nDate: {self.date}\nDuration: {self.duration} minutes\nCalories: {self.calories}"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []
        self.unsaved_workouts = []  #
        self._create_user_file()
    
    def _create_user_file(self):
        with open(f"{self.name}.txt", 'w') as file:
            file.write(f"Name: {self.name}\nAge: {self.age}\nWeight: {self.weight}\n\n")
    
    def add_workout(self, workout):
        self.unsaved_workouts.append(workout) 
        print("Workout added to memory. Use 'Save Workouts' option to save to file.")
    
    def save_workouts(self):
        if not self.unsaved_workouts:
            return "No unsaved workouts to save."
        
        for workout in self.unsaved_workouts:
            self.workouts.append(workout)
            self._save_workout(workout)
        
        count = len(self.unsaved_workouts)
        self.unsaved_workouts.clear()
        return f"{count} workout(s) saved successfully."
    
    def _save_workout(self, workout):
        with open(f"{self.name}.txt", 'a') as file:
            file.write(f"\n{str(workout)}\n{'-'*50}\n")
    
    def read_data(self):
        try:
            with open(f"{self.name}.txt", 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "User data not found."

def user_management_menu(users):
    while True:
        print("\n=== User Management ===")
        print("1. Create New User")
        print("2. Update User Info")
        print("3. View All Users")
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            weight = float(input("Enter weight (kg): "))
            users[name] = User(name, age, weight)
            print(f"User {name} created successfully!")
            
        elif choice == '2':
            name = input("Enter user name: ")
            if name in users:
                age = input("Enter new age (press Enter to skip): ")
                weight = input("Enter new weight (press Enter to skip): ")
                users[name].update_info(
                    age=int(age) if age else None,
                    weight=float(weight) if weight else None
                )
                print("User info updated successfully!")
            else:
                print("User not found!")
                
        elif choice == '3':
            if not users:
                print("No users exist.")
            else:
                print("\nExisting Users:")
                for name in users:
                    print(f"- {name}")
                    
        elif choice == '4':
            break
            
def workout_menu(users):
    if not users:
        print("No users exist. Please create a user first.")
        return
        
    print("\nSelect User:")
    for name in users:
        print(f"- {name}")
    
    name = input("Enter user name: ")
    if name not in users:
        print("User not found!")
        return
        
    user = users[name]
    
    while True:
        print(f"\n=== Workout Menu for {name} ===")
        print("1. Add New Workout")
        print("2. View Unsaved Workouts")
        print("3. Save Workouts to File")
        print("4. View All Workouts")
        print("5. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            exercise = input("Enter exercise name: ")
            duration = int(input("Enter duration (minutes): "))
            calories = int(input("Enter calories burned: "))
            workout = Workout(exercise, duration, calories)
            user.add_workout(workout)
            print(f"Workout added to memory. Total unsaved workouts: {len(user.unsaved_workouts)}")
            
        elif choice == '2':
            if not user.unsaved_workouts:
                print("No unsaved workouts.")
            else:
                print("\n=== Unsaved Workouts ===")
                for i, workout in enumerate(user.unsaved_workouts, 1):
                    print(f"\nWorkout #{i}")
                    print(workout)
                    print('-'*50)
                    
        elif choice == '3':
            result = user.save_workouts()
            print(result)
            
        elif choice == '4':
            print("\n=== All Workout Data ===")
            print(user.read_data())
            
        elif choice == '5':
            break

def main():
    users = {}
    
    while True:
        print("\n=== Workout Tracking System ===")
        print("1. User Management")
        print("2. Workout Management")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            user_management_menu(users)
        elif choice == '2':
            workout_menu(users)
        elif choice == '3':
            print("Thank you for using the Workout Tracking System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()