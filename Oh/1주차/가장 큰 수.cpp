#include <bits/stdc++.h>

using namespace std;

bool comp(string &a, string &b) {
    return a + b > b + a;
}

string solution(vector<int> numbers) {
    vector<string> strNumbers;
    
    for (int num : numbers) {
        strNumbers.push_back(to_string(num));
    }
    
    sort(strNumbers.begin(), strNumbers.end(), comp);
    
    if (strNumbers[0] == "0") return "0";
    
    string answer = "";
    for (string num : strNumbers) {
        answer += num;
    }
    
    return answer;
}
