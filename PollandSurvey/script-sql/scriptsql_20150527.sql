ALTER TABLE `sur_question_option`
	CHANGE COLUMN `limit_time` `duration_time` INT(11) NULL DEFAULT '0' AFTER `use_question_no`;
	
	
insert into sur_m_language_label( module,default_label,message_en,message_th,active) values('survey.label', 'duration_time', 'Duration Time (Minute)', 'ระยะเวลา (นาที)', 1);
insert into sur_m_language_label( module,default_label,message_en,message_th,active) values('survey.label', 'minute', 'Minutes', 'นาที', 1);

insert into sur_m_language_label( module,default_label,message_en,message_th,active) values('survey.message', 'help_duration_time', 'set 0 is not defined', '0 ไม่กำหนดเวลา', 1);