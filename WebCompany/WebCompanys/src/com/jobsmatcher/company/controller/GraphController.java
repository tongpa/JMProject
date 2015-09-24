package com.jobsmatcher.company.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.jobsmatcher.company.dao.CompanyDao;
import com.jobsmatcher.company.dao.PositionDao;

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
}
