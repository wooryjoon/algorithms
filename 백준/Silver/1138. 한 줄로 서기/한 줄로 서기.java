import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        String[] ans = new String[N];
        for (int i = 0; i < N; i++){
            int cnt = -1;
            // ans배열 돌면서 cnt 체크
            for (int j = 0; j < N; j++){
                if (ans[j] == null) cnt ++;
                if (cnt == Integer.parseInt(arr[i])){
                    // 자리 찾음
                    ans[j] = String.valueOf(i+1);
                    break;
                }
            }
        }
        for (String e : ans){
            System.out.print(e+" ");
        }
    }
}
