package com.kevin.calculator;

import org.junit.Assert;
import org.junit.Test;

public class CalculatorAppTest {

	@Test
	public void testAddCalculatorApp() {
		String str = "+";
		double a = 20.0;
		double b = 10.0;
		Assert.assertEquals(30.0, CalculatorApp.runner(str, a, b), 0);
	}

	@Test
	public void testSubtractCalculatorApp() {
		String str = "-";
		double a = 20.0;
		double b = 10.0;
		Assert.assertEquals(10.0, CalculatorApp.runner(str, a, b), 0);
	}

	@Test
	public void testMultiplyCalculatorApp() {
		String str = "*";
		double a = 20.0;
		double b = 10.0;
		Assert.assertEquals(200.0, CalculatorApp.runner(str, a, b), 0);
	}

	@Test
	public void testDivideCalculatorApp() {
		String str = "/";
		double a = 20.0;
		double b = 10.0;
		Assert.assertEquals(2.0, CalculatorApp.runner(str, a, b), 0);
	}

	@Test
	public void testReminderCalculatorApp() {
		String str = "%";
		double a = 5.0;
		double b = 2.0;
		Assert.assertEquals(1.0, CalculatorApp.runner(str, a, b), 0);
	}

	@Test
	public void testErrorCalculatorApp() {
		String str = "$";
		double a = 5.0;
		double b = 2.0;
		Assert.assertEquals(0.0, CalculatorApp.runner(str, a, b), 0);
	}

}
