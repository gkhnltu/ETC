package test01;
import java.util.Scanner;
public class a10今天的代码 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
//		double a=0;
//		int b=0;
//		
//		while(a<=100){
//			a+=2.5;
//			b+=1;
//			if(b%5==0) {
//				a=a-6;
//			}
//		}
//
//		System.out.println(b);
//		
//		int i=0;
//		while (i<5) {
//			int j=0;
//			while (j<=i) {
//				System.out.print('*');
//				j+=1;
//			}
//			i+=1;
//			System.out.println();
//		}
		
//		Scanner scanner=new Scanner(System.in);
//		System.out.println("请输入一 数字");
//		int a=scanner.nextInt();
//		int s=0;
//		for(int i=0;i<)
		
//		Scanner scanner=new Scanner(System.in);
//
//		int a=scanner.nextInt();
//		int s=1;
//		for(int i=1;i<=a;i++) {
//			s*=i;
//		}
//		System.out.println(s);

//		for(int i=1;i<10;i++) {
//			for(int j=1;j<=i;j++) {
//				int n=i*j;
//				System.out.print(j+"*"+i+"="+n+"\t");
//			}
//		System.out.println();
//		}
//		
//		
		
//	ss:for(int i=0;i<0;i++) {
//			for(int j=1;j<3;j++) {
//				if(j%2==0) {
//					break ss;
//				}
//				System.out.println('i='+i);
//				System.out.println("j="+j);
//			}
//		}
//		
//		System.out.print("双循环结束");
//		aa:for(int i=1;i<3;i++) {
//			for(int j=1;j<3;j++) {
//				if(j%2==0) {
//					continue aa;
//				}
//				System.out.println("i="+i);
//				System.out.println("j="+j);
//			}
//		}
//		
//	for(int i=0;i<10;i++) {
//		int a=(int)(Math.random()*100);
//		System.out.println(a);
//	}
//		
//	System.out.println(Math.pow(3,2));
//	System.out.println(Math.sqrt(9));
//	System.out.println(Math.abs(-5));
		
		
//		int[] my=new int[5];
//		for(int i=0;i<5;i++) {
//			my[i]=(int)(Math.random()*100);
//		}
//		for(int i:my) {
//			System.out.println(i+" ");
//		}
//		
//		int[] mya=new int[5];
//		for(int i=0;i<5;i++) {
//			mya[i]=(int)(Math.random()*100);
//		}
//		for(int i:mya) {
//			System.out.println(i+" ");
//		}
//		System.out.println();
//		int max=0;
//		max=mya[0];
//		for(int i=1;i<mya.length;i++) {
//			if(max<mya[i]) {
//				max=mya[i];
//			}
//		}
//		System.out.println("max="+max);	

		
		Scanner scanner=new Scanner(System.in);
		String str=scanner.next();
		char[] mych=new char[str.length()];
		for(int i=0;i<mych.length;i++) {
			mych[i]=str.charAt(i);
		}
		mych[0]='a';
		char c=mych[0];
		System.out.println(mych);
		
		
		
		
		
		
		
		
		
		
	
		
		
	}

}
