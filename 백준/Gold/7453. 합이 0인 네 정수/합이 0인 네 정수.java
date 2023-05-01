import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static long ans;
	static int[] A, B, C, D;
	static int[] AB, CD;
	static int index;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());

		A = new int[N];
		B = new int[N];
		C = new int[N];
		D = new int[N];
		AB = new int[N * N];
		CD = new int[N * N];
		ans = 0;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			A[i] = Integer.parseInt(st.nextToken());
			B[i] = Integer.parseInt(st.nextToken());
			C[i] = Integer.parseInt(st.nextToken());
			D[i] = Integer.parseInt(st.nextToken());
		}

		index = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				AB[index] = A[i] + B[j];
				CD[index] = C[i] + D[j];
				index++;
			}
		}

		Arrays.sort(AB);
		Arrays.sort(CD);

		System.out.println(twopointer());
	}

	private static long twopointer() {

		int pl = 0; 
		int pr = CD.length - 1;
		long cnt = 0;

		while (pl < N * N && pr >= 0) {

			long lVal = AB[pl];
			long rVal = CD[pr];
			long lCnt = 0;
			long rCnt = 0;

			if (lVal + rVal == 0) {

				while (pl < AB.length && AB[pl] == lVal) {
					lCnt++;
					pl++;
				}

				while (pr >= 0 && CD[pr] == rVal) {
					rCnt++;
					pr--;
				}
				cnt += rCnt * lCnt;

			}
			else if (lVal + rVal < 0)
				pl++;
			else
				pr--; 

		}

		return cnt;
	}
}