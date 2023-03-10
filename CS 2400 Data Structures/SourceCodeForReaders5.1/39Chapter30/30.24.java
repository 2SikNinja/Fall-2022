// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public int getShortestPath(T begin, T end, StackInterface<T> path)
{
   resetVertices();
   boolean done = false;
   QueueInterface<VertexInterface<T>> vertexQueue = new LinkedQueue<>();
   VertexInterface<T> originVertex = vertices.getValue(begin);
   VertexInterface<T> endVertex = vertices.getValue(end);
   originVertex.visit();

   // Assertion: resetVertices() has executed setCost(0)
   // and setPredecessor(null) for originVertex

   vertexQueue.enqueue(originVertex);
   while (!done && !vertexQueue.isEmpty())
   {
      VertexInterface<T> frontVertex = vertexQueue.dequeue();
      Iterator<VertexInterface<T>> neighbors = frontVertex.getNeighborIterator();
      while (!done && neighbors.hasNext())
      {
         VertexInterface<T> nextNeighbor = neighbors.next();
         if (!nextNeighbor.isVisited())
         {
            nextNeighbor.visit();
            nextNeighbor.setCost(1 + frontVertex.getCost());
            nextNeighbor.setPredecessor(frontVertex);
            vertexQueue.enqueue(nextNeighbor);
         } // end if

         if (nextNeighbor.equals(endVertex))
            done = true;
      } // end while
   } // end while

   // Traversal ends; construct shortest path
   int pathLength = (int)endVertex.getCost();
   path.push(endVertex.getLabel());

   VertexInterface<T> vertex = endVertex;
   while (vertex.hasPredecessor())
   {
      vertex = vertex.getPredecessor();
      path.push(vertex.getLabel());
   } // end while

   return pathLength;
} // end getShortestPath

