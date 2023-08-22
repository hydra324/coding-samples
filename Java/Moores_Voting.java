// "static void main" must be defined in a public class.
public class Main {
    
    static int findMajorityElement(int[] n){
        int count=0,prev_element=-1;
        
        for(int num:n){
            if(prev_element!=num) count--;
            else count++;
            if(count<0){
                prev_element=num;
                count=1;
            }
        }
        count=0;
        for(int num:n){
            if(num==prev_element) count++;
        }
        return count>n.length/2 ? prev_element : -1;
    }
    public static void main(String[] args) {
        System.out.println(findMajorityElement(new int[]{1,1,1,1,2,3}));
    }
}
