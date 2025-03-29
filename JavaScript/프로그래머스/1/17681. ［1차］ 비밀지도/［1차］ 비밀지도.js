function solution(n, arr1, arr2) {
    var answer = [];
    var temp = [];

    for (let i=0; i<n; i++) {
        temp.push((arr1[i] | arr2[i]).toString(2).padStart(n, "0")); 
    }
    
    for (let j=0; j<n; j++) {
        answer[j] = "";
        for (let m=0; m<n; m++) {
            if (temp[j][m] == "1") answer[j] += "#";
            if (temp[j][m] == "0") answer[j] += " ";
        }
    }
    return answer;
}