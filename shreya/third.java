import java.util.*;

class Main

{
    public static int[] group_sol(int N,int[] a)
    {
        int maxE = -1;
int[] arr=a;
int n=N;

//int result[]={0};
List<Integer> arrlist = new ArrayList<Integer>();
for (int i = 0; i < n; i++) {

maxE = Math.max(maxE, arr[i]);

}

int[] freq = new int[maxE + 1];

for (int i = 0; i < n; i++) {

freq[arr[i]]++;

}

int maxF = -1;

for (int i = 0; i <= maxE; i++) {

maxF = Math.max(maxF, freq[i]);

}

while(maxF > 0){

for(int i=maxE; i>=0;i--){

if(maxF == freq[i])

arrlist.add(i);

}

maxF--;

}

Object[] result2 = arrlist.toArray();
int intArray[] = new int[result2.length];
for(int i=0; i<result2.length; i++){
         intArray[i] = (int) result2[i];
      }
return intArray;

}

public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

int n = sc.nextInt();

int[] arr = new int[n];

for(int i=0;i<n;i++)

arr[i] = sc.nextInt();

int[] out = group_sol(n, arr);

for( int i=0;i<out.length;i++)
{
    System.out.println(out[i]);
}

}

}