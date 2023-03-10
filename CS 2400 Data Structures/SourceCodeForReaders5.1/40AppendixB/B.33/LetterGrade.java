/** A public enumeration of letter grades.
    @author Frank M. Carrano
    @author Timothy M. Henry
    @version 5.0
*/
public enum LetterGrade
{
   A("A", 4.0), A_MINUS("A-", 3.7), B_PLUS("B+", 3.3), B("B", 3.0), 
   B_MINUS("B-", 2.7), C_PLUS("C+", 2.3), C("C", 2.0), C_MINUS("C-", 1.7),
   D_PLUS("D+", 1.3), D("D", 1.0), F("F", 0.0);

   private final String grade;
   private final double points;

   private LetterGrade(String letterGrade, double qualityPoints)
   {
      grade = letterGrade;
      points = qualityPoints;
   } // end constructor

   public String getGrade()
   {
      return grade;
   } // end getGrade

   public double getQualityPoints()
   {
      return points;
   } // end getQualityPoints

   public String toString()
   {
      return getGrade();
   } // end toString
} // end LetterGrade
