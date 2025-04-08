#include <iostream>
using namespace std;

void sort(double& num1, double& num2, double& num3)
{
	if (num1 > num2)
	{
		swap(num1, num2);
	}
	if (num2 > num3)
	{
		swap(num2, num3);
	}
	if (num1 > num2)
	{
		swap(num1, num2);
	}
}

int main()
{
	double num1, num2, num3;

	cout << "세 개의 실수를 입력하세요: ";
	cin >> num1 >> num2 >> num3;

	sort(num1, num2, num3);

	cout << "정렬된 숫자: " << num1 << ", " << num2 << ", " << num3 << endl;

	return 0;
}