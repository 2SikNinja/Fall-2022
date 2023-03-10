// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0

public class Name implements Cloneable
// . . .

public Object clone()
{
   Name theCopy = null;

   try
   {
      theCopy = (Name)super.clone(); // Object can throw an exception
   }
   catch (CloneNotSupportedException e)
   {
      System.err.println("Name cannot clone: " + e.toString());
   }

   return theCopy;
} // end clone

