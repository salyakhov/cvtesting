package org.salyrus.cvtesting;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.sikuli.script.*;

import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;

public class App {
    public static void main( String[] args ) {
        Screen s = new Screen();
        String homePath = System.getProperty("user.dir");
        log("homePath=" + homePath);
//        String fileName = homePath + "/" + System.currentTimeMillis() + ".png";
//        log("fileName=" + fileName);
//        s.saveCapture(fileName);

        Path path = FileSystems.getDefault().getPath("src/main/resources/geckodriver");
        System.setProperty("webdriver.gecko.driver",path.toString());

        WebDriver driver = new FirefoxDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.navigate().to("http://www.google.com");

        WebElement element = driver.findElement(By.name("q"));
        element.sendKeys("Knock, Knock, Neo");
        element.submit();

        log("Page title is: " + driver.getTitle());

        String testCasePath = "src/main/resources/testcase-00-google";
        //ImagePath.add("");

        final String gLogoPath = Paths.get(homePath, testCasePath, "googlelogo_color_92x30dp.png").toString();
        Pattern gLogo = new Pattern(gLogoPath);

        try {
            Match match = s.wait(gLogo, 10);
            match.highlight();

            TimeUnit.SECONDS.sleep(3);

        } catch (FindFailed e) {
            String screenshot = screenshot(s, homePath);
            log("ERROR: can't find image " + gLogoPath + ", screenshot available at " + screenshot + ", error: " + e.getMessage());
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }

//            s.wait("spotlight-input.png");
//            s.click();
//            s.write("hello world#ENTER.");

    }

    private static String screenshot(Screen s, String homePath) {
        String fileName = Paths.get(homePath, + System.currentTimeMillis() + ".png").toString();
        s.saveCapture(fileName);
        return fileName;
    }

    private static void log(String message) {
        System.out.println(message);
    }
}
