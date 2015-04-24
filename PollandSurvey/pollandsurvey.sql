/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : pollandsurvey

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2015-04-24 19:24:17
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
) ENGINE=InnoDB AUTO_INCREMENT=368 DEFAULT CHARSET=utf8;

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

-- ----------------------------
-- Table structure for sur_basic_question
-- ----------------------------
DROP TABLE IF EXISTS `sur_basic_question`;
CREATE TABLE `sur_basic_question` (
  `id_question` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_basic_data` bigint(20) NOT NULL,
  `answer` bit(1) DEFAULT b'0',
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_question`,`id_basic_data`),
  KEY `fk_sur_basic_question_sur_basic_data` (`id_basic_data`),
  CONSTRAINT `fk_sur_basic_question_sur_basic_data` FOREIGN KEY (`id_basic_data`) REFERENCES `sur_basic_data` (`id_basic_data`),
  CONSTRAINT `fk_sur_basic_question_sur_question` FOREIGN KEY (`id_question`) REFERENCES `sur_question` (`id_question`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_basic_question
-- ----------------------------
INSERT INTO `sur_basic_question` VALUES ('53', '148', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('53', '149', '', '2');
INSERT INTO `sur_basic_question` VALUES ('53', '150', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('54', '151', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('54', '152', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('54', '153', '', '3');
INSERT INTO `sur_basic_question` VALUES ('55', '154', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('55', '155', '', '2');
INSERT INTO `sur_basic_question` VALUES ('55', '156', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('56', '157', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('56', '158', '', '2');
INSERT INTO `sur_basic_question` VALUES ('56', '159', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('57', '160', '', '1');
INSERT INTO `sur_basic_question` VALUES ('57', '161', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('57', '162', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('58', '163', '', '1');
INSERT INTO `sur_basic_question` VALUES ('58', '164', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('58', '166', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('59', '167', '', '1');
INSERT INTO `sur_basic_question` VALUES ('59', '168', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('59', '169', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('97', '276', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('97', '277', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('97', '278', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('98', '279', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('98', '280', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('98', '281', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('98', '282', '\0', '4');
INSERT INTO `sur_basic_question` VALUES ('102', '293', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('102', '294', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('102', '295', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('102', '296', '\0', '4');
INSERT INTO `sur_basic_question` VALUES ('103', '297', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('103', '298', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('103', '299', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('103', '300', '\0', '4');
INSERT INTO `sur_basic_question` VALUES ('122', '361', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('122', '362', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('122', '363', '\0', '3');
INSERT INTO `sur_basic_question` VALUES ('123', '364', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('123', '365', '\0', '2');
INSERT INTO `sur_basic_question` VALUES ('123', '366', '\0', '1');
INSERT INTO `sur_basic_question` VALUES ('123', '367', '\0', '2');

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
-- Table structure for sur_invitation
-- ----------------------------
DROP TABLE IF EXISTS `sur_invitation`;
CREATE TABLE `sur_invitation` (
  `id_invitation` bigint(20) NOT NULL AUTO_INCREMENT,
  `from_name` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `id_question_project` bigint(20) NOT NULL,
  `content` text,
  `create_date` datetime NOT NULL,
  `update_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_invitation`),
  KEY `ix_sur_invitation_id_question_project` (`id_question_project`),
  CONSTRAINT `sur_invitation_ibfk_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_invitation
-- ----------------------------

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_member_user
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=368 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_m_voter_type
-- ----------------------------
INSERT INTO `sur_m_voter_type` VALUES ('1', 'contact', '');
INSERT INTO `sur_m_voter_type` VALUES ('2', 'invite', '');
INSERT INTO `sur_m_voter_type` VALUES ('3', 'external', '');
INSERT INTO `sur_m_voter_type` VALUES ('4', 'JM', '');

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
  `question` varchar(255) DEFAULT NULL,
  `help_message` varchar(255) DEFAULT NULL,
  `text_label` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `active` bit(1) DEFAULT b'1',
  `id_question_project` bigint(20) NOT NULL,
  `order` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_question`),
  KEY `fk_sur_question_tg_user_1` (`user_id`),
  KEY `fk_sur_question_id_question_project_1` (`id_question_project`) USING BTREE,
  KEY `fk_sur_question_sur_question_type_1` (`id_question_type`),
  CONSTRAINT `fk_sur_question_sur_question_project_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `fk_sur_question_sur_question_type_1` FOREIGN KEY (`id_question_type`) REFERENCES `sur_m_question_type` (`id_question_type`),
  CONSTRAINT `fk_sur_question_tg_user_1` FOREIGN KEY (`user_id`) REFERENCES `tg_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question
-- ----------------------------
INSERT INTO `sur_question` VALUES ('53', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 4', '', '', '3', '', '10', '1');
INSERT INTO `sur_question` VALUES ('54', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 2', '', '', '3', '', '10', '2');
INSERT INTO `sur_question` VALUES ('55', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 7', '', '', '3', '', '10', '4');
INSERT INTO `sur_question` VALUES ('56', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 0', '', '', '3', '', '10', '3');
INSERT INTO `sur_question` VALUES ('57', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 5', '', '', '3', '', '10', '5');
INSERT INTO `sur_question` VALUES ('58', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 3', '', '', '3', '', '10', '6');
INSERT INTO `sur_question` VALUES ('59', '1', 'ผลลบในข้อใดมีค่าเท่ากับ 6', '', '', '3', '', '10', '8');
INSERT INTO `sur_question` VALUES ('97', '1', 'test', '', '', '6', '', '11', '1');
INSERT INTO `sur_question` VALUES ('98', '1', 'test', '', '', '6', '', '11', '2');
INSERT INTO `sur_question` VALUES ('102', '1', 'ทดสอบ', '', '', '3', '', '10', '7');
INSERT INTO `sur_question` VALUES ('103', '2', 'เลือกมากกว่า 1 ข้อ', '', '', '3', '', '10', '9');
INSERT INTO `sur_question` VALUES ('122', '4', 'test', '', '', '3', '', '10', '10');
INSERT INTO `sur_question` VALUES ('123', '4', 'test', '', '', '3', '', '10', '11');

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

-- ----------------------------
-- Table structure for sur_question_option
-- ----------------------------
DROP TABLE IF EXISTS `sur_question_option`;
CREATE TABLE `sur_question_option` (
  `id_question_option` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_question_project` bigint(20) DEFAULT NULL,
  `id_question_theme` bigint(20) DEFAULT NULL,
  `name_publication` varchar(255) DEFAULT NULL,
  `activate_date` datetime DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  `header_message` text,
  `footer_message` text,
  `welcome_message` text,
  `end_message` text,
  `gen_code` varchar(20) DEFAULT NULL,
  `limit_time` int(11) DEFAULT '0',
  `redirect_url` varchar(255) DEFAULT NULL,
  `show_navigator` bit(1) DEFAULT b'0',
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_question_option`),
  KEY `id_question_option` (`id_question_option`),
  KEY `id_question_project` (`id_question_project`) USING BTREE,
  KEY `id_question_theme` (`id_question_theme`),
  CONSTRAINT `sur_question_option_ibfk_1` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `sur_question_option_ibfk_2` FOREIGN KEY (`id_question_theme`) REFERENCES `sur_m_question_theme` (`id_question_theme`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_option
-- ----------------------------
INSERT INTO `sur_question_option` VALUES ('2', '10', '2', 'ทดสอบ', '2014-12-04 00:00:00', '2015-05-31 23:59:59', 'Header', 'Footer', '<h1>ยินดีต้อนรับการทำงาน</h1><br>', 'Thank you', null, '0', 'http://google.co.th', '\0', '2014-12-04 11:45:44');
INSERT INTO `sur_question_option` VALUES ('9', '11', '2', '11', '2015-02-01 00:00:00', '2015-02-28 23:59:59', 'Header', 'Footer', 'welcome', 'end', null, '0', 'http://google.co.th', '\0', '2015-02-17 16:11:04');

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_question_project
-- ----------------------------
INSERT INTO `sur_question_project` VALUES ('10', 'test', 'test', '3', '1', '', '', '', '', '2014-12-03 17:53:38', '2014-12-03 17:53:38', '');
INSERT INTO `sur_question_project` VALUES ('11', 'test', 'test', '6', '1', null, null, null, null, '2015-02-17 11:30:38', '2015-02-17 11:30:38', '');
INSERT INTO `sur_question_project` VALUES ('12', 'test 123456 45896585 42', 'test', '3', '1', '', '', '', '', '2015-02-20 16:10:36', '2015-02-20 16:10:36', '');

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
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`id_respondents`),
  KEY `ix_sur_respondents_id_question_option` (`id_question_option`),
  KEY `ix_sur_respondents_id_question_project` (`id_question_project`),
  KEY `ix_sur_respondents_id_voter` (`id_voter`),
  CONSTRAINT `sur_respondents_ibfk_1` FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`),
  CONSTRAINT `sur_respondents_ibfk_2` FOREIGN KEY (`id_question_project`) REFERENCES `sur_question_project` (`id_question_project`),
  CONSTRAINT `sur_respondents_ibfk_3` FOREIGN KEY (`id_question_option`) REFERENCES `sur_question_option` (`id_question_option`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_respondents
-- ----------------------------
INSERT INTO `sur_respondents` VALUES ('1', '1', '127.0.0.1', '2015-02-25 18:53:14', '10', '2', '', '2015-02-25 18:53:14');
INSERT INTO `sur_respondents` VALUES ('2', '4', '127.0.0.1', '2015-02-26 15:02:28', '10', '2', '\0', '2015-02-26 15:02:28');

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_user_gen_code
-- ----------------------------
INSERT INTO `sur_user_gen_code` VALUES ('11', '21', '2', '212DB9F36D05E84E2', '0', '', '2015-05-23 23:59:59', '2015-04-23 12:33:57');

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
  `id_voter_type` bigint(20) NOT NULL,
  `birthdate` date DEFAULT NULL,
  `id_gender` bigint(20) NOT NULL,
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`id_voter`),
  KEY `ix_sur_voter_id_marriage_status` (`id_marriage_status`),
  KEY `ix_sur_voter_id_gender` (`id_gender`),
  KEY `ix_sur_voter_id_voter_type` (`id_voter_type`),
  CONSTRAINT `sur_voter_ibfk_1` FOREIGN KEY (`id_marriage_status`) REFERENCES `sur_m_marriage_status` (`id_marriage_status`),
  CONSTRAINT `sur_voter_ibfk_2` FOREIGN KEY (`id_voter_type`) REFERENCES `sur_m_voter_type` (`id_voter_type`),
  CONSTRAINT `sur_voter_ibfk_3` FOREIGN KEY (`id_gender`) REFERENCES `sur_m_gender` (`id_gender`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sur_voter
-- ----------------------------
INSERT INTO `sur_voter` VALUES ('1', 'tong_pa@hotmail.com', 'Mr.', 'padungrat', 'makchu', null, '1', '1', '1972-01-01', '1', '2015-02-25 15:53:21');
INSERT INTO `sur_voter` VALUES ('4', 'tongpama@gmail.com', 'Mr.', 'padungrat', 'makchu', null, '1', '1', '1972-01-01', '1', '2015-02-26 14:55:28');

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tg_user
-- ----------------------------
INSERT INTO `tg_user` VALUES ('1', 'manager', 'manager@somedomain.com', 'Example manager', '936caf7d6ce9b98102d1ec36e7208248546a4d4437e5508c8270a3674c8f8309dff8b37e00ab4652d489a54fc74766339cf838f8c8275c762030217abb581e1e', '2014-10-13 09:46:21');
INSERT INTO `tg_user` VALUES ('2', 'editor', 'editor@somedomain.com', 'Example editor', '874eecf7ca79324ffa4b53141702afc5c29f28c329c3c2a50c371861f227301681bbbd207c1c3e1039a664190c123be2ce6c49f5c5f4ffd3eac49baa11145365', '2014-10-13 09:46:21');
INSERT INTO `tg_user` VALUES ('3', 'tong', 'tong_pa@hotmail.com', 'tong', 'fe378b5c5ff97bf65e336807ebdab4fcbddd859dc452532a2c3a8b3875698393068afc9380b3944091211dd458a95a1fc0f1fea626837e3cecbea5b564177c73', '2014-10-13 11:12:32');
INSERT INTO `tg_user` VALUES ('4', 'develop1', 'develop1@test.com', 'develop1', null, '2014-10-13 11:14:01');
INSERT INTO `tg_user` VALUES ('5', 'develop2', 'develop2@test.com', 'develop2', null, '2014-10-13 11:14:18');
INSERT INTO `tg_user` VALUES ('6', 'gain', 'gain@jobmatcher.com', 'gain', '20f8fc30065ceb3bdf88705ceadbe469228c4f41427b34cac90915cd6f47379dbd4873a23a721d39fe29b8c0216ec0d2c59db61a8968abf7256bf94126dc04f0', '2015-02-17 11:20:22');
INSERT INTO `tg_user` VALUES ('21', 'padungsandy@gmail.com', 'padungsandy@gmail.com', 'aaaaa sssss', '21c210b93f7868c713915eb4f15cf0dc8da5f28488e94b4c1725ba98216caf4b4e18d97857474b91197da72804792d9292ce28942da415d32cfe607f15236b8c', '2015-04-23 12:33:57');

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
