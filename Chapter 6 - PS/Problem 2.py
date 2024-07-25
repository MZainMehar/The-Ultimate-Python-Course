# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

sub1 = int(input("Enter the marks of the first subject: "))
sub2 = (int(input("Enter the marks of the second subject: ")))
sub3 = (int(input("Enter the marks of the third subject: ")))

total = sub1 + sub2 + sub3
percentage = (total/3) * 100

if(percentage > 40 and sub1 > 33 and sub2 > 33 and sub3 > 33):
    print("Congratulations! You have passed the exam.")

else:
    print("Sorry! You have failed the exam.")

    