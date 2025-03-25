function solution(ingredient) {
    var cnt = 0;
    const hamburger = [1,2,3,1];
    var stack = [];
    for (let i=0; i < ingredient.length; i++) {
        stack.push(ingredient[i]);
        let j = stack.length - 1;
        if (JSON.stringify(stack.slice(j-3, j+1)) === JSON.stringify(hamburger)) {
            cnt +=1;
            stack.splice(-4);
        }
    }
    return cnt;
}