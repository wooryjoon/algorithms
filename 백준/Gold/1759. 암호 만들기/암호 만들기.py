import sys
input = sys.stdin.readline

# 암호 : L개의 알파벳으로 구성
# 최소 조건 : 모음 1개 자음 2개
# 알파벳이 증가하는 순서로 배열
# C개의 알파벳을 조합해 길이가 L인 암호를 만든다.

L,C = list(map(int,input().split())) 
alphabets = list(input().strip().split())
alphabets.sort()
ans = []
vowel = set(['a','e','i','o','u'])
# DFS로 길이가L인 문자열을 만든다.
# 다만, 최소 조건을 만족하지 못하는 경우에는 pass

def isVowel (alpha) :
    if alpha in vowel:
        return True
    return False

def DFS(startIdx,depth,arr,vowels):
    if vowels >= L - 1 : return # 이미 모음이 L-1개가 차버려서, 자음 2개를 못 넣는 경우
    if depth == L and vowels : 
        ans.append(''.join(arr))
        return
    for i in range(startIdx,C):
        arr.append(alphabets[i])
        if isVowel(alphabets[i]): DFS(i+1,depth+1,arr,vowels+1)
        else : DFS(i+1,depth+1,arr,vowels)
        arr.pop()

DFS(0,0,[],0)
print('\n'.join(ans))
