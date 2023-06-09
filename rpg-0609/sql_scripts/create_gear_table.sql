CREATE TABLE `rpg`.`gears` (
  `gid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `gear_id` SMALLINT NOT NULL,
  `level` TINYINT NOT NULL DEFAULT 1,
  `owner_id` INT UNSIGNED NOT NULL,
  `wearer_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`gid`),
  UNIQUE INDEX `gid_UNIQUE` (`gid` ASC) VISIBLE,
  INDEX `gear_owner_id_idx` (`owner_id` ASC) VISIBLE,
  INDEX `gear_wearer_id_idx` (`wearer_id` ASC) VISIBLE,
  CONSTRAINT `gear_owner_id`
    FOREIGN KEY (`owner_id`)
    REFERENCES `rpg`.`users` (`uid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `gear_wearer_id`
    FOREIGN KEY (`wearer_id`)
    REFERENCES `rpg`.`characters` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
