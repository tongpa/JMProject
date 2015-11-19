package com.jobsmatcher.company.dao;

import java.util.Date;
import java.util.List;

import com.jobsmatcher.company.model.PositionPostDate;
import com.jobsmatcher.company.model.ViewPositionPostDate;

public interface PositionPostDateDao  extends AbstractDao<PositionPostDate, String>{
	
	public List<PositionPostDate> getPositionPostDateByPosition(String id);
	public void deleteById(PositionPostDate positionPostDate);
	public void deleteByPosition(int id);
	
	public void deleteByCompany(int id);
	
	public void deleteById(int id);
	
	public boolean updatePositionPostDate(PositionPostDate positionPostDate);
	
	public List<ViewPositionPostDate> getViewPositionPostBateByPosition(String id);
	
	public List<PositionPostDate> getPositionPostDeteByPositionAndDate(Integer positionId,Date postDate);
}
