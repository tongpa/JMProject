package com.jobsmatcher.company.controller;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List; 
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
 
 
 


import org.codehaus.jackson.map.ObjectMapper;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller; 
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
  















import com.jobsmatcher.company.dao.PositionDao;
import com.jobsmatcher.company.dao.PositionPostDateDao; 

 
import com.jobsmatcher.company.model.Position;
import com.jobsmatcher.company.model.PositionPostDate;
import com.jobsmatcher.company.utility.Util;

 
@Controller
@RequestMapping(value = "jobs")
public class PositionController {
	
	private Util util = new Util(); ;
	
	@Autowired
	private PositionDao positionDao;
	@Autowired
	private PositionPostDateDao positionPostDateDao;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView index() {
		ModelAndView model = new ModelAndView( );
		  model.addObject("title", "Spring Security Login Form - Database Authentication");
		  model.addObject("message", "This page is for ROLE_ADMIN only!");
		  model.setViewName("position/index");
		   
		  //System.out.println("load");
		  return model;
	 
		}
	
	@RequestMapping(value = "search", method = RequestMethod.POST)
	@ResponseBody
    public Map<String, Object> search( @RequestParam(value = "keysearch", required=true ) Integer keysearch,
    		@RequestParam(value = "start", required=true ) Integer start,
    		@RequestParam(value = "limit", required=true ) Integer limit,
    		@RequestParam(value = "page", required=true ) Integer page,
    		
    		HttpServletRequest request, HttpServletResponse response,HttpSession sec) {
		Map<String, Object> books = new HashMap<String, Object>();
		List<Position> listposition = new ArrayList<Position>();
		
		System.out.println("start : " + start);
		System.out.println("limit : " + limit);
		System.out.println("page : " + page);
		
		
		listposition = positionDao.getPositionByCompany( keysearch.toString(),start.intValue(),limit.intValue(),page.intValue() );
		books.put("company", listposition);
		/* 
		keysearch = keysearch.trim(); 
		
		if(keysearch.length() > 0){
			  
			listposition = positionDao.getPositionByCompany( keysearch  );
		 	books.put("company", listposition);
		}
			
		 */
		
		int size = positionDao.getSizePositionByCompany(keysearch.toString());
	 	books.put("total", size);
	 	
		return books;
    }
	
	@RequestMapping(value = "addJobss", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> addJobss(@RequestBody Position position, HttpSession sec) {
		Map<String, Comparable> response = new HashMap<String, Comparable>();
		response.put("success", true);
        response.put("msg", "Welcome tong"  );
		return response;
	}
	 
	@RequestMapping(value = "addJobs", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> addJobs(@RequestBody Position position, HttpSession sec) {
		Map<String, Comparable> response = new HashMap<String, Comparable>();
		try {
			
			 
			if(position.getId_position() ==0){
				
				System.out.println(position.getPost_date());
				 
				//position.setPost_date(util.convertDate(position.getPost_date()));
				 
				System.out.println(position.getPost_date());
				
				
				positionDao.saveOrUpdate(position);
				
				PositionPostDate positionPostDate = new PositionPostDate();
				
				if(position.getId_position() != 0){
					positionPostDate.setId_position(position.getId_position());
					positionPostDate.setPost_date(position.getPost_date());
					
					positionPostDateDao.saveOrUpdate(positionPostDate);
				
				}
				
				positionPostDate = null; 
				
				
				 
			}
			else{
				
				positionDao.updatePosition(position);
			}
	        response.put("success", true);
	        response.put("msg", "Welcome tong"  );
	    } catch(Exception e) {
	        response.put("success", false);
	        response.put("msg", e.getMessage());
	    }
		return response;
 
		}
	
	
	@RequestMapping(value = "delJobs", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> delJobs(@RequestBody Position position,HttpSession sec){
		Map<String, Comparable> responses = new HashMap<String, Comparable>();
		
		//System.out.println(position.getId_position());
//		System.out.println(id_position);
		try {
	        
			positionPostDateDao.deleteByPosition(position.getId_position());
			positionDao.deleteById(position);
	         responses.put("success", true);
	         responses.put("msg", "Welcome tong"  );
	        } catch(Exception e) {
	         responses.put("success", false);
	         responses.put("msg", e.getMessage());
	        }
//		
		return responses;
	}
	
	
	@RequestMapping(value = "addPostDate", method = RequestMethod.POST)
	public @ResponseBody Map<String, Comparable> addPostDate( @RequestBody String position,
			//@RequestParam(value = "keysearch", required=true ) Integer keysearch,
			//@PathVariable("post_date") Date post_date, @PathVariable("id_position") int id_position, @PathVariable("id_position_post_date") int id_position_post_date,
			HttpSession sec) {
		Map<String, Comparable> response = new HashMap<String, Comparable>();
		try {
			//ObjectMapper mapper = new ObjectMapper();
			
			//PositionPostDate positionPostDate = mapper.readValue(position, PositionPostDate.class);
			System.out.println(position);
			 
			 
			JSONParser parser = new JSONParser();
			Object obj = parser.parse(position) ;
			JSONObject jsonObject = (JSONObject) obj;
			
			String name = (String) jsonObject.get("post_date");
			System.out.println(name);
			
			PositionPostDate positionPostDate = new PositionPostDate();
			
			positionPostDate.setId_position(util.convertInteger((String)jsonObject.get("id_position")));
			positionPostDate.setPost_date(util.convertDate((String)jsonObject.get("post_date")   ));
			
			positionPostDateDao.saveOrUpdate(positionPostDate);
			
			
	        response.put("success", true);
	        response.put("msg", "Welcome tong"  );
	    } catch(Exception e) {
	        response.put("success", false);
	        response.put("msg", e.getMessage());
	    }
		return response;
 
		}
	
}
