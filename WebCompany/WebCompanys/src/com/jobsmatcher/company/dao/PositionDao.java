package com.jobsmatcher.company.dao;

 
import java.util.List;
 


import com.jobsmatcher.company.model.Company;
import com.jobsmatcher.company.model.Position;
import com.jobsmatcher.company.model.ViewPositionPostDate;

public interface PositionDao extends AbstractDao<Position, String>{
	public List<Position> getPositionByCompany(String id,int start,int limit, int page);
	public int getSizePositionByCompany(String id);
	public void deleteById(Position position);

	public void deleteByCompany(int id);
	public boolean updatePosition(Position position);
	
	
	
	public List<ViewPositionPostDate> getPositionPostDateById(int id,int start,int limit, int page);
	public int getSizePositionPostDateById(int id);
}
