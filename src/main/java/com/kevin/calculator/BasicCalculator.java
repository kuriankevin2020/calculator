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
}
