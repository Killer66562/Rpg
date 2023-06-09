CREATE TABLE `rpg`.`items` (
  `iid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `item_id` SMALLINT UNSIGNED NOT NULL,
  `count` INT UNSIGNED NOT NULL DEFAULT 0,
  `owner_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`iid`),
  INDEX `uid_idx` (`owner_id` ASC) VISIBLE,
  CONSTRAINT `item_owner_id`
    FOREIGN KEY (`owner_id`)
    REFERENCES `rpg`.`users` (`uid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
