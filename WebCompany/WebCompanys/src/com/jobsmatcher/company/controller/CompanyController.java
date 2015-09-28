package com.jobsmatcher.company.controller;
 
import java.util.HashMap;
import java.util.List;
import java.util.Map; 

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.log4j.Logger; 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller; 
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
 

 



import com.jobsmatcher.company.dao.CompanyDao;
import com.jobsmatcher.company.dao.PositionDao;
import com.jobsmatcher.company.dao.PositionPostDateDao;
import com.jobsmatcher.company.model.Company; 

//import static org.springframework.http.MediaType.APPLICATION_JSON_VALUE;
@Controller
@RequestMapping(value = "company")
public class CompanyController {
	
	final static Logger logger = Logger.getLogger(CompanyController.class);
	@Autowired
	private CompanyDao companyDao;
	@Autowired
	private PositionDao positionDao;
	
	@Autowired
	private PositionPostDateDao positionPostDateDao;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView index(HttpServletRequest request, HttpServletResponse response) {
		try{
			request.setCharacterEncoding("UTF-8");
			response.setContentType("text/html; charset=UTF-8");
			
			
			
			}
		catch(Exception ex){
			//ex.printStackTrace();
			logger.error(ex.getMessage());
		}
		ModelAndView model = new ModelAndView( );
		
		  model.addObject("title", "Spring Security Login Form - Database Authentication");
		  model.addObject("message", "This page is for ROLE_ADMIN only!");
		  model.setViewName("company/index");
		  
		 // model.setViewName("company/sample");
		  //System.out.println("load");
		  return model;
	 
		}
	
	
	@RequestMapping(value = "totalCompany", method = RequestMethod.GET)
	@ResponseBody
	public   Map<String, List<Map<String, String>> > totalCompany( HttpServletRequest request, HttpServletResponse response, HttpSession sec){
		List<Map<String, String>> book = companyDao.getTotalComnany();
		Map<String, List<Map<String, String>> > books = new HashMap<String, List<Map<String, String>> >();
		if(book.size() > 0){
			books.put("totalCompany",   book);
		}
		return books;
	}
	
	@RequestMapping(value = "history", method = RequestMethod.GET)
	@ResponseBody
	public   Map<String, List<Map<String, String>> > showHistory( 
			@RequestParam(value = "start", required=true ) Integer start,
    		@RequestParam(value = "limit", required=true ) Integer limit,
    		@RequestParam(value = "page", required=true ) Integer page,
			
			HttpServletRequest request, HttpServletResponse response, HttpSession sec){
		List<Map<String, String>> book = companyDao.listTotalInDate(null, null, start.intValue(),limit.intValue(),page.intValue());
		Map<String, List<Map<String, String>> > books = new HashMap<String, List<Map<String, String>> >();
		if(book.size() > 0){
			books.put("history",   book);
		}
		return books;
	}
	
	@RequestMapping(value = "search", method = RequestMethod.POST)
	@ResponseBody
    public Map<String, Object> search( @RequestParam(value = "keysearch", required=true,defaultValue= "") String keysearch,
    		@RequestParam(value = "start", required=true ) Integer start,
    		@RequestParam(value = "limit", required=true ) Integer limit,
    		@RequestParam(value = "page", required=true ) Integer page,
    		HttpServletRequest request, HttpServletResponse response,HttpSession sec ) {
		
		Map<String, Object> books = new HashMap<String, Object>();
		 
		logger.info("Start : " + start);
		logger.info("limit : " + limit);
		logger.info("page : " + page);
		
		keysearch = keysearch.trim();
		 
		
		if(keysearch.length() > 0){
			  
			books.put("total",  companyDao.getSizeByName( keysearch)); 
			books.put("company", companyDao.listCompanyByName(  keysearch ,start.intValue(),limit.intValue(),page.intValue() ));
			 
		}
		
		return books;
    }
	 
	
	@RequestMapping(value = "addCompany", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> addCompany(@RequestBody Company company, HttpSession sec){
		Map<String, Comparable> response = new HashMap<String, Comparable>();
		//System.out.println(company);
		try {
	        
			if (company.getId_company() == 0){
				companyDao.saveCompany(company);
			}
			else {
				companyDao.updateCompany(company);
			}
	         response.put("success", true);
	         response.put("msg", "Welcome tong"  );
	        } catch(Exception ex) {
	         response.put("success", false);
	         response.put("msg", ex.getMessage());
	         logger.error(ex.getMessage());
	        }
		
		return response;
	}
	
	
	@RequestMapping(value = "delCompany", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> delCompany(@RequestBody Company company, HttpSession sec){
		Map<String, Comparable> response = new HashMap<String, Comparable>();
		//System.out.println(company);
		try {
	        
			positionPostDateDao.deleteByCompany(company.getId_company());
			positionDao.deleteByCompany(company.getId_company());
			companyDao.deleteById(company);
	         response.put("success", true);
	         response.put("msg", "Welcome tong"  );
	        } catch(Exception ex) {
	         response.put("success", false);
	         response.put("msg", ex.getMessage());
	         logger.error(ex.getMessage());
	        }
		
		return response;
	}
	
}
