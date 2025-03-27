function solution(participant, completion){
    const match = new Map();
    
    for (let i=0; i<participant.length; i++) {
        p = participant[i];
        c = completion[i];
        
        match.set(p, (match.get(p) || 0) +1);
        match.set(c, (match.get(c) || 0) -1);
    }
    
    for (let [k,v] of match) {
        if (v > 0) return k;
    }
}