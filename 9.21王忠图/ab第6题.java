package ��ҵ01;

import java.util.Scanner;

import javax.print.DocFlavor.INPUT_STREAM;

public class ab��6�� {
	 
	 String name="�򵥵�";
	 String sex="��";
	 int age=12;
	 String type="����";

	void setName(String Name) {
		name=Name;		
	}
	String getName() {
		return name;
	}
	void setAge(int Age) {
		if(Age>=0 &&Age<=120) {
			age=Age;
		}else {
			System.out.println("���䲻��ȷ");
		}
		}
	int getAge() {
		return age;
	}
	void setSex(String Sex) {
		if(Sex=="��" || Sex=="Ů") {
			sex=Sex;
		}else {
			System.out.println("���õ��Ա𲻺Ϸ�");
		}
		
	}
	String getSex() {
		return sex;
	}

	
	void setType(String Type) {
		type=Type;
	}
	String getType() {
		return type;

	}



}




