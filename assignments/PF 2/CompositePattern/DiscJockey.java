
/**
 * Write a description of class DiscJockey here.
 * 
 
 * @version 0.0.1
 */

import java.util.ArrayList;

public class DiscJockey
{
    private ArrayList<SongComponent> songs = new ArrayList<SongComponent>();

    /**
     * Constructor for objects of class DiscJockey
     */
    public DiscJockey()
    {
        SongGroup group = new SongGroup();
        
        group.add(new Song("Lose Yourself"));
        group.add(new Song("Protect Ya Neck"));
        
        songs.add(group);
        
        songs.add(new Song("Tha Squeeze"));
        songs.add(new Song("Role model"));
        
        SongGroup g2 = new SongGroup();
        g2.add(new Song("aa"));
        group.add(g2);
    }
    
    public void start(){
        for(SongComponent s : songs){
            s.play();
        }
    }

}
