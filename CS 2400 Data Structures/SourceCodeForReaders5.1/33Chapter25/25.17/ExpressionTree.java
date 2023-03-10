package TreePackage;
/**
    A class that implements an expression tree by extending BinaryTree.
 
    @author Frank M. Carrano
    @author Timothy M. Henry
    @version 5.0
*/
public class ExpressionTree extends BinaryTree<String>
                            implements ExpressionTreeInterface
{
   public ExpressionTree()
   {
   } // end default constructor

   public double evaluate()
   {
      return evaluate(getRootNode());
   } // end evaluate

   private double evaluate(BinaryNode<String> rootNode)
   {
      double result;
      if (rootNode == null)
         result = 0;
      else if (rootNode.isLeaf())
      {
         String variable = rootNode.getData();
         result = getValueOf(variable);
      }
      else
      {
         double firstOperand = evaluate(rootNode.getLeftChild());
         double secondOperand = evaluate(rootNode.getRightChild());
         String operator = rootNode.getData();
         result = compute(operator, firstOperand, secondOperand);
      } // end if

      return result;
   } // end evaluate

   private double getValueOf(String variable)
   { // Strings allow multicharacter variables
      
      double result = 0;
      
      // To be defined. 

      return result;
   } // end getValueOf
   
   private double compute(String operator, double firstOperand, double secondOperand)
   {
      double result = 0;
      
      // To be defined.
      
      return result;
   } // end compute
} // end ExpressionTree
