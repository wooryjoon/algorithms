import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 * 시뮬레이션
 * 
 * 101 * 101 배열 , rowNum, colNum, time, sortList
 * 
 * 
 *
 */
public class Main {
	static int[][] board;
	static int[] cnt;
	static int rowNum = 3;
	static int colNum = 3;
	static int time = 0;
	static ArrayList<int[]> sortList;
	static StringTokenizer st;
	
	static int r;
	static int c;
	static int k;

	public static void main(String[] args) throws Exception {
		// ************************입력*************************************
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine()," ");
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		board = new int[101][101];
		
		
		for (int i = 0; i < 3; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for (int j = 0; j < 3; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		//***************************구현부**********************************
		
		while (true) {
			// 초기화 필요
			if (board[r-1][c-1] == k) break;
			if (time > 100) {
				time = -1;
				break;
			}
			// R연산  vs C연산
			if (rowNum >= colNum) {
				int max = 0;
				// 행 정렬 (값,등장 횟수)    정렬 조건 : 등장 횟수 오름차순, 값 오름차순
				int[][] temp = new int[101][101];
				for (int i = 0; i < rowNum; i++) {
					sortList = new ArrayList<int[]>();
					cnt = new int[101];
					
					for (int j = 0; j < colNum; j++) {
						if (board[i][j] == 0) continue;
						cnt[board[i][j]] ++;
					}
					
					for (int k = 1; k < cnt.length; k++) {
						if (cnt[k] > 0) {
							int[] tempArr = {k,cnt[k]};
							sortList.add(tempArr);
						}
					}
					// 정렬
					Collections.sort(sortList,(o1, o2) -> {
						// 등장 횟수 오름차순 정렬
						if (o1[1] == o2[1]) {
							return o1[0] - o2[0];
						}
						return o1[1] - o2[1];
					});
					
					// 정렬된 list 값 순서대로 임시 board에 넣기
					int k = 0;
					for (int l = 0; l < sortList.size(); l++) {
						int[] arr = sortList.get(l);
						temp[i][k++] = arr[0];
						temp[i][k++] = arr[1];
					}
					// 행 1 추가
					max =  Math.max(max,sortList.size() * 2);
				}
				colNum = Math.min(max, 100);
				board = temp;
			}
			else  {

				int[][] temp = new int[101][101];
				int max = 0;
				for (int i = 0; i < colNum; i++) {
					sortList = new ArrayList<int[]>();
					cnt = new int[101];
					
					for (int j = 0; j < rowNum; j++) {
						if (board[j][i] == 0) continue;
						cnt[board[j][i]] ++;
					}
					
					for (int k = 1; k < cnt.length; k++) {
						if (cnt[k] > 0) {
							int[] tempArr = {k,cnt[k]};
							sortList.add(tempArr);
						}
					}
					// 정렬
					Collections.sort(sortList,(o1, o2) -> {
						// 등장 횟수 오름차순 정렬
						if (o1[1] == o2[1]) {
							return o1[0] - o2[0];
						}
						return o1[1] - o2[1];
					});
					// 정렬된 list 값 순서대로 임시 board에 넣기
					int k = 0;
					for (int l = 0; l < sortList.size(); l++) {
						int[] arr = sortList.get(l);
						temp[k][i] = arr[0];
						temp[k+1][i] = arr[1];
						k += 2;
					}
					// 행 1 추가
					max =  Math.max(max,sortList.size() * 2);
				}
				board = temp;
				rowNum = Math.min(max, 100);
			}
			
			time ++;
		}
		System.out.println(time);
	}

}