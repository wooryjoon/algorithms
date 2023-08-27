import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제 정리
 * 아기상어 4방향
 * 물고기가 자기보다 크기가 크면 못감
 * 크기가 같으면 지나가기만 가능
 * 크기가 작으면 잡아먹음
 *
 * BFS로 위쪽 - 왼쪽 을 우선으로 탐색.
 * 먹기 가능한 물고기를 발견하면 바로 먹고, x,y를 거기로 옮기고 사이즈 키우고 return true;
 * BFS 탐색을 해도 먹을 수 있는 물고기가 없으면 return false;
 *
 *
 * while true :
 *      // 물고기 못먹고 끝나면 바로 break
 *      if (!eatFish()) : break;
 *      // 물고기 먹었으면 size와 물고기위치 업데이트됨.
 *      time ++;
 *      //
 * def eatFish:
 *      큐에 x,y담기
 *      위쪽-왼쪽 순서로 탐색 시작
 *      만약 범위 내에 있고,
 *      자기보다 몸집이 작은 물고기면 먹고 return
 *      if board[i][j] == size : 큐에 담아서 ㄱㄱ
 *
 *      while문 끝날떄까지 리턴 안되면 return false;
 *
 * 필요변수
 * 정답 time, 물고기 정보 담는 2차원 board, BFS 함수
 * */

class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static int N;
    static int[][] board;
    static int time;
    static int size;
    static int[] dx = {0,0,1,-1};
    static int[] dy = {1,-1,0,0
    };
    static int startX = 0;
    static int startY = 0;
    static int eatedFish = 0;
    static ArrayList<int[]> cand;
    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        int T = 1;
        for (int tc = 1; tc <= T; tc++){
            run();
        }
    }
    public static void run () throws Exception {
        N = Integer.parseInt(br.readLine());
        time = 0;
        board = new int[N][N];
        size = 2;
        startX = 0;
        startY = 0;
        eatedFish = 0;

        // board 채우기
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 9){
                    startX = i;
                    startY = j;
                    board[i][j] = 0;
                }
            }
        }
        // 입력 완료 구현 시작

        while (true){
            // 현재 BFS에서 후보군을 담을 cand 배열리스트 생성
            cand = new ArrayList<>();
            eatFish(startX,startY);
            // cand가 비어있으면 먹을게 없는것.
            if (cand.size() == 0) break;
            // cand가 안 비어있다면 정렬후 0번째 원소만 뽑아내기
            Collections.sort(cand,(o1, o2)->{
                // 거리가 같으면
                if (o1[0] == o2[0]){
                    // x행이 같으면
                    if (o1[1] == o2[1]) return o1[2]-o2[2];
                    // x행이 다르면 x행 기준 정렬
                    else return o1[1]-o2[1];
                }
                // 거리가 다르면
                else return o1[0]-o2[0];
            });
            // 먹기
            int[] select = cand.get(0);
            int dist = select[0], x = select[1], y = select[2];
            board[x][y] = 0;
            // 현재까지 먹은 물고기 개수가 size와 같다면 사이즈 키우기
            eatedFish ++;
            if (eatedFish == size){
                size ++;
                eatedFish = 0;
            }
            startX = x;
            startY = y;
            time += dist;

        }
        System.out.println(time);
    }
    public static void eatFish(int i, int j){
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{i,j,0});
        int[][] visited = new int[N][N];
        visited[i][j] = 1;
        int currMaxDist = Integer.MAX_VALUE;
        while (!q.isEmpty()){
            int[] curr = q.removeFirst();

            int x = curr[0];
            int y = curr[1];
            int dist = curr[2];

            // 거리를 벗어나는 애들은 안보기.
            if (dist >= currMaxDist) continue;

            for (int d = 0; d < 4; d++){
                int nx = x + dx[d];
                int ny = y + dy[d];
                // 범위 내, 방문 안함
                if (nx >= 0 && nx < N && ny >= 0 && ny< N && visited[nx][ny] == 0){
                    // 다음 칸이 자기보다 몸집이 작은 물고기
                    if (board[nx][ny] <= 6 && board[nx][ny] >= 1 && board[nx][ny] < size){
                        // 후보리스트에 담고 방문 처리
                        cand.add(new int[]{dist+1,nx,ny});
                        visited[nx][ny] = 1;
                        currMaxDist = dist + 1;
                    }
                    // 다음칸이 빈칸이거나 몸집이 같은 경우
                   else  if (board[nx][ny] == 0 || board[nx][ny] == size){
                        // 방문 처리
                        visited[nx][ny] = 1;
                        q.add(new int[]{nx,ny,dist+1});
                    }
                }
            }
        }
    }


}