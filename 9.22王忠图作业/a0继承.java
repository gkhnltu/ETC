package ��ҵ04;

public class a0�̳� {
	public static class Father{
		public Father() {
			System.out.println("����father�Ĺ��캯��");
		}
	}
	public static class Son extends Father{
		Son(){
			System.out.println("����Son�Ĺ��캯��");
		}
	}
	public static class Father2{
		int a;
	    Father2() {
			
		}
	    Father2(int a){
	    	this.a=a;
	    }
	}
	public static class Son2 extends Father2 {
		int b;
		 Son2() {
			System.out.println("����Son�Ĺ��캯��");
		}
		Son2(int b){
			this.b=b;
		}
	}

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		Son2 son2=new Son2();
		Son son=new Son();

	}

}
