class Solution {
    int answer = 0;

    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(0, k, dungeons, visited);
        return answer;
    }

    public void dfs(int depth, int fatigue, int[][] dungeons, boolean[] visited) {
        answer = Math.max(answer, depth);

        for (int i = 0; i < dungeons.length; i++) {
            int need = dungeons[i][0];
            int cost = dungeons[i][1];

            if (!visited[i] && fatigue >= need) {
                visited[i] = true;
                dfs(depth + 1, fatigue - cost, dungeons, visited);
                visited[i] = false;
            }
        }
    }
}
