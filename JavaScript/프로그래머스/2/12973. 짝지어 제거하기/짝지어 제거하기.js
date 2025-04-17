function solution(s)
{
    stack = [];
    idx = 0;
    
    while (idx < s.length) {
        stack.push(s[idx++]);
        l = stack.length;
        if (l >= 2 && stack[l - 1] == stack[l - 2]) {
            stack.pop();
            stack.pop();
        }
    }
    
    if (stack.length == 0) return 1;
    return 0;
}