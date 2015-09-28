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
import com.jobsmatcher.company.model.Position;

@Controller
@RequestMapping(value = "graph")
public class GraphController {
	
	final static Logger logger = Logger.getLogger(GraphController.class);
	@Autowired
	private CompanyDao companyDao;
	@Autowired
	private PositionDao positionDao;
	
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView index(HttpServletRequest request, HttpServletResponse response) {
		try{
			request.setCharacterEncoding("UTF-8");
			response.setContentType("text/html; charset=UTF-8");
			
			
			
			}
		catch(Exception ex){
			ex.printStackTrace();
		}
		ModelAndView model = new ModelAndView( );
		
		  model.addObject("title", "Spring Security Login Form - Database Authentication");
		  model.addObject("message", "This page is for ROLE_ADMIN only!");
		  model.setViewName("graph/index");
		  
		 // model.setViewName("company/sample");
		  //System.out.println("load");
		  return model;
	 
		}
	
	@RequestMapping(value = "showGraph", method = RequestMethod.GET)
	public @ResponseBody Map<String, List<Map<String, String>> > showGraph( 
			
			@RequestParam(value = "startDate", required=true ) String startDate,
			@RequestParam(value = "stopDate", required=true ) String stopDate, 
    		
    		HttpServletRequest request, HttpServletResponse response,HttpSession sec) {
		

		
		List<Map<String, String>> book = companyDao.listTotalInDate(startDate, stopDate, 0, 0, 1);
		
		Map<String, List<Map<String, String>> > books = new HashMap<String, List<Map<String, String>> >();
		if(book.size() > 0){
			books.put("history",   book);
		}


		
		
		
		
		return books;
	}
	
}
