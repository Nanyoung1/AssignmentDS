#include <iostream>
using namespace std;

int main()
{
	int n = 1;

	while ((n + 1) * (n + 1) * (n + 1) < 12000)
	{
		n++;
	}

	cout << "n�� 3���� 12000���� ���� ���� ū ���� n��: " << n << endl;

	return 0;
}