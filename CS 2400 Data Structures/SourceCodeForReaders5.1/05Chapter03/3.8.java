// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
	private class Node
	{
	   private T    data; // Entry in bag
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
	} // end Node
