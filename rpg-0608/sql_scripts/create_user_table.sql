CREATE TABLE `rpg`.`users` (
  `uid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `dc_id` BIGINT NOT NULL,
  `level` BIGINT NOT NULL DEFAULT 1,
  `money` BIGINT NOT NULL DEFAULT 60000,
  `exp` BIGINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`uid`),
  UNIQUE INDEX `uid_UNIQUE` (`uid` ASC) VISIBLE,
  UNIQUE INDEX `dc_id_UNIQUE` (`dc_id` ASC) VISIBLE);