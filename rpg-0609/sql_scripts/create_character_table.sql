CREATE TABLE `rpg`.`characters` (
  `cid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `character_id` VARCHAR(45) NOT NULL,
  `level` SMALLINT NOT NULL DEFAULT 1,
  `owner_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`cid`),
  UNIQUE INDEX `cid_UNIQUE` (`cid` ASC) VISIBLE,
  INDEX `owned_user_id_idx` (`owner_id` ASC) VISIBLE,
  CONSTRAINT `owned_user_id`
    FOREIGN KEY (`owner_id`)
    REFERENCES `rpg`.`users` (`uid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);