import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

/**
 * 아이디어
 * while 낚시왕이 끝 열까지
 *  해당 열에서 가장 가까운 상어를 잡고 ans += z
 *  board를 2중 포문으로 순회하며 상어를 회수하고 board 청소
 *  sharks에 상어 정보를 담고, 다 담았으면 sharks를 순회하며 이동 시작
 *  s를 압축해주고, 남은 s만큼 이동.
 *  d == 1 or 2 : 상하로 이동하는 상어 -> nx가 0 이거나 R-1에 도달하면 방향 전환
 *  d == 3 or 4 : 좌우로 이동하는 상어 -> ny가 0 이거나 C-1에 도달하면 방향 전환
 *  그렇게 s동안 모두 이동하고, 최종 위치에 도달
 *  최종 위치가 빈칸이면 그대로 넣고, 뭔가 들어있으면 들어있는 z랑 들어갈 z 비교해서 체인지
 *  모든 상어의 최종 위치가 결정되는 king 위치를 다시 이동 시킨다.
 *
 *  필요 변수
 *  정답변수 ans, 상어 정보 담는 sharks, 상어를 저장할 3차원 배열
 *
 *  필요 함수
 *  상어 잡는 함수
 *  상어 움직이는 함수
 */
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static int[][][] board;
    static boolean[][] sharkBoard;
    static int ans;
    static Stack<int[]> sharkStack;
    static int R;
    static int C;
    static int M;
    static int[] dx = {0,-1,1,0,0};
    static int[] dy = {0,0,0,1,-1};

    public static void main(String[] args) throws Exception {
        int T = 1;
        for (int tc = 1; tc <= T; tc ++){
            ans = 0;
            run();
            System.out.println(ans);
        }
    }
    public static void run () throws Exception {
        // 입력 받기
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        // 행 길이
        R = Integer.parseInt(st.nextToken());
        // 열 길이
        C = Integer.parseInt(st.nextToken());
        // 상어 수
        M = Integer.parseInt(st.nextToken());
        // board 초기화
        board = new int[R][C][3];
        sharkBoard = new boolean[R][C];
        ans = 0;
        sharkStack = new Stack<>();
        // M번만큼 돌며 board에 상어 넣기
        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            // r : 행 c : 열 s : 속력 d : 방향 z : 크기
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            if (d <= 2) s = s % ((R-1) * 2);
            else if (d >= 3) s = s % ((C-1) * 2);

            board[r-1][c-1] = new int[] {s,d,z};
            sharkBoard[r-1][c-1] = true;
        }
        //*******************************구현부****************************
        //  * while 낚시왕이 끝 열까지
        int man = 0;
        while (man != C){
            // 현재 열에서 가장 가까운 상어 찾아서 죽이는 함수
            findCloseShark(man);
            // board의 상어 정보를 shark에 넣으며 board를 비우는 함수
            cleanBoard_makeSharkStack();
            // 상어를 움직이는 함수
            moveShark(sharkStack);
            man ++;
        }
    }
    public static void findCloseShark(int currY){
        // 열 고정한채로 행을 내려가며 상어 찾기
        for (int i = 0; i < R; i++){
            // 상어를 발견하면?
            if (sharkBoard[i][currY]) {
                ans += board[i][currY][2];
                board[i][currY] = null;
                sharkBoard[i][currY] = false;
                break;
            }
        }
    }
    public static void cleanBoard_makeSharkStack(){
        // board를 2중 포문으로 돌면서 board 수거하고, sharkBoard도 수거
        // 스택 만들기
        // 이중 포문 시작
        for (int i = 0; i < R; i++){
            for (int j = 0; j < C; j++){
                if (sharkBoard[i][j]){
                    sharkBoard[i][j] = false;
                    int s = board[i][j][0];
                    int d = board[i][j][1];
                    int z = board[i][j][2];
                    int [] temp = {i,j,s,d,z};
                    sharkStack.push(temp);
                    board[i][j] = null;
                }
            }
        }
    }
    public static void moveShark(Stack<int[]> sharkStack) {
        // 스택을 비우면서 상어 이동시키기
        while (!sharkStack.isEmpty()) {
            int[] currShark = sharkStack.pop();
            int x = currShark[0];
            int y = currShark[1];
            int s = currShark[2];
            int d = currShark[3];
            int z = currShark[4];
            // 상어의 정보를 바탕으로 이동 시작
            // 1초동안 s만큼 움직이므로
            int ns = s;
            // 최초 위치에서 벽을 향해 있는 경우
            if (x + dx[d] < 0 || x + dx[d] >= R || y + dy[d] < 0 ||
            y + dy[d] >= C){
                if (d <= 2 && (x == 0 || x == R - 1)) {
                    if (d == 2) d = 1;
                    else d = 2;
                }
                // d가 1,2일때는 y가 0이거나 C-1일때
                if (d >= 3 && (y == 0 || y == C - 1)) {
                    if (d == 3) d = 4;
                    else d = 3;
                }
            }
            while (ns > 0) {
                x += dx[d];
                y += dy[d];
                // 다음 칸이 테두리 칸이면 방향을 바꾼다.
                // d가 1,2일때는 x가 0이거나 R-1일때
                if (d <= 2 && (x == 0 || x == R - 1)) {
                    if (d == 2) d = 1;
                    else d = 2;
                }
                // d가 1,2일때는 y가 0이거나 C-1일때
                if (d >= 3 && (y == 0 || y == C - 1)) {
                    if (d == 3) d = 4;
                    else d = 3;
                }
                // 방향을 바꾸든 안바꾸든 뭐... 끝.
                ns--;

            }
            // 모든 이동이 종료된 후 최종 위치 파악
            // 상어가 있으면 크기 비교 후 넣기

            if (sharkBoard[x][y]) {
                int old_z = board[x][y][2];
                int new_z = z;
                if (new_z > old_z) board[x][y] = new int[]{s, d, z};
            }
            // 상어가 없으면 그대로 넣기
            else {
                board[x][y] = new int[]{s, d, z};
                sharkBoard[x][y] = true;
            }
        }
        // 모든 스택이 종료 -> 위치 변환 완료
    }
}
