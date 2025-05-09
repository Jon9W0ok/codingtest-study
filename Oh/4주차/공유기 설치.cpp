#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n, c, num, st, router, start, end, mid, ans = 0;
	cin >> n >> c;
	vector<int> pos;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		pos.push_back(num);
	}
	sort(pos.begin(), pos.end());
	start = 1;                             // 최소 거리
	end = pos[n - 1] - pos[0];             // 최대 거리

	while (start <= end)
	{
		router = 1;
		mid = (start + end) / 2;
		st = pos[0];

		for (int i = 1; i < n; i++)
		{
			if (pos[i] - st >= mid)
			{
				router++;
				st = pos[i];
			}
		}

		if (router >= c) // 현재 mid가 너무 작거나 딱 맞는 상황 -> 공유기 더 설치 가능할수도
		{
			ans = max(ans, mid);
			start = mid + 1; // 더 넓은 최소 거리를 찾기 위해
		}

		else // 현재 mid가 너무 크기 때문에 더 많은 공유기를 설치할 수 없음 -> 최소 거리를 줄이기 위해 end = mid - 1
			end = mid - 1;
	}
	cout << ans;
	return 0;
}
