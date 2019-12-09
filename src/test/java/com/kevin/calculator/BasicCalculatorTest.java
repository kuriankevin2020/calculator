package com.kevin.calculator;

import org.junit.Assert;
import org.junit.Test;

public class BasicCalculatorTest {

	@Test
	public void testAdd() {
		double a = 20.0;
		double b = 10.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.add(a, b);
		Assert.assertEquals(30.0, result, 0);
	}

	@Test
	public void testSubtract() {
		double a = 20.0;
		double b = 10.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.subtract(a, b);
		Assert.assertEquals(10.0, result, 0);
	}

	@Test
	public void testMultiply() {
		double a = 20.0;
		double b = 10.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.multiply(a, b);
		Assert.assertEquals(200.0, result, 0);
	}

	@Test
	public void testDivide() {
		double a = 20.0;
		double b = 10.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.divide(a, b);
		Assert.assertEquals(2.0, result, 0);
	}

	@Test
	public void testReminder() {
		double a = 5.0;
		double b = 2.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.reminder(a, b);
		Assert.assertEquals(1.0, result, 0);
	}

	@Test
	public void testAbsolute() {
		double a = -20.0;
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.absolute(a);
		Assert.assertEquals(20.0, result, 0);
	}

	@Test
	public void testAverage() {
		double a = 5.0;
		double[] arr = { 10.0, 20.0, 30.0, 40.0, 50.0 };
		iBasicCalculator calculator = new BasicCalculator();
		double result = calculator.average(a, arr);
		Assert.assertEquals(30.0, result, 0);
	}

}
