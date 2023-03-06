
def calculate_net_Proceeds( netProceed,  dividends,  costBasic ):
	return (netProceed + dividends) / costBasic -1

student_name = str(input("- Enter your student name: "))
student_id = str(input("- Please enter your student id: "))
netProceed = int(input("Next, enter net proceed amount: "))
dividends = int(input("Next, enter dividend amount: "))
costBasic = int(input("Next, enter cost basic amount: "))

results = calculate_net_Proceeds(netProceed=netProceed, dividends=dividends, costBasic=costBasic)
print(f'Student: {student_name} \n')
print(f'Student id: {student_id} \n')
print("Calculating your result...")

if(results < 55):
    print("Risk to invest")

if(results >= 65 and results <=75):
    print("Medium risk to invest")
    
if(results > 85):
    print("Risk to invest")
    