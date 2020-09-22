package 作业04;

public class a第8题 {
	public static class Che{
		public Che() {
			
		}
		String name;	
		void speak() {
			
		}
	}
	public static class Bm extends Che{
		Bm(String name){
			this.name=name;
			System.out.println(name);
		}
	}
	public static class Ad extends Che{
		Ad(String name){
			this.name=name;
			System.out.println(name);
		}
	}
	public static class Byd extends Che{
		Byd(String name){
			this.name=name;
			System.out.println(name);
		}
	}

	
	
	
	public static void main(String[] args) {
		// TODO 自动生成的方法存根
//		8.写一个汽车的多态案例,如汽车类是父类,宝马的子类,操作打印各自子类的品牌
		Bm bm=new Bm("宝马");
		Ad ad=new Ad("奥迪");
		Byd byd=new Byd("比亚迪");
		
		
		
	}

}
