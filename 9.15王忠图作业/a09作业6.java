package test01;
import java.util.Scanner;
import java.util.Scanner;

public class a09作业6 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
//		6．编程题：数组元素查找(查找指定元素第一次在数组中出现的索引)
		Scanner scanner=new Scanner(System.in);
		System.out.print("请输入要查找的元素：");
		int arr[]= {1,3,4,5,6};
		int a=scanner.nextInt();
		for(int c=0;c<arr.length;c++) {
			if(a==arr[c]) {
				System.out.println(c);
			}
				
		
		}
				
		
		
		
	}

}
