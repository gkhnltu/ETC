package test01;

import junit.framework.TestResult;
import junit.framework.TestSuite;

public class a04作业 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		TestSuite sr=new TestSuite(b03作业.class,b04作业.class);
		TestResult rr=new TestResult();
		sr.run(rr);
		System.out.println("运行数量:"+rr.runCount());

	}

}
