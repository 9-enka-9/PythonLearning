#include<bits/stdc++.h>
using namespace std;
int main()
{
    int x,y,z,n;
    cin >> n >> x >> y >> z;
    string s = "";
    for (int i = 0; i < z; i++)
    {
        if(i % 2 == 0) s+='0';
        else s+='1';
    }

    for (int i = 0; i < x; i++)
    {
        if(i % 2 == 0) s+='A';
        else s+='B';
    }
        for (int i = 0; i < y; i++)
    {
        if(i % 2 == 0) s+='a';
        else s+='b';
    }
    if(s.size() < n)
    {
        for (int i = s.size(); i < n - s.size(); i++)
        {
            if(i % 2 == 0) s+='a';
            else s+='b';
        }
    }
    cout << s;
    return 0;
}