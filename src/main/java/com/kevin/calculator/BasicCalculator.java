package com.kevin.calculator;

public class BasicCalculator implements iBasicCalculator {

	public double add(double a, double b) {
		return (a + b);
	}

	public double subtract(double a, double b) {
		return (a - b);
	}

	public double multiply(double a, double b) {
		return (a * b);
	}

	public double divide(double a, double b) {
		return (a / b);
	}

	public double reminder(double a, double b) {
		return (a % b);
	}

	public double absolute(double a) {
		double temp = a * 2;
		return (a - temp);
	}

	public double average(double a, double[] arr) {
		double sum = 0;
		for (int i = 0; i < a; i++) {
			sum = sum + arr[i];
		}
		return (sum / a);
	}

}
