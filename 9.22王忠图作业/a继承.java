package ��ҵ04;

public class a�̳� {
	public static class Father{
		int a=10;
		private int b=20;
	}
	public static class Son extends Father{
		
	}

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		Son son=new Son();
		System.out.println(son.a);
		Father f=new Father();
		System.out.println(f.a);
		son.a=100;
		System.out.println(son.a);
		System.out.println(f.a);

	}

}
