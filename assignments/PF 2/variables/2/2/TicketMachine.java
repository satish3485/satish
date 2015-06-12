
/**
 * Write a description of class TicketMachine here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class TicketMachine
{
    
    // instance variables
    // The price of a ticket from this machine.
    private int price;
    // The amount of money entered by a customer so far.
    private int balance;
    // The total amount of money collected by this machine.
    private int total;

    /**
     * Create a machine that issues tickets of the given price.
     */
    public TicketMachine(int cost)
    {
        price = cost;
        balance = 0;
        total = 0;
    }
}
