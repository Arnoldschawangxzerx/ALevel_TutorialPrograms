# Input number of students
a=0
while a != 2:
    
    Class = input("Enter class name")
    if Class== "AL":
        Class_Size=4
    elif Class== "AS":
        Class_Size=5
    elif Class== "O3":
        Class_Size=3
    # Initialize lists for student names and their marks
    Student_Name = [None] * Class_Size  # Create a list with a size equal to the number of students
    Student_Marks = [[None] * 2 for _ in range(Class_Size)]  # Create a 2D list for student marks (2 Subjectsjects per student)

    # List of Subjectsjects
    Subjects = ['Math', 'English']
    Class=["AL", "AS", "O3"]

    # Get names of students
    for count in range(Class_Size):
        name = input(f"Enter the name of student {count+1}: ")
        Student_Name[count] = name  # Assign student name at index `count`

    # Get marks for each student in each Subjectsject
    
    for i in range(len(Subjects)):  # Loop through each Subject (2 Subjects in total)
        for j in range(Class_Size):  # Loop through each student
            print()
            num = int(input(f"Enter marks of {Student_Name[j]} in {Subjects[i]}: "))  # Get marks
            Student_Marks[j][i] = num  # Assign the mark to the student's Subjects in the 2D list

    # Print the marks list
    print("Marks for each student:")
    for j in range(Class_Size):  # Loop through each student
        print(f"{Student_Name[j]}: Math - {Student_Marks[j][0]}, English - {Student_Marks[j][1]}")
a +=1
