package ��ҵ04;
import java.security.PublicKey;
public class a05��̬ {
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
			 
			System.out.println(age+"���"+kkk+name+"�������Ľ�");
		
		}
	}
	public static class Rrr extends Animal{
		Rrr(String name,int age,String kkk) {
			this.name=name;
			this.age=age;
			this.kkk=kkk;
				 System.out.println(age+"���"+kkk+name+"�������Ľ�");
		}
		
	}	
	public static class Bbb extends Animal{
		Bbb(String name,int age,String kkk) {
			this.name=name;
			this.age=age;
			this.kkk=kkk;
				 System.out.println(age+"���"+kkk+name+"����Ľ�");
		}
		}
	
	public static void test(Animal an) {
		an.speak();
	}

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		Dog dog=new Dog("����",2,"��������");
		Rrr rrr=new Rrr("С��", 3, "�ӷ�");
		Bbb bbb=new Bbb("С��", 4,"�׻�");
		
		test(rrr);
		test(bbb);
		test(dog);
		

	}

}
