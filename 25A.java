import java.util.Scanner;


public class twentyFiveA 
{
    
    public static void main(String [] args)
    {
        Scanner scan = new Scanner(System.in); //scanner to take in input
        int n = scan.nextInt();
        int numbers [] = new int[n];
        scan.nextLine(); // nextInt() doesn't account for the newline character so  move the cursor manually to the next line
     
        for(int i = 0; i < n; i++)
        {
            numbers[i] = scan.nextInt();
        }
        
        int countEven = 0;
        boolean evenness = false;
        for (int i = 0; i < n; i++)
        {
            if(numbers[i] % 2 == 0)
            {
                countEven ++; 
            }
            if (countEven > 1)
            {
                evenness = true; //if more than 1 even number occur this means that the evenness across sequence is even
                break;
            }
        }
        
        for (int i = 0; i < n; i++)
        {
            if (evenness && numbers[i] % 2 != 0 || !evenness && numbers[i] % 2 == 0)
            {
                System.out.println(i+1); // if a number is met with different evenness, it is the unique one
                break;
            }
            
        }
    }
    
}