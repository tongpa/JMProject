ALTER TABLE `sur_log_survey`
MODIFY COLUMN `thread`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER `exception`;


ALTER TABLE `sur_respondents`
ADD COLUMN `key_gen`  varchar(255) NULL AFTER `id_question_option`,
ADD INDEX (`key_gen`) ;

