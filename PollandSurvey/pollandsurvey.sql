/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : pollandsurvey

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2015-06-12 19:43:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for migrate_version
-- ----------------------------
DROP TABLE IF EXISTS `migrate_version`;
CREATE TABLE `migrate_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of migrate_version
-- ----------------------------

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` text,
  `year` int(11) DEFAULT NULL,
  `genre` int(11) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of movie
-- ----------------------------

-- ----------------------------
-- Table structure for sur_address
-- ----------------------------
DROP TABLE IF EXISTS `sur_address`;
CREATE TABLE `sur_address` (
  `id_address` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_address_type` bigint(20) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id_voter` bigint(20) NOT NULL,
  PRIMARY KEY (`id_address`),
  KEY `ix_sur_address_id_address_type` (`id_address_type`),
  KEY `ix_sur_address_id_voter` (`id_voter`),
  CONSTRAINT `sur_address_ibfk_1` FOREIGN KEY (`id_address_type`) REFERENCES `sur_m_address_type` (`id_address_type`),
  CONSTRAINT `sur_address_ibfk_2` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_address
-- ----------------------------

-- ----------------------------
-- Table structure for sur_basic_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_basic_data`;
CREATE TABLE `sur_basic_data` (
  `id_basic_data` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_basic_data_type` bigint(20) NOT NULL,
  PRIMARY KEY (`id_basic_data`),
  KEY `fk_basic_data_type_sur_basic_data_1` (`id_basic_data_type`),
  CONSTRAINT `fk_basic_data_type_sur_basic_data_1` FOREIGN KEY (`id_basic_data_type`) REFERENCES `sur_m_basic_data_type` (`id_basic_data_type`)
) ENGINE=InnoDB AUTO_INCREMENT=695 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_basic_data
-- ----------------------------
INSERT INTO `sur_basic_data` VALUES ('148', '1');
INSERT INTO `sur_basic_data` VALUES ('149', '1');
INSERT INTO `sur_basic_data` VALUES ('150', '1');
INSERT INTO `sur_basic_data` VALUES ('151', '1');
INSERT INTO `sur_basic_data` VALUES ('152', '1');
INSERT INTO `sur_basic_data` VALUES ('153', '1');
INSERT INTO `sur_basic_data` VALUES ('154', '1');
INSERT INTO `sur_basic_data` VALUES ('155', '1');
INSERT INTO `sur_basic_data` VALUES ('156', '1');
INSERT INTO `sur_basic_data` VALUES ('157', '1');
INSERT INTO `sur_basic_data` VALUES ('158', '1');
INSERT INTO `sur_basic_data` VALUES ('159', '1');
INSERT INTO `sur_basic_data` VALUES ('160', '1');
INSERT INTO `sur_basic_data` VALUES ('161', '1');
INSERT INTO `sur_basic_data` VALUES ('162', '1');
INSERT INTO `sur_basic_data` VALUES ('163', '1');
INSERT INTO `sur_basic_data` VALUES ('164', '1');
INSERT INTO `sur_basic_data` VALUES ('166', '1');
INSERT INTO `sur_basic_data` VALUES ('167', '1');
INSERT INTO `sur_basic_data` VALUES ('168', '1');
INSERT INTO `sur_basic_data` VALUES ('169', '1');
INSERT INTO `sur_basic_data` VALUES ('276', '1');
INSERT INTO `sur_basic_data` VALUES ('277', '1');
INSERT INTO `sur_basic_data` VALUES ('278', '1');
INSERT INTO `sur_basic_data` VALUES ('279', '1');
INSERT INTO `sur_basic_data` VALUES ('280', '1');
INSERT INTO `sur_basic_data` VALUES ('281', '1');
INSERT INTO `sur_basic_data` VALUES ('282', '1');
INSERT INTO `sur_basic_data` VALUES ('293', '1');
INSERT INTO `sur_basic_data` VALUES ('294', '1');
INSERT INTO `sur_basic_data` VALUES ('295', '1');
INSERT INTO `sur_basic_data` VALUES ('296', '1');
INSERT INTO `sur_basic_data` VALUES ('404', '1');
INSERT INTO `sur_basic_data` VALUES ('405', '1');
INSERT INTO `sur_basic_data` VALUES ('406', '1');
INSERT INTO `sur_basic_data` VALUES ('407', '1');
INSERT INTO `sur_basic_data` VALUES ('408', '1');
INSERT INTO `sur_basic_data` VALUES ('409', '1');
INSERT INTO `sur_basic_data` VALUES ('410', '1');
INSERT INTO `sur_basic_data` VALUES ('411', '1');
INSERT INTO `sur_basic_data` VALUES ('412', '1');
INSERT INTO `sur_basic_data` VALUES ('413', '1');
INSERT INTO `sur_basic_data` VALUES ('414', '1');
INSERT INTO `sur_basic_data` VALUES ('415', '1');
INSERT INTO `sur_basic_data` VALUES ('416', '1');
INSERT INTO `sur_basic_data` VALUES ('417', '1');
INSERT INTO `sur_basic_data` VALUES ('418', '1');
INSERT INTO `sur_basic_data` VALUES ('419', '1');
INSERT INTO `sur_basic_data` VALUES ('420', '1');
INSERT INTO `sur_basic_data` VALUES ('421', '1');
INSERT INTO `sur_basic_data` VALUES ('422', '1');
INSERT INTO `sur_basic_data` VALUES ('423', '1');
INSERT INTO `sur_basic_data` VALUES ('424', '1');
INSERT INTO `sur_basic_data` VALUES ('425', '1');
INSERT INTO `sur_basic_data` VALUES ('426', '1');
INSERT INTO `sur_basic_data` VALUES ('427', '1');
INSERT INTO `sur_basic_data` VALUES ('428', '1');
INSERT INTO `sur_basic_data` VALUES ('429', '1');
INSERT INTO `sur_basic_data` VALUES ('430', '1');
INSERT INTO `sur_basic_data` VALUES ('431', '1');
INSERT INTO `sur_basic_data` VALUES ('432', '1');
INSERT INTO `sur_basic_data` VALUES ('433', '1');
INSERT INTO `sur_basic_data` VALUES ('434', '1');
INSERT INTO `sur_basic_data` VALUES ('435', '1');
INSERT INTO `sur_basic_data` VALUES ('436', '1');
INSERT INTO `sur_basic_data` VALUES ('437', '1');
INSERT INTO `sur_basic_data` VALUES ('438', '1');
INSERT INTO `sur_basic_data` VALUES ('439', '1');
INSERT INTO `sur_basic_data` VALUES ('440', '1');
INSERT INTO `sur_basic_data` VALUES ('441', '1');
INSERT INTO `sur_basic_data` VALUES ('442', '1');
INSERT INTO `sur_basic_data` VALUES ('443', '1');
INSERT INTO `sur_basic_data` VALUES ('444', '1');
INSERT INTO `sur_basic_data` VALUES ('445', '1');
INSERT INTO `sur_basic_data` VALUES ('446', '1');
INSERT INTO `sur_basic_data` VALUES ('447', '1');
INSERT INTO `sur_basic_data` VALUES ('448', '1');
INSERT INTO `sur_basic_data` VALUES ('449', '1');
INSERT INTO `sur_basic_data` VALUES ('450', '1');
INSERT INTO `sur_basic_data` VALUES ('451', '1');
INSERT INTO `sur_basic_data` VALUES ('452', '1');
INSERT INTO `sur_basic_data` VALUES ('453', '1');
INSERT INTO `sur_basic_data` VALUES ('454', '1');
INSERT INTO `sur_basic_data` VALUES ('455', '1');
INSERT INTO `sur_basic_data` VALUES ('456', '1');
INSERT INTO `sur_basic_data` VALUES ('457', '1');
INSERT INTO `sur_basic_data` VALUES ('458', '1');
INSERT INTO `sur_basic_data` VALUES ('459', '1');
INSERT INTO `sur_basic_data` VALUES ('460', '1');
INSERT INTO `sur_basic_data` VALUES ('461', '1');
INSERT INTO `sur_basic_data` VALUES ('462', '1');
INSERT INTO `sur_basic_data` VALUES ('463', '1');
INSERT INTO `sur_basic_data` VALUES ('464', '1');
INSERT INTO `sur_basic_data` VALUES ('465', '1');
INSERT INTO `sur_basic_data` VALUES ('466', '1');
INSERT INTO `sur_basic_data` VALUES ('467', '1');
INSERT INTO `sur_basic_data` VALUES ('468', '1');
INSERT INTO `sur_basic_data` VALUES ('469', '1');
INSERT INTO `sur_basic_data` VALUES ('470', '1');
INSERT INTO `sur_basic_data` VALUES ('471', '1');
INSERT INTO `sur_basic_data` VALUES ('472', '1');
INSERT INTO `sur_basic_data` VALUES ('473', '1');
INSERT INTO `sur_basic_data` VALUES ('474', '1');
INSERT INTO `sur_basic_data` VALUES ('475', '1');
INSERT INTO `sur_basic_data` VALUES ('476', '1');
INSERT INTO `sur_basic_data` VALUES ('477', '1');
INSERT INTO `sur_basic_data` VALUES ('478', '1');
INSERT INTO `sur_basic_data` VALUES ('479', '1');
INSERT INTO `sur_basic_data` VALUES ('480', '1');
INSERT INTO `sur_basic_data` VALUES ('481', '1');
INSERT INTO `sur_basic_data` VALUES ('482', '1');
INSERT INTO `sur_basic_data` VALUES ('483', '1');
INSERT INTO `sur_basic_data` VALUES ('484', '1');
INSERT INTO `sur_basic_data` VALUES ('485', '1');
INSERT INTO `sur_basic_data` VALUES ('486', '1');
INSERT INTO `sur_basic_data` VALUES ('487', '1');
INSERT INTO `sur_basic_data` VALUES ('488', '1');
INSERT INTO `sur_basic_data` VALUES ('489', '1');
INSERT INTO `sur_basic_data` VALUES ('490', '1');
INSERT INTO `sur_basic_data` VALUES ('491', '1');
INSERT INTO `sur_basic_data` VALUES ('492', '1');
INSERT INTO `sur_basic_data` VALUES ('493', '1');
INSERT INTO `sur_basic_data` VALUES ('494', '1');
INSERT INTO `sur_basic_data` VALUES ('495', '1');
INSERT INTO `sur_basic_data` VALUES ('496', '1');
INSERT INTO `sur_basic_data` VALUES ('497', '1');
INSERT INTO `sur_basic_data` VALUES ('498', '1');
INSERT INTO `sur_basic_data` VALUES ('499', '1');
INSERT INTO `sur_basic_data` VALUES ('500', '1');
INSERT INTO `sur_basic_data` VALUES ('501', '1');
INSERT INTO `sur_basic_data` VALUES ('502', '1');
INSERT INTO `sur_basic_data` VALUES ('503', '1');
INSERT INTO `sur_basic_data` VALUES ('504', '1');
INSERT INTO `sur_basic_data` VALUES ('505', '1');
INSERT INTO `sur_basic_data` VALUES ('506', '1');
INSERT INTO `sur_basic_data` VALUES ('507', '1');
INSERT INTO `sur_basic_data` VALUES ('508', '1');
INSERT INTO `sur_basic_data` VALUES ('509', '1');
INSERT INTO `sur_basic_data` VALUES ('510', '1');
INSERT INTO `sur_basic_data` VALUES ('511', '1');
INSERT INTO `sur_basic_data` VALUES ('512', '1');
INSERT INTO `sur_basic_data` VALUES ('513', '1');
INSERT INTO `sur_basic_data` VALUES ('514', '1');
INSERT INTO `sur_basic_data` VALUES ('515', '1');
INSERT INTO `sur_basic_data` VALUES ('516', '1');
INSERT INTO `sur_basic_data` VALUES ('517', '1');
INSERT INTO `sur_basic_data` VALUES ('518', '1');
INSERT INTO `sur_basic_data` VALUES ('519', '1');
INSERT INTO `sur_basic_data` VALUES ('520', '1');
INSERT INTO `sur_basic_data` VALUES ('521', '1');
INSERT INTO `sur_basic_data` VALUES ('522', '1');
INSERT INTO `sur_basic_data` VALUES ('523', '1');
INSERT INTO `sur_basic_data` VALUES ('524', '1');
INSERT INTO `sur_basic_data` VALUES ('525', '1');
INSERT INTO `sur_basic_data` VALUES ('526', '1');
INSERT INTO `sur_basic_data` VALUES ('527', '1');
INSERT INTO `sur_basic_data` VALUES ('528', '1');
INSERT INTO `sur_basic_data` VALUES ('529', '1');
INSERT INTO `sur_basic_data` VALUES ('530', '1');
INSERT INTO `sur_basic_data` VALUES ('531', '1');
INSERT INTO `sur_basic_data` VALUES ('532', '1');
INSERT INTO `sur_basic_data` VALUES ('533', '1');
INSERT INTO `sur_basic_data` VALUES ('534', '1');
INSERT INTO `sur_basic_data` VALUES ('535', '1');
INSERT INTO `sur_basic_data` VALUES ('536', '1');
INSERT INTO `sur_basic_data` VALUES ('537', '1');
INSERT INTO `sur_basic_data` VALUES ('538', '1');
INSERT INTO `sur_basic_data` VALUES ('539', '1');
INSERT INTO `sur_basic_data` VALUES ('540', '1');
INSERT INTO `sur_basic_data` VALUES ('541', '1');
INSERT INTO `sur_basic_data` VALUES ('542', '1');
INSERT INTO `sur_basic_data` VALUES ('543', '1');
INSERT INTO `sur_basic_data` VALUES ('544', '1');
INSERT INTO `sur_basic_data` VALUES ('545', '1');
INSERT INTO `sur_basic_data` VALUES ('546', '1');
INSERT INTO `sur_basic_data` VALUES ('547', '1');
INSERT INTO `sur_basic_data` VALUES ('548', '1');
INSERT INTO `sur_basic_data` VALUES ('549', '1');
INSERT INTO `sur_basic_data` VALUES ('550', '1');
INSERT INTO `sur_basic_data` VALUES ('551', '1');
INSERT INTO `sur_basic_data` VALUES ('552', '1');
INSERT INTO `sur_basic_data` VALUES ('553', '1');
INSERT INTO `sur_basic_data` VALUES ('554', '1');
INSERT INTO `sur_basic_data` VALUES ('555', '1');
INSERT INTO `sur_basic_data` VALUES ('556', '1');
INSERT INTO `sur_basic_data` VALUES ('557', '1');
INSERT INTO `sur_basic_data` VALUES ('558', '1');
INSERT INTO `sur_basic_data` VALUES ('559', '1');
INSERT INTO `sur_basic_data` VALUES ('560', '1');
INSERT INTO `sur_basic_data` VALUES ('561', '1');
INSERT INTO `sur_basic_data` VALUES ('562', '1');
INSERT INTO `sur_basic_data` VALUES ('563', '1');
INSERT INTO `sur_basic_data` VALUES ('564', '1');
INSERT INTO `sur_basic_data` VALUES ('565', '1');
INSERT INTO `sur_basic_data` VALUES ('566', '1');
INSERT INTO `sur_basic_data` VALUES ('567', '1');
INSERT INTO `sur_basic_data` VALUES ('568', '1');
INSERT INTO `sur_basic_data` VALUES ('569', '1');
INSERT INTO `sur_basic_data` VALUES ('570', '1');
INSERT INTO `sur_basic_data` VALUES ('571', '1');
INSERT INTO `sur_basic_data` VALUES ('572', '1');
INSERT INTO `sur_basic_data` VALUES ('573', '1');
INSERT INTO `sur_basic_data` VALUES ('574', '1');
INSERT INTO `sur_basic_data` VALUES ('575', '1');
INSERT INTO `sur_basic_data` VALUES ('576', '1');
INSERT INTO `sur_basic_data` VALUES ('577', '1');
INSERT INTO `sur_basic_data` VALUES ('578', '1');
INSERT INTO `sur_basic_data` VALUES ('579', '1');
INSERT INTO `sur_basic_data` VALUES ('580', '1');
INSERT INTO `sur_basic_data` VALUES ('581', '1');
INSERT INTO `sur_basic_data` VALUES ('582', '1');
INSERT INTO `sur_basic_data` VALUES ('583', '1');
INSERT INTO `sur_basic_data` VALUES ('584', '1');
INSERT INTO `sur_basic_data` VALUES ('585', '1');
INSERT INTO `sur_basic_data` VALUES ('586', '1');
INSERT INTO `sur_basic_data` VALUES ('587', '1');
INSERT INTO `sur_basic_data` VALUES ('588', '1');
INSERT INTO `sur_basic_data` VALUES ('589', '1');
INSERT INTO `sur_basic_data` VALUES ('590', '1');
INSERT INTO `sur_basic_data` VALUES ('591', '1');
INSERT INTO `sur_basic_data` VALUES ('592', '1');
INSERT INTO `sur_basic_data` VALUES ('593', '1');
INSERT INTO `sur_basic_data` VALUES ('594', '1');
INSERT INTO `sur_basic_data` VALUES ('595', '1');
INSERT INTO `sur_basic_data` VALUES ('596', '1');
INSERT INTO `sur_basic_data` VALUES ('597', '1');
INSERT INTO `sur_basic_data` VALUES ('598', '1');
INSERT INTO `sur_basic_data` VALUES ('599', '1');
INSERT INTO `sur_basic_data` VALUES ('600', '1');
INSERT INTO `sur_basic_data` VALUES ('601', '1');
INSERT INTO `sur_basic_data` VALUES ('602', '1');
INSERT INTO `sur_basic_data` VALUES ('603', '1');
INSERT INTO `sur_basic_data` VALUES ('604', '1');
INSERT INTO `sur_basic_data` VALUES ('605', '1');
INSERT INTO `sur_basic_data` VALUES ('606', '1');
INSERT INTO `sur_basic_data` VALUES ('607', '1');
INSERT INTO `sur_basic_data` VALUES ('608', '1');
INSERT INTO `sur_basic_data` VALUES ('609', '1');
INSERT INTO `sur_basic_data` VALUES ('610', '1');
INSERT INTO `sur_basic_data` VALUES ('611', '1');
INSERT INTO `sur_basic_data` VALUES ('612', '1');
INSERT INTO `sur_basic_data` VALUES ('613', '1');
INSERT INTO `sur_basic_data` VALUES ('614', '1');
INSERT INTO `sur_basic_data` VALUES ('615', '1');
INSERT INTO `sur_basic_data` VALUES ('616', '1');
INSERT INTO `sur_basic_data` VALUES ('617', '1');
INSERT INTO `sur_basic_data` VALUES ('618', '1');
INSERT INTO `sur_basic_data` VALUES ('619', '1');
INSERT INTO `sur_basic_data` VALUES ('620', '1');
INSERT INTO `sur_basic_data` VALUES ('621', '1');
INSERT INTO `sur_basic_data` VALUES ('622', '1');
INSERT INTO `sur_basic_data` VALUES ('623', '1');
INSERT INTO `sur_basic_data` VALUES ('624', '1');
INSERT INTO `sur_basic_data` VALUES ('625', '1');
INSERT INTO `sur_basic_data` VALUES ('626', '1');
INSERT INTO `sur_basic_data` VALUES ('627', '1');
INSERT INTO `sur_basic_data` VALUES ('628', '1');
INSERT INTO `sur_basic_data` VALUES ('629', '1');
INSERT INTO `sur_basic_data` VALUES ('630', '1');
INSERT INTO `sur_basic_data` VALUES ('631', '1');
INSERT INTO `sur_basic_data` VALUES ('632', '1');
INSERT INTO `sur_basic_data` VALUES ('633', '1');
INSERT INTO `sur_basic_data` VALUES ('634', '1');
INSERT INTO `sur_basic_data` VALUES ('635', '1');
INSERT INTO `sur_basic_data` VALUES ('636', '1');
INSERT INTO `sur_basic_data` VALUES ('637', '1');
INSERT INTO `sur_basic_data` VALUES ('638', '1');
INSERT INTO `sur_basic_data` VALUES ('639', '1');
INSERT INTO `sur_basic_data` VALUES ('640', '1');
INSERT INTO `sur_basic_data` VALUES ('641', '1');
INSERT INTO `sur_basic_data` VALUES ('642', '1');
INSERT INTO `sur_basic_data` VALUES ('643', '1');
INSERT INTO `sur_basic_data` VALUES ('644', '1');
INSERT INTO `sur_basic_data` VALUES ('645', '1');
INSERT INTO `sur_basic_data` VALUES ('646', '1');
INSERT INTO `sur_basic_data` VALUES ('647', '1');
INSERT INTO `sur_basic_data` VALUES ('648', '1');
INSERT INTO `sur_basic_data` VALUES ('649', '1');
INSERT INTO `sur_basic_data` VALUES ('650', '1');
INSERT INTO `sur_basic_data` VALUES ('651', '1');
INSERT INTO `sur_basic_data` VALUES ('652', '1');
INSERT INTO `sur_basic_data` VALUES ('653', '1');
INSERT INTO `sur_basic_data` VALUES ('654', '1');
INSERT INTO `sur_basic_data` VALUES ('655', '1');
INSERT INTO `sur_basic_data` VALUES ('656', '1');
INSERT INTO `sur_basic_data` VALUES ('657', '1');
INSERT INTO `sur_basic_data` VALUES ('658', '1');
INSERT INTO `sur_basic_data` VALUES ('659', '1');
INSERT INTO `sur_basic_data` VALUES ('660', '1');
INSERT INTO `sur_basic_data` VALUES ('661', '1');
INSERT INTO `sur_basic_data` VALUES ('662', '1');
INSERT INTO `sur_basic_data` VALUES ('663', '1');
INSERT INTO `sur_basic_data` VALUES ('664', '1');
INSERT INTO `sur_basic_data` VALUES ('665', '1');
INSERT INTO `sur_basic_data` VALUES ('666', '1');
INSERT INTO `sur_basic_data` VALUES ('667', '1');
INSERT INTO `sur_basic_data` VALUES ('668', '1');
INSERT INTO `sur_basic_data` VALUES ('669', '1');
INSERT INTO `sur_basic_data` VALUES ('670', '1');
INSERT INTO `sur_basic_data` VALUES ('671', '1');
INSERT INTO `sur_basic_data` VALUES ('672', '1');
INSERT INTO `sur_basic_data` VALUES ('673', '1');
INSERT INTO `sur_basic_data` VALUES ('674', '1');
INSERT INTO `sur_basic_data` VALUES ('675', '1');
INSERT INTO `sur_basic_data` VALUES ('676', '1');
INSERT INTO `sur_basic_data` VALUES ('677', '1');
INSERT INTO `sur_basic_data` VALUES ('678', '1');
INSERT INTO `sur_basic_data` VALUES ('679', '1');
INSERT INTO `sur_basic_data` VALUES ('680', '1');
INSERT INTO `sur_basic_data` VALUES ('681', '1');
INSERT INTO `sur_basic_data` VALUES ('682', '1');
INSERT INTO `sur_basic_data` VALUES ('683', '1');
INSERT INTO `sur_basic_data` VALUES ('684', '1');
INSERT INTO `sur_basic_data` VALUES ('685', '1');
INSERT INTO `sur_basic_data` VALUES ('686', '1');
INSERT INTO `sur_basic_data` VALUES ('687', '1');
INSERT INTO `sur_basic_data` VALUES ('688', '1');
INSERT INTO `sur_basic_data` VALUES ('689', '1');
INSERT INTO `sur_basic_data` VALUES ('690', '1');
INSERT INTO `sur_basic_data` VALUES ('691', '1');
INSERT INTO `sur_basic_data` VALUES ('692', '1');
INSERT INTO `sur_basic_data` VALUES ('693', '1');
INSERT INTO `sur_basic_data` VALUES ('694', '1');
INSERT INTO `sur_basic_data` VALUES ('297', '2');
INSERT INTO `sur_basic_data` VALUES ('298', '2');
INSERT INTO `sur_basic_data` VALUES ('299', '2');
INSERT INTO `sur_basic_data` VALUES ('300', '2');
INSERT INTO `sur_basic_data` VALUES ('361', '4');
INSERT INTO `sur_basic_data` VALUES ('362', '4');
INSERT INTO `sur_basic_data` VALUES ('363', '4');
INSERT INTO `sur_basic_data` VALUES ('364', '4');
INSERT INTO `sur_basic_data` VALUES ('365', '4');
INSERT INTO `sur_basic_data` VALUES ('366', '4');
INSERT INTO `sur_basic_data` VALUES ('367', '4');
INSERT INTO `sur_basic_data` VALUES ('368', '4');
INSERT INTO `sur_basic_data` VALUES ('369', '4');
INSERT INTO `sur_basic_data` VALUES ('370', '4');
INSERT INTO `sur_basic_data` VALUES ('371', '4');
INSERT INTO `sur_basic_data` VALUES ('372', '4');
INSERT INTO `sur_basic_data` VALUES ('373', '4');
INSERT INTO `sur_basic_data` VALUES ('374', '4');
INSERT INTO `sur_basic_data` VALUES ('375', '4');
INSERT INTO `sur_basic_data` VALUES ('376', '4');
INSERT INTO `sur_basic_data` VALUES ('377', '4');
INSERT INTO `sur_basic_data` VALUES ('378', '4');
INSERT INTO `sur_basic_data` VALUES ('379', '4');
INSERT INTO `sur_basic_data` VALUES ('380', '4');
INSERT INTO `sur_basic_data` VALUES ('381', '4');
INSERT INTO `sur_basic_data` VALUES ('382', '4');
INSERT INTO `sur_basic_data` VALUES ('383', '4');
INSERT INTO `sur_basic_data` VALUES ('384', '4');
INSERT INTO `sur_basic_data` VALUES ('385', '4');
INSERT INTO `sur_basic_data` VALUES ('386', '4');
INSERT INTO `sur_basic_data` VALUES ('387', '4');
INSERT INTO `sur_basic_data` VALUES ('388', '4');
INSERT INTO `sur_basic_data` VALUES ('389', '4');
INSERT INTO `sur_basic_data` VALUES ('390', '4');
INSERT INTO `sur_basic_data` VALUES ('391', '4');
INSERT INTO `sur_basic_data` VALUES ('392', '4');
INSERT INTO `sur_basic_data` VALUES ('393', '4');
INSERT INTO `sur_basic_data` VALUES ('394', '4');
INSERT INTO `sur_basic_data` VALUES ('395', '4');
INSERT INTO `sur_basic_data` VALUES ('396', '4');
INSERT INTO `sur_basic_data` VALUES ('397', '4');
INSERT INTO `sur_basic_data` VALUES ('398', '4');
INSERT INTO `sur_basic_data` VALUES ('399', '4');
INSERT INTO `sur_basic_data` VALUES ('400', '4');
INSERT INTO `sur_basic_data` VALUES ('401', '4');
INSERT INTO `sur_basic_data` VALUES ('402', '4');
INSERT INTO `sur_basic_data` VALUES ('403', '4');

-- ----------------------------
-- Table structure for sur_basic_data_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_basic_data_type`;
CREATE TABLE `sur_basic_data_type` (
  `id_basic_data_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_basic_data_type`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='1 radio,2 check,3 text,4 date,5 time,6 number,  7 multimedia';

-- ----------------------------
-- Records of sur_basic_data_type
-- ----------------------------
INSERT INTO `sur_basic_data_type` VALUES ('1', 'Radio', '');
INSERT INTO `sur_basic_data_type` VALUES ('2', 'Check', '');
INSERT INTO `sur_basic_data_type` VALUES ('3', 'Combobox', '');
INSERT INTO `sur_basic_data_type` VALUES ('4', 'Image', '');

-- ----------------------------
-- Table structure for sur_basic_question
-- ----------------------------
DROP TABLE IF EXISTS `sur_basic_question`;
CREATE TABLE `sur_basic_question` (
  `id_question` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_basic_data` bigint(20) NOT NULL,
  `answer` bit(1) DEFAULT b'0',
  `order` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT '0',
  PRIMARY KEY (`id_question`,`id_basic_data`),
  KEY `fk_sur_basic_question_sur_basic_data` (`id_basic_data`),
  CONSTRAINT `fk_sur_basic_question_sur_basic_data` FOREIGN KEY (`id_basic_data`) REFERENCES `sur_basic_data` (`id_basic_data`),
  CONSTRAINT `fk_sur_basic_question_sur_question` FOREIGN KEY (`id_question`) REFERENCES `sur_question` (`id_question`)
) ENGINE=InnoDB AUTO_INCREMENT=214 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_basic_question
-- ----------------------------
INSERT INTO `sur_basic_question` VALUES ('53', '148', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('53', '149', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('53', '150', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('54', '151', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('54', '152', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('54', '153', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('55', '154', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('55', '155', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('55', '156', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('56', '157', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('56', '158', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('56', '159', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('57', '160', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('57', '161', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('57', '162', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('58', '163', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('58', '164', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('58', '166', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('59', '167', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('59', '168', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('59', '169', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('97', '276', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('97', '277', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('97', '278', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('98', '279', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('98', '280', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('98', '281', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('98', '282', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('102', '293', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('102', '294', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('102', '295', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('102', '296', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('103', '297', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('103', '298', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('103', '299', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('103', '300', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('122', '361', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('122', '362', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('122', '363', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('123', '364', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('123', '365', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('123', '366', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('123', '367', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('124', '368', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('124', '369', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('124', '370', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('124', '371', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '372', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '373', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '374', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '375', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '376', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '377', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '378', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('125', '379', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '380', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '381', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '382', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '383', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '384', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '385', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '386', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '387', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '388', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '389', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '390', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('126', '391', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('127', '392', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('127', '393', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('127', '394', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('127', '395', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '396', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '397', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '398', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '399', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '400', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '401', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '402', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('128', '403', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('129', '404', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('129', '405', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('129', '406', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('130', '407', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('130', '408', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('131', '409', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('131', '410', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('132', '411', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('132', '412', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('133', '413', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('133', '414', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('134', '415', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('134', '416', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('135', '417', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('135', '418', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('136', '419', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('136', '420', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('137', '421', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('137', '422', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('138', '423', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('138', '424', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('139', '425', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('139', '426', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('140', '427', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('140', '428', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('141', '429', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('141', '430', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('142', '431', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('142', '432', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('143', '433', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('143', '434', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('144', '435', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('144', '436', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('145', '437', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('145', '438', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('146', '439', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('146', '440', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('147', '441', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('147', '442', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('148', '443', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('148', '444', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('149', '445', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('149', '446', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('150', '447', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('150', '448', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('151', '449', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('151', '450', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('152', '451', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('152', '452', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('153', '453', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('153', '454', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('154', '455', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('154', '456', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('154', '457', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('154', '458', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('155', '459', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('155', '460', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('155', '461', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('155', '462', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('156', '463', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('156', '464', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('156', '465', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('156', '466', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('157', '467', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('157', '468', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('157', '469', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('157', '470', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('158', '471', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('158', '472', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('158', '473', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('158', '474', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('159', '475', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('159', '476', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('159', '477', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('159', '478', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('160', '479', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('160', '480', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('160', '481', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('160', '482', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('161', '483', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('161', '484', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('161', '485', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('161', '486', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('162', '487', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('162', '488', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('162', '489', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('162', '490', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('163', '491', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('163', '492', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('163', '493', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('163', '494', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('164', '495', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('164', '496', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('164', '497', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('164', '498', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('165', '499', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('165', '500', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('165', '501', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('165', '502', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('166', '503', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('166', '504', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('166', '505', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('166', '506', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('167', '507', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('167', '508', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('167', '509', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('167', '510', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('168', '511', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('168', '512', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('168', '513', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('168', '514', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('169', '515', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('169', '516', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('169', '517', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('169', '518', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('170', '519', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('170', '520', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('170', '521', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('170', '522', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('171', '523', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('171', '524', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('171', '525', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('171', '526', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('172', '527', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('172', '528', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('172', '529', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('172', '530', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('173', '531', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('173', '532', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('173', '533', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('173', '534', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('174', '535', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('174', '536', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('174', '537', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('174', '538', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('175', '539', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('175', '540', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('175', '541', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('175', '542', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('176', '543', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('176', '544', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('176', '545', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('176', '546', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('177', '547', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('177', '548', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('177', '549', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('177', '550', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('178', '551', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('178', '552', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('178', '553', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('178', '554', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('179', '555', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('179', '556', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('179', '557', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('179', '558', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('180', '559', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('180', '560', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('180', '561', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('180', '562', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('181', '563', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('181', '564', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('181', '565', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('181', '566', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('182', '567', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('182', '568', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('182', '569', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('182', '570', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('183', '571', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('183', '572', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('183', '573', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('183', '574', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('184', '575', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('184', '576', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('184', '577', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('184', '578', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('185', '579', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('185', '580', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('185', '581', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('185', '582', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('186', '583', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('186', '584', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('186', '585', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('186', '586', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('187', '587', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('187', '588', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('187', '589', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('187', '590', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('188', '591', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('188', '592', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('188', '593', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('188', '594', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('189', '595', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('189', '596', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('189', '597', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('189', '598', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('190', '599', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('190', '600', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('190', '601', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('190', '602', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('191', '603', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('191', '604', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('191', '605', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('191', '606', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('192', '607', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('192', '608', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('192', '609', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('192', '610', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('193', '611', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('193', '612', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('193', '613', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('193', '614', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('194', '615', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('194', '616', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('194', '617', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('194', '618', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('195', '619', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('195', '620', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('195', '621', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('195', '622', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('196', '623', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('196', '624', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('196', '625', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('196', '626', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('197', '627', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('197', '628', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('197', '629', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('197', '630', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('198', '631', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('198', '632', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('198', '633', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('198', '634', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('199', '635', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('199', '636', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('199', '637', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('199', '638', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('200', '639', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('200', '640', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('200', '641', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('200', '642', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('201', '643', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('201', '644', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('201', '645', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('201', '646', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('202', '647', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('202', '648', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('202', '649', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('202', '650', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('203', '651', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('203', '652', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('203', '653', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('203', '654', '', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('204', '655', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('204', '656', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('204', '657', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('204', '658', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('205', '659', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('205', '660', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('205', '661', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('205', '662', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('206', '663', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('206', '664', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('206', '665', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('206', '666', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('207', '667', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('207', '668', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('207', '669', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('207', '670', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('208', '671', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('208', '672', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('208', '673', '', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('208', '674', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('209', '675', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('209', '676', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('209', '677', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('209', '678', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('210', '679', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('210', '680', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('210', '681', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('210', '682', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('211', '683', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('211', '684', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('211', '685', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('211', '686', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('212', '687', '\0', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('212', '688', '', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('212', '689', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('212', '690', '\0', '4', '0');
INSERT INTO `sur_basic_question` VALUES ('213', '691', '', '1', '0');
INSERT INTO `sur_basic_question` VALUES ('213', '692', '\0', '2', '0');
INSERT INTO `sur_basic_question` VALUES ('213', '693', '\0', '3', '0');
INSERT INTO `sur_basic_question` VALUES ('213', '694', '\0', '4', '0');

-- ----------------------------
-- Table structure for sur_boolean_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_boolean_data`;
CREATE TABLE `sur_boolean_data` (
  `id_basic_data` bigint(20) NOT NULL,
  `value` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_basic_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_boolean_data
-- ----------------------------

-- ----------------------------
-- Table structure for sur_fix_difficulty_level
-- ----------------------------
DROP TABLE IF EXISTS `sur_fix_difficulty_level`;
CREATE TABLE `sur_fix_difficulty_level` (
  `id_fix_difficulty_level` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_fix_difficulty_level`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_fix_difficulty_level
-- ----------------------------
INSERT INTO `sur_fix_difficulty_level` VALUES ('1', 'Easy', '', '2015-05-22 14:26:19', null);
INSERT INTO `sur_fix_difficulty_level` VALUES ('2', 'Normal', '', '2015-05-22 14:26:29', null);
INSERT INTO `sur_fix_difficulty_level` VALUES ('3', 'Hard', '', '2015-05-22 14:26:37', null);

-- ----------------------------
-- Table structure for sur_fix_email_template_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_fix_email_template_type`;
CREATE TABLE `sur_fix_email_template_type` (
  `id_email_template_type` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_email_template_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_fix_email_template_type
-- ----------------------------
INSERT INTO `sur_fix_email_template_type` VALUES ('1', 'forgot password', '', '2015-04-09 12:16:54', null);
INSERT INTO `sur_fix_email_template_type` VALUES ('2', 'activate user', '', '2015-04-21 14:14:00', null);

-- ----------------------------
-- Table structure for sur_fix_random_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_fix_random_type`;
CREATE TABLE `sur_fix_random_type` (
  `id_fix_random_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_fix_random_type`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_fix_random_type
-- ----------------------------
INSERT INTO `sur_fix_random_type` VALUES ('1', 'not random', '', '2015-05-22 16:03:45', null);
INSERT INTO `sur_fix_random_type` VALUES ('2', 'simple random', '', '2015-05-22 16:03:58', null);
INSERT INTO `sur_fix_random_type` VALUES ('3', 'difficulty level random', '', '2015-05-29 16:52:35', null);

-- ----------------------------
-- Table structure for sur_group_variables
-- ----------------------------
DROP TABLE IF EXISTS `sur_group_variables`;
CREATE TABLE `sur_group_variables` (
  `id_group_variables` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_group_variables`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_group_variables
-- ----------------------------
INSERT INTO `sur_group_variables` VALUES ('1', 'Geography Base', 'Geography Base', '');
INSERT INTO `sur_group_variables` VALUES ('2', 'Phychological Base', 'Phychological Base', '');
INSERT INTO `sur_group_variables` VALUES ('3', 'Social and Culture Base', 'Social and Culture Base', '');

-- ----------------------------
-- Table structure for sur_language_label
-- ----------------------------
DROP TABLE IF EXISTS `sur_language_label`;
CREATE TABLE `sur_language_label` (
  `id_language_label` int(11) NOT NULL AUTO_INCREMENT,
  `module` varchar(255) DEFAULT NULL,
  `default_label` varchar(255) DEFAULT NULL,
  `message_en` varchar(255) DEFAULT NULL,
  `message_th` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_language_label`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_language_label
-- ----------------------------
INSERT INTO `sur_language_label` VALUES ('1', 'opina.locale', 'yes', 'Yes', 'ใช่', '');
INSERT INTO `sur_language_label` VALUES ('2', 'opina.locale', 'no', 'No', 'ไม่ใช่่', '');

-- ----------------------------
-- Table structure for sur_log_survey
-- ----------------------------
DROP TABLE IF EXISTS `sur_log_survey`;
CREATE TABLE `sur_log_survey` (
  `id_log_survey` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip_server` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `message` text,
  `user_name` varchar(255) DEFAULT NULL,
  `current_page` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_log_survey`),
  KEY `ip_server` (`ip_server`),
  KEY `status` (`status`),
  KEY `create_date` (`create_date`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_log_survey
-- ----------------------------
INSERT INTO `sur_log_survey` VALUES ('1', '127.0.0.1', 'INFO', 'user in group : [u\'managers\', u\'creator\'] ', '<User: name=u\'tong\', email=u\'tong_pa@hotmail.com\', display=u\'tong\'>', 'Login', '', '2015-06-09 15:21:05');
INSERT INTO `sur_log_survey` VALUES ('2', '127.0.0.1', 'INFO', 'redirect to create survey page', '<User: name=u\'tong\', email=u\'tong_pa@hotmail.com\', display=u\'tong\'>', 'Login', '', '2015-06-09 15:21:05');

-- ----------------------------
-- Table structure for sur_member_user
-- ----------------------------
DROP TABLE IF EXISTS `sur_member_user`;
CREATE TABLE `sur_member_user` (
  `id_member_user` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `id_voter` bigint(20) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`id_member_user`),
  KEY `ix_sur_member_user_user_id` (`user_id`),
  KEY `ix_sur_member_user_id_voter` (`id_voter`),
  CONSTRAINT `sur_member_user_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`),
  CONSTRAINT `sur_member_user_ibfk_2` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_member_user
-- ----------------------------
INSERT INTO `sur_member_user` VALUES ('1', '21', '6', '2015-04-27 18:25:21', '0000-00-00 00:00:00');
INSERT INTO `sur_member_user` VALUES ('2', '22', '4', '2015-04-28 11:13:59', '0000-00-00 00:00:00');

-- ----------------------------
-- Table structure for sur_multimedia_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_multimedia_data`;
CREATE TABLE `sur_multimedia_data` (
  `id_basic_data` bigint(20) NOT NULL AUTO_INCREMENT,
  `value` varchar(255) DEFAULT NULL,
  `media_type` varchar(255) DEFAULT NULL COMMENT 'IMAGE,\r\nVIDEO,\r\nSOUND,',
  `media_path_file` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_basic_data`),
  CONSTRAINT `fk_sur_multimedia_data_sur_basic_data_1` FOREIGN KEY (`id_basic_data`) REFERENCES `sur_basic_data` (`id_basic_data`)
) ENGINE=InnoDB AUTO_INCREMENT=404 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_multimedia_data
-- ----------------------------
INSERT INTO `sur_multimedia_data` VALUES ('361', 'answer_1.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\122\\answer_1.png');
INSERT INTO `sur_multimedia_data` VALUES ('362', 'answer_2.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\122\\answer_2.png');
INSERT INTO `sur_multimedia_data` VALUES ('363', 'answer_3.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\122\\answer_3.png');
INSERT INTO `sur_multimedia_data` VALUES ('364', 'answer_3.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\123\\answer_3.png');
INSERT INTO `sur_multimedia_data` VALUES ('365', 'answer_4.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\123\\answer_4.png');
INSERT INTO `sur_multimedia_data` VALUES ('366', 'answer_3.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\123\\answer_3.png');
INSERT INTO `sur_multimedia_data` VALUES ('367', 'answer_4.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\123\\answer_4.png');
INSERT INTO `sur_multimedia_data` VALUES ('368', 'Q01-A1.png', 'image/png', '/usr/local/projects/upload/survey/124/Q01-A1.png');
INSERT INTO `sur_multimedia_data` VALUES ('369', 'Q01-A2.png', 'image/png', '/usr/local/projects/upload/survey/124/Q01-A2.png');
INSERT INTO `sur_multimedia_data` VALUES ('370', 'Q01-A3.png', 'image/png', '/usr/local/projects/upload/survey/124/Q01-A3.png');
INSERT INTO `sur_multimedia_data` VALUES ('371', 'Q01-A4.png', 'image/png', '/usr/local/projects/upload/survey/124/Q01-A4.png');
INSERT INTO `sur_multimedia_data` VALUES ('376', 'Q02-A1.png', 'image/png', '/usr/local/projects/upload/survey/125/Q02-A1.png');
INSERT INTO `sur_multimedia_data` VALUES ('377', 'Q02-A2.png', 'image/png', '/usr/local/projects/upload/survey/125/Q02-A2.png');
INSERT INTO `sur_multimedia_data` VALUES ('378', 'Q02-A3.png', 'image/png', '/usr/local/projects/upload/survey/125/Q02-A3.png');
INSERT INTO `sur_multimedia_data` VALUES ('379', 'Q02-A4.png', 'image/png', '/usr/local/projects/upload/survey/125/Q02-A4.png');
INSERT INTO `sur_multimedia_data` VALUES ('388', 'Q03-A1.png', 'image/png', '/usr/local/projects/upload/survey/126/Q03-A1.png');
INSERT INTO `sur_multimedia_data` VALUES ('389', 'Q03-A2.png', 'image/png', '/usr/local/projects/upload/survey/126/Q03-A2.png');
INSERT INTO `sur_multimedia_data` VALUES ('390', 'Q03-A3.png', 'image/png', '/usr/local/projects/upload/survey/126/Q03-A3.png');
INSERT INTO `sur_multimedia_data` VALUES ('391', 'Q03-A4.png', 'image/png', '/usr/local/projects/upload/survey/126/Q03-A4.png');
INSERT INTO `sur_multimedia_data` VALUES ('392', 'Q04-A1.png', 'image/png', '/usr/local/projects/upload/survey/127/Q04-A1.png');
INSERT INTO `sur_multimedia_data` VALUES ('393', 'Q04-A2.png', 'image/png', '/usr/local/projects/upload/survey/127/Q04-A2.png');
INSERT INTO `sur_multimedia_data` VALUES ('394', 'Q04-A3.png', 'image/png', '/usr/local/projects/upload/survey/127/Q04-A3.png');
INSERT INTO `sur_multimedia_data` VALUES ('395', 'Q04-A4.png', 'image/png', '/usr/local/projects/upload/survey/127/Q04-A4.png');
INSERT INTO `sur_multimedia_data` VALUES ('400', 'Q5-A1.png', 'image/png', '/usr/local/projects/upload/survey/128/Q5-A1.png');
INSERT INTO `sur_multimedia_data` VALUES ('401', 'Q5-A2.png', 'image/png', '/usr/local/projects/upload/survey/128/Q5-A2.png');
INSERT INTO `sur_multimedia_data` VALUES ('402', 'Q5-A3.png', 'image/png', '/usr/local/projects/upload/survey/128/Q5-A3.png');
INSERT INTO `sur_multimedia_data` VALUES ('403', 'Q5-A4.png', 'image/png', '/usr/local/projects/upload/survey/128/Q5-A4.png');

-- ----------------------------
-- Table structure for sur_m_address_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_address_type`;
CREATE TABLE `sur_m_address_type` (
  `id_address_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_address_type`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_address_type
-- ----------------------------

-- ----------------------------
-- Table structure for sur_m_basic_data_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_basic_data_type`;
CREATE TABLE `sur_m_basic_data_type` (
  `id_basic_data_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_basic_data_type`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='1 radio,2 check,3 text,4 date,5 time,6 number,  7 multimedia';

-- ----------------------------
-- Records of sur_m_basic_data_type
-- ----------------------------
INSERT INTO `sur_m_basic_data_type` VALUES ('1', 'Radio', '');
INSERT INTO `sur_m_basic_data_type` VALUES ('2', 'Check', '');
INSERT INTO `sur_m_basic_data_type` VALUES ('3', 'Combobox', '');
INSERT INTO `sur_m_basic_data_type` VALUES ('4', 'Image', '');

-- ----------------------------
-- Table structure for sur_m_email_template
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_email_template`;
CREATE TABLE `sur_m_email_template` (
  `id_email_template` int(11) NOT NULL AUTO_INCREMENT,
  `id_email_template_type` int(11) DEFAULT NULL,
  `sender` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `content_template` text,
  `language` varchar(2) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_email_template`),
  KEY `id_email_template_type` (`id_email_template_type`),
  CONSTRAINT `sur_m_email_template_ibfk_1` FOREIGN KEY (`id_email_template_type`) REFERENCES `sur_fix_email_template_type` (`id_email_template_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_email_template
-- ----------------------------
INSERT INTO `sur_m_email_template` VALUES ('1', '1', 'JM team', 'Forgot Password', 'Dear <b>[user_name]</b> <br/>\r\nYou have requested that we email  your PollSurvey Password. <br/>\r\nHere is your complete login information: <br/>\r\n<br/>\r\naccount : [email]  <br/>\r\npassword : [password]  <br/>\r\n<br/><br/>\r\nSincerely', 'en', '', '2015-04-09 12:29:39', null);
INSERT INTO `sur_m_email_template` VALUES ('2', '2', 'JM Team', 'Activation Your PollSurfvey Account', 'Dear <b>[user_name]</b> <br/>\r\nVerify your email address to complete your Pollsurfvey Account registration. <br/>\r\n[activate_url]\r\n<br/>\r\naccount : [email]  <br/>\r\npassword : [password] <br/>\r\n<br/>\r\nthank you. <br/>\r\nJM Team', 'en', '', '2015-04-20 18:07:17', null);

-- ----------------------------
-- Table structure for sur_m_gender
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_gender`;
CREATE TABLE `sur_m_gender` (
  `id_gender` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_gender`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_gender
-- ----------------------------
INSERT INTO `sur_m_gender` VALUES ('1', 'Male', '');
INSERT INTO `sur_m_gender` VALUES ('2', 'Fremale', '');

-- ----------------------------
-- Table structure for sur_m_group_variables
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_group_variables`;
CREATE TABLE `sur_m_group_variables` (
  `id_group_variables` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_group_variables`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_group_variables
-- ----------------------------
INSERT INTO `sur_m_group_variables` VALUES ('1', 'Geography Base', 'Geography Base', '');
INSERT INTO `sur_m_group_variables` VALUES ('2', 'Phychological Base', 'Phychological Base', '');
INSERT INTO `sur_m_group_variables` VALUES ('3', 'Social and Culture Base', 'Social and Culture Base', '');

-- ----------------------------
-- Table structure for sur_m_language
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_language`;
CREATE TABLE `sur_m_language` (
  `id_language` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'TB:JOB_N_LANGUAGE, ',
  `seq` smallint(6) DEFAULT NULL,
  `code2` char(2) DEFAULT NULL,
  `code3` char(3) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `name_local` varchar(255) DEFAULT NULL,
  `status` char(1) DEFAULT 'A',
  `create_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `create_user` varchar(255) DEFAULT NULL,
  `update_date` timestamp NULL DEFAULT NULL,
  `update_user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_language`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_language
-- ----------------------------
INSERT INTO `sur_m_language` VALUES ('1', null, 'TH', 'THA', 'Thai', 'ไทย', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('2', null, 'EN', 'ENG', 'English', 'English', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('3', null, 'FR', 'FRE', 'French', 'français', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('4', null, 'DE', 'DEU', 'German', 'Deutsch', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('5', null, 'ZH', 'ZHO', 'Chinese (Mandarin)', '官話/官话', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('6', null, 'ES', 'SPA', 'Spainish', 'Español', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('7', null, 'JA', 'JPN', '日本語', '4444', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('8', null, 'HI', 'HIN', 'Indian (Hindi)', 'हिन्दी', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('9', null, 'ID', 'IND', 'Bahasa (Indonesia)', 'Bahasa Indonesia', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('10', null, 'PT', 'POR', 'Portuguese', 'Português', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('11', null, 'RU', 'RUS', 'Russian', 'Русский', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('12', null, 'IT', 'ITA', 'Italian', 'Italiano', 'A', '2014-08-06 18:36:14', 'SYSTEM', null, null);
INSERT INTO `sur_m_language` VALUES ('13', null, 'KO', 'KOR', 'Korean', '한국의', 'A', '2014-12-08 12:10:16', 'SYSTEM', null, null);

-- ----------------------------
-- Table structure for sur_m_language_label
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_language_label`;
CREATE TABLE `sur_m_language_label` (
  `id_language_label` int(11) NOT NULL AUTO_INCREMENT,
  `module` varchar(255) DEFAULT NULL,
  `default_label` varchar(255) DEFAULT NULL,
  `message_en` varchar(255) DEFAULT NULL,
  `message_th` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_language_label`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_language_label
-- ----------------------------
INSERT INTO `sur_m_language_label` VALUES ('1', 'survey.label', 'yes', 'Yes', 'ใช่', '');
INSERT INTO `sur_m_language_label` VALUES ('2', 'survey.label', 'no', 'No', 'ไม่ใช่่', '');
INSERT INTO `sur_m_language_label` VALUES ('3', 'survey.label', 'contact', 'Contacts', 'ผู้ติดต่อ', '');
INSERT INTO `sur_m_language_label` VALUES ('4', 'survey.label', 'create_question', 'Create Questions', 'สร้างคำถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('5', 'survey.label', 'create_variable', 'Create Variable', 'สร้างตัวแปร', '');
INSERT INTO `sur_m_language_label` VALUES ('6', 'survey.label', 'create_publication', 'Publication', 'เผยแพร่', '');
INSERT INTO `sur_m_language_label` VALUES ('7', 'survey.label', 'poll_survey', 'Poll and Survey', 'แบบสำรวจ และสอบถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('8', 'survey.label', 'project', 'Project', 'โครงงาน', '');
INSERT INTO `sur_m_language_label` VALUES ('9', 'survey.label', 'add', 'Add', 'เพิ่ม', '');
INSERT INTO `sur_m_language_label` VALUES ('10', 'survey.label', 'delete', 'Delete', 'ลบ', '');
INSERT INTO `sur_m_language_label` VALUES ('11', 'survey.label', 'refresh', 'Refresh', 'ทำใหม่', '');
INSERT INTO `sur_m_language_label` VALUES ('12', 'survey.label', 'save', 'Save', 'บันทึก', '');
INSERT INTO `sur_m_language_label` VALUES ('13', 'survey.message', 'confirm_delete', 'Do you delete : ', 'ต้องการลบหรือไม่ :', '');
INSERT INTO `sur_m_language_label` VALUES ('14', 'survey.message', 'failed', 'Failed', 'ล้มแหลว', '');
INSERT INTO `sur_m_language_label` VALUES ('15', 'survey.message', 'waiting_save', 'Save your Data...', 'กำลังบันทึก', '');
INSERT INTO `sur_m_language_label` VALUES ('16', 'survey.message', 'success', 'Success', 'สำเร็จ', '');
INSERT INTO `sur_m_language_label` VALUES ('17', 'survey.label', 'close', 'Close', 'ปิด', '');
INSERT INTO `sur_m_language_label` VALUES ('18', 'survey.label', 'name', 'Name', 'ชื่อ', '');
INSERT INTO `sur_m_language_label` VALUES ('19', 'survey.label', 'start_date', 'Start Date', 'วันที่เริ่ม', '');
INSERT INTO `sur_m_language_label` VALUES ('20', 'survey.label', 'expire_date', 'Expire Date', 'วันที่สิ้นสุด', '');
INSERT INTO `sur_m_language_label` VALUES ('21', 'survey.label', 'redirect_url', 'Redirect URL', 'เปลี่ยนไปยัง URL', '');
INSERT INTO `sur_m_language_label` VALUES ('22', 'survey.label', 'theme', 'Theme', 'รูปแบบการแสดง', '');
INSERT INTO `sur_m_language_label` VALUES ('23', 'survey.label', 'welcome_message', 'Welcome Message', 'ข้อความต้อนรับ', '');
INSERT INTO `sur_m_language_label` VALUES ('24', 'survey.label', 'goodbye_message', 'Goodbye Message', 'ข้อความกล่าวลา', '');
INSERT INTO `sur_m_language_label` VALUES ('25', 'survey.label', 'header_message', 'Header Message', 'ข้อความบนหัว', '');
INSERT INTO `sur_m_language_label` VALUES ('26', 'survey.label', 'footer_message', 'Footer Message', 'ข้อความด้านล่าง', '');
INSERT INTO `sur_m_language_label` VALUES ('27', 'survey.label', 'project_name', 'Project Name', 'ชื่อโปรแจกต์', '');
INSERT INTO `sur_m_language_label` VALUES ('28', 'survey.label', 'description', 'Description', 'คำบรรยาย', '');
INSERT INTO `sur_m_language_label` VALUES ('29', 'survey.label', 'project_type', 'Project Type', 'ประเภทโครงการ', '');
INSERT INTO `sur_m_language_label` VALUES ('30', 'survey.label', 'please_select', 'Please Select', 'กรุณาเลือก', '');
INSERT INTO `sur_m_language_label` VALUES ('31', 'survey.label', 'detail', 'Details', 'รายละเอียด', '');
INSERT INTO `sur_m_language_label` VALUES ('32', 'survey.label', 'add_project', 'Add Project', 'เพิ่มโครงการ', '');
INSERT INTO `sur_m_language_label` VALUES ('33', 'survey.label', 'view', 'View', 'แสดง', '');
INSERT INTO `sur_m_language_label` VALUES ('34', 'survey.label', 'edit', 'Edit', 'แก้ไข', '');
INSERT INTO `sur_m_language_label` VALUES ('35', 'survey.label', 'question', 'Question', 'คำถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('36', 'survey.label', 'help_message', 'Help Message', 'ข้อความช่วยเหลือ', '');
INSERT INTO `sur_m_language_label` VALUES ('37', 'survey.label', 'image', 'Image ', 'รูปภาพ ', '');
INSERT INTO `sur_m_language_label` VALUES ('38', 'survey.label', 'question_type', 'Question Type', 'รูปแบบคำถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('39', 'survey.label', 'move_up', 'Move Up', 'เลื่อนขึ้น', '');
INSERT INTO `sur_m_language_label` VALUES ('40', 'survey.label', 'move_down', 'Move Down', 'เลื่อนลง', '');
INSERT INTO `sur_m_language_label` VALUES ('41', 'survey.label', 'none_image', 'None Image', 'ไม่พบรูปภาพ', '');
INSERT INTO `sur_m_language_label` VALUES ('42', 'survey.message', 'error_upload_without_extention', 'Please upload files with an extension of {0} only!', 'Please upload files with an extension of {0} only!', '');
INSERT INTO `sur_m_language_label` VALUES ('43', 'survey.message', 'upload', 'Upload', 'Upload', '');
INSERT INTO `sur_m_language_label` VALUES ('44', 'survey.message', 'upload_success', 'The file {0} already added!', 'The file {0} already added!', '');
INSERT INTO `sur_m_language_label` VALUES ('45', 'survey.message', 'page_not_found', 'page not found : ', 'ไม่พบ :', '');
INSERT INTO `sur_m_language_label` VALUES ('46', 'survey.label', 'upload', 'Upload', 'Upload', '');
INSERT INTO `sur_m_language_label` VALUES ('47', 'survey.label', 'answer', 'Answer?', 'คำตอบ?', '');
INSERT INTO `sur_m_language_label` VALUES ('48', 'survey.label', 'create_invitation', 'Invitation', 'คำเชิญ', '');
INSERT INTO `sur_m_language_label` VALUES ('49', 'survey.label', 'email_title', 'Email Subject', 'ชื่อหัวเรื่อง', '');
INSERT INTO `sur_m_language_label` VALUES ('50', 'survey.label', 'update_date', 'Update Date', 'วันที่แก้ไข', '');
INSERT INTO `sur_m_language_label` VALUES ('51', 'survey.label', 'from_name', 'Sender Name', 'ชื่อผู้ส่ง', '');
INSERT INTO `sur_m_language_label` VALUES ('52', 'survey.label', 'show_navigator', 'Show Navigator', 'แสดงตัวนำทาง', '');
INSERT INTO `sur_m_language_label` VALUES ('53', 'survey.label', 'show_navigator_yes', 'Yes, Show', 'แสดง', '');
INSERT INTO `sur_m_language_label` VALUES ('54', 'survey.label', 'show_navigator_no', 'No, Not Show', 'ไม่แสดง', '');
INSERT INTO `sur_m_language_label` VALUES ('55', 'survey.label', 'create_voters', 'Add Voter', 'เพิ่มผู้ทำแบบสอบถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('56', 'survey.label', 'add_voter_from_contract', 'Add From Contract', 'เพิ่มจากผู้ติดต่อ', '');
INSERT INTO `sur_m_language_label` VALUES ('57', 'survey.label', 'voters', 'Voters', 'ผู้ทำแบบสอบถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('58', 'survey.label', 'first_name', 'First Name', 'ชื่อ', '');
INSERT INTO `sur_m_language_label` VALUES ('59', 'survey.label', 'last_name', 'Last Name', 'สกุล', '');
INSERT INTO `sur_m_language_label` VALUES ('60', 'survey.label', 'email', 'Email', 'อีเมล์', '');
INSERT INTO `sur_m_language_label` VALUES ('61', 'survey.label', 'prefix', 'Prefix', 'คำนำหน้า', '');
INSERT INTO `sur_m_language_label` VALUES ('62', 'survey.label', 'gender', 'Gender', 'เพศ', '');
INSERT INTO `sur_m_language_label` VALUES ('63', 'survey.label', 'male', 'male', 'ชาย', '');
INSERT INTO `sur_m_language_label` VALUES ('64', 'survey.label', 'female', 'female', 'หญิง', '');
INSERT INTO `sur_m_language_label` VALUES ('65', 'survey.label', 'other', 'Other', 'อื่น', '');
INSERT INTO `sur_m_language_label` VALUES ('66', 'survey.label', 'confirm', 'Confirm', 'ยืนยัน', '');
INSERT INTO `sur_m_language_label` VALUES ('67', 'survey.message', 'confirm_delete', 'Are you sure you want to do that?', 'ต้องการลบรายการนี้หรือไม่ ?', '');
INSERT INTO `sur_m_language_label` VALUES ('68', 'survey.label', 'email_template', 'Email Template', 'รูปแบบของ อีเมล์', '');
INSERT INTO `sur_m_language_label` VALUES ('69', 'survey.label', 'name_content', 'Name Content', 'ชื่อ คอนเทน', '');
INSERT INTO `sur_m_language_label` VALUES ('70', 'survey.label', 'name_publication', 'Name Publication', 'ชื่อ ', '');
INSERT INTO `sur_m_language_label` VALUES ('71', 'survey.label', 'send', 'Send to Voter', 'ส่ง', '');
INSERT INTO `sur_m_language_label` VALUES ('72', 'survey.label', 'score', 'Score', 'คะแนน', '');
INSERT INTO `sur_m_language_label` VALUES ('73', 'survey.label', 'difficulty_level', 'Difficulty Level', 'ระดับความยาก', '');
INSERT INTO `sur_m_language_label` VALUES ('74', 'survey.label', 'random_type', 'Random Type', 'รูปแบบการสุ่มคำถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('75', 'survey.label', 'show_score', 'Show Score', 'แสดงคะแนนหลังทำเสร็จ', '');
INSERT INTO `sur_m_language_label` VALUES ('76', 'survey.label', 'random_answer', 'Random Answer', 'สุ่มคำตอบ', '');
INSERT INTO `sur_m_language_label` VALUES ('77', 'survey.label', 'use_question_no', 'Question No.', 'จำนวนคำถาม', '');
INSERT INTO `sur_m_language_label` VALUES ('78', 'survey.label', 'all', 'All', 'ทั้งหมด', '');
INSERT INTO `sur_m_language_label` VALUES ('79', 'survey.label', 'duration_time', 'Duration Time (Minute)', 'ระยะเวลา (นาที)', '');
INSERT INTO `sur_m_language_label` VALUES ('80', 'survey.label', 'minute', 'Minutes', 'นาที', '');
INSERT INTO `sur_m_language_label` VALUES ('81', 'survey.message', 'help_duration_time', 'set 0 is not defined', '0 ไม่กำหนดเวลา', '');

-- ----------------------------
-- Table structure for sur_m_marriage_status
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_marriage_status`;
CREATE TABLE `sur_m_marriage_status` (
  `id_marriage_status` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_marriage_status`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_marriage_status
-- ----------------------------
INSERT INTO `sur_m_marriage_status` VALUES ('1', 'Single', '');
INSERT INTO `sur_m_marriage_status` VALUES ('2', 'Married', '');
INSERT INTO `sur_m_marriage_status` VALUES ('3', 'Divorced', '');
INSERT INTO `sur_m_marriage_status` VALUES ('4', 'Separated', '');
INSERT INTO `sur_m_marriage_status` VALUES ('5', 'Widowed', '');
INSERT INTO `sur_m_marriage_status` VALUES ('6', 'Married not Registered', '');

-- ----------------------------
-- Table structure for sur_m_question_project_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_question_project_type`;
CREATE TABLE `sur_m_question_project_type` (
  `id_question_project_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_project_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_question_project_type
-- ----------------------------
INSERT INTO `sur_m_question_project_type` VALUES ('1', 'poll', '');
INSERT INTO `sur_m_question_project_type` VALUES ('2', 'survey', '');

-- ----------------------------
-- Table structure for sur_m_question_theme
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_question_theme`;
CREATE TABLE `sur_m_question_theme` (
  `id_question_theme` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_theme`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_question_theme
-- ----------------------------
INSERT INTO `sur_m_question_theme` VALUES ('1', 'More Question in One Page', 'genshi:pollandsurvey.templates.view.multiquestion', '');
INSERT INTO `sur_m_question_theme` VALUES ('2', 'One Ouestion in One Page', 'genshi:pollandsurvey.templates.view.singlequestion', '');

-- ----------------------------
-- Table structure for sur_m_question_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_question_type`;
CREATE TABLE `sur_m_question_type` (
  `id_question_type` bigint(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_question_type`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_question_type
-- ----------------------------
INSERT INTO `sur_m_question_type` VALUES ('1', 'Single Choice', 'radio', '');
INSERT INTO `sur_m_question_type` VALUES ('2', 'Multi Choice', 'check', '');
INSERT INTO `sur_m_question_type` VALUES ('3', 'Drop Down Menu', 'combobox', '');
INSERT INTO `sur_m_question_type` VALUES ('4', 'Image', 'image', '');
INSERT INTO `sur_m_question_type` VALUES ('5', 'Text', 'text', '');
INSERT INTO `sur_m_question_type` VALUES ('6', 'MultiText', 'textarea', '');
INSERT INTO `sur_m_question_type` VALUES ('7', 'Number', 'textnumber', '');

-- ----------------------------
-- Table structure for sur_m_question_type1
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_question_type1`;
CREATE TABLE `sur_m_question_type1` (
  `id_question_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_question_type1
-- ----------------------------

-- ----------------------------
-- Table structure for sur_m_telephone_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_telephone_type`;
CREATE TABLE `sur_m_telephone_type` (
  `id_telephone_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_telephone_type`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_telephone_type
-- ----------------------------

-- ----------------------------
-- Table structure for sur_m_variables
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_variables`;
CREATE TABLE `sur_m_variables` (
  `id_variables` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id_group_variables` int(11) NOT NULL,
  `table_jm_ref` varchar(255) DEFAULT NULL,
  `field_jm_ref` varchar(255) DEFAULT NULL,
  `id_parent` int(11) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_variables`),
  KEY `ix_sur_variables_id_group_variables` (`id_group_variables`),
  KEY `ix_sur_variables_id_parrent` (`id_parent`) USING BTREE,
  CONSTRAINT `sur_m_variables_ibfk_1` FOREIGN KEY (`id_group_variables`) REFERENCES `sur_m_group_variables` (`id_group_variables`),
  CONSTRAINT `sur_m_variables_ibfk_2` FOREIGN KEY (`id_parent`) REFERENCES `sur_m_variables` (`id_variables`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_variables
-- ----------------------------
INSERT INTO `sur_m_variables` VALUES ('1', 'Gender', null, '1', null, null, null, '');
INSERT INTO `sur_m_variables` VALUES ('2', 'Marrital Status', null, '1', null, null, null, '');
INSERT INTO `sur_m_variables` VALUES ('3', 'Address', null, '1', null, null, null, '');
INSERT INTO `sur_m_variables` VALUES ('4', 'Country', null, '1', null, null, '3', '');
INSERT INTO `sur_m_variables` VALUES ('5', 'Province', null, '1', null, null, '3', '');
INSERT INTO `sur_m_variables` VALUES ('6', 'City', null, '1', null, null, '3', '');
INSERT INTO `sur_m_variables` VALUES ('7', 'County', null, '1', null, null, '3', '');

-- ----------------------------
-- Table structure for sur_m_voter_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_m_voter_type`;
CREATE TABLE `sur_m_voter_type` (
  `id_voter_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_voter_type`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_voter_type
-- ----------------------------
INSERT INTO `sur_m_voter_type` VALUES ('1', 'contact', '');
INSERT INTO `sur_m_voter_type` VALUES ('2', 'invite', '');
INSERT INTO `sur_m_voter_type` VALUES ('3', 'external', '');
INSERT INTO `sur_m_voter_type` VALUES ('4', 'JM', '');
INSERT INTO `sur_m_voter_type` VALUES ('5', 'Voter', '');

-- ----------------------------
-- Table structure for sur_numberic_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_numberic_data`;
CREATE TABLE `sur_numberic_data` (
  `id_basic_data` bigint(20) NOT NULL,
  `max_value` double DEFAULT NULL,
  `max_message` varchar(255) DEFAULT NULL,
  `min_value` double DEFAULT NULL,
  `min_message` varchar(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  `sufix` varchar(255) DEFAULT NULL,
  `value` double DEFAULT NULL,
  PRIMARY KEY (`id_basic_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_numberic_data
-- ----------------------------

-- ----------------------------
-- Table structure for sur_organization
-- ----------------------------
DROP TABLE IF EXISTS `sur_organization`;
CREATE TABLE `sur_organization` (
  `id_organization` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_organization`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_organization
-- ----------------------------

-- ----------------------------
-- Table structure for sur_position
-- ----------------------------
DROP TABLE IF EXISTS `sur_position`;
CREATE TABLE `sur_position` (
  `id_position` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_organization` bigint(20) NOT NULL,
  `position` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `id_voter` bigint(20) NOT NULL,
  PRIMARY KEY (`id_position`),
  UNIQUE KEY `position` (`position`),
  UNIQUE KEY `department` (`department`),
  KEY `ix_sur_position_id_organization` (`id_organization`),
  KEY `ix_sur_position_id_voter` (`id_voter`),
  CONSTRAINT `sur_position_ibfk_1` FOREIGN KEY (`id_organization`) REFERENCES `sur_organization` (`id_organization`),
  CONSTRAINT `sur_position_ibfk_2` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_position
-- ----------------------------

-- ----------------------------
-- Table structure for sur_question
-- ----------------------------
DROP TABLE IF EXISTS `sur_question`;
CREATE TABLE `sur_question` (
  `id_question` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_question_type` bigint(20) NOT NULL,
  `question` text,
  `help_message` varchar(255) DEFAULT NULL,
  `text_label` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `active` bit(1) DEFAULT b'1',
  `id_question_project` bigint(20) NOT NULL,
  `order` int(11) DEFAULT NULL,
  `id_fix_difficulty_level` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id_question`),
  KEY `fk_sur_question_tg_user_1` (`user_id`),
  KEY `fk_sur_question_id_question_project_1` (`id_question_project`) USING BTREE,
  KEY `fk_sur_question_sur_question_type_1` (`id_question_type`),
  KEY `id_fix_difficulty_level` (`id_fix_difficulty_level`),
  CONSTRAINT `fk_sur_question_sur_question_project_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `fk_sur_question_sur_question_type_1` FOREIGN KEY (`id_question_type`) REFERENCES `sur_m_question_type` (`id_question_type`),
  CONSTRAINT `fk_sur_question_tg_user_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`),
  CONSTRAINT `sur_question_ibfk_1` FOREIGN KEY (`id_fix_difficulty_level`) REFERENCES `sur_fix_difficulty_level` (`id_fix_difficulty_level`)
) ENGINE=InnoDB AUTO_INCREMENT=214 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question
-- ----------------------------
INSERT INTO `sur_question` VALUES ('53', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 4', '', '', '3', '', '10', '2', null);
INSERT INTO `sur_question` VALUES ('54', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 2', '', '', '3', '', '10', '3', null);
INSERT INTO `sur_question` VALUES ('55', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 7', '', '', '3', '', '10', '8', null);
INSERT INTO `sur_question` VALUES ('56', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 0', '', '', '3', '', '10', '4', null);
INSERT INTO `sur_question` VALUES ('57', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 5', '', '', '3', '', '10', '1', null);
INSERT INTO `sur_question` VALUES ('58', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 3', '', '', '3', '', '10', '6', null);
INSERT INTO `sur_question` VALUES ('59', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 6', '', '', '3', '', '10', '7', null);
INSERT INTO `sur_question` VALUES ('97', '1', 'test', '', '', '6', '', '11', '1', null);
INSERT INTO `sur_question` VALUES ('98', '1', 'test', '', '', '6', '', '11', '2', null);
INSERT INTO `sur_question` VALUES ('102', '1', 'ทดสอบ', '', '', '3', '', '10', '9', null);
INSERT INTO `sur_question` VALUES ('103', '2', 'เลือกมากกว่า 1 ข้อ', '', '', '3', '', '10', '10', null);
INSERT INTO `sur_question` VALUES ('122', '4', 'test', '', '', '3', '', '10', '11', null);
INSERT INTO `sur_question` VALUES ('123', '4', 'test', '', '', '3', '', '10', '5', null);
INSERT INTO `sur_question` VALUES ('124', '4', 'Which figure completes the series?', '', '', '3', '', '12', '1', null);
INSERT INTO `sur_question` VALUES ('125', '4', 'Which figure completes the series?', '', '', '3', '', '12', '2', null);
INSERT INTO `sur_question` VALUES ('126', '4', 'Which figure completes the series?', '', '', '3', '', '12', '4', null);
INSERT INTO `sur_question` VALUES ('127', '4', 'Which figure completes the series?', '', '', '3', '', '12', '3', null);
INSERT INTO `sur_question` VALUES ('128', '4', 'Which figure completes the series?', '', '', '3', '', '12', '5', null);
INSERT INTO `sur_question` VALUES ('129', '1', 'Test', '', '', '3', '', '13', '1', null);
INSERT INTO `sur_question` VALUES ('130', '1', 'เสนอให้ตัดคำว่า \"พลเมือง\" ออกจากรัฐธรรมนูญทั้งหมด โดยให้ใช้คำว่า \"บุคคล\" แทน ซึ่งเป็นที่ปรากฎในรัฐธรรมนูญ พ.ศ. 2540 และ พ.ศ. 2550 เนื่องจากเห็นว่าการบัญญัติคำว่า \"พลเมือง\" ขึ้นใหม่ อาจนำไปสู่ปัญหาในการบังคับใช้ และการตีความทำให้ประชาชนมีความสงสัยว่าคำว่า ราษฎร ประชาชน บุคคล พลเมือง มีความแตกต่างกันอย่างไร\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '1', '1');
INSERT INTO `sur_question` VALUES ('131', '1', 'เรื่องที่มาของนายกรัฐมนตรี คณะกมธ.ฯ เห็นด้วยในหลักการที่คณะกมธ.ยกร่างฯ กำหนดไว้ในร่างรัฐธรรมนูญ มาตรา 172 ว่าด้วยการให้นายกฯ จะเป็น สส. หรือไม่เป็น สส. ก็ได้ แต่เห็นว่าหลักการดังกล่าวอาจไม่ครอบคลุมหรือแก้ไขปัญหาได้ทุกเหตุการณ์ เช่น ในกรณีที่ไม่มีสภาผู้แทนราษฎรและนายกฯ รักษาการก็พ้นจากตำแหน่ง ส่งผลให้เกิดช่องว่างขึ้น จึงเสนอให้มีการเพิ่มเติมเนื้อหา โดยการกำหนดให้วุฒิสภาปฏิบัติหน้าที่แทนสภาผู้แทนราษฎรเพื่อแก้ไขปัญหาดังกล่าว \r\nท่านเห็นด้วยหรือไม่', '', '', '3', '', '14', '2', '1');
INSERT INTO `sur_question` VALUES ('132', '1', 'เสนอให้ตัดเนื้อหาร่างรัฐธรรมนูญ มาตรา 181 และมาตรา 182 ว่าด้วยการให้นายกฯ สามารถเสนอขอความไว้วางใจจากสภาฯ ได้ และเสนอให้สภาฯ เห็นชอบสาระสำคัญของกฎหมายได้ภายใน 48 ชั่วโมง ออกทั้งหมด เนื่องจากมาตราดังกล่าวเปิดโอกาสให้นายกฯ ขอความไว้วางใจจากสภาฯ แต่หากสภาฯ ลงมติไว้วางใจน้อยกว่ากึ่งหนึ่ง จะให้อำนาจนายกฯ มีอำนาจยุบสภาฯ ได้ สภาพดังกล่าวจึงผิดหลักการและอาจมีปัญหาในการบังคับใช้จริง\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '3', '1');
INSERT INTO `sur_question` VALUES ('133', '1', 'การเลือกตั้ง สส. ระบบสัดส่วนผสมและระบบบัญชีรายชื่อแบบเปิด คณะกมธ.ฯเห็นด้วยกับหลักการของบทบัญญัติดังกล่าว\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '4', '1');
INSERT INTO `sur_question` VALUES ('134', '1', 'เสนอตัดคำว่า \"กลุ่มการเมือง\" ที่บัญญัติไว้ในร่างรัฐธรรมนูญออกทั้งหมด เนื่องจากกลุ่มการเมืองมีลักษณะคล้ายพรรคการเมือง แต่กลไกการกำกับและควบคุมตลอดจนความรับผิดของกลุ่มการเมืองตามที่บัญญัตไว้ในร่างรัฐธรรมนูญนี้กลับมีความแตกต่างหรือมีความเข้มงวดกว่าน้อยกว่าการควบคุมพรรคการเมือง จึงควรกำหนดให้เป็นมาตรฐานเดียวกัน มิเช่นนั้นการดำเนินการดังกล่าวจะเป็นการทำลายสถาบันการเมือง จึงควรตัดกลุ่มการเมืองออกและให้คงเหลือเฉพาะพรรคการเมือง\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '5', '1');
INSERT INTO `sur_question` VALUES ('135', '1', 'ที่มาของวุฒิสภา เห็นว่าควรให้มาจากการสรรหาทั้งหมด และเพิ่มขึ้นตอนหรือเงื่อนไขในการสรรหาไว้แทน โดยแบ่งกลุ่มอาชีพให้ชัดเจน เพิ่มคณะกรรมการสรรหาให้มากขึ้น ควรให้ผู้ที่ดำรงตำแหน่งประธานองค์กรแต่ละวิชาชีพเข้ามา เพื่อเพิ่มความรับผิดชอบ เพราะที่ผ่านมา สว. ที่มาจากการสรรหาส่วนหนึ่งและเลือกตั้งส่วนหนึ่ง กลับมีความขัดแย้งในการปฏิบัติงานร่วมกัน จึงทำให้ถูกครอบงำจากฝ่ายบริหารได้ พร้อมกันนี้ให้ตัดอำนาจการเสนอร่างพระราชบัญญัติ(พ.ร.บ.) โดยวุฒิสภาออก เนื่องจากวุฒิสภาควรเป็นสภากลั่นกรองและควบคุมการบริหารราชแผ่นดินเป็นหลัก\r\nขณะที่เสนอตัดอำนาจของวุฒิสภาในส่วนของการถอดถอนบุคคลที่วุฒิสภาไม่ได้เป็นผู้แต่งตั้งหรือไม่ให้ความเห็นชอบออกทั้งหมด เพราะวุมิสภาควรมีอำนาจถอดถอนเฉพาะบุคคลที่วุฒิสภาให้ความเห็นชอบในการดำรงตำแหน่งเท่านั้น ส่วนผู้ดำรงตำแหน่งทางการเมืองอื่น ที่วุฒิสภาไม่ได้ให้ความชอบก็ควรให้เป็นหน้าที่ของศาลฎีกาแผนกคดีอาญาของผู้ดำรงตำแหน่งทางการเมือง เป็นผู้พิจารณาถอดถอน\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '6', '1');
INSERT INTO `sur_question` VALUES ('136', '1', 'ความสัมพันธ์ระหว่างผู้ดำรงตำแหน่งทางการเมืองกับข้าราชการประจำในการแต่งตั้งข้าราชการระดับสูง คณะกมธ.ฯ เห็นด้วยในหลักการตามร่างของคณะกมธ.ยกร่างฯ แต่ควรมีการเพิ่มรายละเอียดเกี่ยวกับการแต่งตั้ง ย้าย การโอน หรือการเลื่อนข้าราชการไว้ในกฎหมายระดับ พ.ร.บ. เช่น กรณีให้คณะกรรมการจัดทำการคัดเลือกบุคคลที่มีความเหมาะสมที่จะดำรงตำแหน่งจำนวน 3 คน และเสนอชื่อไปยังคณะรัฐมนตรี(ครม.)เพื่อคัดเลือก หาก ครม.เห็นว่าไม่มีผู้เหมาะสม อาจให้คณะกรรมการฯเลือกบุคคลเพื่อเสนอมายัง ครม. ใหม่ได้\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '7', '1');
INSERT INTO `sur_question` VALUES ('137', '1', 'รูปแบบองค์กรบริหารท้องถิ่น เห็นว่า ควรตัดมาตรา 285 ที่เกี่ยวกับการปฏิรูปด้านการบริหารท้องถิ่นออก เนื่องจากประเทศไทยยังขาดความพร้อมในการยกระดับองค์กรปกครองท้องถิ่นเป็นจังหวัดปกครองตนเอง รวมทั้งการกำหนดให้มีกลไกในการจัดตั้งองค์กรบริหารท้องถิ่นเต็มพื้นที่จังหวัด และดำเนินการจัดตั้งองค์กรบริหารท้องถิ่นขึ้นในพื้นที่ที่มีความพร้อมและเหมาะสมโดยเร็วนั้น ประเทศไทยยังไม่สามารถก้าวไปสู่จุดมุ่งหมายดังกล่าวได้ ทั้งในเรื่องความพร้อมของบุคคลากร งบประมาณ กฎหมายรองรับ และอาจส่งผลกระทบต่อความมั่นคงของประเทศชาติได้\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '8', '1');
INSERT INTO `sur_question` VALUES ('138', '1', 'เสนอให้ผู้บริหารท้องถิ่นดำรงตำแหน่งนับแต่วันเลือกตั้งและมีวาระอยู่ในตำแหน่งคราวละ 4 ปี แต่จะดำรงตำแหน่งติดต่อกันเกิน 2 วาระไม่ได้ เพื่อเป็นช่องทางในการให้มีนักการเมืองรุ่นใหม่ มีโอกาสเข้ามาทำหน้าที่ในการบริหารราชการส่วนท้องถิ่น อีกทั้งเพื่อให้เป็นแบบเดียวกันกับการกำหนดให้นายกฯ จะดำรงตำแหน่งติดต่อเกิน 2 วาระไม่ได้\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '9', '1');
INSERT INTO `sur_question` VALUES ('139', '1', 'ศาลรัฐธรรมนูญ คณะกมธ.ฯเห็นว่า การสรรหาและเลือกตุลาการศาลรัฐธรรมนูญ ควรให้เป็นไปตามรัฐธรรมนูญ 2550 ดังเดิม\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '10', '1');
INSERT INTO `sur_question` VALUES ('140', '1', 'การตรวจการใช้อำนาจรัฐ เสนอให้อำนาจถอดถอนผู้ดำรงตำแหน่งทางการเมืองและเจ้าหน้าที่ของรัฐระดับสูง เป็นอำนาจของวุฒิสภา ไม่ควรให้รัฐสภาถอดถอนโดยกำหนดให้วุฒิสภาสามารถถอดถอนบุคคลออกจากตำแหน่งได้เฉพาะบุคคลที่วุฒิสภาให้ความเห็นชอบให้เข้าดำรงตำแหน่งเท่านั้น ส่วนบุคคลอื่นๆ ให้คณะกรรมการป้องกันและปราบปรามการทุจริตแห่งชาติ (ป.ป.ช.) จัดทำสำนวน ยื่นต่อศาลฎีกาฯ เพื่อพิจารณาถอดถอน\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '11', '1');
INSERT INTO `sur_question` VALUES ('141', '1', 'อำนาจการจัดการการเลือกตั้ง เห็นว่า ควรกำหนดให้เป็นหน้าที่ของคณะกรรมการการเลือกตั้ง (กกต.) เช่นเดิม ตามรัฐธรรมนูญ พ.ศ. 2550 แต่ควรแก้ไขเพิ่มเติมองค์ประกอบและที่มาของ กกต. เช่นเดียวกับ ปปช.\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '12', '1');
INSERT INTO `sur_question` VALUES ('142', '1', 'การควบรวมผู้ตรวจการแผ่นดินและคณะกรรมการสิทธิมนุษยชนแห่งชาติ เห็นว่า ไม่ควรมีการควบรวมเข้าด้วยกัน เนื่องจากทั้งสององค์กรมีบทบาทและหน้าที่เฉพาะเรื่อง และการกำหนดไว้เช่นรัฐธรรมนูญ พ.ศ. 2550 ย่อมเป็นไปตามหลักธรรมาภิบาลและสอดคล้องกับหลักสากลแล้ว แต่องค์ประกอบของทั้งสององค์ควรปรับจำนวนลง\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '13', '1');
INSERT INTO `sur_question` VALUES ('143', '1', 'การตั้งสภาตรวจสอบภาคพลเมือง สมัชชาคุณธรรมแห่งชาติ สมัชชาพลเมือง คณะกรรมการประเมินผลแห่งชาติ คณะกรรมการดำเนินการแต่งตั้งข้าราชการโดยระบบคุณธรรม คณะกรรมการดำเนินการจัดการเลือกตั้ง (กจต.) คณะกรรมการการกระจายอำนาจแห่งชาติ คณะกมธ.ฯเห็นว่า ไม่ควรกำหนดให้มีการจัดตั้งองค์กรใหม่มากจนเกินไป เนื่องจากการตั้งองค์กรขึ้นมาใหม่นั้น มีหน้าที่ที่ไม่ชัดเจนและมีขอบเขตที่กว้างมากเกินไป\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '14', '1');
INSERT INTO `sur_question` VALUES ('144', '1', 'การตั้งคณะกรรมการเสริมสร้างความปรองดองแห่งชาติ สภาขับเคลื่อนการปฏิรูปประเทศ คณะกรรมการยุทธศาสตร์การปฏิรูปแห่งชาติ คณะกมธ.ฯ มีความเห็นสนับสนุนให้มีการจัดตั้งคณะกรรมการชุดดังกล่าวทั้งหมด เพื่อให้สอดคล้องกับแผนการดำเนินการตามแนวทางปฏิรูปด้านต่างๆ\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '15', '1');
INSERT INTO `sur_question` VALUES ('145', '1', 'การกำหนดเวลาบังคับใช้รัฐธรรมนูญ เห็นว่า ควรบัญญัติบทเฉพาะกาลเพื่อกำหนดเงื่อนไขห้ามไม่ให้มีการแก้ไขเพิ่มเติมรัฐธรรมนูญนี้ในระยะเวลา 5 ปี ภายหลังมีการประกาศใช้รัฐธรรมนูญ เพื่อให้เกิดการดำเนินการปฏิรูปในด้านต่างๆ และสอดคล้องกับการกำหนดระยะเวลาไว้ในหมวดของการปฏิรูป\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '16', '1');
INSERT INTO `sur_question` VALUES ('146', '1', 'เห็นควรให้มีการกำหนดบทเฉพาะกาล เพื่อเกี่ยวกับการลงสมัคร สว. โดยควรกำหนดให้ สว. ซึ่งดำรงตำแหน่งอยู่ ณ วันที่ 24 พ.ค. 2557 และยังไม่ครบวาระ แต่ต้องพ้นจากตำแหน่งตามคำสั่งคณะรักษาความสงบแห่งชาติ (คสช.) เท่านั้น ที่สามารถเข้าสู่ตำแหน่ง สว. ได้ โดยไม่ถือว่ามีลักษณะต้องห้ามตามรัฐธรรมนูญ ไม่ควรให้ครอบคลุมถึง สว. ที่เข้ารับหน้าที่และปฏิบัติหน้าที่ระหว่าง พ.ศ. 2551 - 2557 ด้วย เนื่องจาก สว. ซึ่งดำรงแหน่งอยู่ ณ วันที่ 24 พ.ค. 2557 นั้น ยังไม่ครบวาระการดำรงตำแหน่ง ส่วน สว. ที่เข้ารับหน้าที่ระหว่าง พ.ศ. 2551 - 2557 ดำรงตำแหน่งครบวาระแล้ว\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '17', '1');
INSERT INTO `sur_question` VALUES ('147', '1', 'กรอบเวลาในการจัดทำพ.ร.บ. ประกอบรัฐธรรมนูญ เห็นว่า ควรมีการขยายกรอบเวลาที่กำหนดให้ สนช. ต้องพิจารณาร่าง พ.ร.บ. ประกอบรัฐธรรมนูญ โดยให้ สนช. มีเวลาพิจารณาร่าง พ.ร.บ. ประกอบรัฐธรรมนูญว่าด้วยการเลือกตั้ง สส. และการได้มาซึ่ง สว. ร่าง พ.ร.บ.ประกอบรัฐธรรมนูญว่าด้วยพรรคการเมืองและกลุ่มการเมือง และร่าง พ.ร.บ.ประกอบรัฐธรรมนูญว่าด้วย กกต. ภายใน 120 วัน จากเดิมที่กำหนดไว้ 60 วัน นับแต่วันที่ได้รับร่างจากคณะกมธ.ยกร่างฯ ส่วนร่าง พ.ร.บ. ประกอบรัฐธรรมนูญฉบับอื่นๆ อีก 9 ฉบับ ให้ สนช. มีเวลาพิจารณาให้เสร็จภายใน 180 วัน จากเดิมที่กำหนดไว้ 120 วัน เนื่องจากกรอบเวลาที่ร่างรัฐธรรมนูญกำหนดไว้เดิมไม่เพียงพอสำหรับการพิจารณา จะทำให้ร่าง พ.ร.บ. ประกอบรัฐธรรมนูญทั้งหมดไมได้รับการพิจารณาด้วยความรอบคอบ\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '18', '1');
INSERT INTO `sur_question` VALUES ('148', '1', 'การปฏิรูปด้านสาธารณสุข เห็นว่า ควรกำหนดให้มีคณะกรรมการยุทธศาสตร์การสาธารณสุขแห่งชาติที่เป็นอิสระจากหน่วยงานของรัฐ ควบคุมดูแลกระทรวงสาธารณสุข สำนักงานหลักประกันสุขภาพแห่งชาติ และสำนักงานคณะกรรมการสุขภาพแห่งชาติมีหน้าที่เสนอความเห็นต่อการกำหนดนโยบายสุขภาพ\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '19', '1');
INSERT INTO `sur_question` VALUES ('149', '1', 'หนังสือสัญญาที่ต้องได้รับความเห็นชอบจากรัฐสภา เห็นว่า ไม่ควรจะกำหนดให้คณะรัฐมนตรีเสนอกรอบเจรจาที่เป็นสาระเนื้อหาสำคัญ อันจะนำไปสู่การจัดทำหนังสือสัญญานั้นต่อคณะกมธ.การต่างประเทศของรัฐสภา เพื่อขอความเห็นชอบจากรัฐสภา เนื่องจากจะก่อให้เกิดปัญหาและข้อจำกัดในการเจรจา รวมทั้งอาจก่อให้ความเสียเปรียบในการเจรจาได้ โดยจะเป็นประโยชน์กับคู่เจรจามากกว่าหน่วยงานราชการไทยที่เกี่ยวข้อง\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '20', '1');
INSERT INTO `sur_question` VALUES ('150', '1', 'แนวนโยบายพื้นฐานแห่งรัฐในการพัฒนาด้านวิทยาศาสตร์ เห็นว่า ควรเพิ่มเนื้อหาในร่างรัฐธรรมนูญโดยกำหนดให้รัฐต้องส่งเสริมและสนับสนุนงานวิจัยและพัฒนาเพื่อการวิทยาศาสตร์ นวัตกรรม และการอุตสาหกรรม อย่างต่อเนื่อง\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '21', '1');
INSERT INTO `sur_question` VALUES ('151', '1', 'เห็นควรให้ตัดถ้อยคำในร่างรัฐธรรมนูญ มาตรา 76ว่าด้วยการกำหนดเงื่อนไขการพิจารณาส่งผู้สมัครรับเลือกตั้งเป็น สส. ทั้งแบบแบ่งเขตและบัญชีรายชื่อที่ต้องมีการหยั่งเสียงประชาชนหรือสมาชิกพรรคการเมืองในเขตเลือกตั้ง ซึ่งมีเงื่อนไขต้องมีรายชื่อผู้สมัครรับเลือกตั้งเป็นเพศตรงข้ามไม่น้อยกว่า 1 ใน 3 ออกทั้งหมด เนื่องจากทำให้เกิดความขัดแย้งกับมาตรา 4 และมาตรา 5 ของร่างรัฐธรรมนุญ ที่กำหนดให้ศักดิ์ศรีความเป็นมนุษย์มีความเสมอภาคและเท่าเทียมกัน \r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '22', '1');
INSERT INTO `sur_question` VALUES ('152', '1', 'การกำหนดว่า \"เพศสภาพ\" ไว้ในร่างรัฐธรรมนูญ เห็นว่า ควรตัดคำดังกล่าวออกไป เนื่องจากการกำหนดในเรื่องการเลือกปฏิบัติโดยไม่ธรรมต่อบุคคล เพราะเหตุแห่งความแตกต่างในเรื่องถิ่นกำเนิด เชื้อชาติ เพศ อายุ เป็นต้นนั้น ตามรัฐธรรมนูญ พ.ศ. 2550 สามารถตีความในเชิงคุ้มครองสิทธิได้อย่างกว้างขวางอยู่แล้ว\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '23', '1');
INSERT INTO `sur_question` VALUES ('153', '1', 'การเพิ่มเติมถ้อยคำเกี่ยวกับสิทธิของบุคคลในมาตรา 38 เห็นว่า การเพิ่มสิทธิของบุคคลในการสมรสตามร่างรัฐธรรมนูญยังไม่มีความชัดเจนในการได้รับความคุ้มครอง จึงควรกำหนดไว้เช่นเดียวกับรัฐธรรมนูญ พ.ศ. 2550 นอกจากนี้ควรกำหนดความคุ้มครองสิทธิความเป็นส่วนตัวของบุคคลสาธารณะให้ได้ความคุ้มครองเช่นเดียวกับบุคคลทั่วไป\r\nท่านเห็นด้วยหรือไม่?', '', '', '3', '', '14', '24', '1');
INSERT INTO `sur_question` VALUES ('154', '1', '42 is what percentage of 168?', 'help !', '', '3', '', '16', '1', '2');
INSERT INTO `sur_question` VALUES ('155', '1', '36 is what percentage of 80 ?', '', '', '3', '', '16', '2', '2');
INSERT INTO `sur_question` VALUES ('156', '1', 'What percentage of 175 is 91 ?', '', '', '3', '', '16', '3', '2');
INSERT INTO `sur_question` VALUES ('157', '1', '60 Ps. Is what percent of Rs. 24 ?', '', '', '3', '', '16', '4', '2');
INSERT INTO `sur_question` VALUES ('158', '1', '16 m is what percentage of 8 km?', '', '', '3', '', '16', '5', '2');
INSERT INTO `sur_question` VALUES ('159', '1', '25% of 96 + 75% of 48 = ?% of 80', '', '', '3', '', '16', '6', '2');
INSERT INTO `sur_question` VALUES ('160', '1', '70 percent of a number is 140. What is 68% of the number ?', '', '', '3', '', '16', '7', '2');
INSERT INTO `sur_question` VALUES ('161', '1', '30% of a number is 180. What is 15% of three times of the same number ?', '', '', '3', '', '16', '8', '2');
INSERT INTO `sur_question` VALUES ('162', '1', '39% of a number exceeds 19% of the same by 48. What is the number ?', '', '', '3', '', '16', '9', '2');
INSERT INTO `sur_question` VALUES ('163', '1', 'A number when increased by 30% gives 78. What is the number?', '', '', '3', '', '16', '10', '2');
INSERT INTO `sur_question` VALUES ('164', '1', 'A number when decreased by 14% of it, gives 215. What is the number', '', '', '3', '', '16', '11', '2');
INSERT INTO `sur_question` VALUES ('165', '1', '40% of a number, when added to 42, results in the number itself. What is the number?', '', '', '3', '', '16', '12', '2');
INSERT INTO `sur_question` VALUES ('166', '1', '24% of a number, when subtracted from 74.4, gives the number itself. What is the number ?', '', '', '3', '', '16', '13', '2');
INSERT INTO `sur_question` VALUES ('167', '1', 'In a fraction, the numerator is decreased by 25% and the denominator is increased by 20, then the value of the fraction becomes 15/16. Find the original fraction?', '', '', '3', '', '16', '14', '2');
INSERT INTO `sur_question` VALUES ('168', '1', 'The price of a pen is increased from Rs. 80 to Rs. 96. What is the percentage of increased in its price ?', '', '', '3', '', '16', '15', '2');
INSERT INTO `sur_question` VALUES ('169', '1', 'The greatest number which divides 245 and 1295 and leaves the remainder of 9 and 7 respectively is', '', '', '3', '', '16', '16', '2');
INSERT INTO `sur_question` VALUES ('170', '1', 'The distance between A\'s house and his office is 61 km. For reaching his house from office he covers 54 km 860 m by taxi, 5 km 65 m bytongaand the rest by rickshaw. Hoe much distance ', '', '', '3', '', '16', '17', '2');
INSERT INTO `sur_question` VALUES ('171', '1', 'If the cost of 25 packets of 12 pencils each is Rs. 750, then the cost of 30 packets of 8 pencils each is', '', '', '3', '', '16', '18', '2');
INSERT INTO `sur_question` VALUES ('172', '1', 'I have some 5-rupee coins and 2-rupee coins. The number of 2-rupee coins is 4 times that of the other kind. If I have Rs. 117 with me number of 5-rupee coins is', '', '', '3', '', '16', '19', '2');
INSERT INTO `sur_question` VALUES ('173', '1', 'How many different numbers of 3 digits can be formed by using 2, 4, 6, 8, 9?', '', '', '3', '', '16', '20', '2');
INSERT INTO `sur_question` VALUES ('174', '1', 'D gave C half of his pots. C gave J half of the pots she received from D. J kept 8 of those pots and gave the remaining 10 to A. How many pots did D give to C?', '', '', '3', '', '16', '21', '2');
INSERT INTO `sur_question` VALUES ('175', '1', 'If you save Rs.2 on Jan 1, Rs. 4 on Feb 1, Rs. 6 on Mar 1 and so on then how much you save in 1 year?', '', '', '3', '', '16', '22', '2');
INSERT INTO `sur_question` VALUES ('176', '1', 'A salesman\'s term was changed from a flat 5% commission on all sales to Rs. 1000 fixed salary and 2.5% commission on all sales exceeding Rs. 4000. If he gets Rs. 600 more according to ', '', '', '3', '', '16', '23', '2');
INSERT INTO `sur_question` VALUES ('177', '1', 'What sum of money was divided among A, B and C if B and C get Rs. 100, C and A get Rs. 150 and A gets twice as much as B?', '', '', '3', '', '16', '24', '2');
INSERT INTO `sur_question` VALUES ('178', '1', 'A clock gains 15 seconds per day and another loses 45 seconds per day. After what length of time will the first clock 12 hrs ahead of the second?', '', '', '3', '', '16', '25', '2');
INSERT INTO `sur_question` VALUES ('179', '1', 'A number when halved is half as short of 100 at it exceeds 100 now. What is it?', '', '', '3', '', '16', '26', '2');
INSERT INTO `sur_question` VALUES ('180', '1', 'At a club each member shook hands with every other member. If there were totally 190 handshakes how many members were present?', '', '', '3', '', '16', '27', '2');
INSERT INTO `sur_question` VALUES ('181', '1', 'Showing a lady Vineet said\'\" She is the daughter of my grandfather\'s only son.\" How is Vineet related to her?', '', '', '3', '', '16', '28', '2');
INSERT INTO `sur_question` VALUES ('182', '1', 'In a code if RATIONAL is written as RTANIOLA then the code for TRIBAL is', '', '', '3', '', '16', '29', '2');
INSERT INTO `sur_question` VALUES ('183', '1', '6, 15, 36, 75, ___', '', '', '3', '', '16', '30', '2');
INSERT INTO `sur_question` VALUES ('184', '1', 'In what time will a sum of money doubles itself at 5% SI?', '', '', '3', '', '16', '31', '2');
INSERT INTO `sur_question` VALUES ('185', '1', 'Two men start walking a certain distance one at 4 kmph and the other at 5 kmph. The latter reaches the place 45 min before the former. Find the distance.', '', '', '3', '', '16', '32', '2');
INSERT INTO `sur_question` VALUES ('186', '1', 'A direction post was turned in an accident in such a way that the arrow which was showing east is now pointing to south. A traveler travels in a direction thinking it to be west. In what ', '', '', '3', '', '16', '33', '2');
INSERT INTO `sur_question` VALUES ('187', '1', 'If 63+25=16, 12+18=12 and 23+17=13, then 54+22=__', '', '', '3', '', '16', '34', '2');
INSERT INTO `sur_question` VALUES ('188', '1', 'Find k if 734726k is divisible by 24.', '', '', '3', '', '16', '35', '2');
INSERT INTO `sur_question` VALUES ('189', '1', 'In a year 28th Feb is Tuesday. If the leap year is excluded then 28th march will be', '', '', '3', '', '16', '36', '2');
INSERT INTO `sur_question` VALUES ('190', '1', '5 boys took part in a race. Ram finished before Mohan but behind Gopal. Abbas finished before Sailesh but behind Mohan. Who won the race?', '', '', '3', '', '16', '37', '2');
INSERT INTO `sur_question` VALUES ('191', '1', 'No man is a tan. Some tans are not pans.', '', '', '3', '', '16', '38', '2');
INSERT INTO `sur_question` VALUES ('192', '1', 'A solid cube is painted black on three adjacent sides and is cut into 216 equal pieces. How many small pieces have at least two sides painted?', '', '', '3', '', '16', '39', '2');
INSERT INTO `sur_question` VALUES ('193', '1', 'Choose the set of the statements which are logically related.\r\nA. All apples are fruits \r\nB. All fruits are sweet.\r\nC.All apples are sweet \r\nD. All apples are priced\r\nE. All fruits are priced \r\nF. All fruits are available', '', '', '3', '', '16', '40', '2');
INSERT INTO `sur_question` VALUES ('194', '1', 'In a class composed of x girls and y boys what part of the class is composed of girls', '', '', '3', '', '16', '41', '2');
INSERT INTO `sur_question` VALUES ('195', '1', 'What is the maximum number of half-pint bottles of cream that can be filled with a 4-gallon can of cream(2 pt.=1 qt. and 4 qt.=1 gal)', '', '', '3', '', '16', '42', '2');
INSERT INTO `sur_question` VALUES ('196', '1', 'If the operation,^ is defined by the equation x ^ y = 2x + y,what is the value of a in 2 ^ a = a ^ 3', '', '', '3', '', '16', '43', '2');
INSERT INTO `sur_question` VALUES ('197', '1', 'A coffee shop blends 2 kinds of coffee,putting in 2 parts of a 33p. a gm. grade to 1 part of a 24p. agm.If the mixture is changed to 1 part of the 33p. a gm. to 2 parts of the less expensive ', '', '', '3', '', '16', '44', '2');
INSERT INTO `sur_question` VALUES ('198', '1', 'There are 200 questions on a 3 hrexamination.Among these questions are 50 mathematics problems.It is suggested that twice as much time be spent on each maths problem as for each ', '', '', '3', '', '16', '45', '2');
INSERT INTO `sur_question` VALUES ('199', '1', 'In a group of 15,7 have studied Latin, 8 have studied Greek, and 3 have not studied either.How many of these studied both Latin and Greek', '', '', '3', '', '16', '46', '2');
INSERT INTO `sur_question` VALUES ('200', '1', 'If 13 = 13w/(1-w) ,then (2w)2 =', '', '', '3', '', '16', '47', '2');
INSERT INTO `sur_question` VALUES ('201', '1', 'If a and b are positive integers and (a-b)/3.5 = 4/7, then', '', '', '3', '', '16', '48', '2');
INSERT INTO `sur_question` VALUES ('202', '1', 'In june a baseball team that played 60 games had won 30% of its game played. After a phenomenal winning streak this team raised its average to 50% .How many games must the team ', '', '', '3', '', '16', '49', '2');
INSERT INTO `sur_question` VALUES ('203', '1', 'M men agree to purchase a gift for Rs. D. If three men drop out how much more will each have to contribute towards the purchase of the gift/', '', '', '3', '', '16', '50', '2');
INSERT INTO `sur_question` VALUES ('204', '1', 'A company contracts to paint 3 houses. Mr.Brown can paint a house in 6 days while Mr.Black would take 8 days and Mr.Blue 12 days. After 8 days Mr.Brown goes on vacation and Mr. Black ', '', '', '3', '', '16', '51', '2');
INSERT INTO `sur_question` VALUES ('205', '1', 'A company contracts to paint 3 houses. Mr.Brown can paint a house in 6 days while Mr.Black would take 8 days and Mr.Blue 12 days. After 8 days Mr.Brown goes on vacation and Mr. Black ', '', '', '3', '', '16', '52', '2');
INSERT INTO `sur_question` VALUES ('206', '1', '2 hours after a freight train leaves Delhi a passenger train leaves the same station travelling in the same direction at an average speed of 16 km/hr. After travelling 4 hrs the passenger ', '', '', '3', '', '16', '53', '2');
INSERT INTO `sur_question` VALUES ('207', '1', 'If 2x-y=4 then calculate 6x-3y=?', '', '', '3', '', '16', '54', '2');
INSERT INTO `sur_question` VALUES ('208', '1', 'If x=y=2z and xyz=256 then what is the value of x?', '', '', '3', '', '16', '55', '2');
INSERT INTO `sur_question` VALUES ('209', '1', 'Calculate (1/10)18 - (1/10)20 = ?', '', '', '3', '', '16', '56', '2');
INSERT INTO `sur_question` VALUES ('210', '1', 'Pipe A can fill an empty tank in 20 minutes and Pipe B in 30 mins and Pipe C can empty the same in 40 mins. If all of them work together, find the time taken to fill the tank?', '', '', '3', '', '16', '57', '2');
INSERT INTO `sur_question` VALUES ('211', '1', 'Thirty men take 20 days to complete a job working 9 hours a day. How many hour a day should 40 men work to complete the job?', '', '', '3', '', '16', '58', '2');
INSERT INTO `sur_question` VALUES ('212', '1', 'Find the smallest number in a GP whose sum is 38 and product 1728?', '', '', '3', '', '16', '59', '2');
INSERT INTO `sur_question` VALUES ('213', '1', 'A goat is tied to one corner of a square plot of side 12 meter by a rope 7 meter long. Find the area it can graze?', '', '', '3', '', '16', '60', '2');

-- ----------------------------
-- Table structure for sur_question_email_template
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_email_template`;
CREATE TABLE `sur_question_email_template` (
  `id_question_email_template` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_question_project` bigint(20) DEFAULT NULL,
  `content` text,
  `subject` varchar(255) DEFAULT NULL,
  `from_name` varchar(255) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_question_email_template`),
  KEY `id_question_project` (`id_question_project`),
  CONSTRAINT `sur_question_email_template_ibfk_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_email_template
-- ----------------------------

-- ----------------------------
-- Table structure for sur_question_invitation
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_invitation`;
CREATE TABLE `sur_question_invitation` (
  `id_question_invitation` bigint(20) NOT NULL AUTO_INCREMENT,
  `name_content` varchar(255) DEFAULT NULL,
  `from_name` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `id_question_project` bigint(20) NOT NULL,
  `content` text,
  `create_date` datetime NOT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_question_invitation`),
  KEY `ix_sur_invitation_id_question_project` (`id_question_project`),
  CONSTRAINT `sur_question_invitation_ibfk_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_invitation
-- ----------------------------
INSERT INTO `sur_question_invitation` VALUES ('1', 'Test', 'Test', 'Test', '13', 'hello [name]<br><br>&nbsp;<a href=\"[url]\">[url]</a><br><br><br>thank you<br><br>', '2015-05-19 10:13:12', null);
INSERT INTO `sur_question_invitation` VALUES ('2', 'ร่าง รธน', 'Survey', 'ร่าง รธน', '14', '', '2015-06-02 08:37:28', null);
INSERT INTO `sur_question_invitation` VALUES ('3', 'Questionnaire Aptitude Test', 'jm', 'Questionnaire Aptitude Test', '16', 'Hello [name]<br>&nbsp;&nbsp;&nbsp; please Do it.<br><br><a href=\"[url]\">[url]</a><br><br><br>thank you<br>jm​', '2015-06-08 16:04:42', null);

-- ----------------------------
-- Table structure for sur_question_media
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_media`;
CREATE TABLE `sur_question_media` (
  `id_question` bigint(20) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `media_type` varchar(255) DEFAULT NULL,
  `media_path_file` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_question`),
  KEY `id_question` (`id_question`),
  CONSTRAINT `sur_question_media_ibfk_1` FOREIGN KEY (`id_question`) REFERENCES `sur_question` (`id_question`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_media
-- ----------------------------
INSERT INTO `sur_question_media` VALUES ('122', 'question_3.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\122\\question_3.png');
INSERT INTO `sur_question_media` VALUES ('123', 'question_3.png', 'image/png', 'c:\\temp\\upload\\poll\\images\\123\\question_3.png');
INSERT INTO `sur_question_media` VALUES ('124', 'Q01.png', 'image/png', '/usr/local/projects/upload/survey/124/Q01.png');
INSERT INTO `sur_question_media` VALUES ('125', 'Q02.png', 'image/png', '/usr/local/projects/upload/survey/125/Q02.png');
INSERT INTO `sur_question_media` VALUES ('126', 'Q03.png', 'image/png', '/usr/local/projects/upload/survey/126/Q03.png');
INSERT INTO `sur_question_media` VALUES ('127', 'Q04.png', 'image/png', '/usr/local/projects/upload/survey/127/Q04.png');
INSERT INTO `sur_question_media` VALUES ('128', 'Q5.png', 'image/png', '/usr/local/projects/upload/survey/128/Q5.png');

-- ----------------------------
-- Table structure for sur_question_option
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_option`;
CREATE TABLE `sur_question_option` (
  `id_question_option` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_question_project` bigint(20) DEFAULT NULL,
  `id_question_theme` bigint(20) DEFAULT NULL,
  `id_question_invitation` bigint(20) DEFAULT NULL,
  `id_fix_random_type` bigint(20) DEFAULT NULL,
  `random_answer` bit(1) DEFAULT b'1',
  `name_publication` varchar(255) DEFAULT NULL,
  `activate_date` datetime DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  `header_message` text,
  `footer_message` text,
  `welcome_message` text,
  `end_message` text,
  `gen_code` varchar(20) DEFAULT NULL,
  `show_score` bit(1) DEFAULT b'0',
  `use_question_no` int(11) DEFAULT '0' COMMENT 'Show Number Question',
  `duration_time` int(11) DEFAULT '0',
  `redirect_url` varchar(255) DEFAULT NULL,
  `send_status` bit(1) DEFAULT b'0' COMMENT '0=not send to voter,1=send to voter already',
  `show_navigator` bit(1) DEFAULT b'0',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_question_option`),
  KEY `id_question_option` (`id_question_option`),
  KEY `id_question_project` (`id_question_project`) USING BTREE,
  KEY `id_question_theme` (`id_question_theme`),
  KEY `id_question_invitation` (`id_question_invitation`),
  KEY `id_fix_random_type` (`id_fix_random_type`),
  CONSTRAINT `sur_question_option_ibfk_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `sur_question_option_ibfk_2` FOREIGN KEY (`id_question_theme`) REFERENCES `sur_m_question_theme` (`id_question_theme`),
  CONSTRAINT `sur_question_option_ibfk_3` FOREIGN KEY (`id_question_invitation`) REFERENCES `sur_question_invitation` (`id_question_invitation`),
  CONSTRAINT `sur_question_option_ibfk_4` FOREIGN KEY (`id_fix_random_type`) REFERENCES `sur_fix_random_type` (`id_fix_random_type`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_option
-- ----------------------------
INSERT INTO `sur_question_option` VALUES ('2', '10', '2', null, null, '', 'ทดสอบ', '2014-12-04 00:00:00', '2015-05-31 23:59:59', 'Header', 'Footer', '<h1>ยินดีต้อนรับการทำงาน</h1><br>', 'Thank you', null, '\0', '0', '0', 'http://google.co.th', '\0', '\0', '2014-12-04 11:45:44');
INSERT INTO `sur_question_option` VALUES ('9', '11', '2', null, null, '', '11', '2015-02-01 00:00:00', '2015-02-28 23:59:59', 'Header', 'Footer', 'welcome', 'end', null, '\0', '0', '0', 'http://google.co.th', '\0', '\0', '2015-02-17 16:11:04');
INSERT INTO `sur_question_option` VALUES ('10', '12', '2', null, null, '', 'CompanyA', '2015-05-07 00:00:00', '2016-05-31 23:59:59', '', '', '', '', null, '\0', '0', '0', '', '\0', '\0', '2015-05-07 14:56:21');
INSERT INTO `sur_question_option` VALUES ('11', '13', '1', '1', '1', '', 'test', '2015-05-01 00:00:00', '2015-06-30 23:59:59', '', '', '', '', null, '\0', '1', '0', '', '\0', '\0', '2015-05-22 17:44:58');
INSERT INTO `sur_question_option` VALUES ('12', '14', '2', '2', '1', '\0', 'รอบที่1', '2015-06-01 00:00:00', '2015-07-31 23:59:59', '', '', '', '', null, '\0', '24', '0', '', '\0', '\0', '2015-06-02 08:40:00');
INSERT INTO `sur_question_option` VALUES ('13', '16', '2', '3', '1', '\0', 'Questionnaire Aptitude Test(JM)', '2015-06-08 00:00:00', '2017-09-30 23:59:59', '', '', '', '', null, '\0', '20', '0', '', '\0', '\0', '2015-06-08 16:05:47');

-- ----------------------------
-- Table structure for sur_question_project
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_project`;
CREATE TABLE `sur_question_project` (
  `id_question_project` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `id_question_project_type` bigint(20) NOT NULL,
  `header_message` varchar(255) DEFAULT NULL,
  `footer_message` varchar(255) DEFAULT NULL,
  `welcome_text` varchar(255) DEFAULT NULL,
  `end_text` varchar(255) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_project`),
  KEY `fk_sur_question_project_tg_user_1` (`user_id`),
  KEY `fk_sur_question_project_type_sur_question_project_1` (`id_question_project_type`),
  CONSTRAINT `fk_sur_question_project_tg_user_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`),
  CONSTRAINT `fk_sur_question_project_type_sur_question_project_1` FOREIGN KEY (`id_question_project_type`) REFERENCES `sur_m_question_project_type` (`id_question_project_type`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_project
-- ----------------------------
INSERT INTO `sur_question_project` VALUES ('10', 'test', 'test', '3', '1', '', '', '', '', '2014-12-03 17:53:38', '2014-12-03 17:53:38', '');
INSERT INTO `sur_question_project` VALUES ('11', 'test', 'test', '6', '1', null, null, null, null, '2015-02-17 11:30:38', '2015-02-17 11:30:38', '');
INSERT INTO `sur_question_project` VALUES ('12', 'Practice Test', 'test', '3', '1', '', '', '', '', '2015-02-20 16:10:36', '2015-02-20 16:10:36', '');
INSERT INTO `sur_question_project` VALUES ('13', 'ทดสอบiq', 'ทดสอบiq ความรู้​ความสามารถ', '3', '1', null, null, null, null, '2015-05-19 06:41:31', '2015-05-19 06:41:31', '');
INSERT INTO `sur_question_project` VALUES ('14', 'ร่าง รธน.', '', '3', '2', null, null, null, null, '2015-06-02 07:57:23', '2015-06-02 07:57:23', '');
INSERT INTO `sur_question_project` VALUES ('16', 'Questionnaire Aptitude Test', 'Questionnaire Aptitude Test', '3', '2', null, null, null, null, '2015-06-08 14:52:29', '2015-06-08 14:52:29', '');

-- ----------------------------
-- Table structure for sur_question_project_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_project_type`;
CREATE TABLE `sur_question_project_type` (
  `id_question_project_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_project_type`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_project_type
-- ----------------------------
INSERT INTO `sur_question_project_type` VALUES ('1', 'poll', '');
INSERT INTO `sur_question_project_type` VALUES ('2', 'survey', '');

-- ----------------------------
-- Table structure for sur_question_theme
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_theme`;
CREATE TABLE `sur_question_theme` (
  `id_question_theme` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `template` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_theme`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_theme
-- ----------------------------
INSERT INTO `sur_question_theme` VALUES ('1', 'More Question in One Page', 'genshi:pollandsurvey.templates.view.multiquestion', '');
INSERT INTO `sur_question_theme` VALUES ('2', 'One Ouestion in One Page', 'genshi:pollandsurvey.templates.view.singlequestion', '');

-- ----------------------------
-- Table structure for sur_question_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_type`;
CREATE TABLE `sur_question_type` (
  `id_question_type` bigint(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_question_type`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_type
-- ----------------------------
INSERT INTO `sur_question_type` VALUES ('1', 'Single Choice', 'radio', '');
INSERT INTO `sur_question_type` VALUES ('2', 'Multi Choice', 'check', '');
INSERT INTO `sur_question_type` VALUES ('3', 'Drop Down Menu', 'combobox', '');
INSERT INTO `sur_question_type` VALUES ('4', 'Image', 'image', '');

-- ----------------------------
-- Table structure for sur_question_type1
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_type1`;
CREATE TABLE `sur_question_type1` (
  `id_question_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_question_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_type1
-- ----------------------------

-- ----------------------------
-- Table structure for sur_question_validation
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_validation`;
CREATE TABLE `sur_question_validation` (
  `id_question` bigint(20) NOT NULL AUTO_INCREMENT,
  `enable_validation` bit(1) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_question`),
  KEY `fk_sur_question_validation_id_question_1` (`id_question`),
  CONSTRAINT `fk_sur_question_validation_sur_question_1` FOREIGN KEY (`id_question`) REFERENCES `sur_question` (`id_question`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_validation
-- ----------------------------

-- ----------------------------
-- Table structure for sur_reply_basic_question
-- ----------------------------
DROP TABLE IF EXISTS `sur_reply_basic_question`;
CREATE TABLE `sur_reply_basic_question` (
  `id_resp_reply` bigint(20) NOT NULL,
  `id_basic_data` bigint(20) NOT NULL,
  `answer_text` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_resp_reply`,`id_basic_data`),
  KEY `ix_sur_reply_basic_question_id_resp_reply` (`id_resp_reply`),
  KEY `ix_sur_reply_basic_question_id_basic_data` (`id_basic_data`),
  CONSTRAINT `sur_reply_basic_question_ibfk_1` FOREIGN KEY (`id_resp_reply`) REFERENCES `sur_resp_reply` (`id_resp_reply`),
  CONSTRAINT `sur_reply_basic_question_ibfk_2` FOREIGN KEY (`id_basic_data`) REFERENCES `sur_basic_data` (`id_basic_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_reply_basic_question
-- ----------------------------
INSERT INTO `sur_reply_basic_question` VALUES ('1', '149', null);
INSERT INTO `sur_reply_basic_question` VALUES ('2', '151', null);
INSERT INTO `sur_reply_basic_question` VALUES ('3', '155', null);
INSERT INTO `sur_reply_basic_question` VALUES ('4', '157', null);
INSERT INTO `sur_reply_basic_question` VALUES ('5', '160', null);
INSERT INTO `sur_reply_basic_question` VALUES ('6', '163', null);
INSERT INTO `sur_reply_basic_question` VALUES ('7', '293', null);
INSERT INTO `sur_reply_basic_question` VALUES ('8', '167', null);
INSERT INTO `sur_reply_basic_question` VALUES ('9', '297', null);
INSERT INTO `sur_reply_basic_question` VALUES ('9', '299', null);
INSERT INTO `sur_reply_basic_question` VALUES ('10', '149', null);
INSERT INTO `sur_reply_basic_question` VALUES ('11', '155', null);
INSERT INTO `sur_reply_basic_question` VALUES ('12', '158', null);
INSERT INTO `sur_reply_basic_question` VALUES ('13', '160', null);
INSERT INTO `sur_reply_basic_question` VALUES ('14', '163', null);
INSERT INTO `sur_reply_basic_question` VALUES ('15', '294', null);
INSERT INTO `sur_reply_basic_question` VALUES ('16', '297', null);
INSERT INTO `sur_reply_basic_question` VALUES ('16', '299', null);
INSERT INTO `sur_reply_basic_question` VALUES ('17', '152', null);
INSERT INTO `sur_reply_basic_question` VALUES ('18', '167', null);
INSERT INTO `sur_reply_basic_question` VALUES ('19', '365', null);
INSERT INTO `sur_reply_basic_question` VALUES ('20', '361', null);

-- ----------------------------
-- Table structure for sur_respondents
-- ----------------------------
DROP TABLE IF EXISTS `sur_respondents`;
CREATE TABLE `sur_respondents` (
  `id_respondents` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_voter` bigint(20) NOT NULL,
  `response_ip` varchar(255) DEFAULT NULL,
  `respondent_data` datetime NOT NULL,
  `id_question_project` bigint(20) NOT NULL,
  `id_question_option` bigint(20) NOT NULL,
  `finished` bit(1) DEFAULT b'0',
  `score_exam` int(11) DEFAULT '0',
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`id_respondents`),
  KEY `ix_sur_respondents_id_question_option` (`id_question_option`),
  KEY `ix_sur_respondents_id_question_project` (`id_question_project`),
  KEY `ix_sur_respondents_id_voter` (`id_voter`),
  CONSTRAINT `sur_respondents_ibfk_1` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`),
  CONSTRAINT `sur_respondents_ibfk_2` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `sur_respondents_ibfk_3` FOREIGN KEY (`id_question_option`) REFERENCES `sur_question_option` (`id_question_option`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_respondents
-- ----------------------------
INSERT INTO `sur_respondents` VALUES ('1', '1', '127.0.0.1', '2015-02-25 18:53:14', '10', '2', '', '0', '2015-02-25 18:53:14');
INSERT INTO `sur_respondents` VALUES ('2', '4', '127.0.0.1', '2015-02-26 15:02:28', '10', '2', '\0', '0', '2015-02-26 15:02:28');
INSERT INTO `sur_respondents` VALUES ('3', '1', null, '2015-05-26 18:43:55', '13', '11', '', '0', '2015-05-26 18:43:55');
INSERT INTO `sur_respondents` VALUES ('4', '4', null, '2015-05-26 18:44:02', '13', '11', '\0', '0', '2015-05-26 18:44:02');
INSERT INTO `sur_respondents` VALUES ('5', '6', null, '2015-05-26 18:44:07', '13', '11', '\0', '0', '2015-05-26 18:44:07');
INSERT INTO `sur_respondents` VALUES ('6', '1', null, '2015-06-08 17:18:15', '16', '13', '\0', '0', '2015-06-08 17:18:15');
INSERT INTO `sur_respondents` VALUES ('7', '4', null, '2015-06-08 17:18:21', '16', '13', '\0', '0', '2015-06-08 17:18:21');
INSERT INTO `sur_respondents` VALUES ('8', '6', null, '2015-06-08 17:18:26', '16', '13', '\0', '0', '2015-06-08 17:18:26');

-- ----------------------------
-- Table structure for sur_resp_reply
-- ----------------------------
DROP TABLE IF EXISTS `sur_resp_reply`;
CREATE TABLE `sur_resp_reply` (
  `id_resp_reply` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_respondents` bigint(20) NOT NULL,
  `id_question` bigint(20) NOT NULL,
  `response_date` datetime NOT NULL,
  PRIMARY KEY (`id_resp_reply`),
  KEY `ix_sur_resp_reply_id_question` (`id_question`),
  KEY `ix_sur_resp_reply_id_respondents` (`id_respondents`),
  CONSTRAINT `sur_resp_reply_ibfk_1` FOREIGN KEY (`id_respondents`) REFERENCES `sur_respondents` (`id_respondents`),
  CONSTRAINT `sur_resp_reply_ibfk_2` FOREIGN KEY (`id_question`) REFERENCES `sur_question` (`id_question`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_resp_reply
-- ----------------------------
INSERT INTO `sur_resp_reply` VALUES ('1', '1', '53', '2015-02-26 14:04:57');
INSERT INTO `sur_resp_reply` VALUES ('2', '1', '54', '2015-02-26 14:07:52');
INSERT INTO `sur_resp_reply` VALUES ('3', '1', '55', '2015-02-26 14:08:10');
INSERT INTO `sur_resp_reply` VALUES ('4', '1', '56', '2015-02-26 14:08:25');
INSERT INTO `sur_resp_reply` VALUES ('5', '1', '57', '2015-02-26 14:08:31');
INSERT INTO `sur_resp_reply` VALUES ('6', '1', '58', '2015-02-26 14:08:34');
INSERT INTO `sur_resp_reply` VALUES ('7', '1', '102', '2015-02-26 14:08:37');
INSERT INTO `sur_resp_reply` VALUES ('8', '1', '59', '2015-02-26 14:08:40');
INSERT INTO `sur_resp_reply` VALUES ('9', '1', '103', '2015-02-26 14:08:52');
INSERT INTO `sur_resp_reply` VALUES ('10', '2', '53', '2015-02-26 15:04:41');
INSERT INTO `sur_resp_reply` VALUES ('11', '2', '55', '2015-02-26 15:04:44');
INSERT INTO `sur_resp_reply` VALUES ('12', '2', '56', '2015-02-26 15:04:48');
INSERT INTO `sur_resp_reply` VALUES ('13', '2', '57', '2015-02-26 15:05:01');
INSERT INTO `sur_resp_reply` VALUES ('14', '2', '58', '2015-02-26 15:05:03');
INSERT INTO `sur_resp_reply` VALUES ('15', '2', '102', '2015-02-26 15:05:09');
INSERT INTO `sur_resp_reply` VALUES ('16', '2', '103', '2015-02-26 15:05:13');
INSERT INTO `sur_resp_reply` VALUES ('17', '2', '54', '2015-02-26 15:39:07');
INSERT INTO `sur_resp_reply` VALUES ('18', '2', '59', '2015-02-26 16:18:13');
INSERT INTO `sur_resp_reply` VALUES ('19', '1', '123', '2015-02-26 16:28:51');
INSERT INTO `sur_resp_reply` VALUES ('20', '1', '122', '2015-04-07 16:38:06');
INSERT INTO `sur_resp_reply` VALUES ('161', '6', '154', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('162', '6', '155', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('163', '6', '156', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('164', '6', '157', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('165', '6', '158', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('166', '6', '159', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('167', '6', '160', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('168', '6', '161', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('169', '6', '162', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('170', '6', '163', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('171', '6', '164', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('172', '6', '165', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('173', '6', '166', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('174', '6', '167', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('175', '6', '168', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('176', '6', '169', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('177', '6', '170', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('178', '6', '171', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('179', '6', '172', '2015-06-09 10:09:44');
INSERT INTO `sur_resp_reply` VALUES ('180', '6', '173', '2015-06-09 10:09:44');

-- ----------------------------
-- Table structure for sur_sys_config
-- ----------------------------
DROP TABLE IF EXISTS `sur_sys_config`;
CREATE TABLE `sur_sys_config` (
  `id_sys_config` int(11) NOT NULL AUTO_INCREMENT,
  `default_code` varchar(255) DEFAULT NULL,
  `default_value` varchar(255) DEFAULT NULL,
  `default_type_value` varchar(255) DEFAULT NULL,
  `code_country` varchar(3) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_sys_config`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_sys_config
-- ----------------------------
INSERT INTO `sur_sys_config` VALUES ('1', 'expired_activate_code', '30', 'date', 'th', '', '2015-04-21 14:37:18', null);
INSERT INTO `sur_sys_config` VALUES ('2', 'random_activate_code_length', '15', 'int', 'th', '', null, null);

-- ----------------------------
-- Table structure for sur_sys_environment
-- ----------------------------
DROP TABLE IF EXISTS `sur_sys_environment`;
CREATE TABLE `sur_sys_environment` (
  `id_sys_environment` bigint(20) NOT NULL AUTO_INCREMENT,
  `environment_key` varchar(20) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_sys_environment`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_sys_environment
-- ----------------------------
INSERT INTO `sur_sys_environment` VALUES ('1', 'DB_VERSION', '0.2015.05.22.12.06', '', '2015-05-22 12:07:29');
INSERT INTO `sur_sys_environment` VALUES ('2', 'APP_VERSION', '0.2015.05.22.12.06', '', '2015-05-22 12:07:31');

-- ----------------------------
-- Table structure for sur_sys_feature_create
-- ----------------------------
DROP TABLE IF EXISTS `sur_sys_feature_create`;
CREATE TABLE `sur_sys_feature_create` (
  `id_sys_feature_create` bigint(20) NOT NULL AUTO_INCREMENT,
  `no_feature` varchar(20) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT b'1',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_sys_feature_create`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_sys_feature_create
-- ----------------------------

-- ----------------------------
-- Table structure for sur_telephone
-- ----------------------------
DROP TABLE IF EXISTS `sur_telephone`;
CREATE TABLE `sur_telephone` (
  `id_telephone` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_telephone_type` bigint(20) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id_voter` bigint(20) NOT NULL,
  PRIMARY KEY (`id_telephone`),
  KEY `ix_sur_telephone_id_voter` (`id_voter`),
  KEY `ix_sur_telephone_id_telephone_type` (`id_telephone_type`),
  CONSTRAINT `sur_telephone_ibfk_1` FOREIGN KEY (`id_telephone_type`) REFERENCES `sur_m_telephone_type` (`id_telephone_type`),
  CONSTRAINT `sur_telephone_ibfk_2` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_telephone
-- ----------------------------

-- ----------------------------
-- Table structure for sur_text_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_text_data`;
CREATE TABLE `sur_text_data` (
  `id_basic_data` bigint(20) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `multi_line` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id_basic_data`),
  CONSTRAINT `fk_sur_text_data_sur_basic_data_1` FOREIGN KEY (`id_basic_data`) REFERENCES `sur_basic_data` (`id_basic_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_text_data
-- ----------------------------
INSERT INTO `sur_text_data` VALUES ('148', '4 - 1', '\0');
INSERT INTO `sur_text_data` VALUES ('149', '6 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('150', '8 - 5 ', '\0');
INSERT INTO `sur_text_data` VALUES ('151', '5 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('152', '3 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('153', '7 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('154', '9 - 1', '\0');
INSERT INTO `sur_text_data` VALUES ('155', '7 - 0', '\0');
INSERT INTO `sur_text_data` VALUES ('156', '8 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('157', '5 - 0', '\0');
INSERT INTO `sur_text_data` VALUES ('158', '1 - 1', '\0');
INSERT INTO `sur_text_data` VALUES ('159', '5 - 1', '\0');
INSERT INTO `sur_text_data` VALUES ('160', '9 - 4', '\0');
INSERT INTO `sur_text_data` VALUES ('161', '5 - 5', '\0');
INSERT INTO `sur_text_data` VALUES ('162', '5 - 1', '\0');
INSERT INTO `sur_text_data` VALUES ('163', '5 - 2', '\0');
INSERT INTO `sur_text_data` VALUES ('164', '8 - 7', '\0');
INSERT INTO `sur_text_data` VALUES ('166', '7 - 6', '\0');
INSERT INTO `sur_text_data` VALUES ('167', '6 - 0', '\0');
INSERT INTO `sur_text_data` VALUES ('168', '5 - 5', '\0');
INSERT INTO `sur_text_data` VALUES ('169', '8 - 6', '\0');
INSERT INTO `sur_text_data` VALUES ('276', 'test', '\0');
INSERT INTO `sur_text_data` VALUES ('277', 'test 1', '\0');
INSERT INTO `sur_text_data` VALUES ('278', 'test 2', '\0');
INSERT INTO `sur_text_data` VALUES ('279', 'test', '\0');
INSERT INTO `sur_text_data` VALUES ('280', 'test', '\0');
INSERT INTO `sur_text_data` VALUES ('281', 'test', '\0');
INSERT INTO `sur_text_data` VALUES ('282', 'test', '\0');
INSERT INTO `sur_text_data` VALUES ('293', '1', '\0');
INSERT INTO `sur_text_data` VALUES ('294', '2', '\0');
INSERT INTO `sur_text_data` VALUES ('295', '3', '\0');
INSERT INTO `sur_text_data` VALUES ('296', '4', '\0');
INSERT INTO `sur_text_data` VALUES ('297', '1', '\0');
INSERT INTO `sur_text_data` VALUES ('298', '2', '\0');
INSERT INTO `sur_text_data` VALUES ('299', '3', '\0');
INSERT INTO `sur_text_data` VALUES ('300', '4', '\0');
INSERT INTO `sur_text_data` VALUES ('404', 'Test', '\0');
INSERT INTO `sur_text_data` VALUES ('405', 'Aaa', '\0');
INSERT INTO `sur_text_data` VALUES ('406', 'Bbb', '\0');
INSERT INTO `sur_text_data` VALUES ('407', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('408', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('409', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('410', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('411', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('412', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('413', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('414', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('415', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('416', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('417', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('418', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('419', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('420', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('421', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('422', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('423', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('424', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('425', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('426', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('427', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('428', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('429', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('430', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('431', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('432', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('433', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('434', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('435', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('436', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('437', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('438', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('439', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('440', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('441', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('442', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('443', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('444', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('445', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('446', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('447', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('448', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('449', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('450', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('451', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('452', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('453', 'เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('454', 'ไม่เห็นด้วย', '\0');
INSERT INTO `sur_text_data` VALUES ('455', '20%', '\0');
INSERT INTO `sur_text_data` VALUES ('456', '25%', '\0');
INSERT INTO `sur_text_data` VALUES ('457', '30%', '\0');
INSERT INTO `sur_text_data` VALUES ('458', '40%', '\0');
INSERT INTO `sur_text_data` VALUES ('459', '65%', '\0');
INSERT INTO `sur_text_data` VALUES ('460', '55%', '\0');
INSERT INTO `sur_text_data` VALUES ('461', '45%', '\0');
INSERT INTO `sur_text_data` VALUES ('462', '35%', '\0');
INSERT INTO `sur_text_data` VALUES ('463', '102%', '\0');
INSERT INTO `sur_text_data` VALUES ('464', '52%', '\0');
INSERT INTO `sur_text_data` VALUES ('465', '68%', '\0');
INSERT INTO `sur_text_data` VALUES ('466', '72%', '\0');
INSERT INTO `sur_text_data` VALUES ('467', '5/2%', '\0');
INSERT INTO `sur_text_data` VALUES ('468', '3/2%', '\0');
INSERT INTO `sur_text_data` VALUES ('469', '8/9%', '\0');
INSERT INTO `sur_text_data` VALUES ('470', '2/9%', '\0');
INSERT INTO `sur_text_data` VALUES ('471', '13%', '\0');
INSERT INTO `sur_text_data` VALUES ('472', '14%', '\0');
INSERT INTO `sur_text_data` VALUES ('473', '2%', '\0');
INSERT INTO `sur_text_data` VALUES ('474', 'None', '\0');
INSERT INTO `sur_text_data` VALUES ('475', '90', '\0');
INSERT INTO `sur_text_data` VALUES ('476', '80', '\0');
INSERT INTO `sur_text_data` VALUES ('477', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('478', '75', '\0');
INSERT INTO `sur_text_data` VALUES ('479', '156', '\0');
INSERT INTO `sur_text_data` VALUES ('480', '136', '\0');
INSERT INTO `sur_text_data` VALUES ('481', '176', '\0');
INSERT INTO `sur_text_data` VALUES ('482', '196', '\0');
INSERT INTO `sur_text_data` VALUES ('483', '160', '\0');
INSERT INTO `sur_text_data` VALUES ('484', '80', '\0');
INSERT INTO `sur_text_data` VALUES ('485', '280', '\0');
INSERT INTO `sur_text_data` VALUES ('486', '270', '\0');
INSERT INTO `sur_text_data` VALUES ('487', '180', '\0');
INSERT INTO `sur_text_data` VALUES ('488', '260', '\0');
INSERT INTO `sur_text_data` VALUES ('489', '240', '\0');
INSERT INTO `sur_text_data` VALUES ('490', '280', '\0');
INSERT INTO `sur_text_data` VALUES ('491', '66', '\0');
INSERT INTO `sur_text_data` VALUES ('492', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('493', '80', '\0');
INSERT INTO `sur_text_data` VALUES ('494', '90', '\0');
INSERT INTO `sur_text_data` VALUES ('495', '270', '\0');
INSERT INTO `sur_text_data` VALUES ('496', '275', '\0');
INSERT INTO `sur_text_data` VALUES ('497', '250', '\0');
INSERT INTO `sur_text_data` VALUES ('498', '240', '\0');
INSERT INTO `sur_text_data` VALUES ('499', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('500', '70', '\0');
INSERT INTO `sur_text_data` VALUES ('501', '80', '\0');
INSERT INTO `sur_text_data` VALUES ('502', '90', '\0');
INSERT INTO `sur_text_data` VALUES ('503', '70', '\0');
INSERT INTO `sur_text_data` VALUES ('504', '65', '\0');
INSERT INTO `sur_text_data` VALUES ('505', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('506', '80', '\0');
INSERT INTO `sur_text_data` VALUES ('507', '3/4', '\0');
INSERT INTO `sur_text_data` VALUES ('508', '3/2', '\0');
INSERT INTO `sur_text_data` VALUES ('509', '3/5', '\0');
INSERT INTO `sur_text_data` VALUES ('510', '3/9', '\0');
INSERT INTO `sur_text_data` VALUES ('511', '40%', '\0');
INSERT INTO `sur_text_data` VALUES ('512', '20%', '\0');
INSERT INTO `sur_text_data` VALUES ('513', '60%', '\0');
INSERT INTO `sur_text_data` VALUES ('514', '70%', '\0');
INSERT INTO `sur_text_data` VALUES ('515', '118', '\0');
INSERT INTO `sur_text_data` VALUES ('516', '148', '\0');
INSERT INTO `sur_text_data` VALUES ('517', '135', '\0');
INSERT INTO `sur_text_data` VALUES ('518', '145', '\0');
INSERT INTO `sur_text_data` VALUES ('519', '1.075 km', '\0');
INSERT INTO `sur_text_data` VALUES ('520', '10.75 km', '\0');
INSERT INTO `sur_text_data` VALUES ('521', '0.1075 km', '\0');
INSERT INTO `sur_text_data` VALUES ('522', '0.0107 km', '\0');
INSERT INTO `sur_text_data` VALUES ('523', '600', '\0');
INSERT INTO `sur_text_data` VALUES ('524', '720', '\0');
INSERT INTO `sur_text_data` VALUES ('525', '640', '\0');
INSERT INTO `sur_text_data` VALUES ('526', '800', '\0');
INSERT INTO `sur_text_data` VALUES ('527', '7', '\0');
INSERT INTO `sur_text_data` VALUES ('528', '8', '\0');
INSERT INTO `sur_text_data` VALUES ('529', '9', '\0');
INSERT INTO `sur_text_data` VALUES ('530', '10', '\0');
INSERT INTO `sur_text_data` VALUES ('531', '30', '\0');
INSERT INTO `sur_text_data` VALUES ('532', '40', '\0');
INSERT INTO `sur_text_data` VALUES ('533', '50', '\0');
INSERT INTO `sur_text_data` VALUES ('534', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('535', '72', '\0');
INSERT INTO `sur_text_data` VALUES ('536', '64', '\0');
INSERT INTO `sur_text_data` VALUES ('537', '48', '\0');
INSERT INTO `sur_text_data` VALUES ('538', '36', '\0');
INSERT INTO `sur_text_data` VALUES ('539', 'Rs. 136', '\0');
INSERT INTO `sur_text_data` VALUES ('540', 'Rs. 146', '\0');
INSERT INTO `sur_text_data` VALUES ('541', 'Rs. 156', '\0');
INSERT INTO `sur_text_data` VALUES ('542', 'Rs. 166', '\0');
INSERT INTO `sur_text_data` VALUES ('543', 'Rs. 6000 ', '\0');
INSERT INTO `sur_text_data` VALUES ('544', 'Rs. 8000', '\0');
INSERT INTO `sur_text_data` VALUES ('545', 'Rs. 12000', '\0');
INSERT INTO `sur_text_data` VALUES ('546', 'Rs. 16000', '\0');
INSERT INTO `sur_text_data` VALUES ('547', '200', '\0');
INSERT INTO `sur_text_data` VALUES ('548', '225', '\0');
INSERT INTO `sur_text_data` VALUES ('549', '240', '\0');
INSERT INTO `sur_text_data` VALUES ('550', '250', '\0');
INSERT INTO `sur_text_data` VALUES ('551', '120 days', '\0');
INSERT INTO `sur_text_data` VALUES ('552', '240 days', '\0');
INSERT INTO `sur_text_data` VALUES ('553', '480 days', '\0');
INSERT INTO `sur_text_data` VALUES ('554', '720 days', '\0');
INSERT INTO `sur_text_data` VALUES ('555', '110', '\0');
INSERT INTO `sur_text_data` VALUES ('556', '132', '\0');
INSERT INTO `sur_text_data` VALUES ('557', '144', '\0');
INSERT INTO `sur_text_data` VALUES ('558', '150', '\0');
INSERT INTO `sur_text_data` VALUES ('559', '19', '\0');
INSERT INTO `sur_text_data` VALUES ('560', '75', '\0');
INSERT INTO `sur_text_data` VALUES ('561', '35', '\0');
INSERT INTO `sur_text_data` VALUES ('562', '20', '\0');
INSERT INTO `sur_text_data` VALUES ('563', 'father', '\0');
INSERT INTO `sur_text_data` VALUES ('564', 'son', '\0');
INSERT INTO `sur_text_data` VALUES ('565', 'brother', '\0');
INSERT INTO `sur_text_data` VALUES ('566', 'mother', '\0');
INSERT INTO `sur_text_data` VALUES ('567', 'TRIAKB', '\0');
INSERT INTO `sur_text_data` VALUES ('568', 'TIRALB', '\0');
INSERT INTO `sur_text_data` VALUES ('569', 'TIRLBA', '\0');
INSERT INTO `sur_text_data` VALUES ('570', 'TIRABL', '\0');
INSERT INTO `sur_text_data` VALUES ('571', '126', '\0');
INSERT INTO `sur_text_data` VALUES ('572', '122', '\0');
INSERT INTO `sur_text_data` VALUES ('573', '128', '\0');
INSERT INTO `sur_text_data` VALUES ('574', '138', '\0');
INSERT INTO `sur_text_data` VALUES ('575', '10 yrs', '\0');
INSERT INTO `sur_text_data` VALUES ('576', '20 yrs', '\0');
INSERT INTO `sur_text_data` VALUES ('577', '15 yrs', '\0');
INSERT INTO `sur_text_data` VALUES ('578', '17 yrs', '\0');
INSERT INTO `sur_text_data` VALUES ('579', '5 km', '\0');
INSERT INTO `sur_text_data` VALUES ('580', '15 km', '\0');
INSERT INTO `sur_text_data` VALUES ('581', '20 km', '\0');
INSERT INTO `sur_text_data` VALUES ('582', '12 km', '\0');
INSERT INTO `sur_text_data` VALUES ('583', 'south', '\0');
INSERT INTO `sur_text_data` VALUES ('584', 'north', '\0');
INSERT INTO `sur_text_data` VALUES ('585', 'east', '\0');
INSERT INTO `sur_text_data` VALUES ('586', 'west', '\0');
INSERT INTO `sur_text_data` VALUES ('587', '13', '\0');
INSERT INTO `sur_text_data` VALUES ('588', '17', '\0');
INSERT INTO `sur_text_data` VALUES ('589', '20', '\0');
INSERT INTO `sur_text_data` VALUES ('590', '24', '\0');
INSERT INTO `sur_text_data` VALUES ('591', '4', '\0');
INSERT INTO `sur_text_data` VALUES ('592', '8', '\0');
INSERT INTO `sur_text_data` VALUES ('593', '6', '\0');
INSERT INTO `sur_text_data` VALUES ('594', '2', '\0');
INSERT INTO `sur_text_data` VALUES ('595', 'Sunday', '\0');
INSERT INTO `sur_text_data` VALUES ('596', 'Monday', '\0');
INSERT INTO `sur_text_data` VALUES ('597', 'Tuesday', '\0');
INSERT INTO `sur_text_data` VALUES ('598', 'Saturday', '\0');
INSERT INTO `sur_text_data` VALUES ('599', 'Ram', '\0');
INSERT INTO `sur_text_data` VALUES ('600', 'Gopal', '\0');
INSERT INTO `sur_text_data` VALUES ('601', 'Mohan', '\0');
INSERT INTO `sur_text_data` VALUES ('602', 'Abbas', '\0');
INSERT INTO `sur_text_data` VALUES ('603', 'Some mans are pans', '\0');
INSERT INTO `sur_text_data` VALUES ('604', 'No man is a pan', '\0');
INSERT INTO `sur_text_data` VALUES ('605', 'All mans are not pans', '\0');
INSERT INTO `sur_text_data` VALUES ('606', 'None', '\0');
INSERT INTO `sur_text_data` VALUES ('607', '18', '\0');
INSERT INTO `sur_text_data` VALUES ('608', '17', '\0');
INSERT INTO `sur_text_data` VALUES ('609', '16', '\0');
INSERT INTO `sur_text_data` VALUES ('610', 'None', '\0');
INSERT INTO `sur_text_data` VALUES ('611', 'ABC', '\0');
INSERT INTO `sur_text_data` VALUES ('612', 'BCD', '\0');
INSERT INTO `sur_text_data` VALUES ('613', 'ADE', '\0');
INSERT INTO `sur_text_data` VALUES ('614', 'None', '\0');
INSERT INTO `sur_text_data` VALUES ('615', 'y/(x+y)', '\0');
INSERT INTO `sur_text_data` VALUES ('616', 'x/xy', '\0');
INSERT INTO `sur_text_data` VALUES ('617', 'x/(x+y)', '\0');
INSERT INTO `sur_text_data` VALUES ('618', 'y/xy', '\0');
INSERT INTO `sur_text_data` VALUES ('619', '16', '\0');
INSERT INTO `sur_text_data` VALUES ('620', '24', '\0');
INSERT INTO `sur_text_data` VALUES ('621', '30', '\0');
INSERT INTO `sur_text_data` VALUES ('622', '64', '\0');
INSERT INTO `sur_text_data` VALUES ('623', '0', '\0');
INSERT INTO `sur_text_data` VALUES ('624', '1', '\0');
INSERT INTO `sur_text_data` VALUES ('625', '-1', '\0');
INSERT INTO `sur_text_data` VALUES ('626', '4', '\0');
INSERT INTO `sur_text_data` VALUES ('627', 'Rs.90', '\0');
INSERT INTO `sur_text_data` VALUES ('628', 'Rs.1.00', '\0');
INSERT INTO `sur_text_data` VALUES ('629', 'Rs.3.00', '\0');
INSERT INTO `sur_text_data` VALUES ('630', 'Rs.8.00', '\0');
INSERT INTO `sur_text_data` VALUES ('631', '36', '\0');
INSERT INTO `sur_text_data` VALUES ('632', '72', '\0');
INSERT INTO `sur_text_data` VALUES ('633', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('634', '100', '\0');
INSERT INTO `sur_text_data` VALUES ('635', '0', '\0');
INSERT INTO `sur_text_data` VALUES ('636', '3', '\0');
INSERT INTO `sur_text_data` VALUES ('637', '4', '\0');
INSERT INTO `sur_text_data` VALUES ('638', '5', '\0');
INSERT INTO `sur_text_data` VALUES ('639', '1/4', '\0');
INSERT INTO `sur_text_data` VALUES ('640', '1/2', '\0');
INSERT INTO `sur_text_data` VALUES ('641', '1', '\0');
INSERT INTO `sur_text_data` VALUES ('642', '5', '\0');
INSERT INTO `sur_text_data` VALUES ('643', 'b < a ', '\0');
INSERT INTO `sur_text_data` VALUES ('644', 'b > a', '\0');
INSERT INTO `sur_text_data` VALUES ('645', 'b = a', '\0');
INSERT INTO `sur_text_data` VALUES ('646', 'b >= a', '\0');
INSERT INTO `sur_text_data` VALUES ('647', '12', '\0');
INSERT INTO `sur_text_data` VALUES ('648', '20', '\0');
INSERT INTO `sur_text_data` VALUES ('649', '24', '\0');
INSERT INTO `sur_text_data` VALUES ('650', '30', '\0');
INSERT INTO `sur_text_data` VALUES ('651', 'D/(M-3)', '\0');
INSERT INTO `sur_text_data` VALUES ('652', 'MD/3', '\0');
INSERT INTO `sur_text_data` VALUES ('653', 'M/(D-3)', '\0');
INSERT INTO `sur_text_data` VALUES ('654', '3D/(M2-3M)', '\0');
INSERT INTO `sur_text_data` VALUES ('655', '7', '\0');
INSERT INTO `sur_text_data` VALUES ('656', '8', '\0');
INSERT INTO `sur_text_data` VALUES ('657', '11', '\0');
INSERT INTO `sur_text_data` VALUES ('658', '12', '\0');
INSERT INTO `sur_text_data` VALUES ('659', '7', '\0');
INSERT INTO `sur_text_data` VALUES ('660', '8', '\0');
INSERT INTO `sur_text_data` VALUES ('661', '11', '\0');
INSERT INTO `sur_text_data` VALUES ('662', '12', '\0');
INSERT INTO `sur_text_data` VALUES ('663', '30', '\0');
INSERT INTO `sur_text_data` VALUES ('664', '40', '\0');
INSERT INTO `sur_text_data` VALUES ('665', '58', '\0');
INSERT INTO `sur_text_data` VALUES ('666', '60', '\0');
INSERT INTO `sur_text_data` VALUES ('667', '12', '\0');
INSERT INTO `sur_text_data` VALUES ('668', '15', '\0');
INSERT INTO `sur_text_data` VALUES ('669', '18', '\0');
INSERT INTO `sur_text_data` VALUES ('670', '20', '\0');
INSERT INTO `sur_text_data` VALUES ('671', '16', '\0');
INSERT INTO `sur_text_data` VALUES ('672', '12', '\0');
INSERT INTO `sur_text_data` VALUES ('673', '8', '\0');
INSERT INTO `sur_text_data` VALUES ('674', '6', '\0');
INSERT INTO `sur_text_data` VALUES ('675', '99/1020', '\0');
INSERT INTO `sur_text_data` VALUES ('676', '99/10', '\0');
INSERT INTO `sur_text_data` VALUES ('677', '0.9', '\0');
INSERT INTO `sur_text_data` VALUES ('678', 'None of these', '\0');
INSERT INTO `sur_text_data` VALUES ('679', '171/7 mins', '\0');
INSERT INTO `sur_text_data` VALUES ('680', '20 mins', '\0');
INSERT INTO `sur_text_data` VALUES ('681', '8 mins', '\0');
INSERT INTO `sur_text_data` VALUES ('682', 'None of these', '\0');
INSERT INTO `sur_text_data` VALUES ('683', '8 hrs', '\0');
INSERT INTO `sur_text_data` VALUES ('684', '7 1/2 hrs', '\0');
INSERT INTO `sur_text_data` VALUES ('685', '7 hrs', '\0');
INSERT INTO `sur_text_data` VALUES ('686', '9 hrs', '\0');
INSERT INTO `sur_text_data` VALUES ('687', '1/2 kmph', '\0');
INSERT INTO `sur_text_data` VALUES ('688', '7/12 kmph', '\0');
INSERT INTO `sur_text_data` VALUES ('689', '5 kmph', '\0');
INSERT INTO `sur_text_data` VALUES ('690', 'None of these', '\0');
INSERT INTO `sur_text_data` VALUES ('691', '38.5 sq.m', '\0');
INSERT INTO `sur_text_data` VALUES ('692', '155 sq.m', '\0');
INSERT INTO `sur_text_data` VALUES ('693', '144 sq.m', '\0');
INSERT INTO `sur_text_data` VALUES ('694', '19.25 sq.m', '\0');

-- ----------------------------
-- Table structure for sur_timestamp_data
-- ----------------------------
DROP TABLE IF EXISTS `sur_timestamp_data`;
CREATE TABLE `sur_timestamp_data` (
  `id_basic_data` bigint(20) NOT NULL,
  `format_type` varchar(255) DEFAULT NULL COMMENT 'DATE,\r\nTIME,\r\nTIMESTAMP',
  `show_second` bit(1) DEFAULT NULL,
  `format_time` varchar(255) DEFAULT NULL COMMENT 'F24,F12',
  `value` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_basic_data`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_timestamp_data
-- ----------------------------

-- ----------------------------
-- Table structure for sur_user
-- ----------------------------
DROP TABLE IF EXISTS `sur_user`;
CREATE TABLE `sur_user` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `id_gender` int(11) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `accept_tnc` bit(1) DEFAULT b'1',
  `count_send_activate` int(11) DEFAULT '0',
  `count_send_forgot` int(11) DEFAULT '0',
  `create_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `create_user` varchar(255) DEFAULT NULL,
  `update_date` timestamp NULL DEFAULT NULL,
  `update_user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_id` (`user_id`),
  KEY `country` (`country`),
  CONSTRAINT `sur_user_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_user
-- ----------------------------
INSERT INTO `sur_user` VALUES ('21', 'aaaaa', 'sssss', '15/58', 'manager', '1', 'TH', '', '0', '0', '2015-04-23 05:33:57', 'SYSTEM', null, null);
INSERT INTO `sur_user` VALUES ('22', 'padungrat', 'makchu', '1234', 'bangkok', '1', 'TH', '', '0', '0', '2015-04-28 04:10:26', 'SYSTEM', null, null);

-- ----------------------------
-- Table structure for sur_user_gen_code
-- ----------------------------
DROP TABLE IF EXISTS `sur_user_gen_code`;
CREATE TABLE `sur_user_gen_code` (
  `id_user_gen_code` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `id_gen_code_type` int(11) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `count` int(11) DEFAULT '0',
  `success` bit(1) DEFAULT b'0',
  `expire_date` datetime DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_user_gen_code`),
  KEY `user_id` (`user_id`),
  KEY `id_gen_code_type` (`id_gen_code_type`),
  CONSTRAINT `sur_user_gen_code_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`),
  CONSTRAINT `sur_user_gen_code_ibfk_2` FOREIGN KEY (`id_gen_code_type`) REFERENCES `sur_fix_email_template_type` (`id_email_template_type`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_user_gen_code
-- ----------------------------
INSERT INTO `sur_user_gen_code` VALUES ('11', '21', '2', '212DB9F36D05E84E2', '0', '', '2015-05-23 23:59:59', '2015-04-23 12:33:57');
INSERT INTO `sur_user_gen_code` VALUES ('12', '22', '2', '229653AD5BE8AC48D', '0', '', '2015-05-28 23:59:59', '2015-04-28 11:10:26');

-- ----------------------------
-- Table structure for sur_user_social_network
-- ----------------------------
DROP TABLE IF EXISTS `sur_user_social_network`;
CREATE TABLE `sur_user_social_network` (
  `id_user_social_network` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `provider_id` varchar(255) DEFAULT NULL,
  `provider_user_id` varchar(255) DEFAULT NULL,
  `access_token` varchar(255) DEFAULT NULL,
  `secret` varchar(255) DEFAULT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `profile_url` varchar(512) DEFAULT NULL,
  `image_url` varchar(512) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_user_social_network`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `sur_user_social_network_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_user_social_network
-- ----------------------------

-- ----------------------------
-- Table structure for sur_variables
-- ----------------------------
DROP TABLE IF EXISTS `sur_variables`;
CREATE TABLE `sur_variables` (
  `id_variables` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id_group_variables` int(11) NOT NULL,
  `table_jm_ref` varchar(255) DEFAULT NULL,
  `field_jm_ref` varchar(255) DEFAULT NULL,
  `id_parent` int(11) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_variables`),
  KEY `ix_sur_variables_id_group_variables` (`id_group_variables`),
  KEY `ix_sur_variables_id_parrent` (`id_parent`) USING BTREE,
  CONSTRAINT `sur_variables_ibfk_1` FOREIGN KEY (`id_group_variables`) REFERENCES `sur_group_variables` (`id_group_variables`),
  CONSTRAINT `sur_variables_ibfk_2` FOREIGN KEY (`id_parent`) REFERENCES `sur_variables` (`id_variables`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_variables
-- ----------------------------
INSERT INTO `sur_variables` VALUES ('1', 'Gender', null, '1', null, null, null, '');
INSERT INTO `sur_variables` VALUES ('2', 'Marrital Status', null, '1', null, null, null, '');
INSERT INTO `sur_variables` VALUES ('3', 'Address', null, '1', null, null, null, '');
INSERT INTO `sur_variables` VALUES ('4', 'Country', null, '1', null, null, '3', '');
INSERT INTO `sur_variables` VALUES ('5', 'Province', null, '1', null, null, '3', '');
INSERT INTO `sur_variables` VALUES ('6', 'City', null, '1', null, null, '3', '');
INSERT INTO `sur_variables` VALUES ('7', 'County', null, '1', null, null, '3', '');

-- ----------------------------
-- Table structure for sur_voter
-- ----------------------------
DROP TABLE IF EXISTS `sur_voter`;
CREATE TABLE `sur_voter` (
  `id_voter` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `timezone` varchar(255) DEFAULT NULL,
  `id_marriage_status` bigint(20) NOT NULL,
  `birthdate` date DEFAULT NULL,
  `user_id_owner` int(11) DEFAULT NULL,
  `id_gender` bigint(20) NOT NULL,
  `create_date` datetime NOT NULL,
  `active` bit(1) DEFAULT b'1',
  PRIMARY KEY (`id_voter`),
  KEY `ix_sur_voter_id_marriage_status` (`id_marriage_status`),
  KEY `ix_sur_voter_id_gender` (`id_gender`),
  KEY `user_id_owner` (`user_id_owner`),
  CONSTRAINT `sur_voter_ibfk_1` FOREIGN KEY (`id_marriage_status`) REFERENCES `sur_m_marriage_status` (`id_marriage_status`),
  CONSTRAINT `sur_voter_ibfk_3` FOREIGN KEY (`id_gender`) REFERENCES `sur_m_gender` (`id_gender`),
  CONSTRAINT `sur_voter_ibfk_4` FOREIGN KEY (`user_id_owner`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_voter
-- ----------------------------
INSERT INTO `sur_voter` VALUES ('1', 'tong_pa@hotmail.com', 'Mr.', 'padungrat', 'makchu', null, '1', '1972-01-01', '3', '1', '2015-02-25 15:53:21', '');
INSERT INTO `sur_voter` VALUES ('4', 'tongpama@gmail.com', 'Mr.', 'padungrat', 'makchu', null, '1', '1972-01-01', '3', '1', '2015-02-26 14:55:28', '');
INSERT INTO `sur_voter` VALUES ('6', 'padungsandy@gmail.com', 'Mr.', 'padungrat', 'makchu', null, '1', '1972-01-01', '3', '1', '2015-04-28 11:13:14', '');

-- ----------------------------
-- Table structure for sur_voter_map_type
-- ----------------------------
DROP TABLE IF EXISTS `sur_voter_map_type`;
CREATE TABLE `sur_voter_map_type` (
  `id_voter_map_type` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_voter` bigint(20) DEFAULT NULL,
  `id_voter_type` bigint(20) DEFAULT NULL,
  `is_send` bit(1) DEFAULT b'1' COMMENT '0= not send email, 1= send email',
  `create_date` datetime DEFAULT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_voter_map_type`),
  KEY `id_voter` (`id_voter`),
  KEY `id_voter_type` (`id_voter_type`),
  KEY `id_voter_map_type` (`id_voter_map_type`),
  CONSTRAINT `sur_voter_map_type_ibfk_1` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`),
  CONSTRAINT `sur_voter_map_type_ibfk_2` FOREIGN KEY (`id_voter_type`) REFERENCES `sur_m_voter_type` (`id_voter_type`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_voter_map_type
-- ----------------------------
INSERT INTO `sur_voter_map_type` VALUES ('1', '1', '1', '', '2015-05-12 18:12:27', '0000-00-00 00:00:00');
INSERT INTO `sur_voter_map_type` VALUES ('2', '4', '1', '', '2015-05-12 18:12:29', '0000-00-00 00:00:00');
INSERT INTO `sur_voter_map_type` VALUES ('3', '6', '1', '', '2015-05-12 18:12:32', '0000-00-00 00:00:00');
INSERT INTO `sur_voter_map_type` VALUES ('4', '1', '5', '', '2015-05-12 18:12:34', '0000-00-00 00:00:00');
INSERT INTO `sur_voter_map_type` VALUES ('5', '4', '5', '', '2015-05-12 18:12:37', '0000-00-00 00:00:00');
INSERT INTO `sur_voter_map_type` VALUES ('6', '6', '5', '', '2015-05-12 18:12:39', '0000-00-00 00:00:00');

-- ----------------------------
-- Table structure for tg_group
-- ----------------------------
DROP TABLE IF EXISTS `tg_group`;
CREATE TABLE `tg_group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(16) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `group_name` (`group_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_group
-- ----------------------------
INSERT INTO `tg_group` VALUES ('1', 'managers', 'Managers Group', '2014-10-13 09:46:21');
INSERT INTO `tg_group` VALUES ('2', 'voter', 'Voter Group', '2014-10-13 11:12:42');
INSERT INTO `tg_group` VALUES ('3', 'System Analysis', null, '2014-10-13 11:12:57');
INSERT INTO `tg_group` VALUES ('4', 'creator', 'Creator Group', '2015-04-23 12:14:33');

-- ----------------------------
-- Table structure for tg_group_permission
-- ----------------------------
DROP TABLE IF EXISTS `tg_group_permission`;
CREATE TABLE `tg_group_permission` (
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`group_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `tg_group_permission_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `tg_group` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tg_group_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `tg_permission` (`permission_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_group_permission
-- ----------------------------
INSERT INTO `tg_group_permission` VALUES ('1', '1');
INSERT INTO `tg_group_permission` VALUES ('2', '2');
INSERT INTO `tg_group_permission` VALUES ('3', '2');
INSERT INTO `tg_group_permission` VALUES ('4', '2');

-- ----------------------------
-- Table structure for tg_permission
-- ----------------------------
DROP TABLE IF EXISTS `tg_permission`;
CREATE TABLE `tg_permission` (
  `permission_id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_name` varchar(63) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`permission_id`),
  UNIQUE KEY `permission_name` (`permission_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_permission
-- ----------------------------
INSERT INTO `tg_permission` VALUES ('1', 'manage', 'This permission give an administrative right to the bearer');
INSERT INTO `tg_permission` VALUES ('2', 'User', 'User');

-- ----------------------------
-- Table structure for tg_user
-- ----------------------------
DROP TABLE IF EXISTS `tg_user`;
CREATE TABLE `tg_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `email_address` (`email_address`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_user
-- ----------------------------
INSERT INTO `tg_user` VALUES ('1', 'manager', 'manager@somedomain.com', 'Example manager', '936caf7d6ce9b98102d1ec36e7208248546a4d4437e5508c8270a3674c8f8309dff8b37e00ab4652d489a54fc74766339cf838f8c8275c762030217abb581e1e', '2014-10-13 09:46:21');
INSERT INTO `tg_user` VALUES ('2', 'editor', 'editor@somedomain.com', 'Example editor', '874eecf7ca79324ffa4b53141702afc5c29f28c329c3c2a50c371861f227301681bbbd207c1c3e1039a664190c123be2ce6c49f5c5f4ffd3eac49baa11145365', '2014-10-13 09:46:21');
INSERT INTO `tg_user` VALUES ('3', 'tong', 'tong_pa@hotmail.com', 'tong', '99ab3ab5793170a6bc0843a07b532d376c00b8a64f3f65230a3de687ba0e96259324a0be2466c91235e6c364777f89a19b842dba9df2db1623a85cb303bd0962', '2014-10-13 11:12:32');
INSERT INTO `tg_user` VALUES ('4', 'develop1', 'develop1@test.com', 'develop1', null, '2014-10-13 11:14:01');
INSERT INTO `tg_user` VALUES ('5', 'develop2', 'develop2@test.com', 'develop2', null, '2014-10-13 11:14:18');
INSERT INTO `tg_user` VALUES ('6', 'gain', 'gain@jobmatcher.com', 'gain', '20f8fc30065ceb3bdf88705ceadbe469228c4f41427b34cac90915cd6f47379dbd4873a23a721d39fe29b8c0216ec0d2c59db61a8968abf7256bf94126dc04f0', '2015-02-17 11:20:22');
INSERT INTO `tg_user` VALUES ('21', 'padungsandy@gmail.com', 'padungsandy@gmail.com', 'aaaaa sssss', 'af45c69991c001cc9c647f20fc96efd50ddb805ffdc3f08e450f4ab792b3e2476ba92ab50458f054940559cc684ae1b3d7b69425fc1e0f3ac31e4a1dc480ca41', '2015-04-23 12:33:57');
INSERT INTO `tg_user` VALUES ('22', 'tongpama@gmail.com', 'tongpama@gmail.com', 'padungrat makchu', '176abcd0dbe8b3c42f4785ec1825c77cc814c36497c1b9b89cdddb7a425d084c2e33ca5a8fc368605a6831cec0bc5bebc40e18d245d167a833b585eb8d9c0261', '2015-04-28 11:10:26');

-- ----------------------------
-- Table structure for tg_user_group
-- ----------------------------
DROP TABLE IF EXISTS `tg_user_group`;
CREATE TABLE `tg_user_group` (
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`group_id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `tg_user_group_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tg_user_group_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `tg_group` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_user_group
-- ----------------------------
INSERT INTO `tg_user_group` VALUES ('1', '1');
INSERT INTO `tg_user_group` VALUES ('3', '1');
INSERT INTO `tg_user_group` VALUES ('3', '4');
INSERT INTO `tg_user_group` VALUES ('4', '2');
INSERT INTO `tg_user_group` VALUES ('5', '2');
INSERT INTO `tg_user_group` VALUES ('6', '2');
INSERT INTO `tg_user_group` VALUES ('21', '2');
INSERT INTO `tg_user_group` VALUES ('22', '2');
