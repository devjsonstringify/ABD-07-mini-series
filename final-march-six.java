
import java.util.Scanner;

class FinalMarchSix {
    
    int calculateNetProceeds( int netProceed,  int dividends,  int costBasic ){
	return (netProceed + dividends) / costBasic -1;
    }
	
  public static void main(String[] args) {
    String studentName, studentId;
    int netProceed, dividends, costBasic, results;

	Scanner myObj = new Scanner(System.in);
	FinalMarchSix myObj1 = new FinalMarchSix();

    System.out.println("- Enter your student name: ");
    studentName = myObj.nextLine();

	System.out.println("- Enter your student id: ");
    studentId = myObj.nextLine();

	System.out.println("Next, enter net proceed amount: ");
	netProceed = myObj.nextInt();
	
	System.out.println("Next, enter dividend amount: ");
	dividends = myObj.nextInt();
	
	System.out.println("Next, enter cost basic amount: ");
	costBasic = myObj.nextInt();
	
	
	results = myObj1.calculateNetProceeds(netProceed, dividends, costBasic);
	System.out.println(results);
	
	System.out.println(studentName + "\n");
	System.out.println(studentId + "\n");
	System.out.println("Calculating your result...");
	
	if(results < 55){
	    System.out.println("Risk to invest");
	}
	
	if(results >= 65 && results <= 75){
	     System.out.println("Medium risk to invest");
	}
	
	if(results > 85){
	    System.out.println("Risk to invest");
	}
	

  }
}
