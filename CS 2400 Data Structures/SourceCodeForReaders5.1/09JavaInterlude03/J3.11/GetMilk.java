/**
   Demonstrates the behavior of a finally block.
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public class GetMilk
{
   public static void main(String[] args)
   {
      try
      {
         openRefrigerator();
         takeOutMilk();
         pourMilk();
         putBackMilk();
      }
      catch (NoMilkException e)
      {
         System.out.println(e.getMessage());
      }
      finally
      {
         closeRefrigerator();
      }
   } // end main
   
   public static void openRefrigerator()
   {
      System.out.println("Open the refrigerator door.");
   } // end openRefrigerator
   
   public static void takeOutMilk() throws NoMilkException
   {
      if (Math.random() < 0.5)
         System.out.println("Take out the milk.");
      else
         throw new NoMilkException("Out of Milk!");
   } // end openRefrigerator
   
   // < The methods pourMilk, putBackMilk, and closeRefrigerator are analogous to
   //   openRefrigerator and are here. >
   // . . .
} // end GetMilk
