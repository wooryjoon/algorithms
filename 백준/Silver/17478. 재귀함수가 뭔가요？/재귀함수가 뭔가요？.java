import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static int N;
    public static int M;
    public static int[][] board;
    public static int x;
    public static int y;
    public static int[] dx =  {-1,0,1,0};
    public static int[] dy =  {0,1,0,-1};
    public static int currdir;
    public static int cnt;
    public static int K;
    // 상 우 하 좌
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        K = Integer.parseInt(br.readLine());


        System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
        DFS(0);


    }
    public static void print1(int depth) {
        if (depth >= K) return;
        StringBuilder strs = new StringBuilder();
        for (int i = 0; i < depth; i++){
            strs.append("____");
        }
        System.out.println(strs + "\"재귀함수가 뭔가요?\"");
        System.out.println(strs + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
        System.out.println(strs+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
        System.out.println(strs+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
        print1(depth+1);
    }
    public static void print2 (int depth) {
        if (depth < 0) return;
        StringBuilder strs = new StringBuilder();
        for (int i = 0; i < depth; i++){
            strs.append("____");
        }
        System.out.println(strs + "라고 답변하였지.");
        print2(depth-1);
    }

    public static void DFS(int depth) {
        StringBuilder strs = new StringBuilder();
        for (int i = 0; i < K; i++){
            strs.append("____");
        }
        print1(depth);
        System.out.println(strs + "\"재귀함수가 뭔가요?\"");
        System.out.println(strs + "\"재귀함수는 자기 자신을 호출하는 함수라네\"");
        print2(K-depth);
    }

}


