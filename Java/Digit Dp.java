// Digit Dp 

// Here the question is how many numbers have sum of digits is equal to sum.

// Solution :

// Here the logic is set numbers 0-9 in every possible digit and check the remaining sum same like            knapsack problem and count how many ways we can make subset sum to target.

public class Main {
    
    static Integer[][][] dp;
    public static void main(String[] args) {
        
        String number = "11235";
        int sum = 5 ;
        dp = new Integer[number.length()+1][sum+1][2];
        int result = solve(number,number.length(),sum,1);
        System.out.println(result);
    }
    
    static int solve(String boundary, int index, int remain_sum, int tight){
        if(remain_sum<0) return 0;
        if(index == 1){
            if(remain_sum>=0 && remain_sum<=9) return 1;
            return 0;
        }
        
        if(dp[index][remain_sum][tight]!=null) return dp[index][remain_sum][tight];
        int ans = 0;
        int upper_digit = tight == 1 ? (int)(boundary.charAt(boundary.length()-index)-'0') : 9;
        for(int dig = 0;dig<=upper_digit;dig++){
            int current_tight = (tight==1 && dig==upper_digit) ? 1 :0;
            ans+=solve(boundary, index-1, remain_sum-dig, current_tight);
        }
        
        return dp[index][remain_sum][tight]=ans;
    }
    
    // tight variable is for not exceeding the currrent digit in the number 
    // For example 5236
    // 1st digit max value will be 5 it should not exceed 5
    // 2nd digit max value will be 2 it should not exceed 2 when it first digit is set to 5 otherwise if              first digit is set to 0-4 any value second digit can got till 0-9.
    
    
}
