package com.jobsmatcher.company.dao;

 
import java.util.List;
 

import com.jobsmatcher.company.model.Company;
import com.jobsmatcher.company.model.Position;

public interface PositionDao extends AbstractDao<Position, String>{
	public List<Position> getPositionByCompany(String id,int start,int limit, int page);
	public void deleteById(Position position);

	public void deleteByCompany(int id);
	public boolean updatePosition(Position position);
	
	public int getSizePositionByCompany(String id);
}
