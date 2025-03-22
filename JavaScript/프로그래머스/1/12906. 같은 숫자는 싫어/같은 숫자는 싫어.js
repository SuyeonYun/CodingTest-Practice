function solution(arr)
{
    var answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == answer[answer.length - 1]) continue;
        answer.push(arr[i])
    }
    
    return answer;
}