import os

def list_directory_path(path):
    for root, subdirs, files in os.walk(path):
        for name in files:
             with open('workout.txt', 'w') as file_object:
                contents = file_object.write("Bench: 12 reps and 3 sets\nSquat: 6 reps and 6 sets\nBent over rows: 12 reps and 3 sets\nCurls: 12 reps and 4 sets")
             with open('contacts.txt') as file_object:
                contents = file_object.read()
                print(contents.strip())
                print("\nThe path of the file is:")
                print(os.path.join(path, name))

def report_file_sizes(directory):
    for root, subdirs, files in os.walk(directory):
        for name in files:
            print(f"\nThe file {root} holds {name} which is: " + str(os.path.getsize(name)) +" bytes\n")
            
        
            

os.makedirs('my_workout_files', exist_ok=True)
print("Welcome! Please provide which directory you would like to choose!")

while True:
    user_input = input("Option includes: my_workout_files (type my_workout_files) ").lower()
    print("\nFile contents include:")
    try:
        if user_input == "my_workout_files":
            list_directory_path(user_input)
            report_file_sizes(user_input)
            break
    except FileNotFoundError:
        print("\nSorry, file was not found! Please try again.\n")
