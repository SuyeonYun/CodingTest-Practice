function solution(strings, n) {
    var answer = [];
    strings.sort(function (a, b) {
        if (a[n] == b[n]) return a.localeCompare(b);
        return a[n].localeCompare(b[n]);
    });
    return strings;
}