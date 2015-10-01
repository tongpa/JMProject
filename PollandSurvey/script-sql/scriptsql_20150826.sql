ALTER TABLE `sur_user`
ADD COLUMN `birthdate`  date NULL AFTER `last_name`,
ADD COLUMN `language`  varchar(255) NULL AFTER `birthdate`;