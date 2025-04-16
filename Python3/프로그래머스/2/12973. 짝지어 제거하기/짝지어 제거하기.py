def solution(s):
    idx = 0
    st = []
    
    while idx < len(s):    
        st.append(s[idx])
        
        if len(st) >= 2 and st[-1] == st[-2]:
            st.pop()
            st.pop()
            
        idx += 1
    if st:
        return 0
    return 1