package test01;
import junit.framework.TestCase;
import org.junit.Before;
import org.junit.Test;

public class b04��ҵ extends TestCase{
	protected double v1;
	protected double v2;
	@Before
	public void setUp(){
		v1=5.3;
		v2=5.7;
		
	}
	@Test
	public void testAdd(){
		System.out.println("�����õĴ���:"+this.countTestCases());
		//��ȡTestCase������,Ĭ���Ǻ�����
		String name=this.getName();
		System.out.println("name="+name);
		//�趨TestCase������
		this.setName("testtNewAdd");
		String name2=this.getName();
		System.out.print("name2="+name2);
		
	}
	public void tearDown(){
		System.out.println("�������������"+(v1+v2));
	}

	
}
