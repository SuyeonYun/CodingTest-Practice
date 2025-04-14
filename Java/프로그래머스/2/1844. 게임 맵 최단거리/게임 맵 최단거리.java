import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1}); // x, y, distance

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0], y = cur[1], dist = cur[2];

            if (x == n - 1 && y == m - 1) return dist;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1) {
                    maps[nx][ny] = 0; // 방문 처리
                    queue.add(new int[]{nx, ny, dist + 1});
                }
            }
        }

        return -1;
    }
}
