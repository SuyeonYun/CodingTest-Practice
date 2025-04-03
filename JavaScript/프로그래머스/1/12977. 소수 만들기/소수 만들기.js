function is_prime(number) {
    if (number < 2) return false;
    if (number == 2) return true;
    for (let i=2; i<number; i++) {
        if (number % i == 0) return false;
    }
    return true;
}

function solution(nums) {
    var answer = 0;
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            for (let k=j+1; k<nums.length; k++) {
                if (is_prime(nums[i] + nums[j] + nums[k])) answer++;
            }
        }
    }
    return answer;
}