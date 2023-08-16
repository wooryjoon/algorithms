import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 맨 위 가스관은 맨 위 빵집에 되도록 연결해야한다.
// 최초에 가스관이 생성되면서 visit했던 곳은 그대로 놔둔다 왜?
    // 1. 어차피 동일한 빵집으로 연결
    // 2. 혹은 어차피 나가리 될 칸
class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static int R;
    static int C;
    static int ans;
    static char[][] board;
    static int[] dx;
    static int[][] visited;
    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        visited = new int[R][C];
        dx = new int[] {-1,0,1};
        for (int i = 0; i < R; i++){
            board[i] = br.readLine().toCharArray();
        }

        //*************************구현부***************************
        // 맨 윗 칸부터 재귀적으로 접근하며 끝열에 도달할 시 count ++
        for (int i = 0; i < R; i++){
            visited[i][0] = 1;
            if (DFS(i,0)) ans++;
        }
        System.out.println(ans);
    }
    public static boolean DFS(int x, int y){
        // 종료 조건 : 마지막 열에 도달
        if (y == C-1) {
            return true;
        }
        // 수행 연산
        for (int i = 0; i < 3; i++){
            int nx = x + dx[i];
            int ny = y + 1;
            if (nx >= 0 && nx < R && ny >= 0 && ny < C
            && visited[nx][ny] == 0 && board[nx][ny] == '.'){
                visited[nx][ny] = 1;
                if (DFS(nx,ny)) return true;
            }
        }
        return false;
    }


}