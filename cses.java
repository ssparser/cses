import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class cses {

    // Function to find the upper bound in a sorted list
    static int upper_bound(ArrayList<Integer> arr, int k) {
        int low = 0;
        int high = arr.size() - 1;
        int ans = arr.size();
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr.get(mid) > k) {
                ans = mid;
                high = mid - 1;
            } 
            else {
                low = mid + 1;
            }
        }
        return ans;
    }

    // Function to find the best ticket each customer can buy
    public static ArrayList<Integer> concertTickets(ArrayList<Integer> price, ArrayList<Integer> pay) {
        // To store the prices of all tickets.
        ArrayList<Integer> maxPrice = new ArrayList<Integer>(price);
        
        // Sort the ticket prices in ascending order
        Collections.sort(maxPrice);
        
        // Create an array 'ans' to store the answer for each customer.
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for (int i = 0; i < pay.size(); i++) {
            ans.add(0);
        }
        
        // Now iterate through every customer.
        for (int i = 0; i < pay.size(); i++) {
            int temp = pay.get(i);
            
            // Find the upper bound of maximum price offered by customer in the list.
            int itr = upper_bound(maxPrice, temp);
            
            // If it points to the beginning that means no ticket is available for the customer.
            if (itr == 0) {
                ans.set(i, -1);
            } else {
                // Decrement the iterator to get the actual index and then remove that ticket price from the list
                itr--;
                ans.set(i, maxPrice.get(itr));
                maxPrice.remove(itr);
            }
        }
        
        // Return the array answer.
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String n1 = sc.nextLine();
int n = Integer.parseInt(String.valueOf(n1.charAt(0)));
int m = Integer.parseInt(String.valueOf(n1.charAt(1)));

        
        // Reading ticket prices
        ArrayList<Integer> price = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            price.add(sc.nextInt());
        }
        
        // Reading customer payments
        ArrayList<Integer> pay = new ArrayList<Integer>();
        for (int i = 0; i < m; i++) {
            pay.add(sc.nextInt());
        }
        
        // Call the function to get the results
        ArrayList<Integer> result = concertTickets(price, pay);
        
        // Print the result
        for (int res : result) {
            System.out.print(res + " ");
        }
        System.out.println();
        
        sc.close();
    }
}
