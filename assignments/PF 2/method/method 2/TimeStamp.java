public class TimeStamp
{
    private int currentTime;
    private TimeStamp stamp1;
    
    public TimeStamp(int currentTime)
    {
        this.currentTime = currentTime;
    }
    
    public TimeStamp(int x, double y){
    
    }
    
    public void showTimeStamp(){
        System.out.println(this.currentTime);
    }
   
}
