function solution(a, b) {
    var ans = 0;
    for (let i=0; i<a.length; i++) {
        ans += a[i] * b[i];
    }
    return ans;
}