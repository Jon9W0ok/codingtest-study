#include <bits/stdc++.h>
using namespace std;

vector<vector<string>> ticket;
vector<string> answer;
bool check[10001];
bool isAnswer;
// ticketCnt : 지금까지 사용한 항공권의 개수 -> 주어진 항공권을 모두 사용해야함.
void dfs(string start, int ticketCnt){ 
    answer.push_back(start);
    
    //현재 까지 사용한 항공권 개수가 전체 항공권 개수와 같다면
    if (ticketCnt == ticket.size()) { 
        isAnswer = true;
        return;
    }
    
    for (int i = 0; i < ticket.size(); i++) {
        if (check[i]) continue;
        if (ticket[i][0] == start) {
            check[i] = true;
            dfs(ticket[i][1], ticketCnt+1);
            
            if (!isAnswer) {
                answer.pop_back();
                check[i] = false;
            }
        }
    }
    
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    ticket = tickets;
    dfs("ICN", 0);
    
    return answer;
}
