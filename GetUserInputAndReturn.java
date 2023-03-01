import java.util.Scanner;


public class GetUserInputAndReturn {
 
    static int calculatePercentage(int math, int  english, int science, int history){
        int sum = math + english + science + history / 4;
        return sum;
    }
    
    static void printNextLn(String value){
        System.out.println(value);
    }
    
    public static void main(String[] args) {
        String studentName, studentId;
        int math, english, science, history, sum;
        
        Scanner myObj = new Scanner(System.in);
        System.out.println("Please enter the following details \n");
       
        printNextLn("Student name:");
        studentName = myObj.nextLine();
        
        printNextLn("Student id:");
        studentId = myObj.nextLine();
        
        printNextLn("Math score:");
        math = myObj.nextInt();
        
        printNextLn("English score:");
        english = myObj.nextInt();
        
        printNextLn("Science score: ");
        science = myObj.nextInt();
        
        printNextLn("History score: ");
        history = myObj.nextInt();

        printNextLn("Student name:" + studentName + "\n");
        printNextLn("Student id:" + studentId + "\n");
        printNextLn("Score:" + calculatePercentage(math, english, science, history) + "\n");
        
    }

}