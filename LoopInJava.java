import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class LoopInJava {
    static void introMessage(){
        System.out.println("This program will demonstrate the loops in Java programming language. \n");
        System.out.println("Enter five words and number from 0-4 to extract word:  \n");
    }
    
    public static void main(String[] args) {
        introMessage();
        int x = 0;
        int wordsCount = 5;
        List<String> listOfWords = new ArrayList<String>(); 
        Scanner myObj = new Scanner(System.in);
        
        while(x < wordsCount){
            String newValue = myObj.nextLine();
            listOfWords.add(newValue);
            x++;
        }
        
        System.out.println("Now, enter number between  0-4");
        int selectedWord = myObj.nextInt();
        System.out.println("You extracted the word:" + " " + listOfWords.get(selectedWord));
    }
}