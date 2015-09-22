package com.jobsmatcher.company.dao;

import java.util.List;

import com.jobsmatcher.company.model.PositionPostDate;

public interface PositionPostDateDao  extends AbstractDao<PositionPostDate, String>{
	
	public List<PositionPostDate> getPositionPostDateByPosition(String id);
	public void deleteById(PositionPostDate positionPostDate);
	public void deleteByPosition(int id);
	
	public void deleteByCompany(int id);
	
	public boolean updatePositionPostDate(PositionPostDate positionPostDate);
}
