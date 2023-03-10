// Recursively searches a chain of nodes for desiredItem,
// beginning with the node that currentNode references.
// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
private boolean search(Node currentNode, T desiredItem)
{
   boolean found;

   if (currentNode == null)
      found = false;
   else if (desiredItem.equals(currentNode.getData()))
      found = true;
   else
      found = search(currentNode.getNextNode(), desiredItem);
    
   return found;
} // end search

public boolean contains(T anEntry)
{
   return search(firstNode, anEntry);
} // end contains

