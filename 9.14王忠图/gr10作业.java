package test;
import java.util.Scanner;
public class gr10��ҵ {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		/*һ.����Ĵ�����дһ��
		��.������װeclipse
		
		��.д��main��������Ҫ��
		1��public�Ǳ�ʾ����Ȩ��
		2��static�Ǳ�ʾ��̬���Σ�û�ж���Ҳ�ܵ������еľ�̬����
		3��main�����ǳ�������
		4��String�ַ�����
		
		
		��.��д��int,float,double,char,long�ֱ�ռ�ڴ�Ĵ�С
		1��int      4
		2��float    4
		3��double   8
		4��char     2
		5��long     8
		
		
		��.ǿ������ת����ôת��*/
		//��.�����:
		//������,���趨һ������,Ȼ��ӿ���̨����һ������,������趨�����ִ�,��ʾ����������ִ���,
		//������������С��,��ʾ�����������С��,���������ȷ,��ʾ�����������ȷ
		
		Scanner scan=new Scanner(System.in);
		
		int a=10;
		System.out.println("������µ����֣�");
		int b=scan.nextInt();
		if(a>b) {
			System.out.println("�����������С��");
		}else if(a<b){
			System.out.print("����������ִ���");
		}else {
			System.out.print("�����������ȷ");
		}
		
		
	}

}
