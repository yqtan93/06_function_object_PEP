user_database = {
    "student" : [
            {"first name" : "Quinn", "last name" : "Butler", "class name" : "3C"}, 
            {"first name" : "Barbara", "last name" : "Banks", "class name" : "4A"},
            {"first name" : "Parker", "last name" : "Fleming", "class name" : "3C"},
            {"first name" : "Mylie", "last name" : "Potts", "class name" : "3B"},
            {"first name" : "Mylie", "last name" : "Morgan", "class name" : "4A"},
            {"first name" : "Cason", "last name" : "Blackburn", "class name" : "4A"},
            {"first name" : "Joseph", "last name" : "Taylor", "class name" : "3C"}
            ],
    "teacher" : [
            {"first name" : "Holly", "last name" : "Le", "class name" : ["3C", "4A"], "subject" : "math"},
            {"first name" : "Asher", "last name" : "Cameron", "class name" : ["3B", "3C"], "subject" : "english"},
            {"first name" : "Dominik", "last name" : "Reed", "class name" : ["3B", "3C", "4A"], "subject" : "history"},
            ],
    "homeroom_teacher" : [
            {"first name" : "Jaydon", "last name" : "Berger", "class name" : "4A"},
            {"first name" : "Jovany", "last name" : "Riggs", "class name" : "3C"},
            {"first name" : "Eugene", "last name" : "Anthony", "class name" : "3B"}
            ]
    }

# Function to display command choice (create, manage, end)
def display_command():
    print("++++++++++++++++ Command menu ++++++++++++++++")
    print("----------------------------------------------")
    print("1. create new user profile")
    print("2. manage existing user profile")
    print("3. exit the program")

# Function to display user type (student, teacher, homeroom teacher, end)
def display_user():
    print("++++++++++++++ Create user menu ++++++++++++++")
    print("----------------------------------------------")
    print("1. create a student profile")
    print("2. create a teacher profile")
    print("3. create a homeschool teacher profile")
    print("4. back to previous menu")

def display_manage():
    print("++++++++++++++ Manage user menu ++++++++++++++")
    print("----------------------------------------------")
    print("1. student profile")
    print("2. teacher profile")
    print("3. homeroom teacher profile")
    print("4. class list")
    print("5. back to previous menu")


# Function to prompt command choice
def select_command():

    print("Welcome to the School management system!\n")

    display_command()

    command = input("\nPlease select from the menu: ")
# While loop for command choice: create, manage, and end
    # If command create entered
    if command == '1':
        create_user()
    # If command manage is entered
    elif command == '2':
        manage_user()
    # Command end
    elif command == '3':
        print('\nExiting the program... Goodbye!')
    else:
        print('\nInvalid option. Please enter a listed option on the menu.')
        select_command()

# Function for command create
def create_user():
    # Prompt user to select user type
    display_user()

    user_type = input("\nPlease select from the menu: ")
    # If student is selected
    if user_type == "1":
    # Prompt to enter student first name, last name, and class name
        first_name = input("Your first name: ")
        last_name = input("Your last name: ")
        class_name = input("Your class name: ")
    # Save student data 
        user_database["student"].append({
            "first name" : first_name,
            "last name" : last_name,
            "class name" : class_name 
        })
    # Print success message
        print("\nStudent account created successfully.")
        
    # Show create command list again
        print("")
        create_user()

    # If teacher is selected
    elif user_type == "2":  
    # Prompt to enter teacher first name, last name, class name, and subject they teach
        first_name = input("Your first name: ")
        last_name = input("Your last name: ")
        subject_name = input("Subject you teach: ")
        #Empty class list and subject list
        class_list = []
        
        while True:
            class_name = input("\nClass you teach (Please enter one at a time, leave empty to exit): ")
            
            if class_name.strip() == "":
                break
            class_list.append(class_name)
        
    # Save teacher data 
        user_database["teacher"].append({
            "first name" : first_name,
            "last name" : last_name,
            "class name" : class_list,
            "subject" : subject_name 
        })
    # Print success message
        print("\nTeacher account created successfully.") 

    # Show create command list again
        print("")
        create_user()

    # If homeroom teacher is selected
    elif user_type == "3":    
    # Prompt to enter homeroom teacher first name, last name, class name, and subject they teach
        first_name = input("Your first name: ")
        last_name = input("Your last name: ")
        class_name = input("Class you lead: ")
        
    # Save homeroom teacher data 
        user_database["homeroom_teacher"].append({
            "first name" : first_name,
            "last name" : last_name,
            "class name" : class_name 
        })
    # Print success message
        print("\nHomeroom teacher account created successfully.")  

    # Show create command list again
        print("")
        create_user()

    # If user wants to go back to previous menu
    elif user_type == "4":
        select_command()

    # Ask user to enter a valid option
    else:
        print("\nInvalid selection. Please select an option from the menu.")
        create_user()

# Function to manage user
def manage_user():
    # Prompt user to select command
    display_manage()

    command = input("\nPlease select from the menu: ")
# While loop for command choice: student, teacher, homeroom teacher, class
    # If student is selected
    if command == '1':
        # Prompt to enter student name
        first_name = input("\nStudent first name: ")
        last_name = input("\nStudent last name: ")
        # List all classes the student attend and the homeroom teacher of the class
        for student in user_database["student"]:
            if student["first name"] == first_name and student["last name"] == last_name: 
                print(f"Student: {first_name} {last_name}\nClass: {student['class name']}\n")
                print(f"+++++++++++ List of subjects taken ++++++++++++")
                print("-----------------------------------------------") 
                print("   Subject   |   Teacher  ")
                print("-----------------------------")  
                for teacher in user_database["teacher"]:
                    if student["class name"] in teacher["class name"]:
                        subject = teacher["subject"]
                        teacher_name = f"{teacher['first name']} {teacher['last name']}" 
                        print(f"{subject:<12} | {teacher_name:>12}")        
    
        # Show manage command list again
        print("")
        manage_user()
        
    # If teacher is selected
    elif command == '2':
        # Prompt to enter teacher name
        first_name = input("Teacher first name: ")
        last_name = input("Teacher last name: ")

        # List all the classes teach by the teacher
        for teacher in user_database["teacher"]:
            if teacher["first name"] == first_name and teacher["last name"] == last_name: 
                print(f"Teacher: {first_name} {last_name}\n")
                print("+++ Class list +++")
                print("------------------")
                for classes in teacher["class name"]:
                    print(classes)

        # Show manage command list 
        print("")
        manage_user()

    # If homeroom teacher is selected
    elif command == '3':
        # Prompt to enter homeroom teacher name
        first_name = input("Homeroom teacher first name: ")
        last_name = input("Homeroom teacher last name: ")
        # Display class and list of student leads by the homeroom teacher
        for homeroom_teacher in user_database["homeroom_teacher"]:
            if homeroom_teacher["first name"] == first_name and homeroom_teacher["last name"] == last_name: 
                print(f"Homeroom teacher: {first_name} {last_name}\nClass: {homeroom_teacher['class name']}\n")
                print(f"+++++++++++ Student in class {homeroom_teacher['class name']} ++++++++++++")
                print("----------------------------------------------")
                for student in user_database["student"]:
                    if student["class name"] == homeroom_teacher["class name"]:
                        print(f"{student['first name']} {student['last name']}")

        # Show manage command list again
        print("")
        manage_user()

    # If class is selected
    elif command == '4':
        # Prompt to enter class name
        class_name = input("Class name: ")
        # Display all students and homeroom teacher
        for homeroom_teacher in user_database["homeroom_teacher"]:
            if homeroom_teacher["class name"] == class_name: 
                print(f"Homeroom teacher: {homeroom_teacher['first name']} {homeroom_teacher['last name']}\nClass: {homeroom_teacher['class name']}\n")
                print(f"+++++++++++ Student in class {homeroom_teacher['class name']} ++++++++++++")
                print("----------------------------------------------")
                for student in user_database["student"]:
                    if student["class name"] == class_name:
                        print(f"{student['first name']} {student['last name']}")

        # Show manage command list again
        print("")
        manage_user()

    # If go back to prev menu is selected
    elif command == '5':
        select_command()

    else:
        print('Invalid option. Please enter a listed option on the menu.\n')
        manage_user()


# Start the program
select_command()



