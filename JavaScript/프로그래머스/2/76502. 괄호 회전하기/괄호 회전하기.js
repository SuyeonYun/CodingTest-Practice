function is_right(str, start_idx) {
    let stack = [];
    let cur, last;
    for (let i=start_idx; i<start_idx + str.length/2; i++) {
        cur = str[i];
        last = stack[stack.length - 1];
        if ((cur == ")" && last == "(")
           || (cur == "}" && last== "{")
           || (cur == "]" && last == "[")) {
            stack.pop();
            continue;
        }
        stack.push(str[i]);
        
        if (stack.length < 1) break;
    }
    if (stack.length == 0) return true;
    return false;
}

function solution(s) {
    var answer = 0;
    s += s;
    for (let i=0; i<s.length/2; i++) {
        if (is_right(s, i)) answer += 1;
    }
    return answer;
}