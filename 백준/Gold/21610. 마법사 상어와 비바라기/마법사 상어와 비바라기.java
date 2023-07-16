import com.sun.security.jgss.GSSUtil;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str," ");
         int N = Integer.parseInt(st.nextToken());
         int M = Integer.parseInt(st.nextToken());
         int [][] board = new int[N][N];
         int [][] move = new int[M][2];
         boolean[][] visit = new boolean[N][N];
        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine()," ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine()," ");
            for (int j = 0; j < 2; j++){
                move[i][j] = Integer.parseInt(st.nextToken());
            }
        }





        ArrayList<int[]> clouds = new ArrayList<>();
        int[] dx = {0,0,-1,-1,-1,0,1,1,1};
        int[] dy = {0,-1,-1,0,1,1,1,0,-1};
        int[][] init = {{N-1,0},{N-1,1},{N-2,0},{N-2,1}};
        // 비바라기 시전
        for(int[] e : init) {
            clouds.add(e);
        }
        // M번의 이동 시작
        for (int i = 0; i < M; i++) {
            int[] currMove = move[i];
            // 현재 명령의 방향과 속도 설정
            int d = currMove[0];
            int s = currMove[1];
            // 구름 이동 -> 모든 구름이 d방향으로 s칸 만큼 이동 + 비내리기
            for (int j = 0; j < clouds.size(); j++) {
                int[] arr = clouds.get(j);
                int nx = (arr[0] + dx[d] * (s%N));
                int ny = (arr[1] + dy[d] * (s%N));
                if (nx >= 0) nx = nx % N;
                else if (nx < 0) nx = N + nx;
                if (ny >= 0) ny = ny % N;
                else if (ny < 0) ny = N + ny;
                board[nx][ny] += 1;
                int[] temp = {nx,ny}; // 구름이 최종 이동한 위치
                clouds.set(j,temp);
                visit[nx][ny] = true;

            }
            ArrayList<int[]> newClouds = new ArrayList<>();
            ArrayList<String> newRemember = new ArrayList<>();
            // 물복사버그
            for (int j = 0; j < clouds.size(); j++) {
                int[] arr = {2,4,6,8};
                int x = clouds.get(j)[0];
                int y = clouds.get(j)[1];
                int cnt = 0;
                for (int dir : arr) { // 대각선 4방향 체크
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];
                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                    if (board[nx][ny] >= 1) cnt ++;
                }
                board[x][y] += cnt;
            }

            // 물의 양이 2 이상인 칸에 구름 생성, 물 양 - 2 이때, 원래 구름이 있던 곳은 안돼!
            for (int x = 0; x < N; x++) {
                for (int y = 0; y < N; y++) {
                    int[] arr = {x,y};
                    if (board[x][y] >= 2 && !visit[x][y]) {
                        board[x][y] -= 2;
                        newClouds.add(arr);
                        newRemember.add(Arrays.toString(arr));
                    }

                }
            }

            clouds = newClouds;
            visit = new boolean[N][N];


        }
        // M번 이동 종료 후 물의 양 합 구하기
        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans += board[i][j];
            }
        }

        System.out.println(ans);
    }
}
