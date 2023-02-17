
print('Bonjour, please enter the following information')
student_name = str(input('Name: '))
student_id = int(input('Student id: '))

def notification(name,  score, status="pass"):
    message = print(f'Hi, {name}  you {status} the exam. Your average score is {score}')
    return message
    
list_of_subjects_dictionary = {
	"Introduction to Computer Work Function": 0,
	"Programming Languages and Problem Solving": 0,
	"Mathematics Applied to Computer Science": 0,
	"Software and Hardware Environment": 0,
	"Introduction to Database Operations": 0
}

initial_count = 0
subject_length = len(list_of_subjects_dictionary)
total_scores = int(0)

print('Please enter the following score for the following subjects')
while initial_count < subject_length:
	subject = list(list_of_subjects_dictionary)[initial_count]
	data = int(input(f'- {subject}: '))
	list_of_subjects_dictionary.update({ subject: data})
	initial_count += 1

for x in list_of_subjects_dictionary.values():
	total_scores += x

average = int(total_scores / subject_length)
min_passing_score = 50

if(average <= min_passing_score):
	notification(name=student_name,  score=average, status="fail")
else:
	notification(name=student_name, score=average)