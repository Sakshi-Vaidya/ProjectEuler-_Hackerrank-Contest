import java.util.*;  
import java.math.BigInteger;

public class Power_digit_sum {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
      
        while(t-- > 0) {
            
            int n = sc.nextInt();
            
            BigInteger pow = BigInteger.ONE;
            
            for(int i = 1; i <= n; i++) {
                pow = pow.multiply(new BigInteger("2")); 
            }
            
            int sum = 0;            
            while(pow.compareTo(BigInteger.ZERO) > 0) {
              
                BigInteger d = pow.mod(BigInteger.TEN);
                sum += d.intValue();
              
                pow = pow.divide(BigInteger.TEN);
            }
            
            System.out.println(sum);  
        }

        sc.close();
    }
}