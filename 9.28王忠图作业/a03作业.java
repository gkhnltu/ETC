package test01;

import junit.framework.TestCase;

public class a03��ҵ extends TestCase{
	protected int v1,v2;
	protected void setUp(){
		v1=3;
		v2=4;
		System.out.print("����֮ǰ����");
	}
	public void testAdd(){
		double r=v1+v2;
		assertTrue(r==7);
	}
	public void tearDown(){
		System.out.print("����֮�����");
	}

}
