import java.util.Scanner;
/**
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public class FirstProgram
{
   public static void main(String[] args)
   {
      Scanner keyboard = new Scanner(System.in);
      System.out.println("Hello out there.");
      System.out.println("Want to talk some more?"); 
      System.out.println("Answer yes or no.");

      String answer = keyboard.next();
      if (answer.equals("yes"))
         System.out.println("Nice weather we are having.");
      System.out.println("Good-bye.");
   } // end main
} // end FirstProgram
