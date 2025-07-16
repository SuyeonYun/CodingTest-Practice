#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int l;
    cin >> l;

    vector<long long> d(l);
    for (int i = 0; i < l; ++i) {
        cin >> d[i];
    }

    int n;
    cin >> n;

    for (int t = 0; t < n; ++t) {
        int type;
        cin >> type;

        if (type == 1) {
            int idx;
            long long noise;
            cin >> idx >> noise;
            --idx; // 0-indexed

            int i = idx;
            long long left = noise;
            while (i >= 0 && left > 0) {
                long long absorb = min(d[i], left);
                d[i] += absorb;
                left -= absorb;
                if (absorb == 0) break;
                --i;
            }

            i = idx + 1;
            long long right = noise;
            while (i < l && right > 0) {
                long long absorb = min(d[i], right);
                d[i] += absorb;
                right -= absorb;
                if (absorb == 0) break;
                ++i;
            }
        } else {
            int idx;
            cin >> idx;
            cout << d[idx - 1] << '\n';
        }
    }

    return 0;
}
