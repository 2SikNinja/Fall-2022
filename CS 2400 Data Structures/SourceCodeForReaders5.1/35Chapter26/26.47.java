// @author Frank M. Carrano, Timothy M. Henry
// @version 5.0
public Iterator<K> getKeyIterator()
{
   return new KeyIterator();
} // end getKeyIterator

private class KeyIterator implements Iterator<K>
{
   Iterator<Entry<K, V>> localIterator;
   
   public KeyIterator()
   {
      localIterator = bst.getInorderIterator();
   } // end default constructor
   
   public boolean hasNext()
   {
      return localIterator.hasNext();
   } // end hasNext
   
   public K next()
   {
      Entry<K, V> nextEntry = localIterator.next();
      return nextEntry.getKey();
   } // end next
   
   public void remove()
   {
      throw new UnsupportedOperationException();
   } // end remove
} // end KeyIterator

