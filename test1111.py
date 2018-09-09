import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        int [][]arr = new int [n][3];
        for(int i = 0;i<n;i++){
        	String []str = sc.nextLine().split(" ");
        	arr[i][0] = Integer.valueOf(str[0]);
        	arr[i][1] = Integer.valueOf(str[1]);
        	arr[i][2] = Integer.valueOf(str[2]);
        }
        int count=0;
        for(int i = 0;i<n;i++){
        	boolean flag = true;
        	for(int j = 0;j<n;j++){
        		if(j!=i&&compare(arr,i,j)){
        			flag = false;
        			break;
        		}
        	}
        	if(flag==false){
        		count++;
        	}
        }
        System.out.println(count);
        
    }
    public static boolean compare(int [][]arr, int a,int b){
    	if(arr[b][0]>arr[a][0]&&arr[b][1]>arr[a][1]&&arr[b][2]>arr[a][2])
    		return true;
    	return false;
    }
}
