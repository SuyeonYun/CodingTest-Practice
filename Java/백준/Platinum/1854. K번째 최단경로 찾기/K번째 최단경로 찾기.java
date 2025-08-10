import java.io.*;
import java.util.*;

class Node {
	int idx, weight;
	public Node(int idx, int weight) {
		this.idx = idx;
		this.weight = weight;
	}
}

class NodeComparator implements Comparator<Node> {

	@Override
	public int compare(Node arg0, Node arg1) {
		return arg0.weight - arg1.weight;
	}
	
}

public class Main {
	
	static int start = 1;
	static List<List<Node>> alist = new ArrayList<>();
	static PriorityQueue<Node> pq = new PriorityQueue<>(1, new NodeComparator());
	static List<PriorityQueue<Integer>> dist = new ArrayList<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		for (int i=0; i<n+1; i++) {
			alist.add(new ArrayList<Node>());
			dist.add(new PriorityQueue<Integer>(Collections.reverseOrder()));
		}
		
		dist.get(start).add(0);
		
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			
			alist.get(a).add(new Node(b, c));
		}
		
		pq.add(new Node(start, 0));
		
		while(!pq.isEmpty()) {
			
			//다익스트라 시작
			Node cur = pq.poll();
			for (int i=0; i<alist.get(cur.idx).size(); i++) {
				Node next = alist.get(cur.idx).get(i);
				int nextWeight = cur.weight + next.weight;
				if (dist.get(next.idx).size() < k) {
					dist.get(next.idx).add(nextWeight);
					pq.add(new Node(next.idx, nextWeight));
				}
				else {
					if (dist.get(next.idx).peek() > nextWeight) {
						dist.get(next.idx).poll();
						dist.get(next.idx).add(nextWeight);
						pq.add(new Node(next.idx, nextWeight));
					}
				}
			}
		}
		
		String result;
		for (int i=1; i<n+1; i++) {
			if (dist.get(i).size() < k) result = "-1\n";
			else result = String.valueOf(dist.get(i).peek()) + "\n";
			bw.write(result);
		}

		
		bw.flush();
	}
}