import java.util.*;

public class twentySevenB 
{
    public static void main(String [] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int given = ((n * (n - 1)) / 2) - 1; //given list of games (with 1 missing)
        
        int games[][] = new int[given][2]; // each field will carry a game score which means 2 columns 1 for each participant
        
        for(int i = 0; i < given; i++)
        {
            games[i][0] = scan.nextInt();
            games[i][1] = scan.nextInt();
            scan.nextLine();
        }
        
//        for (int i = 0; i < given; i++)
//        {
//            System.out.println(games[i][0] + " , " + games[i][1]);
//        }
        
        int occurences [] = new int[n]; // this will carry occurences of each participant, they should all appear n - 1 times
        int speeds [] = new int[n]; //  this will carry number of wins for each participant(their sleeping speed)
        for(int i = 0; i < given; i++)
        {
            for(int x = 0; x < n; x++)
            {
                if(games[i][0] == x + 1)
                {
                    speeds[x] ++; // check first participant (X) in each game, they are the winner
                }
            }
            
            for(int j = 0; j < 2; j++)
            {
                for(int k = 0; k < n; k++)
                {
                    if(games[i][j] == k + 1)
                    {
                        occurences[k] ++; // count number of times a partcipant appear
                    }
                }
            }
        }
        
        int missing [] = new int [2]; // carry missing game particiants' indices with respect to the occurances and speeds arrays
        int m = 0;
        for(int k = 0; k < n; k++)
        {
            if(occurences[k] < n - 1)
            {
                missing[m++] = k;
            }
        }
        
        if(speeds[missing[0]] > speeds[missing[1]])
        {
            System.out.println((missing[0]+1) + " " + (missing[1]+1));
        }
        else
        {
            System.out.println((missing[1]+1) + " " + (missing[0]+1));
        }
    }
}
