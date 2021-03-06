import io.appium.java_client.AppiumDriver;

import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;


public class QQ二次登录 {

	public static void main(String[] args) throws MalformedURLException, InterruptedException{
		// TODO 自动生成的方法存根
		DesiredCapabilities des=new DesiredCapabilities();
		des.setCapability("platformName", "android");//设定设备的平台
		des.setCapability("deviceName","Android Emulator");//设备名
		des.setCapability("platformVersion","4.4.4");//平台版本
		des.setCapability("noReset",true);//不要再次重装app
		des.setCapability("appPackage","com.tencent.qqlite");//设定包名
		des.setCapability("appActivity","com.tencent.mobileqq.activity.LoginActivity");//设定主页地址

		AppiumDriver dr=new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),des);
		Thread.sleep(2000);
		String[] my={"87654321"};
		String[] nm={"12345678"};
		dr.findElementByAccessibilityId("请输入QQ号码或手机或邮箱").click();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("请输入QQ号码或手机或邮箱").clear();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("请输入QQ号码或手机或邮箱").sendKeys(my);
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("请输入密码").click();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("请输入密码").clear();
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("请输入密码").sendKeys(nm);
		Thread.sleep(2000);
		dr.findElementByAccessibilityId("登录QQ").click();
//登录后要验证码不会了！！
	}

}
