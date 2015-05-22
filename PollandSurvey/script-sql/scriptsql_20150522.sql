ALTER TABLE `sur_basic_question`
ADD COLUMN `score`  int NULL DEFAULT 0 AFTER `order`;

CREATE TABLE `sur_sys_environment` (
`id_sys_environment`  bigint NOT NULL AUTO_INCREMENT ,
`environment_key`  varchar(20) NULL ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  datetime NULL ,
PRIMARY KEY (`id_sys_environment`)
);

CREATE TABLE `sur_fix_difficulty_level` (
`id_fix_difficulty_level`  bigint NOT NULL AUTO_INCREMENT ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  datetime NULL ,
`update_date`  datetime NULL ,
PRIMARY KEY (`id_fix_difficulty_level`)
);
INSERT INTO `sur_fix_difficulty_level` (`id_fix_difficulty_level`, `description`, `active`, `create_date`, `update_date`) VALUES (1, 'Easy', '1', '2015-5-22 14:26:19', NULL);
INSERT INTO `sur_fix_difficulty_level` (`id_fix_difficulty_level`, `description`, `active`, `create_date`, `update_date`) VALUES (2, 'Normal', '1', '2015-5-22 14:26:29', NULL);
INSERT INTO `sur_fix_difficulty_level` (`id_fix_difficulty_level`, `description`, `active`, `create_date`, `update_date`) VALUES (3, 'Hard', '1', '2015-5-22 14:26:37', NULL);


ALTER TABLE `sur_question`
ADD COLUMN `id_fix_difficulty_level`  bigint NULL AFTER `order`;

ALTER TABLE `sur_question` ADD FOREIGN KEY (`id_fix_difficulty_level`) REFERENCES `sur_fix_difficulty_level` (`id_fix_difficulty_level`);

CREATE TABLE `sur_fix_random_type` (
`id_fix_random_type type`  bigint NOT NULL AUTO_INCREMENT ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  datetime NULL ,
`update_date`  datetime NULL ,
PRIMARY KEY (`id_fix_random type`)
);
INSERT INTO `sur_fix_random_type` (`id_fix_random_type`, `description`, `active`, `create_date`, `update_date`) VALUES (1, 'simple random', '1', '2015-5-22 15:57:31', NULL);
INSERT INTO `sur_fix_random_type` (`id_fix_random_type`, `description`, `active`, `create_date`, `update_date`) VALUES (2, 'difficulty level random', '1', '2015-5-22 15:58:42', NULL);


ALTER TABLE `sur_question_option`
ADD COLUMN `id_fix_random_type`  bigint NULL AFTER `id_question_invitation`;

ALTER TABLE `sur_question_option` ADD FOREIGN KEY (`id_fix_random_type`) REFERENCES `sur_fix_random_type` (`id_fix_random_type`);

ALTER TABLE `sur_question_option`
ADD COLUMN `show_score`  bit(1) NULL DEFAULT 0 AFTER `gen_code`;

ALTER TABLE `sur_question_option`
ADD COLUMN `random_answer`  bit(1) NULL DEFAULT 1 AFTER `id_fix_random_type`;



