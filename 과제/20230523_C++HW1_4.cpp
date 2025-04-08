#include <iostream>
using namespace std;

int main()
{
	int count = 0;

	for (int n = 100; n <= 200; n++)
	{
		if ((n % 5 == 0 || n % 6 == 0) && !(n % 5 == 0 && n % 6 == 0))
		{
			cout << n << " ";
			count++;

			if (count % 10 == 0)
				cout << endl;
		}

	}

	return 0;
}