package 作业04;

public class Asuper {
	public static class Father{
		Father(int a){
			System.out.println("我是Father的构造函数");
			System.out.println("a="+a);
		}
		void test() {
			System.out.println("我是Father的test函数");
		}
		private int aa=20;
		int getAA() {
			return aa;
		}
		public static class Son extends Father{
			Son(){//2.super必须写在子类的构造函数第一行
//				int b=20;
				super(20);//调用父类的有参构造
			}

		void test02() {
			System.out.println("我是Son的test02函数");
			super.test();
		}
		void test03() {
			System.out.println(super.aa);
		}
		void setaa(int AA) {
			super.aa=AA;
		}
	}
	
	

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		Son son=new Son();
		son.test();
		son.test02();
		
		son.test03();
		son.setaa(200);
		son.test03();
		
		Father f=new Father(10);
		System.out.println(f.getAA());
}
}
}