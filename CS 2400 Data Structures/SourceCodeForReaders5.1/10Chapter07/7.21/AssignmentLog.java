import java.sql.Date;
/**
   A class that represents a log of assignments ordered by priority.
   
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public class AssignmentLog
{
   private PriorityQueueInterface<Assignment> log;

   public AssignmentLog()
   {
      log = new PriorityQueue<>();
   } // end constructor

   public void addProject(Assignment newAssignment)
   {
      log.add(newAssignment);
   } // end addProject

   public void addProject(String courseCode, String task, Date dueDate)
   {
      Assignment newAssignment = new Assignment(courseCode, task, dueDate);
      addProject(newAssignment);
   } // end addProject

   public Assignment getNextProject()
   {
      return log.peek();
   } // end getNextProject

   public Assignment removeNextProject()
   {
      return log.remove();
   } // end removeNextProject
} // end AssignmentLog
