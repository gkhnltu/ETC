package test01;

import static org.junit.Assert.*;
import junit.framework.TestCase;

import org.junit.Test;

public class b03��ҵ extends TestCase{
	@Test
	public void testAb(){
		System.out.print("����b03��ҵ");
		int num=5;
		String tm="hello";
		String str="test ceshi";
		assertEquals("test ceshi",str);
		assertFalse(num>6);
		assertNotNull(tm);
		
	}


}
