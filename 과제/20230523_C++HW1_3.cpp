#include <iostream>
using namespace std;

int main()
{
	int n = 1;

	while ((n + 1) * (n + 1) * (n + 1) < 12000)
	{
		n++;
	}

	cout << "n의 3승이 12000보다 작은 가장 큰 정수 n은: " << n << endl;

	return 0;
}