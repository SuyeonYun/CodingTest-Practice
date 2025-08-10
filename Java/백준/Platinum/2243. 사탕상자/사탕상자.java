import java.io.*;
import java.util.*;

public class Main {
	
	static int n;
	
	static long[] idxtree;
	
	public static long update(int idx, int data, int curIdx, int leftIdx, int rightIdx) {
		if (idx < leftIdx || idx > rightIdx) return idxtree[curIdx];
		if (leftIdx == rightIdx) return idxtree[curIdx] = (long) idxtree[curIdx] + data;
		
		int mid = (leftIdx + rightIdx) / 2;
		return idxtree[curIdx] = update(idx, data, curIdx*2, leftIdx, mid) + update(idx, data, curIdx*2+1, mid+1, rightIdx);
	}
	
	public static int pop(int rank, int curIdx, int leftIdx, int rightIdx) {
		if (leftIdx == rightIdx) return leftIdx;
		
		int mid = (leftIdx + rightIdx) / 2;
		if (idxtree[curIdx*2] >= rank) return pop(rank, curIdx*2, leftIdx, mid);
		else return pop(rank - (int) idxtree[curIdx * 2], curIdx*2+1, mid+1, rightIdx);
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		
		idxtree = new long[4000001];
		
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			if (a==1) {
				int result = pop( b, 1, 1, 1000000);
				update(result, -1, 1, 1, 1000000);
				bw.write(String.valueOf(result) + "\n");
			}
			
			else {
				int c = Integer.parseInt(st.nextToken());
				update(b, c, 1, 1, 1000000);
			}
		}
		
		bw.flush();
	}
}