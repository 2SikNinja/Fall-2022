/**
   A class that represents a person's nickname.
 
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public class NickName
{
   private Name nick;
   
   public NickName()
   {
      nick = new Name();
   } // end default constructor
   
   public void setNickName(String nickName)
   {
      nick.setFirst(nickName);
   } // end setNickName
   
   public String getNickName()
   {
      return nick.getFirst();
   } // end getNickName
} // end NickName
