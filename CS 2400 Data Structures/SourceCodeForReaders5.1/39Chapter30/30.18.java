// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public boolean addEdge(T begin, T end, double edgeWeight)
{
   boolean result = false;
   VertexInterface<T> beginVertex = vertices.getValue(begin);
   VertexInterface<T> endVertex = vertices.getValue(end);
   if ( (beginVertex != null) && (endVertex != null) )
      result = beginVertex.connect(endVertex, edgeWeight);
   if (result)
      edgeCount++;
   return result;
} // end addEdge

public boolean addEdge(T begin, T end)
{
   return addEdge(begin, end, 0);
} // end addEdge
