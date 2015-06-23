CREATE TABLE `sur_use_external_link` (
`id_use_external_link`  bigint NOT NULL AUTO_INCREMENT ,
`id_user`  bigint NULL ,
`user_name`  varchar(255) NULL ,
`user_type`  varchar(255) NULL ,
`id_test`  bigint NULL ,
`no_test`  int NULL ,
`id_question_option`  bigint NULL ,
`create_date`  datetime NULL ,
PRIMARY KEY (`id_use_external_link`)
)
;


ALTER TABLE `sur_use_external_link`
ADD COLUMN `active`  bit(1) NULL DEFAULT 1 AFTER `id_question_option`;


ALTER TABLE `sur_question_option`
ADD COLUMN `use_default`  bit(1) NULL DEFAULT 0 AFTER `show_navigator`;


ALTER TABLE `sur_question_option`
ADD COLUMN `no_use`  int NULL DEFAULT 0 AFTER `use_default`;




