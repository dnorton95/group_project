CREATE DATABASE  IF NOT EXISTS `group_project` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `group_project`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: group_project
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ratings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `comment` varchar(600) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `restaurant_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ratings_users_idx` (`user_id`),
  KEY `fk_ratings_restaurants1_idx` (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
INSERT INTO `ratings` VALUES (1,4,'My favorite Italian restaurant in the Atlanta area. The squid ink pasta is a must to try.','2024-05-01 14:18:21','2024-05-06 19:44:19',1,2),(2,5,'Employees go above and beyond for their customers. The food is delicious, you cannot go wrong with their menu.','2024-05-01 14:18:21','2024-05-06 19:45:00',2,5),(3,4,'Great food, wonderful ambiance, and delightful owners.','2024-05-01 14:18:21','2024-05-06 19:45:22',3,4),(4,4,'Still killin it!! Love the vibes! Love the food!','2024-05-01 14:18:21','2024-05-06 19:45:44',4,1),(5,5,' We ordered the soup du jour, crawfish bisque, and it was sooooo delicious! Looking forward to going back.','2024-05-01 14:18:21','2024-05-06 19:46:07',5,7),(6,4,'still the best!','2024-05-07 09:49:25','2024-05-07 09:49:25',1,2);
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurants` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `cuisine` varchar(45) NOT NULL,
  `street` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `state` char(2) NOT NULL,
  `zip_code` int NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'Sushi Den','Japanese','1487 S Pearl St','Denver','CO',80210,'303-777-0826','2024-05-01 11:25:47','2024-05-01 11:25:47'),(2,'La Tavola Trattoria','Italian','992 Virginia Ave NE','Atlanta','GA',30306,'404-873-5430','2024-05-01 11:58:36','2024-05-01 11:58:36'),(3,'Daawat Grill','Indian','820 Pike St','Seattle','WA',98101,'206-467-7272','2024-05-01 11:58:36','2024-05-01 11:58:36'),(4,'Cantaloop','Ethiopian','7095 Hollywood Blvd','Los Angeles','CA',90028,'213-652-2331','2024-05-01 11:58:36','2024-05-01 11:58:36'),(5,'TJ Birria Y Mas','Mexican','2025 N Durham Dr Ste A','Houston','TX',77008,'713-393-7461','2024-05-01 11:58:36','2024-05-01 11:58:36'),(6,'Cafe Katja','German','70 Orchard St','New York','NY',10002,'212-219-9545','2024-05-01 11:58:36','2024-05-01 11:58:36'),(7,'Atchafalaya Restaurant','Creole','901 Louisiana Ave','New Orleans','LA',70115,'504-891-9626','2024-05-01 11:58:36','2024-05-01 11:58:36');
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(200) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Jennifer','MacIsaac','jmacisaac@gmail.cm','jjjjjjjj','2024-05-01 13:51:56','2024-05-01 13:51:56'),(2,'Sue','Silva','ssilva@gmail.com','ssssssss','2024-05-01 13:51:56','2024-05-01 13:51:56'),(3,'Maureen','Browne','mbrown@gmail.com','mmmmmmmm','2024-05-01 13:51:56','2024-05-01 13:51:56'),(4,'Kerry','Cain','kcain@gmail.com','kkkkkkkk','2024-05-01 13:51:56','2024-05-01 13:51:56'),(5,'Tom','Ayers','tayers@gmail.com','tttttttt','2024-05-01 13:51:56','2024-05-01 13:51:56');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'group_project'
--

--
-- Dumping routines for database 'group_project'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-07 11:18:36
