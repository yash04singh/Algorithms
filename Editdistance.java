/* Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace 
Solution time = O(m+n)
         space = O(2*128*4 bytes)
*/


import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Editdistance
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		System.out.println("Enter String no. 1");
		Scanner sc = new Scanner(System.in);
		String s1 = sc.nextLine();
		System.out.println("Enter String no. 2");
		String s2 = sc.nextLine();
		
		int sp1[] = new int[128];
		int sp2[] = new int[128];
		int m = s1.length();
		int n = s2.length();
		int count1 = 0;
		int count2 = 0;
		for(int i=0;i<m;i++){
				sp1[s1.charAt(i)]++;
			}
		for(int i=0;i<n;i++){
				sp2[s2.charAt(i)]++;
				
				}
		for(int i = 0;i<n;i++){
				if(sp1[s2.charAt(i)]!=0){
					sp1[s2.charAt(i)]--;
					sp2[s2.charAt(i)]--;
				}
			}
		for(int i=0;i<128;i++){
				if(sp2[i]!=0)count2++;
				if(sp1[i]!=0)count1++;
				
				   }
			
		if(count1 > count2)
			System.out.println("Minimum No. of steps to change string1 to string2  " + count1);
		else System.out.println("Minimum No. of steps to change string1 to string2 " +count2);
			
			}
}
