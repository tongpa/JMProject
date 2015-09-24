package com.jobsmatcher.company.dao.impl;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import com.jobsmatcher.company.model.Position;
import com.jobsmatcher.company.model.PositionPostDate;
import com.jobsmatcher.company.model.ViewPositionPostDate;
import com.jobsmatcher.company.dao.PositionPostDateDao;
@Repository
public class PositionPostDateImpl extends AbstractDaoImpl<PositionPostDate, String> implements PositionPostDateDao{
	
	final static Logger logger = Logger.getLogger(PositionPostDateImpl.class); 
	protected PositionPostDateImpl() {
		
        super(PositionPostDate.class);
        
        
    }

	@SuppressWarnings("unchecked")
	@Transactional(readOnly=true)
	@Override
	public List<PositionPostDate> findAll() {
		return (List<PositionPostDate>) getCurrentSession().createQuery("from PositionPostDate c  order by c.post_date desc").list(); 
	}

	@Override
	public PositionPostDate findByName(String name) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	@Transactional(readOnly=true)
	@SuppressWarnings("unchecked")
	public List<PositionPostDate> getPositionPostDateByPosition(String id) {
		List<PositionPostDate> users = new ArrayList<PositionPostDate>();
		//System.out.println("company id :" + id); 
		
		String sql = "from PositionPostDate c where id_position = " + id + " order by c.post_date desc ";
		users = getCurrentSession()
			.createQuery(sql)
			//.setParameter(0, id)
			.list();
 	
		 return users;
	}

	@Override
	public void deleteById(PositionPostDate positionPostDate) {
		StringBuffer sb = new StringBuffer();
		sb.append("delete from job_position_post_date where id_position_post_date = ").append(positionPostDate.getId_position_post_date());
		
		int v = getCurrentSession().createSQLQuery(sb.toString()).executeUpdate(); 
		
		logger.info("Delete job_position_post_date : " + v);
	}

	@Override
	public void deleteByPosition(int id) {
		StringBuffer sb = new StringBuffer();
		sb.append("delete from job_position_post_date where id_position = ").append(id);
		
		int v = getCurrentSession().createSQLQuery(sb.toString()).executeUpdate(); 
		logger.info("delete job_position_post_date : " + v);
		
	}

	@Override
	public boolean updatePositionPostDate(PositionPostDate positionPostDate) {
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
	   
		
		StringBuffer sb = new StringBuffer();
		sb.append("update job_position_post_date set ");
		sb.append("id_position = '" ).append( positionPostDate.getId_position()  ).append( "'"  ).append( " , ");
		
		sb.append("post_date = '"  ).append(df.format(positionPostDate.getPost_date())   ).append( "'").append( " , ");
		
		
		sb.append(" where id_position_post_date = '" + positionPostDate.getId_position_post_date()+ "'");
		
		int v = getCurrentSession().createSQLQuery(sb.toString()).executeUpdate(); 
		 //System.out.println(v);
		//getCurrentSession().update(newCom);
		 
		//System.out.println(serial);
		 sb = null;
		 df = null;
		return true;
	}

	@Override
	public void deleteByCompany(int id) {
		StringBuffer sb = new StringBuffer();
		sb.append("delete from  job_position_post_date  where job_position_post_date.id_position in  (select job_position.id_position from job_position where job_position.id_company_data = ").append(id).append(")");
		
		int v = getCurrentSession().createSQLQuery(sb.toString()).executeUpdate(); 
		logger.info("delete job_position_post_date : " + v);
		
	}

	@Override
	public List<ViewPositionPostDate> getViewPositionPostBateByPosition(
			String id) {
		
		return null;
	}

	@Override
	public void deleteById(int id) {
		StringBuffer sb = new StringBuffer();
		sb.append("delete from job_position_post_date where id_position_post_date = ").append(id);
		
		int v = getCurrentSession().createSQLQuery(sb.toString()).executeUpdate(); 
		logger.info("delete job_position_post_date : " + v);
		
	}
 
}
