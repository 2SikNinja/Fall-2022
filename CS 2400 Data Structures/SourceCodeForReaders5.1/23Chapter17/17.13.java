// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public void add(T newEntry)
{
   firstNode = add(newEntry, firstNode);
   numberOfEntries++;
} // end add

private Node add(T newEntry, Node currentNode)
{
   if ( (currentNode == null) ||
        (newEntry.compareTo(currentNode.getData()) <= 0) )
   {
      currentNode = new Node(newEntry, currentNode);
   }
   else
   {
      Node nodeAfter = add(newEntry, currentNode.getNextNode());
      currentNode.setNextNode(nodeAfter);
   } // end if

   return currentNode;
} // end add
