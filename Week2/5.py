N = int(input())           
letters = "ABCEHKMOPTXY"       
for _ in range(N):
    p = input()            
    if len(p) == 6 and p[0] in letters and p[1:4].isdigit() and p[4] in letters and p[5] in letters:
        print("Yes")
    else:
        print("No")
