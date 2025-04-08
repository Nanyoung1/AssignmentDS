#include <iostream>
using namespace std;

int main()
{
	double pound_to_kilogram = 0.45359237;
	double inch_to_meter = 0.0254;

	double weight_pounds;
	double height_inches;

	cout << "Enter weight in pounds: ";
	cin >> weight_pounds;

	cout << "Enter height in inches: ";
	cin >> height_inches;

	double weight_in_kilogram = weight_pounds * pound_to_kilogram;
	double height_in_meter = height_inches * inch_to_meter;

	double bmi = weight_in_kilogram / (height_in_meter * height_in_meter);

	cout << "BMI is " << bmi << endl;

	return 0;
}