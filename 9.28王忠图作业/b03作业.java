package test01;

import static org.junit.Assert.*;
import junit.framework.TestCase;

import org.junit.Test;

public class b03作业 extends TestCase{
	@Test
	public void testAb(){
		System.out.print("我是b03作业");
		int num=5;
		String tm="hello";
		String str="test ceshi";
		assertEquals("test ceshi",str);
		assertFalse(num>6);
		assertNotNull(tm);
		
	}


}
