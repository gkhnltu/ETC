package ��ҵ04;

public class a��װ {
	public static class Maker{
		pivate int a;
		 Maker(int a) {
			this.a=a;
		}
		 int getA() {
			 return this.a;
		 }
		 void setA(int a) {
			 this.a=a;
		 }
	}

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		Maker maker=new Maker(20);
		System.out.println(maker.getA());
		maker.setA(200);
		System.out.println(maker.getA());

	}

}
