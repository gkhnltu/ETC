package 作业04;
import java.security.PublicKey;
public class a05多态 {
	public static class Animal{
		 Animal() {
			
		}
		 String name;
		 int age;
		 String kkk;
		 void speak() {
			 
		 }
	}	
	public static class Dog extends Animal{
		Dog(String name,int age,String kkk) {
			this.name=name;
			this.age=age;
			this.kkk=kkk;
			 
			System.out.println(age+"岁的"+kkk+name+"汪汪汪的叫");
		
		}
	}
	public static class Rrr extends Animal{
		Rrr(String name,int age,String kkk) {
			this.name=name;
			this.age=age;
			this.kkk=kkk;
				 System.out.println(age+"岁的"+kkk+name+"喵喵喵的叫");
		}
		
	}	
	public static class Bbb extends Animal{
		Bbb(String name,int age,String kkk) {
			this.name=name;
			this.age=age;
			this.kkk=kkk;
				 System.out.println(age+"岁的"+kkk+name+"吼吼吼的叫");
		}
		}
	
	public static void test(Animal an) {
		an.speak();
	}

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		Dog dog=new Dog("旺财",2,"拉布拉多");
		Rrr rrr=new Rrr("小黑", 3, "加菲");
		Bbb bbb=new Bbb("小白", 4,"白虎");
		
		test(rrr);
		test(bbb);
		test(dog);
		

	}

}
