function solution(s) {
    var temp = [];
    for (let str of s.split(" ")) temp.push(str.length >= 1 ? `${str[0].toUpperCase()}${str.slice(1).toLowerCase()}` : str)
    return temp.join(" ");
}