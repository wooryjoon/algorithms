import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static int N;
    public static int K;
    public static int[][] visited = new int[2][500001];
    public static int ans = 0;
    public static int BFS(){
        Queue<Integer> q = new LinkedList<>();
        q.add(N); // 최초 위치 큐에 넣기
        int time = 0;
        int bro = K;
        while (!q.isEmpty()){
            int len = q.size();
            time ++;
            int flag = time % 2;
            for (int i = 0; i < len; i++){
                int currN = q.poll();

                if (currN -1 >= 0 && visited[flag][currN-1] == -1) {
                    q.add(currN-1);
                    visited[flag][currN-1] = time; // nextN에 도달한 최소 시간
                }
                if (currN + 1 <= 500000 && visited[flag][currN+1] == -1) {
                    q.add(currN+1);
                    visited[flag][currN+1] = time; // nextN에 도달한 최소 시간
                }
                if (currN * 2 <= 500000 && visited[flag][currN*2] == -1) {
                    q.add(currN*2);
                    visited[flag][currN*2] = time; // nextN에 도달한 최소 시간
                }

            }
            bro += time;

            if (bro > 500000) break;
            // 동생의 flag턴 위치에 형이 이미 방문 찍어놨다면
            if (visited[flag][bro] != -1) return time;
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        Arrays.fill(visited[0],-1);
        Arrays.fill(visited[1],-1);

        visited[0][N] = 1; // 최초 위치 짝수턴 방문 처리

        ans = (N == K ? 0 : BFS());
        System.out.println(ans);
            }

    }
