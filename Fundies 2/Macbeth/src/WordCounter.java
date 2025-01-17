import java.util.*;

/** Class to count frequencies of the words generated by an
 *   iterator.
 Template:
 Methods:
 this.contains(Word)           -- boolean
 this.countWords(Iterator<Word>)-- void
 this.words()                   -- int
 this.void printWords(int)      -- void

 */
public class WordCounter extends HashMap<String, Word> {
    HashMap<String, Word> collection;


    /** record the words generated by the given iterator
     * @param it the given iterator over the input text
     */
    public void countWords(Iterator<Word> it) {
        while (it.hasNext()) {
            Word w = it.next();
            if (!this.containsKey(w.w)) {
                this.put(w.w, w);
            }
            else {
                this.get(w.w).increment();
            }
        }
        //System.out.print(this);
    }

    /** Count the number of different words in this Counter 
     * @return the count of different words in this Counter
     */
    public int words() {
        return this.size();
    }


    /** Print the words and their frequencies for the top n words 
     * @param n the numebr of words to print
     */
    public void printWords(int n) {
        Comparator<Word> pred = new Word("").new WordsByFreq();
        ArrayList<Word> l = new ArrayList<Word>(this.values());
        Collections.sort(l, pred);
        ArrayList<Word> result = new ArrayList<Word>();
        for (int index = 0; index < n; index++) {
            result.add(l.get(index));
            
        } 
        System.out.print(result);

    }


}







