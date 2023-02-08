#include <iostream>
using namespace std;

int main() {
  string studentName, studentId;
  float subjMath, subjEnglish, subjScience, subjOther, subjectsTotalMark, result;
  
  cout << "Please enter your name: ";
  cin >> studentName;
  cout << "Next, enter your subjects marks let's start with Math: ";
  cin >> subjMath;
  cout << "Next, is English:";
  cin >> subjEnglish;
  cout << "Next, Science: ";
  cin >> subjScience;
  cout << "And last subject: ";
  cin >> subjOther;
  
  subjectsTotalMark = subjMath + subjEnglish + subjScience + subjOther;
  result = subjectsTotalMark / 4;
  cout << "Your result is: " << result;
  
  
  
  
  return 0;
}
