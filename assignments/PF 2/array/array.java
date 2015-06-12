import java.util.HashMap;
import java.util.HashSet;
/**
 * Write a description of class array here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class array
{
    // instance variables - replace the example below with your own
    public void arrays(){
        
        HashSet<String> mySet = new HashSet<String>();
        mySet.add("one");
        mySet.add("two");
        mySet.add("one");
        
        for(String i : mySet){
            System.out.println(i);
        }
    }
    public boolean find(int a, int b){
        if (a == 2){
            return false;
        }
        if (a == b){
            return true;
        }
        return false;
    }
    public void insertElement()
    {
       int[][] lis = new int[2][];
       lis[0] = new int[3];
       lis[1] = new int[9];
       HashMap<String, String> phoneBook = new HashMap<String, String>();
       phoneBook.put("Charles Nguyen", "(531) 9392 4587");
       phoneBook.put("Lisa Jones", "(402) 4536 4674");
       phoneBook.put("William H. Smith", "(998) 5488 0123");
       phoneBook.put("Charles Nguyen", "322333287");
       for(Object i: phoneBook.keySet()){
           System.out.println(i + "   "+phoneBook.get(i));
       }
    }
}
