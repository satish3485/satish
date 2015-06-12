
/**
 * Write a description of class method here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class method
{
    // instance variables - replace the example below with your own
    public method(int i){
    }
    public int ss(int s){
        return s;
    }
    public int recursion(int r){
        for (int i=0; i<r; i++){
            System.out.println(i);
            recursion(r-1);
          
        }
        return r;
    }
    public static int sum3(int n){ 
    if (n == 1) // base case 
       return  1; 
    else    // general case 
       return n + sum3( n - 1);//tail recursion 
    }
}
