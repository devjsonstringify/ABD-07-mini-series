
import java.util.Scanner; // Import the Scanner class

class GetUserInputs {
  public static void main(String[] args) {
    int x, y, multiplication, addition, subtraction, division;
    Scanner myObj = new Scanner(System.in);
    
    System.out.println("Type a number:");
    x = myObj.nextInt();

    System.out.println("Type another number:");
    y = myObj.nextInt();

    multiplication = x * y;
    addition = x + y;
    subtraction = x - y;
    division = x / y;

    System.out.println("Multiplication" + " "  + multiplication );
    System.out.println("Addition" + " "  + addition);
    System.out.println("Subtraction" + " " + subtraction); 
    System.out.println("Division" + " "  + division); 
  }
}
