// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public boolean hasNeighbor()
{
   return !edgeList.isEmpty();
} // end hasNeighbor

public VertexInterface<T> getUnvisitedNeighbor()
{
   VertexInterface<T> result = null;

   Iterator<VertexInterface<T>> neighbors = getNeighborIterator();
   while ( neighbors.hasNext() && (result == null) )
   {
      VertexInterface<T> nextNeighbor = neighbors.next();
      if (!nextNeighbor.isVisited())
         result = nextNeighbor;
   } // end while

   return result;
} // end getUnvisitedNeighbor

