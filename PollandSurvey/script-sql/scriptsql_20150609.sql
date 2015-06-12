CREATE TABLE `sur_log_survey` (
`id_log_survey`  bigint NOT NULL AUTO_INCREMENT ,
`ip_server`  varchar(20) NULL ,
`status`  varchar(20) NULL ,
'user_name' varchar(255) NULL ,
`message`  text NULL ,
`current_page`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  datetime NULL ,
PRIMARY KEY (`id_log_survey`),
INDEX (`ip_server`) ,
INDEX (`status`) ,
INDEX (`create_date`) 
)
;
