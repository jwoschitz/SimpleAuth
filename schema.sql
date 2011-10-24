SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `login_attempts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(100) COLLATE utf8_bin NOT NULL,
  `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) COLLATE utf8_bin NOT NULL,
  `password` CHAR(64) COLLATE utf8_bin NOT NULL,
  `salt` CHAR(8) COLLATE utf8_bin NOT NULL,
  `is_activated` BOOLEAN NOT NULL DEFAULT '0',
  `activation_token` CHAR(32) COLLATE utf8_bin NOT NULL,
  `activation_token_requested` datetime DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `modified` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `UK_users_email` UNIQUE (`email`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;