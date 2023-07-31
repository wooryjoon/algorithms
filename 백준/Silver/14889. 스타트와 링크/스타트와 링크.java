import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

// 재귀함수를 활용한 완전탐색
public class Main {
	// 조합으로 N개중 N/2 개를 뽑고, 차집합도 구해준다
	// 각각 구한 집합에서 2개를 조합으로 뽑아 score를 구해주고 최소 diff를 갱신해준다.
	public static int N;
	public static int [][] board;
	public static int ans = Integer.MAX_VALUE;
	public static int score(HashSet<Integer> set) {
		int num = 0;
		Integer[] arr = set.toArray(new Integer[N/2]);
		for (int i = 0; i < N/2; i++) {
			for (int j = i+1; j < N/2; j++) {
				num += board[arr[i]][arr[j]];
				num += board[arr[j]][arr[i]];
			}
		}
		return num;
	}
	public static void permutation (int depth,HashSet<Integer> set,int startIdx,ArrayList<Integer> temp) {
		if (depth == N / 2) {
			// N/2명을 다 뽑음
			
			HashSet<Integer> rest = new HashSet<Integer>(temp);
			rest.removeAll(set);
			int setScore = score(set);
			int restScore = score(rest);
			ans = Math.min(ans, Math.abs(setScore-restScore));
			return;
		}
		for (int i = startIdx; i < N; i++) {
				set.add(i);
				permutation(depth+1, set,i+1,temp);
				set.remove(i);
		}
	}
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[N][N];
		ArrayList<Integer> temp = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			temp.add(i);
			for (int j = 0; j < N; j++) {
				board[i][j]= Integer.parseInt(st.nextToken()); 
			}
		}
		
		permutation(0,new HashSet<Integer>(),0,temp);
		System.out.println(ans);
	}
		
}
		