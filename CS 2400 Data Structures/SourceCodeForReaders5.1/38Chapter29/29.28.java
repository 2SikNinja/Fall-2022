// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
GraphInterface<String> roadMap = new UndirectedGraph<String>();
roadMap.addVertex("Provincetown");
roadMap.addVertex("Truro");
// . . .

roadMap.addVertex("Falmouth");
roadMap.addEdge("Provincetown", "Truro", 10);
// . . .

roadMap.addEdge("Hyannis", "Falmouth", 20);

StackInterface<String> bestRoute = new LinkedStack<String>();
double distance = roadMap.getCheapestPath("Truro", "Falmouth", bestRoute);
System.out.println("The shortest route from Truro to Falmouth is " + 
                   distance + " miles long and " +
                   "passes through the following towns:");
while (!bestRoute.isEmpty())
   System.out.println(bestRoute.pop());

