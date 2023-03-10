// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public boolean hasEdge(T begin, T end)
{
   boolean found = false;
   VertexInterface<T> beginVertex = vertices.getValue(begin);
   VertexInterface<T> endVertex = vertices.getValue(end);
   if ( (beginVertex != null) && (endVertex != null) )
   {
      Iterator<VertexInterface<T>> neighbors = beginVertex.getNeighborIterator();
      while (!found && neighbors.hasNext())
      {
         VertexInterface<T> nextNeighbor = neighbors.next();
         if (endVertex.equals(nextNeighbor))
            found = true;
      } // end while
   } // end if
   return found;
} // end hasEdge

