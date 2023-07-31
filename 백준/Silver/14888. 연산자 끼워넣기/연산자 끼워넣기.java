import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DateFormatSymbols;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

// DFS 완탐
public class Main {
	public static int N;
	public static int[] numArr;
	public static int[] gen;
	public static int max = Integer.MIN_VALUE;
	public static int min = Integer.MAX_VALUE;
	// numArr을 순회하면서 각 연산자들을 사용.
	// gen[] -= 1
	
	public static void DFS(int val,int depth) {
		if (depth == N) {
			max = Math.max(val, max);
			min = Math.min(val, min);
			return;
		}
		if (gen[0] > 0) {
			gen[0] -= 1;
			DFS(val+numArr[depth], depth+1);
			gen[0] += 1;
		}
		if (gen[1] > 0) {
			gen[1] -= 1;
			DFS(val-numArr[depth], depth+1);
			gen[1] += 1;
		}
		if (gen[2] > 0) {
			gen[2] -= 1;
			DFS(val*numArr[depth], depth+1);
			gen[2] += 1;
		}
		if (gen[3] > 0) {
			gen[3] -= 1;
			if (val < 0) {
				int temp = -val;
				temp = temp / numArr[depth];
				temp = -temp;
				DFS(temp, depth+1);
			}
			else {
				DFS(val/numArr[depth], depth+1);
			}
			gen[3] += 1;
		}
		
		
	}
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		numArr = new int [N];
		gen = new int[4];
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		for (int i = 0; i < N; i++) {
			numArr[i] = Integer.parseInt(st.nextToken());
		}
		StringTokenizer st2 = new StringTokenizer(br.readLine()," ");
		for (int i = 0; i < 4; i++) {
			gen[i]= Integer.parseInt(st2.nextToken()); 
		}
		DFS(numArr[0], 1);
		System.out.println(max);
		System.out.println(min);
		
		
		
	}
		
}