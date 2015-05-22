ALTER TABLE `sur_question_option`
ADD COLUMN `send_status`  bit(1) NULL DEFAULT 0 COMMENT '0=not send to voter,1=send to voter already' AFTER `redirect_url`;

ALTER TABLE `sur_voter_map_type`
ADD COLUMN `is_send`  bit(1) NULL DEFAULT 1 COMMENT '0= not send email, 1= send email' AFTER `id_voter_type`;


ALTER TABLE `sur_voter`
ADD COLUMN `active`  bit(1) NULL DEFAULT 1 AFTER `create_date`;




