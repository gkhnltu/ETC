package test01;

import io.appium.java_client.AppiumDriver;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.Capabilities;
import org.openqa.selenium.remote.DesiredCapabilities;

public class a01作业 {

	public static void main(String[] args) throws MalformedURLException, InterruptedException {
		// TODO 自动生成的方法存根
		DesiredCapabilities dr=new DesiredCapabilities();
		dr.setCapability("platformName","android");
		dr.setCapability("deviceName","Android Emulator");
		dr.setCapability("platformVersion","4.4.2");
		dr.setCapability("noReset",true);
		dr.setCapability("appPackage","com.android.calculator");
		dr.setCapability("appActivity","com.andoid.calculator");
		Capabilities des;
		AppiumDriver br=new AppiumDriver(new URL("http://127.0.0.1:4723/wd/hub"),dr);
		br.manage().timeouts().implicitlyWait(100, TimeUnit.SECONDS);
		br.findElementById("com.android.calculator2:id/digit7").click();
		Thread.sleep(2);
		br.findElementById("com.android.calculator2:id/plus").click();
		Thread.sleep(2);
		br.findElementById("com.android.calculator2:id/digit9").click();
		Thread.sleep(2);
		br.findElementById("com.android.calculator2:id/equal").click();
		String exp="16";
		String st=br.findElementByClassName("android.windge.EditText").getAttribute("text");
		if(exp.equals(st)){
			System.out.println("加法正确");
		}else{
			System.out.println("加法不正确");
		}

	}

}
