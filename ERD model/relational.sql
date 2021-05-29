-- MySQL Workbench Synchronization
-- Generated: 2021-03-17 18:34
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: nada

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `movies_db`.`MovieGenre` 
DROP FOREIGN KEY `fk_MovieGenre_Movie`;

ALTER TABLE `movies_db`.`MovieGenre` 
ADD INDEX `fk_MovieGenre_Movie_idx` (`Movie_idMovie` ASC) VISIBLE,
DROP INDEX `fk_MovieGenre_Movie_idx` ;
;

CREATE TABLE IF NOT EXISTS `movies_db`.`Cast_Member` (
  `` INT(11) NULL DEFAULT NULL,
  `First_Name` VARCHAR(45) NOT NULL,
  `Last_Name` VARCHAR(45) NOT NULL,
  `Role` VARCHAR(45) NOT NULL,
  `Biography` VARCHAR(600) NULL DEFAULT NULL,
  `Nationality` VARCHAR(45) NOT NULL,
  `Date_Of_Birth` DATE NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `movies_db`.`Movie_has_Cast_Member` (
  `Movie_idMovie` INT(10) UNSIGNED NOT NULL,
  `Cast_Member_First_Name` VARCHAR(45) NOT NULL,
  `Cast_Member_Second_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Movie_idMovie`, `Cast_Member_First_Name`, `Cast_Member_Second_Name`),
  INDEX `fk_Movie_has_Cast_Member_Cast_Member1_idx` (`Cast_Member_First_Name` ASC, `Cast_Member_Second_Name` ASC) VISIBLE,
  INDEX `fk_Movie_has_Cast_Member_Movie1_idx` (`Movie_idMovie` ASC) VISIBLE,
  CONSTRAINT `fk_Movie_has_Cast_Member_Movie1`
    FOREIGN KEY (`Movie_idMovie`)
    REFERENCES `movies_db`.`Movie` (`idMovie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Movie_has_Cast_Member_Cast_Member1`
    FOREIGN KEY (`Cast_Member_First_Name` , `Cast_Member_Second_Name`)
    REFERENCES `movies_db`.`Cast_Member` (`FirstName` , `Second_Name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `movies_db`.`user` (
  `UserID` INT(11) NOT NULL,
  `Email_Address` VARCHAR(45) NOT NULL,
  `UerName` VARCHAR(45) NOT NULL,
  `Date_Of_Birth` DATE NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`UserID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `movies_db`.`user_Watch_Movie` (
  `user_UserID` INT(11) NOT NULL,
  `user_Email_Address` VARCHAR(45) NOT NULL,
  `Movie_idMovie` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`user_UserID`, `user_Email_Address`, `Movie_idMovie`),
  INDEX `fk_user_has_Movie_Movie1_idx` (`Movie_idMovie` ASC) VISIBLE,
  INDEX `fk_user_has_Movie_user1_idx` (`user_UserID` ASC, `user_Email_Address` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_Movie_user1`
    FOREIGN KEY (`user_UserID` , `user_Email_Address`)
    REFERENCES `movies_db`.`user` (`UserID` , `Email_Address`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_Movie_Movie1`
    FOREIGN KEY (`Movie_idMovie`)
    REFERENCES `movies_db`.`Movie` (`idMovie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `movies_db`.`Movie_Criticism` (
  `Rating` INT(11) NOT NULL,
  `Review` VARCHAR(45) NOT NULL,
  `Movie_idMovie` INT(10) UNSIGNED NOT NULL,
  `user_UserID` INT(11) NOT NULL,
  PRIMARY KEY (`Movie_idMovie`),
  INDEX `fk_Movie_Criticism_user1_idx` (`user_UserID` ASC) VISIBLE,
  CONSTRAINT `fk_Movie_Criticism_Movie1`
    FOREIGN KEY (`Movie_idMovie`)
    REFERENCES `movies_db`.`Movie` (`idMovie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Movie_Criticism_user1`
    FOREIGN KEY (`user_UserID`)
    REFERENCES `movies_db`.`user` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

ALTER TABLE `movies_db`.`MovieGenre` 
ADD CONSTRAINT `fk_MovieGenre_Movie`
  FOREIGN KEY (`Movie_idMovie`)
  REFERENCES `movies_db`.`Movie` (`idMovie`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
