
/**
 * Write a description of class SongGroup here.
 * 
 
 * @version 0.0.1
 */

import java.util.ArrayList;


public class SongGroup implements SongComponent
{
    
    // COMPOSITE
    
    private ArrayList<SongComponent> songs = new ArrayList<SongComponent>();

    /**
     * Constructor for objects of class SongGroup
     */
    public SongGroup()
    {
        System.out.println("Creating a SongGroup\n");
    }
    
    public void add(SongComponent song){
        songs.add(song);
    }


    public void play(){
        System.out.println("-------------------------");
        System.out.println("Calling play of a SongGroup");
        for(SongComponent s : songs){
            s.play();
        }
        System.out.println("-------------------------\n");
    }
}
