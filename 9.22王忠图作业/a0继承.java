package 作业04;

public class a0继承 {
	public static class Father{
		public Father() {
			System.out.println("我是father的构造函数");
		}
	}
	public static class Son extends Father{
		Son(){
			System.out.println("我是Son的构造函数");
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
			System.out.println("我是Son的构造函数");
		}
		Son2(int b){
			this.b=b;
		}
	}

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		Son2 son2=new Son2();
		Son son=new Son();

	}

}
