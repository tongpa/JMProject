CREATE TABLE `sur_sys_feature_create` (
`id_sys_feature_create`  bigint NOT NULL AUTO_INCREMENT ,
`no_feature`  varchar(20) NULL ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  datetime NULL ,
`update_date`  datetime NULL ,
PRIMARY KEY (`id_sys_feature_create`)
);

