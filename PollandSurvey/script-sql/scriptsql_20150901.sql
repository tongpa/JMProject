CREATE TABLE `sur_send_mail` (
`id_send_mail`  bigint NOT NULL AUTO_INCREMENT,
`id_question_option`  bigint NULL ,
`id_voter`  bigint NULL ,
`user_id`  int NULL ,
`sender_name`  varchar(255) NULL ,
`receive`  varchar(255) NULL ,
`subject`  varchar(255) NULL ,
`content`  text NULL ,
`status`  varchar(1) NULL ,
`send_date`  datetime NULL ,
`sended_date`  datetime NULL ,
`create_date`  datetime NULL ,
`create_user`  varchar(255) NULL ,
PRIMARY KEY (`id_send_mail`),
INDEX (`id_question_option`) ,
INDEX (`id_voter`) ,
INDEX (`user_id`) 
)
;
