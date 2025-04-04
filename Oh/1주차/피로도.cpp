#include <bits/stdc++.h>

using namespace std;

int answer = 0;
bool visited[8] = {0};

void dfs(int cnt, int k, vector<vector<int>> &dungeons){
    if(cnt > answer) answer = cnt;
    
    for(int i=0; i<dungeons.size(); i++){
        if(!visited[i] && k - dungeons[i][0] >=0){
            visited[i] = 1;
          
            dfs(cnt+1, k - dungeons[i][1], dungeons);
            visited[i] = 0;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons){
    dfs(0, k, dungeons);
    return answer;
}

