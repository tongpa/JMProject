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


INSERT INTO `sur_fix_close_type` (`id_close_type`, `description`, `active`, `create_date`, `update_date`) VALUES (1, 'Close, Start new', '', '2015-9-30 10:57:19', NULL);
INSERT INTO `sur_fix_close_type` (`id_close_type`, `description`, `active`, `create_date`, `update_date`) VALUES (2, 'Close, Remember and Continue', '', '2015-9-30 10:57:23', NULL);
INSERT INTO `sur_fix_close_type` (`id_close_type`, `description`, `active`, `create_date`, `update_date`) VALUES (3, 'Close, Finish', '', '2015-9-30 10:57:25', NULL);




CREATE TABLE `sur_fix_language` (
`id_language`  bigint NOT NULL AUTO_INCREMENT ,
`code`  varchar(5) NULL ,
`description`  varchar(255) NULL ,
`active`  bit(1) NULL DEFAULT 1 ,
`create_date`  timestamp NULL DEFAULT CURRENT_TIMESTAMP ,
PRIMARY KEY (`id_language`)
);

insert into sur_fix_language (code,description) values ('ar','Arabic');
insert into sur_fix_language (code,description) values ('be','Belarusian');
insert into sur_fix_language (code,description) values ('bg','Bulgarian');
insert into sur_fix_language (code,description) values ('cs','Czech');
insert into sur_fix_language (code,description) values ('da','Danish');
insert into sur_fix_language (code,description) values ('de','German');
insert into sur_fix_language (code,description) values ('el','Greek');
insert into sur_fix_language (code,description) values ('en','English');
insert into sur_fix_language (code,description) values ('es','Spanish');
insert into sur_fix_language (code,description) values ('et','Estonian');
insert into sur_fix_language (code,description) values ('fi','Finnish');
insert into sur_fix_language (code,description) values ('fr','French');
insert into sur_fix_language (code,description) values ('ga','Irish');
insert into sur_fix_language (code,description) values ('hi','Hindi');
insert into sur_fix_language (code,description) values ('hr','Croatian');
insert into sur_fix_language (code,description) values ('hu','Hungarian');
insert into sur_fix_language (code,description) values ('in','Indonesian');
insert into sur_fix_language (code,description) values ('is','Icelandic');
insert into sur_fix_language (code,description) values ('it','Italian');
insert into sur_fix_language (code,description) values ('iw','Hebrew');
insert into sur_fix_language (code,description) values ('ja','Japanese');
insert into sur_fix_language (code,description) values ('ko','Korean');
insert into sur_fix_language (code,description) values ('lt','Lithuanian');
insert into sur_fix_language (code,description) values ('lv','Latvian');
insert into sur_fix_language (code,description) values ('mk','Macedonian');
insert into sur_fix_language (code,description) values ('ms','Malay');
insert into sur_fix_language (code,description) values ('mt','Maltese');
insert into sur_fix_language (code,description) values ('nl','Dutch');
insert into sur_fix_language (code,description) values ('no','Norwegian');
insert into sur_fix_language (code,description) values ('pl','Polish');
insert into sur_fix_language (code,description) values ('pt','Portuguese');
insert into sur_fix_language (code,description) values ('ro','Romanian');
insert into sur_fix_language (code,description) values ('ru','Russian');
insert into sur_fix_language (code,description) values ('sk','Slovak');
insert into sur_fix_language (code,description) values ('sl','Slovenian');
insert into sur_fix_language (code,description) values ('sq','Albanian');
insert into sur_fix_language (code,description) values ('sr','Serbian');
insert into sur_fix_language (code,description) values ('sv','Swedish');
insert into sur_fix_language (code,description) values ('th','Thai');
insert into sur_fix_language (code,description) values ('tr','Turkish');
insert into sur_fix_language (code,description) values ('uk','Ukrainian');
insert into sur_fix_language (code,description) values ('vi','Vietnamese');
insert into sur_fix_language (code,description) values ('zh','Chinese');



ALTER TABLE `sur_fix_country`
ADD COLUMN `code`  varchar(5) NULL AFTER `id_country`;


insert into sur_fix_country( code, country_name) values("AF","Afghanistan");
insert into sur_fix_country( code, country_name) values("AL","Albania");
insert into sur_fix_country( code, country_name) values("DZ","Algeria");
insert into sur_fix_country( code, country_name) values("AS","American Samoa");
insert into sur_fix_country( code, country_name) values("AD","Andorra");
insert into sur_fix_country( code, country_name) values("AO","Angola");
insert into sur_fix_country( code, country_name) values("AI","Anguilla");
insert into sur_fix_country( code, country_name) values("AQ","Antarctica");
insert into sur_fix_country( code, country_name) values("AR","Argentina");
insert into sur_fix_country( code, country_name) values("AM","Armenia");
insert into sur_fix_country( code, country_name) values("AW","Aruba");
insert into sur_fix_country( code, country_name) values("AU","Australia");
insert into sur_fix_country( code, country_name) values("AT","Austria");
insert into sur_fix_country( code, country_name) values("AZ","Azerbaijan");
insert into sur_fix_country( code, country_name) values("BS","Bahamas");
insert into sur_fix_country( code, country_name) values("BH","Bahrain");
insert into sur_fix_country( code, country_name) values("BD","Bangladesh");
insert into sur_fix_country( code, country_name) values("BB","Barbados");
insert into sur_fix_country( code, country_name) values("BY","Belarus");
insert into sur_fix_country( code, country_name) values("BE","Belgium");
insert into sur_fix_country( code, country_name) values("BZ","Belize");
insert into sur_fix_country( code, country_name) values("BJ","Benin");
insert into sur_fix_country( code, country_name) values("BM","Bermuda");
insert into sur_fix_country( code, country_name) values("BT","Bhutan");
insert into sur_fix_country( code, country_name) values("BO","Bolivia");
insert into sur_fix_country( code, country_name) values("BA","Bosnia and Herzegowina");
insert into sur_fix_country( code, country_name) values("BW","Botswana");
insert into sur_fix_country( code, country_name) values("BV","Bouvet Island");
insert into sur_fix_country( code, country_name) values("BR","Brazil");
insert into sur_fix_country( code, country_name) values("IO","British Indian Ocean Territory");
insert into sur_fix_country( code, country_name) values("BN","Brunei Darussalam");
insert into sur_fix_country( code, country_name) values("BG","Bulgaria");
insert into sur_fix_country( code, country_name) values("BF","Burkina Faso");
insert into sur_fix_country( code, country_name) values("BI","Burundi");
insert into sur_fix_country( code, country_name) values("KH","Cambodia");
insert into sur_fix_country( code, country_name) values("CM","Cameroon");
insert into sur_fix_country( code, country_name) values("CA","Canada");
insert into sur_fix_country( code, country_name) values("CV","Cape Verde");
insert into sur_fix_country( code, country_name) values("KY","Cayman Islands");
insert into sur_fix_country( code, country_name) values("CF","Central African Republic");
insert into sur_fix_country( code, country_name) values("TD","Chad");
insert into sur_fix_country( code, country_name) values("CL","Chile");
insert into sur_fix_country( code, country_name) values("CN","China");
insert into sur_fix_country( code, country_name) values("CX","Christmas Island");
insert into sur_fix_country( code, country_name) values("CC","Cocos (Keeling) Islands");
insert into sur_fix_country( code, country_name) values("CO","Colombia");
insert into sur_fix_country( code, country_name) values("KM","Comoros");
insert into sur_fix_country( code, country_name) values("CG","Congo");
insert into sur_fix_country( code, country_name) values("CD","Congo,  the Democratic Republic of the");
insert into sur_fix_country( code, country_name) values("CK","Cook Islands");
insert into sur_fix_country( code, country_name) values("CR","Costa Rica");
insert into sur_fix_country( code, country_name) values("CI","Cote d\'Ivoire");
insert into sur_fix_country( code, country_name) values("HR","Croatia (Hrvatska)");
insert into sur_fix_country( code, country_name) values("CU","Cuba");
insert into sur_fix_country( code, country_name) values("CY","Cyprus");
insert into sur_fix_country( code, country_name) values("CZ","Czech Republic");
insert into sur_fix_country( code, country_name) values("DK","Denmark");
insert into sur_fix_country( code, country_name) values("DJ","Djibouti");
insert into sur_fix_country( code, country_name) values("DM","Dominica");
insert into sur_fix_country( code, country_name) values("DO","Dominican Republic");
insert into sur_fix_country( code, country_name) values("EC","Ecuador");
insert into sur_fix_country( code, country_name) values("EG","Egypt");
insert into sur_fix_country( code, country_name) values("SV","El Salvador");
insert into sur_fix_country( code, country_name) values("GQ","Equatorial Guinea");
insert into sur_fix_country( code, country_name) values("ER","Eritrea");
insert into sur_fix_country( code, country_name) values("EE","Estonia");
insert into sur_fix_country( code, country_name) values("ET","Ethiopia");
insert into sur_fix_country( code, country_name) values("FK","Falkland Islands (Malvinas)");
insert into sur_fix_country( code, country_name) values("FO","Faroe Islands");
insert into sur_fix_country( code, country_name) values("FJ","Fiji");
insert into sur_fix_country( code, country_name) values("FI","Finland");
insert into sur_fix_country( code, country_name) values("FR","France");
insert into sur_fix_country( code, country_name) values("GF","French Guiana");
insert into sur_fix_country( code, country_name) values("PF","French Polynesia");
insert into sur_fix_country( code, country_name) values("TF","French Southern Territories");
insert into sur_fix_country( code, country_name) values("GA","Gabon");
insert into sur_fix_country( code, country_name) values("GM","Gambia");
insert into sur_fix_country( code, country_name) values("GE","Georgia");
insert into sur_fix_country( code, country_name) values("DE","Germany");
insert into sur_fix_country( code, country_name) values("GH","Ghana");
insert into sur_fix_country( code, country_name) values("GI","Gibraltar");
insert into sur_fix_country( code, country_name) values("GR","Greece");
insert into sur_fix_country( code, country_name) values("GL","Greenland");
insert into sur_fix_country( code, country_name) values("GD","Grenada");
insert into sur_fix_country( code, country_name) values("GP","Guadeloupe");
insert into sur_fix_country( code, country_name) values("GU","Guam");
insert into sur_fix_country( code, country_name) values("GT","Guatemala");
insert into sur_fix_country( code, country_name) values("GN","Guinea");
insert into sur_fix_country( code, country_name) values("GW","Guinea-Bissau");
insert into sur_fix_country( code, country_name) values("GY","Guyana");
insert into sur_fix_country( code, country_name) values("HT","Haiti");
insert into sur_fix_country( code, country_name) values("HM","Heard and Mc Donald Islands");
insert into sur_fix_country( code, country_name) values("VA","Holy See (Vatican City State)");
insert into sur_fix_country( code, country_name) values("HN","Honduras");
insert into sur_fix_country( code, country_name) values("HK","Hong Kong");
insert into sur_fix_country( code, country_name) values("HU","Hungary");
insert into sur_fix_country( code, country_name) values("IS","Iceland");
insert into sur_fix_country( code, country_name) values("IN","India");
insert into sur_fix_country( code, country_name) values("ID","Indonesia");
insert into sur_fix_country( code, country_name) values("IR","Iran (Islamic Republic of)");
insert into sur_fix_country( code, country_name) values("IQ","Iraq");
insert into sur_fix_country( code, country_name) values("IE","Ireland");
insert into sur_fix_country( code, country_name) values("IL","Israel");
insert into sur_fix_country( code, country_name) values("IT","Italy");
insert into sur_fix_country( code, country_name) values("JM","Jamaica");
insert into sur_fix_country( code, country_name) values("JP","Japan");
insert into sur_fix_country( code, country_name) values("JO","Jordan");
insert into sur_fix_country( code, country_name) values("KZ","Kazakhstan");
insert into sur_fix_country( code, country_name) values("KE","Kenya");
insert into sur_fix_country( code, country_name) values("KI","Kiribati");
insert into sur_fix_country( code, country_name) values("KP","Korea,  Democratic People\'s Republic of");
insert into sur_fix_country( code, country_name) values("KR","Korea,  Republic of");
insert into sur_fix_country( code, country_name) values("KW","Kuwait");
insert into sur_fix_country( code, country_name) values("KG","Kyrgyzstan");
insert into sur_fix_country( code, country_name) values("LA","Lao People\'s Democratic Republic");
insert into sur_fix_country( code, country_name) values("LV","Latvia");
insert into sur_fix_country( code, country_name) values("LB","Lebanon");
insert into sur_fix_country( code, country_name) values("LS","Lesotho");
insert into sur_fix_country( code, country_name) values("LR","Liberia");
insert into sur_fix_country( code, country_name) values("LY","Libyan Arab Jamahiriya");
insert into sur_fix_country( code, country_name) values("LI","Liechtenstein");
insert into sur_fix_country( code, country_name) values("LT","Lithuania");
insert into sur_fix_country( code, country_name) values("LU","Luxembourg");
insert into sur_fix_country( code, country_name) values("MO","Macau");
insert into sur_fix_country( code, country_name) values("MK","Macedonia,  The Former Yugoslav Republic of");
insert into sur_fix_country( code, country_name) values("MG","Madagascar");
insert into sur_fix_country( code, country_name) values("MW","Malawi");
insert into sur_fix_country( code, country_name) values("MY","Malaysia");
insert into sur_fix_country( code, country_name) values("MV","Maldives");
insert into sur_fix_country( code, country_name) values("ML","Mali");
insert into sur_fix_country( code, country_name) values("MT","Malta");
insert into sur_fix_country( code, country_name) values("MH","Marshall Islands");
insert into sur_fix_country( code, country_name) values("MQ","Martinique");
insert into sur_fix_country( code, country_name) values("MR","Mauritania");
insert into sur_fix_country( code, country_name) values("MU","Mauritius");
insert into sur_fix_country( code, country_name) values("YT","Mayotte");
insert into sur_fix_country( code, country_name) values("MX","Mexico");
insert into sur_fix_country( code, country_name) values("FM","Micronesia,  Federated States of");
insert into sur_fix_country( code, country_name) values("MD","Moldova,  Republic of");
insert into sur_fix_country( code, country_name) values("MC","Monaco");
insert into sur_fix_country( code, country_name) values("MN","Mongolia");
insert into sur_fix_country( code, country_name) values("MS","Montserrat");
insert into sur_fix_country( code, country_name) values("MA","Morocco");
insert into sur_fix_country( code, country_name) values("MZ","Mozambique");
insert into sur_fix_country( code, country_name) values("MM","Myanmar");
insert into sur_fix_country( code, country_name) values("NA","Namibia");
insert into sur_fix_country( code, country_name) values("NR","Nauru");
insert into sur_fix_country( code, country_name) values("NP","Nepal");
insert into sur_fix_country( code, country_name) values("NL","Netherlands");
insert into sur_fix_country( code, country_name) values("AN","Netherlands Antilles");
insert into sur_fix_country( code, country_name) values("NC","New Caledonia");
insert into sur_fix_country( code, country_name) values("NZ","New Zealand");
insert into sur_fix_country( code, country_name) values("NI","Nicaragua");
insert into sur_fix_country( code, country_name) values("NE","Niger");
insert into sur_fix_country( code, country_name) values("NG","Nigeria");
insert into sur_fix_country( code, country_name) values("NU","Niue");
insert into sur_fix_country( code, country_name) values("NF","Norfolk Island");
insert into sur_fix_country( code, country_name) values("MP","Northern Mariana Islands");
insert into sur_fix_country( code, country_name) values("NO","Norway");
insert into sur_fix_country( code, country_name) values("OM","Oman");
insert into sur_fix_country( code, country_name) values("PK","Pakistan");
insert into sur_fix_country( code, country_name) values("PW","Palau");
insert into sur_fix_country( code, country_name) values("PA","Panama");
insert into sur_fix_country( code, country_name) values("PG","Papua New Guinea");
insert into sur_fix_country( code, country_name) values("PY","Paraguay");
insert into sur_fix_country( code, country_name) values("PE","Peru");
insert into sur_fix_country( code, country_name) values("PH","Philippines");
insert into sur_fix_country( code, country_name) values("PN","Pitcairn");
insert into sur_fix_country( code, country_name) values("PL","Poland");
insert into sur_fix_country( code, country_name) values("PT","Portugal");
insert into sur_fix_country( code, country_name) values("PR","Puerto Rico");
insert into sur_fix_country( code, country_name) values("QA","Qatar");
insert into sur_fix_country( code, country_name) values("RE","Reunion");
insert into sur_fix_country( code, country_name) values("RO","Romania");
insert into sur_fix_country( code, country_name) values("RU","Russian Federation");
insert into sur_fix_country( code, country_name) values("RW","Rwanda");
insert into sur_fix_country( code, country_name) values("KN","Saint Kitts and Nevis");
insert into sur_fix_country( code, country_name) values("LC","Saint LUCIA");
insert into sur_fix_country( code, country_name) values("VC","Saint Vincent and the Grenadines");
insert into sur_fix_country( code, country_name) values("WS","Samoa");
insert into sur_fix_country( code, country_name) values("SM","San Marino");
insert into sur_fix_country( code, country_name) values("ST","Sao Tome and Principe");
insert into sur_fix_country( code, country_name) values("SA","Saudi Arabia");
insert into sur_fix_country( code, country_name) values("SN","Senegal");
insert into sur_fix_country( code, country_name) values("SC","Seychelles");
insert into sur_fix_country( code, country_name) values("SL","Sierra Leone");
insert into sur_fix_country( code, country_name) values("SG","Singapore");
insert into sur_fix_country( code, country_name) values("SK","Slovakia (Slovak Republic)");
insert into sur_fix_country( code, country_name) values("SI","Slovenia");
insert into sur_fix_country( code, country_name) values("SB","Solomon Islands");
insert into sur_fix_country( code, country_name) values("SO","Somalia");
insert into sur_fix_country( code, country_name) values("ZA","South Africa");
insert into sur_fix_country( code, country_name) values("GS","South Georgia and the South Sandwich Islands");
insert into sur_fix_country( code, country_name) values("ES","Spain");
insert into sur_fix_country( code, country_name) values("LK","Sri Lanka");
insert into sur_fix_country( code, country_name) values("SH","St. Helena");
insert into sur_fix_country( code, country_name) values("PM","St. Pierre and Miquelon");
insert into sur_fix_country( code, country_name) values("SD","Sudan");
insert into sur_fix_country( code, country_name) values("SR","Suriname");
insert into sur_fix_country( code, country_name) values("SJ","Svalbard and Jan Mayen Islands");
insert into sur_fix_country( code, country_name) values("SZ","Swaziland");
insert into sur_fix_country( code, country_name) values("SE","Sweden");
insert into sur_fix_country( code, country_name) values("CH","Switzerland");
insert into sur_fix_country( code, country_name) values("SY","Syrian Arab Republic");
insert into sur_fix_country( code, country_name) values("TW","Taiwan,  Province of China");
insert into sur_fix_country( code, country_name) values("TJ","Tajikistan");
insert into sur_fix_country( code, country_name) values("TZ","Tanzania,  United Republic of");
insert into sur_fix_country( code, country_name) values("TH","Thailand");
insert into sur_fix_country( code, country_name) values("TG","Togo");
insert into sur_fix_country( code, country_name) values("TK","Tokelau");
insert into sur_fix_country( code, country_name) values("TO","Tonga");
insert into sur_fix_country( code, country_name) values("TT","Trinidad and Tobago");
insert into sur_fix_country( code, country_name) values("TN","Tunisia");
insert into sur_fix_country( code, country_name) values("TR","Turkey");
insert into sur_fix_country( code, country_name) values("TM","Turkmenistan");
insert into sur_fix_country( code, country_name) values("TC","Turks and Caicos Islands");
insert into sur_fix_country( code, country_name) values("TV","Tuvalu");
insert into sur_fix_country( code, country_name) values("UG","Uganda");
insert into sur_fix_country( code, country_name) values("UA","Ukraine");
insert into sur_fix_country( code, country_name) values("AE","United Arab Emirates");
insert into sur_fix_country( code, country_name) values("GB","United Kingdom");
insert into sur_fix_country( code, country_name) values("US","United States");
insert into sur_fix_country( code, country_name) values("UM","United States Minor Outlying Islands");
insert into sur_fix_country( code, country_name) values("UY","Uruguay");
insert into sur_fix_country( code, country_name) values("UZ","Uzbekistan");
insert into sur_fix_country( code, country_name) values("VU","Vanuatu");
insert into sur_fix_country( code, country_name) values("VE","Venezuela");
insert into sur_fix_country( code, country_name) values("VN","Viet Nam");
insert into sur_fix_country( code, country_name) values("VG","Virgin Islands (British)");
insert into sur_fix_country( code, country_name) values("VI","Virgin Islands (U.S.)");
insert into sur_fix_country( code, country_name) values("WF","Wallis and Futuna Islands");
insert into sur_fix_country( code, country_name) values("EH","Western Sahara");
insert into sur_fix_country( code, country_name) values("YE","Yemen");
insert into sur_fix_country( code, country_name) values("ZM","Zambia");
insert into sur_fix_country( code, country_name) values("ZW","Zimbabwe");

ALTER TABLE `sur_fix_country`
CHANGE COLUMN `country_name` `description`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL AFTER `code`;


ALTER TABLE `sur_sys_environment`
MODIFY COLUMN `description`  text CHARACTER SET utf8 COLLATE utf8_general_ci NULL AFTER `environment_key`;

INSERT INTO `sur_sys_environment` (`id_sys_environment`, `environment_key`, `description`, `active`, `create_date`) VALUES (4, 'SCORE_VIEW_HTML', '<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n        <title>Background</title>\r\n		<style type=\"text/css\">\r\n			/*table { -pdf-keep-with-next: true; }\r\n			h1 {\r\n				font-size: 500%;\r\n			}\r\n			h2 {\r\n				font-size: 200%;\r\n			}\r\n			h3 {\r\n				font-size: 150%;\r\n			}*/\r\n            @page {\r\n				size: a6 landscape;\r\n				/*size : a5 landscape;*/\r\n				margin: 2cm;\r\n				@frame content_frame {\r\n					left: 10pt;\r\n					top: 10pt;\r\n					right : 10pt;\r\n					bottom: 100pt;\r\n					 width: 400pt;\r\n					height: 280pt; \r\n					-pdf-frame-border: 1;    /* for debugging the layout */\r\n				}\r\n                /*background-image: url(\"http://www.joomlaworks.net/images/demos/galleries/abstract/1.jpg\");*/\r\n				/* \r\n                @frame text {\r\n                    top: 6cm;\r\n                    left: 4cm;\r\n                    right: 4cm;\r\n                    bottom: 4cm;\r\n                    -pdf-frame-border: 1;\r\n                }*/\r\n            }\r\n		\r\n            \r\n        </style>\r\n</head>\r\n\r\n<body >\r\n<center>\r\n     <table border=0  style=\"width: 100%\">\r\n		<tr><td><center><h1><br/></H1></center></td></tr>\r\n		<tr><td><center><font  size=\"8\">CERTIFICATE</font></center></td></tr>\r\n		<tr><td><center><h3><br/></H3></center></td></tr>\r\n		<tr><td><center><h3></H3></center></td></tr>\r\n		<tr><td><center><div  style=\"font-size:150%;\" ><h2>[name]</h2></div></center></td></tr>\r\n		<tr><td><center><h3><br/></H3></center></td></tr>\r\n		<tr><td><center><h3><br/></H3></center></td></tr>   \r\n		<tr><td><center> <b><font color=\"red\" size=\"7\">Scores : [score]</font></b> </center></td></tr>\r\n	</table> \r\n</center>\r\n	\r\n       \r\n</body>\r\n</html>', '', '2015-10-14 16:02:43');

ALTER TABLE `sur_respondents`
ADD COLUMN `image_file`  blob NULL AFTER `id_question_option`;	

