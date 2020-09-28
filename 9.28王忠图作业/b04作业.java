package test01;
import junit.framework.TestCase;
import org.junit.Before;
import org.junit.Test;

public class b04作业 extends TestCase{
	protected double v1;
	protected double v2;
	@Before
	public void setUp(){
		v1=5.3;
		v2=5.7;
		
	}
	@Test
	public void testAdd(){
		System.out.println("被调用的次数:"+this.countTestCases());
		//获取TestCase的名字,默认是函数名
		String name=this.getName();
		System.out.println("name="+name);
		//设定TestCase的名字
		this.setName("testtNewAdd");
		String name2=this.getName();
		System.out.print("name2="+name2);
		
	}
	public void tearDown(){
		System.out.println("用例结束后调用"+(v1+v2));
	}

	
}
