package ��ҵ04;

public class Asuper {
	public static class Father{
		Father(int a){
			System.out.println("����Father�Ĺ��캯��");
			System.out.println("a="+a);
		}
		void test() {
			System.out.println("����Father��test����");
		}
		private int aa=20;
		int getAA() {
			return aa;
		}
		public static class Son extends Father{
			Son(){//2.super����д������Ĺ��캯����һ��
//				int b=20;
				super(20);//���ø�����вι���
			}

		void test02() {
			System.out.println("����Son��test02����");
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
		// TODO �Զ����ɵķ������
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