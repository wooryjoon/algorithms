
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
/**
 * 9명으로 이루어진 두 팀
 * 4번 타자는 1번 선수로 고정
 * x번 선수의 매 이닝 타점을 배열로 저장. score[x] = [1,23,,1,23,1,]
 * 순열DFS로 선수 배치 완탐.
 * 선수 배치가 완료되면 score계산
 * 타순을 배치할 때 특정 이닝에 최소한 아웃이 한명은 있어야함.
 * @author SSAFY
 *
 */
public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int[][] hit; // score[x][y] = x번 선수의 y이닝 타점 
	static int[] visited;
	static ArrayList<Integer> orderList;
	static int ans = Integer.MIN_VALUE;
	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		hit = new int[N+1][10];
		visited = new int[10];
		orderList = new ArrayList<Integer>();
		orderList.add(-1);
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			hit[i][0] = -1;
			for (int j = 1; j <= 9; j++) {
				hit[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// DFS로 타자 순서 배치 시작 -> 1번 선수부터 9번 선수까지 
		DFS(1);
		System.out.println(ans);
	}
	public static void DFS(int depth) {
		// 4번째 칸은 1번 선수를 넣고 다시 DFS
		if (depth == 4) {
			orderList.add(1);
			visited[1] = 1;
			DFS(depth+1);
			orderList.remove(orderList.size()-1);
		}
		if (depth == 10) {
			int scores = makeScore();
			ans = Math.max(ans, scores);
		}
		for (int i = 2; i <= 9; i++) {
			if (visited[i] == 1) continue;
			visited[i] = 1;
			orderList.add(i);
			DFS(depth+1);
			orderList.remove(orderList.size()-1);
			visited[i] = 0;
		}
	}
	public static int makeScore() {
		int scores = 0;
		// 최초 1번 타자부터 시작
		int currOrder = 1;
		// N이닝동안 반복
		for (int inning = 1; inning <= N; inning ++) {
			int out = 0;
			// 현재 이닝의 아웃을 기록하는 타자가 한명도 없으면 이 순서는 x
			boolean flag = false;
			for (int e : hit[inning]) {
				if (e == 0) {
					flag = true;
					break;
				}
			}
			if (!flag) return -1;
			
			int[] onGround = new int[3];
			// 3아웃 될 동안 반복
			while (out < 3) {
				int currPlayer = orderList.get((currOrder));
				int currHit = hit[inning][currPlayer];
				if (currHit == 0) {
					out ++;
					currOrder ++;
					if (currOrder == 10) currOrder = 1;
					continue;
				}
				else scores += run(currHit,onGround);
				currOrder ++;
				if (currOrder == 10) currOrder = 1;
			}
		}
		return scores;
	}
	public static int run(int currHit, int[] onGround) {
		int scores = 0;
		// 기존 주자 점수 내기
		for (int i = 2; i >= 0; i--) {
			if (onGround[i] == 1) {
				if (i + currHit > 2) scores ++;
				else onGround[i+currHit] = onGround[i];
				onGround[i] = 0;
			}
		}
		if (currHit < 4) onGround[currHit-1] = 1;
		else scores ++;
		return scores;
	}

}
