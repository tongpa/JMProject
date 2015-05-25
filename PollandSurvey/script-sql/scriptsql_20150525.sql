ALTER TABLE `sur_question_option`
ADD COLUMN `use_question_no`  int NULL DEFAULT 0 COMMENT 'Show Number Question' AFTER `show_score`;

ALTER TABLE `sur_m_question_theme`
ADD COLUMN `show_navigator`  bit(1) NULL DEFAULT 0 AFTER `active`;


