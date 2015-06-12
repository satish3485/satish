
/**
 * Write a description of class ierative here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
 import java.util.ArrayList;
public class iterative
{
    public ArrayList<car> dd;
    public int search(int[] mylist,int key){
        for (int index = 0; index < mylist.length; index++)
      {
           if ( mylist[index] == key ){
                 System.out.print("i found");
                 return index;
                
                }
           
      
      }
    
      return -1;
    }
    public void max(int[] dat){
        int maxvalue = dat[0];
        for (int i=1; i < dat.length; i++){
            if (dat[i] > maxvalue){
                maxvalue = dat[i];
            }

        }
        System.out.print("max = "+ maxvalue);
        
    }        
    public void min(int[] dat){
        int minvalue = dat[0];
        for(int i=1; i<dat.length; i++){
            if(dat[i] < minvalue){
                minvalue = dat[i];
            }
        }
        System.out.print("min = "+ minvalue);
    }
    
    public void sum(int[] dat){
        int sumvalue = 0;
        for(int i=0; i<dat.length; i++){
            sumvalue += dat[i];
        }
        System.out.print("sum = "+ sumvalue);
    }
   
    public void sum2(int r){
         ArrayList<Integer> s= new ArrayList<Integer>();
         s.add(23);
         s.add(25);
         s.add(23);
         s.add(1,546745);
         dd = new ArrayList<car>();

         
         System.out.println(s.size());
         for (int i=0; i<s.size(); i++){
             if (s.get(i) == r){
                 System.out.println(i);
                }
             
            }
           
        }
}
