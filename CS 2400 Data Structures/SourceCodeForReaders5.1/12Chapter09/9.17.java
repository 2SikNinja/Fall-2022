// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public static void displayArray(int array[], int first, int last) 
{
   if (first <= last)
   {
      displayArray(array, first, last - 1);
      System.out.print(array[last] + " ");
   } // end if
} // end displayArray

