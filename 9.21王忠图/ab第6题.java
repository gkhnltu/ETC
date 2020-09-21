package 作业01;

import java.util.Scanner;

import javax.print.DocFlavor.INPUT_STREAM;

public class ab第6题 {
	 
	 String name="简单点";
	 String sex="男";
	 int age=12;
	 String type="昆仑";

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
			System.out.println("年龄不正确");
		}
		}
	int getAge() {
		return age;
	}
	void setSex(String Sex) {
		if(Sex=="男" || Sex=="女") {
			sex=Sex;
		}else {
			System.out.println("设置的性别不合法");
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




