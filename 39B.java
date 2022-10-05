import java.util.*;

public class thirtyNineB 
{
   public static void main(String [] args)
   {
        LinkedHashMap<Integer, Integer> incomes = new LinkedHashMap<Integer, Integer>(); //to carry year, income pairs and have them ordered the way they're inserted
     
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.nextLine();
     
        int year = 2001; //the initial year value
        for(int i = 0; i < n; i++)
        {
            incomes.put(year++, scan.nextInt()); //add years with every entry and scan the income for each year
        }
        
//        System.out.println(incomes);
        ArrayList<Integer> perfectGrowth = new ArrayList<Integer>(); // carry the years that follow the desired growing trend
        int counter = 1; // counter to keep track of growth(by one every step)
        for(int key : incomes.keySet())
        {
            if(incomes.get(key) > 0 && incomes.get(key) == counter)
            {
                perfectGrowth.add(key);
                counter ++;
            }
        }
        System.out.println(perfectGrowth.size());
        if (!perfectGrowth.isEmpty())
        {
            for(int i = 0; i < perfectGrowth.size(); i++)
            {
                System.out.print(perfectGrowth.get(i) + " ");
            }
        }
        
   }
}
