package test01;

import junit.framework.TestResult;
import junit.framework.TestSuite;

public class a04��ҵ {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		TestSuite sr=new TestSuite(b03��ҵ.class,b04��ҵ.class);
		TestResult rr=new TestResult();
		sr.run(rr);
		System.out.println("��������:"+rr.runCount());

	}

}
