package TreePackage;
/**
   An interface for an expression tree.
   
   @author Frank M. Carrano
   @author Timothy M. Henry
   @version 5.0
*/
public interface ExpressionTreeInterface 
                 extends BinaryTreeInterface<String>
{
   /** Computes the value of the expression in this tree.
       @return  The value of the expression. */
   public double evaluate();
} // end ExpressionTreeInterface
