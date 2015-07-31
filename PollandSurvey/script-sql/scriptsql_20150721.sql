CREATE TABLE `sur_map_voter_external_link` (
  `id_map_voter_external_link` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_use_external_link` bigint(20) DEFAULT NULL,
  `id_user_ref` bigint(20) DEFAULT NULL,
  `id_voter` bigint(20) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_map_voter_external_link`),
  KEY `id_user_external_link` (`id_use_external_link`),
  KEY `id_voter` (`id_voter`),
  CONSTRAINT `sur_map_voter_external_link_ibfk_1` FOREIGN KEY (`id_use_external_link`) REFERENCES `sur_use_external_link` (`id_use_external_link`),
  CONSTRAINT `sur_map_voter_external_link_ibfk_2` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


CREATE TABLE `sur_m_client_project` (
  `id_client_project` bigint(20) NOT NULL AUTO_INCREMENT,
  `descrition` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_client_project`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

 
INSERT INTO `sur_m_client_project` VALUES ('1', 'JM', '1', '2015-07-31 15:34:18', null);



CREATE TABLE `sur_user_client_authen` (
  `id_user_client_authen` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_user` int(20) DEFAULT NULL,
  `client_id` varchar(255) DEFAULT NULL,
  `client_secret` varchar(255) DEFAULT NULL,
  `id_client_project` bigint(20) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_user_client_authen`),
  KEY `id_client_project` (`id_client_project`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `sur_user_client_authen_ibfk_2` FOREIGN KEY (`id_client_project`) REFERENCES `sur_m_client_project` (`id_client_project`),
  CONSTRAINT `sur_user_client_authen_ibfk_3` FOREIGN KEY (`id_user`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;







INSERT INTO `sur_user_client_authen` VALUES ('1', '3', '987654321', '#987654321-123456789', '1', '1', '2015-07-31 15:40:35', null);
