package test01;

import io.appium.java_client.AppiumDriver;

import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;

public class a02��ҵ {

	public static void main(String[] args) throws MalformedURLException, InterruptedException{
		// TODO �Զ����ɵķ������
		DesiredCapabilities des=new DesiredCapabilities();
		des.setCapability("platformName", "android");//�趨�豸��ƽ̨
		des.setCapability("deviceName","Android Emulator");//�豸��
		des.setCapability("platformVersion","4.4.4");//ƽ̨�汾
		des.setCapability("noReset",true);//��Ҫ�ٴ���װapp
		des.setCapability("appPackage","com.tencent.mobileqq");//�趨����
		des.setCapability("appActivity","com.tencent.mobileqq.activity.LoginActivity");//�趨��ҳ��ַ

		AppiumDriver dr=new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
		Thread.sleep(5000);

		
		dr.findElementByAccessibilityId("������QQ������ֻ�������").click();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("������QQ������ֻ�������").clear();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("������QQ������ֻ�������").sendKeys("132456");
		Thread.sleep(2000);
		dr.findElementById("com.tencent.mobileqq:id/password").click();
		Thread.sleep(2000);
		dr.findElementById("com.tencent.mobileqq:id/password").clear();
		Thread.sleep(2000);
		dr.findElementById("com.tencent.mobileqq:id/password").sendKeys("654321");
		Thread.sleep(2000);
		dr.findElementById("com.tencent.mobileqq:id/login").click();
		Thread.sleep(5000);
		dr.swipe(159, 265, 484, 265, 20000);

	}

}
