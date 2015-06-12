
/**
 * Write a description of class fabonacci here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
import java.util.Scanner;
public class fabonacci
{
 
    
    public  int fibonacciRecusion(int number){
        if(number == 1 || number == 2){
            return 1;
        }
 
        return fibonacciRecusion(number-1) + fibonacciRecusion(number -2); //tail recursion
    }

}
