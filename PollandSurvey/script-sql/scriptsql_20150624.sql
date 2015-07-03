ALTER TABLE `sur_use_external_link`
ADD COLUMN `id_voter`  bigint NULL AFTER `id_question_option`;

ALTER TABLE `sur_use_external_link` ADD FOREIGN KEY (`id_voter`) REFERENCES `sur_voter` (`id_voter`);




