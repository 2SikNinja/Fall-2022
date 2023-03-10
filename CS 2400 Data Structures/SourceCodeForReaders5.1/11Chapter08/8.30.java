// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public void addToBack(T newEntry)
{
   DLNode newNode = new DLNode(lastNode, newEntry, null);

   if (isEmpty())
      firstNode = newNode;
   else
      lastNode.setNextNode(newNode);
    
   lastNode = newNode;
} // end addToBack

public void addToFront(T newEntry)
{
   DLNode newNode = new DLNode(null, newEntry, firstNode);

   if (isEmpty())
      lastNode = newNode;
   else
      firstNode.setPreviousNode(newNode);
    
   firstNode = newNode;
} // end addToFront

