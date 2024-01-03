import java.util.Arrays;
import java.util.Scanner;

public class MaximumPathSum1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t  = sc.nextInt();


        while (t-- > 0) {
            int n = sc.nextInt();

            // Create a 2D array to store the triangle of numbers
            int[][] arr = new int[n][];

            // Input values for each row of the array
            for (int i = 0; i < n; i++) {
                arr[i] = new int[i + 1]; // Initialize the array for the current row
                for (int j = 0; j <= i; j++) {
                    arr[i][j] = sc.nextInt(); // Input the value for the current element
                }
            }

            // Call the max function and print the result
            System.out.println(max(arr));
        }

    }

    public static int max(int[][] arr){
        int n = arr.length;
        int[][] dp = new int[n][20];
        for(int[] row: dp){
            Arrays.fill(row,-1);
        }
        return recursive(0,0,arr,n,dp);
    }

    private  static int recursive(int i, int j, int[][]arr,int n,int[][] dp){

        if(i< 0 || i>= n || j < 0 || j>= arr[i].length ){
            return 0;
        }
        if(dp[i][j] != -1){
            return dp[i][j];

        }
        int down = arr[i][j] + recursive(i + 1, j, arr, n,dp);
        int right = arr[i][j] + recursive(i + 1, j + 1, arr, n,dp);

        return dp[i][j]=Math.max(down, right);
    }
}