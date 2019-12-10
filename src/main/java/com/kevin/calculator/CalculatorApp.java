package com.kevin.calculator;

import java.util.Scanner;

public class CalculatorApp {

	static iBasicCalculator calculator = new BasicCalculator();
	static Scanner inputString = new Scanner(System.in);
	static Scanner inputNumber = new Scanner(System.in);

	public static void main(String[] args) {

		System.out.println("!!!Welcome to Calculator App!!!");
		String flag;

		do {
			System.out.print("Enter Operator(+, -, *, /, %): ");
			String str = inputString.nextLine();
			System.out.print("Enter 1st Number: ");
			double a = inputNumber.nextDouble();
			System.out.print("Enter 2nd Number: ");
			double b = inputNumber.nextDouble();

			System.out.println("Result = " + runner(str, a, b));

			System.out.print("Do you want to continue(Y/n): ");
			flag = inputString.nextLine();

		} while (flag.equals("Y"));

		System.out.print("Calculator Terminated");
	}

	public static double runner(String str, double a, double b) {
		double result = 0;
		switch (str) {
		case "+":
			result = calculator.add(a, b);
			break;
		case "-":
			result = calculator.subtract(a, b);
			break;
		case "*":
			result = calculator.multiply(a, b);
			break;
		case "/":
			result = calculator.divide(a, b);
			break;
		case "%":
			result = calculator.reminder(a, b);
			break;
		default:
			System.out.println("Error");
			break;
		}
		return result;
	}
}
