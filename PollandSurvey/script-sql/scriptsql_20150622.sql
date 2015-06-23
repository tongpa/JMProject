ALTER TABLE `sur_log_survey`
CHANGE COLUMN `status` `log_level`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER `ip_server`,
ADD COLUMN `relative_created`  varchar(10) NULL AFTER `ip_server`,
ADD COLUMN `name`  varchar(255) NULL AFTER `relative_created`,
ADD COLUMN `level_text`  varchar(10) NULL AFTER `log_level`,
ADD COLUMN `file_name`  varchar(255) NULL AFTER `message`,
ADD COLUMN `path_name`  varchar(400) NULL AFTER `file_name`,
ADD COLUMN `line_no`  varchar(10) NULL AFTER `path_name`,
ADD COLUMN `milliseconds`  varchar(10) NULL AFTER `line_no`,
ADD COLUMN `exception`  text NULL AFTER `milliseconds`,
ADD COLUMN `thread`  varchar(10) NULL AFTER `exception`;

ALTER TABLE `sur_log_survey`
MODIFY COLUMN `level_text`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER `log_level`,
ADD COLUMN `ip_client`  varchar(20) NULL AFTER `ip_server`;


ALTER TABLE `sur_log_survey`
MODIFY COLUMN `path_name`  text CHARACTER SET utf8 COLLATE utf8_general_ci NULL AFTER `file_name`;

