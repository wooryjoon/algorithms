import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	public static int N;
	public static int M;
	public static int[][] board;
	public static StringTokenizer st;
	public static ArrayList<int[]> chickens;
	public static ArrayList<int[]> currChicken;
	public static ArrayList<int[]> homes;
	public static int min = Integer.MAX_VALUE;
	public static int[][] visited;
	public static int[] dx;
	public static int[] dy;
	//  BOJ 15686 치킨거리
	// 조합으로 치킨 위치 잡고, 잡은 상태에서 BFS로 치킨 거리 구해서 sum 도출
	public static void main(String[] args) throws IOException {
		// Input Parsing
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][N];
		chickens = new ArrayList<int[]>();
		currChicken =  new ArrayList<int[]>();
		homes = new ArrayList<int[]>();
		dx = new int[] {0,0,1,-1};
		dy = new int[] {1,-1,0,0};
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				int[] temp = {i,j};
				if (board[i][j] == 2) chickens.add(temp);
				if (board[i][j] == 1) homes.add(temp);
			}
		}
		// BFS in Combinations
		DFS(0,0);
		System.out.println(min);
	}
	public static void DFS(int depth,int start) {
		if (depth == M) {
			min = Math.min(minDist(), min);
			return;
		}
		
		for (int i = start; i < chickens.size(); i++) {
			int[] temp = chickens.get(i);
			currChicken.add(temp);
			DFS(depth+1,i+1);
			currChicken.remove(currChicken.size()-1);
		}

	}
	public static int minDist() {
		int sumDist = 0;
		for (int[] home : homes) {
			int x = home[0];
			int y = home[1];
			int currMin = Integer.MAX_VALUE;
			for (int[] chicken : currChicken) {
				int cx = chicken[0];
				int cy = chicken[1];
				int currDist = Math.abs(x-cx) + Math.abs(y-cy);
				currMin = Math.min(currMin,currDist);
			}
			sumDist += currMin;
		}
		return sumDist;
	}
	}
