# School administration tool
from cmath import infj
import csv

def write_into_csv(info_list):
    with open('Student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Phone","Email"])

        writer.writerow(info_list)

if __name__ == '__main__':

    condition = True
    count = 1
    while(condition):
        student_info = input("Enter student information for student #{} in following format (Name, Age, No, Email):".format(count))

    
        #split
        student_info_list = student_info.split(' ')
        
        print("\nThe entered information is -\nName: {}\nAge: {}\nPhone: {}\nEmail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is the entered information is correct? (Y/N): ")
        if choice_check == "Y" or "y":
             write_into_csv(student_info_list)

             condition_check = input("Enter (Y/N) if you want to enter another student information: ")
             if condition_check == "Y" or "y":
                condition = True
                count = count + 1
             elif condition_check == "N" or "n":
                condition = False

        elif choice_check == "N" or "n":
            print("Please the check the details")
