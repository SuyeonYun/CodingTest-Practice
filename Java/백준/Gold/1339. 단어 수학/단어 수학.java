import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int idx = 9;
		long result = 0;
		
		List<Character> clist = new ArrayList<>();
		List<String> slist = new ArrayList<>();
		Map<Character, Integer> m = new HashMap<>();
		Map<Character, Integer> freq = new HashMap<>();
		
		for (int i=0; i<n; i++) {
			String s = br.readLine();
			slist.add(s);
			int len = s.length();
			
			for (int j=0; j<len; j++) {
				char ch = s.charAt(len - j  - 1);
				if (!freq.containsKey(ch)) {
					clist.add(ch);
				}
				freq.put(ch, freq.getOrDefault(ch, 0) + (int)Math.pow(10, j));
			}
		}
		
		clist.sort((a, b) -> freq.get(b) - freq.get(a));
		for (int i=0; i<clist.size(); i++) {
			char k = clist.get(i);
			m.put(k, idx--);
		}
		
		for (int i=0; i<slist.size(); i++) {
			int l = slist.get(i).length();
			for (int j=0; j<l; j++) {
				result += m.get(slist.get(i).charAt(j)) * (int)Math.pow(10, l - j  - 1);
			}
		}
		
		String answer = String.valueOf(result);
		bw.write(answer);
		bw.flush();
	}
}