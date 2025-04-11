#include <string>
#include <vector>
#include <queue>

using namespace std;

int map[102][102];
int visited[102][102];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,-1,1};

struct Pos
{
    int x,y,dis;
};


int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    //step1 -> 직사각형 테두리들을 1로만든다.
    for (int i=0;i<rectangle.size();i++)
    {
        for (int j=0;j<rectangle[i].size();j++)
        {
            rectangle[i][j] = rectangle[i][j] * 2;
        }
        int x1 = rectangle[i][0];
        int y1 = rectangle[i][1];
        int x2 = rectangle[i][2];
        int y2 = rectangle[i][3];
        for (int x=x1;x<=x2;x++)
        {
            for (int y=y1;y<=y2;y++)
            {
                map[x][y] = 1;
            }
        }
    }
    
    //step2 -> 직사각형의 바깥 테두리만 남기기 위해 내부를 다시 0으로 밀어준다.
    for (int i=0;i<rectangle.size();i++)
    {        
        int x1 = rectangle[i][0];
        int y1 = rectangle[i][1];
        int x2 = rectangle[i][2];
        int y2 = rectangle[i][3];
        for (int x=x1+1;x<x2;x++)
        {
            for (int y=y1+1;y<y2;y++)
            {
                map[x][y] = 0;
            }
        }
    }
    
    //step3 -> 테두리만 남겼다면 이제부턴 BFS를 통해 길을 찾아가면된다!
    queue<Pos> Q;
    Q.push({characterX*2,characterY*2,0});
    visited[characterX*2][characterY*2] = 1;
    
    vector<int> res;
    
    while(!Q.empty())
    {
        auto cur = Q.front();
        Q.pop();
        
        if (cur.x == itemX*2 && cur.y == itemY*2)
        {
            answer = cur.dis / 2;
            break;
        }
        
        for (int i=0;i<4;i++)
        {
            int nX = cur.x + dx[i];
            int nY = cur.y + dy[i];
            
            if (nX<=0||nX>101||nY<=0||nY>101||visited[nX][nY] == 1)
                continue;
            if (map[nX][nY] == 0)
                continue;
            
            visited[nX][nY] = 1;
            Q.push({nX,nY,cur.dis+1});
        }
        
    }
    
    return answer;
}
