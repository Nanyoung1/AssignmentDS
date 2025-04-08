#include <iostream>
using namespace std;

int main()
{
	const int size = 10;
	int numbers[size];
	int distinct[size];
	int distinctCount = 0;

	cout << "Enter ten numbers: ";
	for (int i = 0; i < size; i++)
	{
		cin >> numbers[i];
	}

	for (int i = 0; i < size; i++)
	{
		bool isduplicate = false;
		for (int j = 0; j < distinctCount; j++)
		{
			if (numbers[i] == distinct[j])
			{
				isduplicate = true;
				break;
			}
		}

		if (!isduplicate)
		{
			distinct[distinctCount] = numbers[i];
			distinctCount++;
		}
	}

	cout << "The distinct numbers are: ";
	for (int i = 0; i < distinctCount; i++)
	{
		cout << distinct[i] << " ";
	}
	cout << endl;

	return 0;
}