#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+5;
vector<int> v[N];
bool vis[N];

int32_t main()
{
	//n is the number of vertices
	//m is the number of edges
	int n, m;
	cout <<"Enter the number of vertices and edges respectively.\n";
	cin >> n >> m;
	cout <<"Enter " << m << " pairs of integers, representing an edge between the integers.\n";
	for(int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}		
	//mark all of the vertices as unvisited
	for(int i = 1; i <= n; i++)
		vis[i] = false;
	for(int i = 1; i <= n; i++)
	{
		//if the vertex is not visited yet, do the following
		if(vis[i] == false)
		{
			for(auto it : v[i])
			{
				if(vis[it] == false)
				{
					//Put both of the vertices in the answer set and break
					vis[i] = true;
					vis[it] = true;
					break;
				}
			}
		}
	}
	for(int i = 1; i <= n; i++)
		if(vis[i])
			cout << i <<" ";
	cout << endl;
	return 0;
}