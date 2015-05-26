ALTER TABLE `sur_question_option`
ADD COLUMN `use_question_no`  int NULL DEFAULT 0 COMMENT 'Show Number Question' AFTER `show_score`;

ALTER TABLE `sur_m_question_theme`
ADD COLUMN `show_navigator`  bit(1) NULL DEFAULT 0 AFTER `active`;


insert into sur_m_language_label( module,default_label,message_en,message_th,active) values('survey.label', 'use_question_no', 'Question No.', 'จำนวนคำถาม', 1);
insert into sur_m_language_label( module,default_label,message_en,message_th,active) values('survey.label', 'all', 'All', 'ทั้งหมด', 1);