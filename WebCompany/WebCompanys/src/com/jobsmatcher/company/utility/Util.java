package com.jobsmatcher.company.utility;

 
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

public class Util {
	
	public  Date convertDate(Date d){
		Date c = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd",Locale.US);
		try{
			Calendar date = Calendar.getInstance();  
		    date.setTime(d);
		    date.add(Calendar.YEAR,543);  
		    c = sdf.parse(sdf.format(date.getTime()));
		     
		}
		catch(Exception ex){
			
		}
		
		return c;
	}
	
	public Date convertDate(String d){
		Date c = new Date();
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");//("MM/dd/yyyy");
		
		
		try{
			c = df.parse(d);
		}
		catch(Exception ex){
			
		}
		
		return c;
		
	}
	
	public int convertInteger(String s){
		int i = 0;
		try{
			i = Integer.parseInt(s);
		}
		catch(Exception ex){
			
		}
		
		return i;
	}
	
	
	public static void main(String[] argv){
		Date d = new Date();
		
		System.out.println(d);
		
		String testDate = "2014-11-27";
		try{ 
			DateFormat formatter = new SimpleDateFormat("yyyy-MM-dd",Locale.US);
			Date date = formatter.parse(testDate);
			
			
			System.out.println(formatter.format( d)   );
			System.out.println(date);
			
			System.out.printf("%s %tB %<te, %<tY", "Due date:", date);
			
			
			String dates = String.format("Post Date [  postdate = %TD]",   new Date());
			System.out.println(dates);
			String datew = String.format("Post Date [  postdate = %tF]",   new Date());
			System.out.println(datew);
			
			
			testDate = "09/17/2558";
			Util u = new Util();
			System.out.println(testDate);
			
			System.out.println(u.convertDate(testDate));
			
			
		}
		catch(Exception ex){
			ex.printStackTrace();
		}
		
	}
}
