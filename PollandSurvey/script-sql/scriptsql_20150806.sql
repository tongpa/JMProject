CREATE TABLE `sur_user_session_authen` (
  `session_value` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



INSERT INTO `sur_user_session_authen` VALUES (null, '1', '2015-08-05 15:30:02', '2015-08-05 23:30:09', null);



INSERT INTO `sur_sys_config` (`id_sys_config`, `default_code`, `default_value`, `default_type_value`, `code_country`, `active`, `create_date`, `update_date`) VALUES (3, 'expired_session_authen', '5', 'time', 'th', '', NULL, NULL);
