import java.util.*;

public class Solution {
    
    static int[][] grid = new int[20][20];
    static int greatestOne = 0;
    
    static void checkHorinzontalForward(int x, int y) {
        if(x + 3 >= 20) {
            return;
        }
        
        int temp = grid[x][y];
        temp *= grid[x + 1][y];
        temp *= grid[x + 2][y];
        temp *= grid[x + 3][y];
        
        if(temp > greatestOne) {
            greatestOne = temp;
        }
    }
    
    static void checkVerticalDownard(int x, int y) {
        if(y + 3 >= 20) {
            return;
        }
        
        int temp = grid[x][y];
        temp *= grid[x][y + 1];
        temp *= grid[x][y + 2];
        temp *= grid[x][y + 3];
        
        if(temp > greatestOne) {
            greatestOne = temp;
        }
    }
    
    static void checkAscendingDiagonal(int x, int y) {
        if(x + 3 >= 20 || y - 3 < 0) {
            return;
        }
        
        int temp = grid[x][y];
        temp *= grid[x + 1][y - 1];
        temp *= grid[x + 2][y - 2];
        temp *= grid[x + 3][y - 3];
        
        if(temp > greatestOne) {
            greatestOne = temp;
        }
    }
    
    static void checkDescendingDiagonal(int x, int y) {
        if(x + 3 >= 20 || y + 3 >= 20) {
            return;
        }
        
        int temp = grid[x][y];
        temp *= grid[x + 1][y + 1];
        temp *= grid[x + 2][y + 2];
        temp *= grid[x + 3][y + 3];
        
        if(temp > greatestOne) {
            greatestOne = temp;
        }
    }

    public static void main(String[] args) {
        
        // Fill the grid
        try(Scanner in = new Scanner(System.in)) {    
            for(int x = 0; x < 20; x++){
                for(int y = 0; y < 20; y++){
                    grid[x][y] = in.nextInt();
                }
            }
        }
        
        // Check for the greatest value in a window
        // of length 4
        for(int x = 0; x < 20; x++) {
            for(int y = 0; y < 20; y++) {
                checkHorinzontalForward(x, y);
                checkVerticalDownard(x, y);
                checkAscendingDiagonal(x, y);
                checkDescendingDiagonal(x, y);
            }
        }
        
        System.out.println(greatestOne);
    }
}