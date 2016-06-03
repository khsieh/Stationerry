import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.*;
import java.io.*;

public class Comm {
    private static String serverRoot = "http://stationerry.pythonanywhere.com/backend/";
    //private static String serverRoot = "http://127.0.0.1:8000/backend/";
    private static String debugRoot = "http://stationerry.pythonanywhere.com/backend/";
    //private static String debugRoot = "http://127.0.0.1:8000/backend/";
    private static final int commVersion = 1;

    private int lastStatus;
    private String lastJSON;

    // User account info
    private static volatile String authToken = "";

    public static final int SUCCESS = 0;
    public static final int JSON_ERROR = -3;
    public static final int API_FAIL = -50;
    public static final int NETWORK_FAIL = -60;
    public static final int AUTH_FAIL = -70;

    public Comm() {
        System.out.println("Creating new Comm");
        lastJSON = "";
    }

    public String getLastJSON() {
        return lastJSON;
    }

    public static void main(String[] args) {
        try {
            Comm c = new Comm();
	    if (args[0].equals("NATALIE_THROW"))
		{
		    String data = new String();
		    String fileName = "logerror.txt";
		    try {
			String line = null;
			// FileReader reads text files in the default encoding.
			FileReader fileReader = new FileReader(fileName);
			
			// Always wrap FileReader in BufferedReader.
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			
			while((line = bufferedReader.readLine()) != null) {
			    data = data + line + "\n";
			}   
			
			// Always close files.
			bufferedReader.close();         
		    }
		    catch(FileNotFoundException ex) {
			System.out.println("Unable to open file '" + fileName + "'");
		    }
		    catch(IOException ex) {
			System.out.println("Error reading file '" + fileName + "'");
			// Or we could just do this: 
			// ex.printStackTrace();
		    }
		    c.apiRequest("sendreport",data);
		    return;
		}
            //c.apiRequest("sendreport", "{\"name\":\"apphello\", \"version\":\"3.2.1\", \"platform\":\"platplat\", \"type\":\"typehello\", \"report\":\"reporthey\"}");
       
            Scanner read = new Scanner (new File(args[0]));
            read.useDelimiter(":::::::");
            String name, version, platform, type, report;

            //while (read.hasNext())
            //{
                name = read.next();
                version = read.next();
                platform = read.next();
                type = read.next();
                report = read.next();
                System.out.println(name);
                System.out.println(version);
                System.out.println(platform);
                System.out.println(type);
                System.out.println(report);
                //JSONObject obj = new JSONObject();
                c.apiRequest("sendreport", "{\"name\":" + name + "," 
                                    +"\"version\":" + version + "," 
                                    +"\"platform\":" + platform + ","
                                    +"\"type\":" + type + ","
                                    +"\"report\":" + report + "}");
                System.out.println("{\"name\":" + name + "," 
                                    +"\"version\":" + version + "," 
                                    +"\"platform\":" + platform + ","
                                    +"\"type\":" + type + ","
                                    +"\"report\":" + report + "}");
            //}
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("wrong ");
            return;
        }    
        
    }

    private int apiRequest(String relUrl, String o) {
        if (o == null) {
            return apiRequestPayload(relUrl, o);
        }
        try {
            //return apiRequestPayload(relUrl, "{\"name\":\"apphello\", \"version\":\"3.2.1\", \"platform\":\"platplat\", \"type\":\"typehello\", \"report\":\"reporthey\"}");
            return apiRequestPayload(relUrl, o);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("died writing value string " + o);
            return JSON_ERROR;
        }
    }

    private int apiRequestBytePayload(String relUrl, byte[] payload) {
        String line;
        StringBuffer jsonString = new StringBuffer();
        try {
            //URL url = new URL(serverRoot + relUrl);
	    URL url = new URL(debugRoot + relUrl);

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            connection.setDoInput(true);
            connection.setDoOutput(true);
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
            connection.setRequestProperty("token", Comm.authToken);
            OutputStream os = connection.getOutputStream();
            os.write(payload);
            os.close();
            BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = br.readLine()) != null) {
                jsonString.append(line);
            }
            br.close();
            connection.disconnect();
            System.out.println(jsonString);
            lastJSON = jsonString.toString();
            lastStatus = API_FAIL;
            try {
                Integer status = 0; 
                lastStatus = status;
                return SUCCESS;
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("failed in apiRequest : fail to readValue from \"status\" ");
                return API_FAIL;
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("failed in apiRequest: failed URL");
            return NETWORK_FAIL;
        }
    }

    private int apiRequestPayload(String relUrl, String payload) {
        String line;
        StringBuffer jsonString = new StringBuffer();
        try {
            //URL url = new URL(serverRoot + relUrl);
	    URL url = new URL(debugRoot + relUrl);

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            connection.setDoInput(true);
            connection.setDoOutput(true);
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
            connection.setRequestProperty("token", Comm.authToken);
            connection.setRequestProperty("commversion", Integer.toString(Comm.commVersion));
            OutputStreamWriter writer = new OutputStreamWriter(connection.getOutputStream(), "UTF-8");
            writer.write(payload);
            writer.close();
            BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = br.readLine()) != null) {
                jsonString.append(line);
            }
            br.close();
            connection.disconnect();
            System.out.println(jsonString);
            lastJSON = jsonString.toString();
            lastStatus = API_FAIL;
            try {
                Integer status = 0;
                lastStatus = status;
                if (lastStatus == -1) {
                    return AUTH_FAIL;
                } else {
                    return SUCCESS;
                }
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("failed in apiRequest : fail to readValue from \"status\" ");
                return API_FAIL;
            }
        } catch (Exception e) {
            System.out.println("apiRequestPayload caught an exception: " + e.getMessage());
            e.printStackTrace();
            return NETWORK_FAIL;
        }
    }
}

