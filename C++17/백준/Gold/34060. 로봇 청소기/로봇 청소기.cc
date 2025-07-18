#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <utility>

using namespace std;

struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<long long>()(((long long)p.first << 32) | (unsigned int)p.second);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int x = 0, prev_y = 0;
    vector<pair<int, int>> dirty;

    for (int i = 0; i < n; ++i) {
        int cur_y;
        cin >> cur_y;
        if (prev_y >= cur_y) {
            ++x;
        }
        dirty.emplace_back(x, cur_y - 1);
        prev_y = cur_y;
    }

    int answer = 0;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    unordered_set<pair<int, int>, pair_hash> remain(dirty.begin(), dirty.end());
    queue<pair<int, int>> q;

    while (!remain.empty()) {
        auto start = *remain.begin();
        q.push(start);
        ++answer;

        while (!q.empty()) {
            auto [cx, cy] = q.front();
            q.pop();

            if (remain.find({cx, cy}) == remain.end()) continue;
            remain.erase({cx, cy});

            for (int i = 0; i < 4; ++i) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx >= 0 && ny >= 0 && remain.find({nx, ny}) != remain.end()) {
                    q.emplace(nx, ny);
                }
            }
        }
    }

    cout << answer << '\n';
    cout << n << '\n';

    return 0;
}
