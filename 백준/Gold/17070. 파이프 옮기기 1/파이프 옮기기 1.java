import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 각 칸의 타입 : 1. 가로 2. 세로 3. 대각선
 * 각 칸의 타입에 따라서 가능한 탐색 방향이 다르다.
 * 가능한 모든 루트로 도착점에 도달하는 모든 경우의 수 구하기
 * DFS or BFS -> 더 직관적인 DFS 선택
 * 각 칸의 타입에 따라 DFS 함수 실행
 * 도착점에 도달하는 경우 cnt ++
 */
public class Main {
    static int N;
    static int[][] board;
    static BufferedReader br;
    static StringTokenizer st;
    static int answer;

    public static void main(String[] args) throws Exception {
        //***************************************INPUT**********************
        br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //*********************************************구현부*****************
        DFS(1,0,1);
        System.out.println(answer);
    }
    public static void DFS(int type, int x, int y){
        if (x == N - 1 && y == N - 1) {
            answer ++;
            return;
        }
        // 가로인 경우
        int nx = x;
        int ny = y;
        if (type == 1){
            check_dgs(x,y);
            check_garo(x,y);
        }
        // 세로인 경우
        if (type == 2){
        check_sero(x,y);
        check_dgs(x,y);
        }
        // 대각선인 경우
        if (type == 3){
            check_sero(x,y);
            check_dgs(x,y);
            check_garo(x,y);
        }
    }
    public static void check_garo(int x, int y){
        if (x <= N-1 && y+1 <= N-1 && board[x][y+1] == 0) DFS(1, x, y+1);
    }
    public static void check_sero(int x, int y){
        if (x+1 <= N-1 && y <= N-1 && board[x+1][y] == 0)
        DFS(2, x+1, y);
    }
    public static void check_dgs(int x, int y){
        if (x+1 <= N-1 && y+1 <= N-1 && (board[x+1][y] + board[x][y+1] + board[x+1][y+1] == 0)) DFS(3, x+1, y+1);
    }


}