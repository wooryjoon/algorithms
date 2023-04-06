#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
	int n;
	vector<int> v;
	stack<int> st;

	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);

		while (1) {
			if (st.empty()) {
				st.push(i);
				break;
			}
			else {
				if (a > v[st.top()]) {
					v[st.top()] = a;
					st.pop();
				}
				else {
					st.push(i);
					break;
				}
			}
		}
	}

	while (!st.empty()) {	//스택에 남은 수는 큰 수가x
		v[st.top()] = -1;
		st.pop();
	}

	for (int n : v) {
		cout << n << " ";
	}
	return 0;
}