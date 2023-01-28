/**
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public class Pair<S, T>
{
   private S first;
   private T second;
   
   public Pair(S firstItem, T secondItem)
   {
      first = firstItem;
      second = secondItem;
   } // end constructor
   
   public String toString()
   {
      return "(" + first + ", " + second + ")";
   } // end toString
} // end Pair
