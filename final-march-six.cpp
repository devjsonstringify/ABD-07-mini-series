#include <iostream>
using namespace std;

 int calculateNetProceeds(int netProceed, int dividends, int costBasic ){
      return (netProceed + dividends) / costBasic -1;
  }
  
int main() {
  string studentName, studentId;
  double netProceed, dividends, costBasic;
  double results;
  
  cout << "- Enter your student name: ";
  cin >> studentName;
  cout << "- Enter student id: ";
  cin >> studentId;
  cout << "Next, enter net proceed amount: ";
  cin >> netProceed;
  cout << "Next, enter dividend amount: ";
  cin >> dividends;
  cout << "Next, enter cost basic amount: ";
  cin >> costBasic;
  
  results = calculateNetProceeds(netProceed, dividends, costBasic);
  
  cout << "student" + studentName + "\n";
  cout << "Id" + studentId + "\n";
  cout << "Calculating your result..."
  
  if(results < 55){
      cout << "Risk to invest";
  }
  
  if(results >= 65 && results <= 75){
      cout << "Medium risk to invest";
  }
  
  if(results > 85){
      cout << "No risk";
  }

  return 0;
}