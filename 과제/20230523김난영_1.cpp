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

	cout << "�� ���� �Ǽ��� �Է��ϼ���: ";
	cin >> num1 >> num2 >> num3;

	sort(num1, num2, num3);

	cout << "���ĵ� ����: " << num1 << ", " << num2 << ", " << num3 << endl;

	return 0;
}