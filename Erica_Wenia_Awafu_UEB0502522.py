print("__________UENR STUDENTS GRADING SYSTEM__________\n")
name = input("Enter Student's name: ")
index = input("Enter student's ID: ")
name = name.capitalize()
try:
    marks =float(input("Enter student's Exam Score: "))
    print("\n___________________________________________")
except ValueError: print("You entered an invalid score!")

try: 
    if marks >= 80 and marks <= 100:
        print(f'Name:{name} \nScore: {marks} \nGrade:A \nGrade Point: 4.0 \nExcellent.')
        print("\n___________________________________________")
            
    elif marks >=75 and marks <= 79:
        print(f'Name:{name} \nScore: {marks} \nGrade:B+ \nGrade Point: 3.5 \nVery Good.')
        print("\n___________________________________________")
        
    elif marks >=70 and marks <= 74:
        print(f'Name:{name} \nScore: {marks} \nGrade:B \nGrade Point: 3.0 \nGood.')
        print("\n___________________________________________")

    elif marks >= 65 and marks <= 69:
        print(f'Name:{name} \nScore: {marks} \nGrade:C+ \nGrade Point: 2.5 \nFairly Good.')
        print("\n___________________________________________")
        
    elif marks >= 60 and marks <= 64:
        print(f'Name:{name} \nScore: {marks} \nGrade:C \nGrade Point: 2.0 \nAbove Average.')
        print("\n___________________________________________")
        
    elif marks >= 55 and marks <= 59:
        print(f'Name:{name} \nScore: {marks} \nGrade:D+ \nGrade Point: 1.5 \nAverage.')
        print("\n___________________________________________")
        
    elif marks >= 50 and marks <= 54:
        print(f'Name:{name} \nScore: {marks} \nGrade:D \nGrade Point: 1.5 \nPass.')
        print("\n___________________________________________")
        
    elif marks >= 0 and marks <= 49:
        print(f'Name:{name} \nScore: {marks} \nGrade:F \nGrade Point: 0.0 \nFail')
        print("\n___________________________________________")
        
    else:
        print(f'{name} invalid score entered !!!')
    print("\n___________________________________________")
except NameError:print("Invalid input!")    

    