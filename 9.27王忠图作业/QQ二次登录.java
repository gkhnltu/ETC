import io.appium.java_client.AppiumDriver;

import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;


public class QQ���ε�¼ {

	public static void main(String[] args) throws MalformedURLException, InterruptedException{
		// TODO �Զ����ɵķ������
		DesiredCapabilities des=new DesiredCapabilities();
		des.setCapability("platformName", "android");//�趨�豸��ƽ̨
		des.setCapability("deviceName","Android Emulator");//�豸��
		des.setCapability("platformVersion","4.4.4");//ƽ̨�汾
		des.setCapability("noReset",true);//��Ҫ�ٴ���װapp
		des.setCapability("appPackage","com.tencent.qqlite");//�趨����
		des.setCapability("appActivity","com.tencent.mobileqq.activity.LoginActivity");//�趨��ҳ��ַ

		AppiumDriver dr=new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
		Thread.sleep(2000);
		String[] my={"87654321"};
		String[] nm={"12345678"};
		dr.findElementByAccessibilityId("������QQ������ֻ�������").click();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("������QQ������ֻ�������").clear();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("������QQ������ֻ�������").sendKeys(my);
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("����������").click();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("����������").clear();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("����������").sendKeys(nm);
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("��¼QQ").click();
//��¼��Ҫ��֤�벻���ˣ���
	}

}
