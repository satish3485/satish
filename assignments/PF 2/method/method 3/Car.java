
/**
 * Write a description of class Car here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Car
{
    private int hr;
    private int hoo;
    
   public Car(int x)
   {
       this.hr = x;
       this.carnumber();  //invoke the method
    }
    public void carnumber(){
        System.out.println(hr);
    }
}
