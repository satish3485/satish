
/**
 * Write a description of class massagepost here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class massagepost extends Post
{
    // instance variables - replace the example below with your own
    public String massage;
    public massagepost massages;
    public massagepost(int a, int b){
         super(a);
        System.out.println(a);
    }
    public void printShortSummary(Post s){
        Post massage = new massagepost(2,3);
        
    }
    public void display(){
        TestAll();
        System.out.println("message");
            massagepost f = new massagepost(3,4);
            display(f);
        }
    public void addcoment(massagepost massages){
        addPost(massages);
    }
    
    public void display(String b){
        System.out.println("username");
        System.out.print("timestamp");
        
    }
    
}
