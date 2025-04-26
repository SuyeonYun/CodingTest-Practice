function solution(numbers) {
    numbers.sort((a, b) => {
        const A = String(a).repeat(3);
        const B = String(b).repeat(3);
        return B.localeCompare(A);
    });
    const answer = numbers.join('');
    return answer[0] === '0' ? '0' : answer;
}
