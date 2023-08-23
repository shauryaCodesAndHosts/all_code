import java.util.*;
class shreya {

	static int maxWater(int height[], int n)
	{
		int max = 0;

		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				int current
					= (Math.min(height[i], height[j])
					* (j - i - 1));

				max = Math.max(max, current);
			}
		}
		return max;
	}

	public static void main(String[] args)
	{
        Scanner sc=new Scanner(System.in);
        int test=sc.nextInt();
		for(int i=0;i<test;i++ )
        {
            int n = sc.nextInt();
            int[] height=new int[n];
			for(int j=0;j<n;j++){
				height[j]=sc.nextInt();
			}
		    System.out.println(maxWater(height, n));
        }
	}
}

