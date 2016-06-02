package com.saito.logerrors;

import android.app.Application;

import org.acra.ACRA;
import org.acra.ReportingInteractionMode;
import org.acra.annotation.ReportsCrashes;

import java.text.SimpleDateFormat;
import java.util.Calendar;

@ReportsCrashes(
        formUri = "http://stationerry.pythonanywhere.com/backend/sendreport/",
        reportType = org.acra.sender.HttpSender.Type.JSON,
        mode = ReportingInteractionMode.TOAST,
        resToastText = R.string.CrashText)


public class App extends Application{
    @Override
    public void onCreate() {
        super.onCreate();
        ACRA.init(this);

        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
        System.out.println( sdf.format(cal.getTime()) );

        int stringId = getApplicationContext().getApplicationInfo().labelRes;
        String appname = getString(stringId);
        String time = sdf.format(cal.getTime());
        ACRA.getErrorReporter().putCustomData("UserID", "Username" );
        ACRA.getErrorReporter().putCustomData("TimeOccured", time);
        ACRA.getErrorReporter().putCustomData("AppName", appname);
        ACRA.getErrorReporter().putCustomData("ActivityName", this.getClass().getSimpleName());
    }
}
