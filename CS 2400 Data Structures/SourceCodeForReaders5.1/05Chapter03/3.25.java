// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0 */
private class Node
{
   private T data;    // Entry in bag
   private Node next; // Link to next node
   
   private Node(T dataPortion)
   {
      this(dataPortion, null);
   } // end constructor
   
   private Node(T dataPortion, Node nextNode)
   {
      data = dataPortion;
      next = nextNode;
   } // end constructor
   
   private T getData()
   {
      return data;
   } // end getData
   
   private void setData(T newData)
   {
      data = newData;
   } // end setData
   
   private Node getNextNode()
   {
      return next;
   } // end getNextNode
   
   private void setNextNode(Node nextNode)
   {
      next = nextNode;
   } // end setNextNode
} // end Node
