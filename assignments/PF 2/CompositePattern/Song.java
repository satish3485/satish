
/**
 * Write a description of class Song here.
 * 
 
 * @version 0.0.1
 */


// LEAF
public class Song implements SongComponent
{

    private String name;
    /**
     * Constructor for objects of class Song
     */
    public Song(String name)
    {
        this.name = name;
        System.out.println("Creating a song with name "+ name + "\n");
    }
    
    public void play(){
        System.out.println("Playing a song " + name + "\n");
    }

}
