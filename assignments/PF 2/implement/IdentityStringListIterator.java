/**
 * TODO: Write a description of class IdentityStringListIterator here.
 * 
 * @author TODO: your name
 */
public class IdentityStringListIterator {
    private String[] itList;
    private int listSize;
    private int pointer;
    public IdentityStringListIterator(String[] array,int arraySize){
        this.itList = array;
        this.listSize = arraySize;
        this.pointer = 0;
    }

    public boolean hasNext(){
        if((pointer) <= listSize && itList[pointer] != null){
            return true;
        }else{
            return false;
        }
    }
    
    public String next(){
        String word = itList[pointer];
        pointer ++;
        return word;
    }

}
