how_many = int(input("How many students: "))

total = 0
passed = 0
failed = 0

for i in range(1, how_many + 1):
    student_name = input(f"Student {i} name: ")
    marks = int(input(f"Student {i} marks: "))

    total = total + marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / how_many


print()
print("===== STUDENT CLASS ANALYZER =====")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Students passed: {passed}")
print(f"Students failed: {failed}")
