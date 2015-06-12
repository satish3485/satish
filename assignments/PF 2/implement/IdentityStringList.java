/**
 * TODO: Write a description of class IdentityStringList here.
 * 
 * @author TODO: your name 
 */
public class IdentityStringList {
    private String[] list;
    private int listSize = 10;
    public IdentityStringList(){
        this.list = new String[this.listSize];
    }
    
    public int size(){
        int i = 0;
        while(i < this.listSize && list[i] != null){
            i++;
        }
        return i;
    }
    
    public void add(String word){
        if(size() < (this.listSize)){
            list[size()] = word;
        }else{
            String[] tempList = list.clone();
            this.listSize *= 2;
            this.list = new String[this.listSize];
            for(int i = 0; i < tempList.length; i++){
                list[i] = tempList[i];
            }
            list[size()] = word;
        }
    }
    
    public String get(int index){
        if(index <= (listSize - 1)){
            return this.list[index];
        }else{
            System.out.println("Invalid index.");
            return null;
        }
    }
    
    public int indexOf(String word){
        for(int i = 0; i < list.length; i++){
            if(list[i] == word){
                return i;
            }
            }
        return -1;
    }
    
    public IdentityStringListIterator iterator(){
        return new IdentityStringListIterator(this.list, this.list.length);
    }
    
}
