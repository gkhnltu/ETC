package test;
import java.util.Scanner;
public class gr10作业 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		/*一.今天的代码重写一遍
		二.独立安装eclipse
		
		三.写出main函数的四要素
		1、public是表示公有权限
		2、static是表示静态修饰，没有对象也能调用类中的静态方法
		3、main函数是程序的入口
		4、String字符串类
		
		
		四.请写出int,float,double,char,long分别占内存的大小
		1、int      4
		2、float    4
		3、double   8
		4、char     2
		5、long     8
		
		
		五.强制类型转换怎么转换*/
		//六.编程题:
		//猜数字,先设定一个数字,然后从控制台输入一个数字,如果比设定的数字大,提示你输入的数字大了,
		//如果输入的数字小了,显示你输入的数字小了,如果输入正确,显示输入的数字正确
		
		Scanner scan=new Scanner(System.in);
		
		int a=10;
		System.out.println("请输入猜的数字：");
		int b=scan.nextInt();
		if(a>b) {
			System.out.println("你输入的数字小了");
		}else if(a<b){
			System.out.print("你输入的数字大了");
		}else {
			System.out.print("输入的数字正确");
		}
		
		
	}

}
