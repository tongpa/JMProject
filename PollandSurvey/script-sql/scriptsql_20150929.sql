CREATE TABLE `sur_m_feature` (
`id_feature`  bigint NOT NULL AUTO_INCREMENT ,
`feature_name`  varchar(255) NULL ,
`id_parent`  bigint NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  timestamp DEFAULT CURRENT_TIMESTAMP ,
`update_date`  timestamp NULL ,
PRIMARY KEY (`id_feature`)
)
;

CREATE TABLE `sur_fix_country` (
`id_country`  bigint NOT NULL AUTO_INCREMENT ,
`country_name`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date` timestamp DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY (`id_country`)
)
;

CREATE TABLE `sur_map_project_type_feature` (
`id_project_type_feature`  bigint NOT NULL ,
`id_question_project_type`  bigint NULL ,
`id_feature`  bigint NULL ,
`id_country`  bigint NULL ,
`create_date`  timestamp DEFAULT CURRENT_TIMESTAMP ,
`update_date`  timestamp NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
PRIMARY KEY (`id_project_type_feature`)
)
;


ALTER TABLE `sur_map_project_type_feature` ADD FOREIGN KEY (`id_question_project_type`) REFERENCES `sur_question_project_type` (`id_question_project_type`);

ALTER TABLE `sur_map_project_type_feature` ADD FOREIGN KEY (`id_feature`) REFERENCES `sur_m_feature` (`id_feature`);

ALTER TABLE `sur_map_project_type_feature` ADD FOREIGN KEY (`id_country`) REFERENCES `sur_fix_country` (`id_country`);


INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (1, 'Single Answer Choice', NULL, '', '2015-9-29 17:33:31', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (2, 'Multi Answer Choice', NULL, '', '2015-9-29 17:33:34', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (3, 'Image Single Answer Choice', NULL, '', '2015-9-29 17:33:36', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (4, 'Image Muti Answer Choice', NULL, '', '2015-9-29 17:33:38', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (5, 'Image Question', NULL, '', '2015-9-29 17:47:45', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (6, 'Help Message in Question', NULL, '', '2015-9-29 17:48:05', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (7, 'Answer', NULL, '', '2015-9-29 17:48:59', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (8, 'Score', NULL, '', '2015-9-29 17:49:38', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (9, 'Theme Publication', NULL, '', '2015-9-29 17:49:52', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (10, 'Show Navigator Publication', NULL, '', '2015-9-29 17:50:03', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (11, 'Show Score/Answer Publication', NULL, '', '2015-9-29 17:50:25', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (12, 'Random Questions Publication', NULL, '', '2015-9-29 17:50:34', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (13, 'Random Answer Publication', NULL, '', '2015-9-29 17:50:52', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (14, 'Limit Question Publication', NULL, '', '2015-9-29 17:51:20', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (15, 'Limit Duration Time Publication', NULL, '', '2015-9-29 17:51:33', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (16, 'Start Date Publication', NULL, '', '2015-9-29 17:51:47', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (17, 'Finish Date Publication', NULL, '', '2015-9-29 17:51:56', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (18, 'Welcome Message Publication', NULL, '', '2015-9-29 17:52:09', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (19, 'Goodbye Message Publication', NULL, '', '2015-9-29 17:52:19', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (20, 'Header Message Publication', NULL, '', '2015-9-29 17:52:29', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (21, 'Footer Message Publication', NULL, '', '2015-9-29 17:52:40', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (22, 'Redirect URL Publication', NULL, '', '2015-9-29 17:53:00', NULL);
INSERT INTO `sur_m_feature` (`id_feature`, `feature_name`, `id_parent`, `active`, `create_date`, `update_date`) VALUES (23, 'Email Template Publication', NULL, '', '2015-9-29 17:53:27', NULL);




CREATE TABLE `sur_fix_close_type` (
`id_close_type`  bigint NOT NULL AUTO_INCREMENT ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  timestamp NULL ON UPDATE CURRENT_TIMESTAMP ,
PRIMARY KEY (`id_close_type`)
)
;

ALTER TABLE `sur_question_option`
ADD COLUMN `id_close_type`  bigint NULL AFTER `id_question_invitation`,
ADD FOREIGN KEY (`id_close_type`) REFERENCES `sur_fix_close_type` (`id_close_type`);







