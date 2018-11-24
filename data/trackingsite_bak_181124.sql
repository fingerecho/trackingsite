-- MySQL dump 10.13  Distrib 5.6.42, for Linux (x86_64)
--
-- Host: localhost    Database: trackingsite
-- ------------------------------------------------------
-- Server version	5.6.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add visiter',7,'add_visiter'),(20,'Can change visiter',7,'change_visiter'),(21,'Can delete visiter',7,'delete_visiter'),(22,'Can add leavings',8,'add_leavings'),(23,'Can change leavings',8,'change_leavings'),(24,'Can delete leavings',8,'delete_leavings');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$FNNwaFcSMnDu$g2+pKJn8+VjKp9hE51SsHZvl813QEzlJG8pOu0kl0NQ=','2018-11-23 01:04:25.980362',1,'fingerechoroot','','','aaa@11.com',1,1,'2018-11-14 19:47:15.747749');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-14 19:49:50.686711','1','Visiter object (1)',1,'[{\"added\": {}}]',7,1),(2,'2018-11-14 23:46:45.542246','36','Visiter object (36)',3,'',7,1),(3,'2018-11-14 23:46:45.547569','35','Visiter object (35)',3,'',7,1),(4,'2018-11-14 23:46:45.550606','34','Visiter object (34)',3,'',7,1),(5,'2018-11-14 23:46:45.553161','33','Visiter object (33)',3,'',7,1),(6,'2018-11-14 23:46:45.555752','32','Visiter object (32)',3,'',7,1),(7,'2018-11-14 23:46:45.558513','31','Visiter object (31)',3,'',7,1),(8,'2018-11-14 23:46:45.561603','30','Visiter object (30)',3,'',7,1),(9,'2018-11-14 23:46:45.565384','29','Visiter object (29)',3,'',7,1),(10,'2018-11-14 23:46:45.568435','28','Visiter object (28)',3,'',7,1),(11,'2018-11-14 23:46:45.571305','27','Visiter object (27)',3,'',7,1),(12,'2018-11-14 23:46:45.574311','26','Visiter object (26)',3,'',7,1),(13,'2018-11-14 23:46:45.577358','25','Visiter object (25)',3,'',7,1),(14,'2018-11-14 23:46:45.579710','24','Visiter object (24)',3,'',7,1),(15,'2018-11-14 23:46:45.582000','23','Visiter object (23)',3,'',7,1),(16,'2018-11-14 23:46:45.584543','22','Visiter object (22)',3,'',7,1),(17,'2018-11-14 23:46:45.586963','21','Visiter object (21)',3,'',7,1),(18,'2018-11-14 23:46:45.589257','20','Visiter object (20)',3,'',7,1),(19,'2018-11-14 23:46:45.591641','19','Visiter object (19)',3,'',7,1),(20,'2018-11-14 23:46:45.595673','18','Visiter object (18)',3,'',7,1),(21,'2018-11-14 23:46:45.598179','17','Visiter object (17)',3,'',7,1),(22,'2018-11-14 23:46:45.601183','16','Visiter object (16)',3,'',7,1),(23,'2018-11-14 23:46:45.603532','15','Visiter object (15)',3,'',7,1),(24,'2018-11-14 23:46:45.606560','14','Visiter object (14)',3,'',7,1),(25,'2018-11-14 23:46:45.608967','13','Visiter object (13)',3,'',7,1),(26,'2018-11-14 23:46:45.611547','12','Visiter object (12)',3,'',7,1),(27,'2018-11-14 23:46:45.613788','11','Visiter object (11)',3,'',7,1),(28,'2018-11-14 23:46:45.615954','10','Visiter object (10)',3,'',7,1),(29,'2018-11-14 23:46:45.618494','9','Visiter object (9)',3,'',7,1),(30,'2018-11-14 23:46:45.620972','8','Visiter object (8)',3,'',7,1),(31,'2018-11-14 23:46:45.623708','7','Visiter object (7)',3,'',7,1),(32,'2018-11-14 23:46:45.625962','6','Visiter object (6)',3,'',7,1),(33,'2018-11-14 23:46:45.628646','5','Visiter object (5)',3,'',7,1),(34,'2018-11-14 23:46:45.631254','4','Visiter object (4)',3,'',7,1),(35,'2018-11-14 23:46:45.633664','3','Visiter object (3)',3,'',7,1),(36,'2018-11-14 23:46:45.636710','2','Visiter object (2)',3,'',7,1),(37,'2018-11-14 23:46:45.639303','1','Visiter object (1)',3,'',7,1),(38,'2018-11-15 16:19:56.244409','39','Visiter object (39)',3,'',7,1),(39,'2018-11-15 16:19:56.247364','38','Visiter object (38)',3,'',7,1),(40,'2018-11-15 16:34:42.104302','40','Visiter object (40)',3,'',7,1),(41,'2018-11-15 18:43:17.909708','47','Visiter object (47)',3,'',7,1),(42,'2018-11-15 18:43:17.913532','46','Visiter object (46)',3,'',7,1),(43,'2018-11-15 18:43:17.917060','45','Visiter object (45)',3,'',7,1),(44,'2018-11-15 18:43:17.922266','44','Visiter object (44)',3,'',7,1),(45,'2018-11-15 18:43:17.925115','43','Visiter object (43)',3,'',7,1),(46,'2018-11-15 18:43:17.927755','42','Visiter object (42)',3,'',7,1),(47,'2018-11-15 18:43:17.931500','41','Visiter object (41)',3,'',7,1),(48,'2018-11-17 01:42:46.645469','93','Visiter object (93)',3,'',7,1),(49,'2018-11-17 01:42:46.648224','92','Visiter object (92)',3,'',7,1),(50,'2018-11-17 01:42:46.652689','91','Visiter object (91)',3,'',7,1),(51,'2018-11-17 01:42:46.655181','90','Visiter object (90)',3,'',7,1),(52,'2018-11-17 01:42:46.658185','89','Visiter object (89)',3,'',7,1),(53,'2018-11-17 01:42:46.660701','88','Visiter object (88)',3,'',7,1),(54,'2018-11-17 01:42:46.663006','87','Visiter object (87)',3,'',7,1),(55,'2018-11-17 01:42:46.665333','86','Visiter object (86)',3,'',7,1),(56,'2018-11-17 01:42:46.667535','85','Visiter object (85)',3,'',7,1),(57,'2018-11-17 01:42:46.670212','84','Visiter object (84)',3,'',7,1),(58,'2018-11-17 01:42:46.672613','83','Visiter object (83)',3,'',7,1),(59,'2018-11-17 01:42:46.674758','82','Visiter object (82)',3,'',7,1),(60,'2018-11-17 01:42:46.677124','81','Visiter object (81)',3,'',7,1),(61,'2018-11-17 01:42:46.679340','80','Visiter object (80)',3,'',7,1),(62,'2018-11-17 01:42:46.681641','79','Visiter object (79)',3,'',7,1),(63,'2018-11-17 01:42:46.684215','78','Visiter object (78)',3,'',7,1),(64,'2018-11-17 01:42:46.686611','77','Visiter object (77)',3,'',7,1),(65,'2018-11-17 01:42:46.688900','76','Visiter object (76)',3,'',7,1),(66,'2018-11-17 01:42:46.692921','75','Visiter object (75)',3,'',7,1),(67,'2018-11-17 01:42:46.695541','74','Visiter object (74)',3,'',7,1),(68,'2018-11-17 01:42:46.697716','73','Visiter object (73)',3,'',7,1),(69,'2018-11-17 01:42:46.699950','72','Visiter object (72)',3,'',7,1),(70,'2018-11-17 01:42:46.702119','71','Visiter object (71)',3,'',7,1),(71,'2018-11-17 01:42:46.704409','70','Visiter object (70)',3,'',7,1),(72,'2018-11-17 01:42:46.706596','69','Visiter object (69)',3,'',7,1),(73,'2018-11-17 01:42:46.709189','68','Visiter object (68)',3,'',7,1),(74,'2018-11-17 01:42:46.711405','67','Visiter object (67)',3,'',7,1),(75,'2018-11-17 01:42:46.713518','66','Visiter object (66)',3,'',7,1),(76,'2018-11-17 01:42:46.715691','65','Visiter object (65)',3,'',7,1),(77,'2018-11-17 01:42:46.717811','64','Visiter object (64)',3,'',7,1),(78,'2018-11-17 01:42:46.719888','63','Visiter object (63)',3,'',7,1),(79,'2018-11-17 01:42:46.722001','62','Visiter object (62)',3,'',7,1),(80,'2018-11-17 01:42:46.724098','61','Visiter object (61)',3,'',7,1),(81,'2018-11-17 01:42:46.726256','60','Visiter object (60)',3,'',7,1),(82,'2018-11-17 01:42:46.728274','59','Visiter object (59)',3,'',7,1),(83,'2018-11-17 01:42:46.730321','58','Visiter object (58)',3,'',7,1),(84,'2018-11-17 01:42:46.732341','57','Visiter object (57)',3,'',7,1),(85,'2018-11-17 01:42:46.734458','56','Visiter object (56)',3,'',7,1),(86,'2018-11-17 01:42:46.736748','55','Visiter object (55)',3,'',7,1),(87,'2018-11-17 01:42:46.739198','54','Visiter object (54)',3,'',7,1),(88,'2018-11-17 01:42:46.741324','53','Visiter object (53)',3,'',7,1),(89,'2018-11-17 01:42:46.743449','52','Visiter object (52)',3,'',7,1),(90,'2018-11-17 01:42:46.745776','51','Visiter object (51)',3,'',7,1),(91,'2018-11-17 01:42:46.748000','50','Visiter object (50)',3,'',7,1),(92,'2018-11-17 01:42:46.750315','49','Visiter object (49)',3,'',7,1),(93,'2018-11-17 22:29:28.805218','103','Visiter object (103)',3,'',7,1),(94,'2018-11-17 22:29:28.808163','102','Visiter object (102)',3,'',7,1),(95,'2018-11-17 22:29:28.810427','101','Visiter object (101)',3,'',7,1),(96,'2018-11-17 23:37:59.687668','104','Visiter object (104)',2,'[{\"changed\": {\"fields\": [\"friend_status\"]}}]',7,1),(97,'2018-11-19 17:56:31.997103','108','Visiter object (108)',3,'',7,1),(98,'2018-11-19 17:56:32.000676','107','Visiter object (107)',3,'',7,1),(99,'2018-11-20 05:54:51.855347','116','Visiter object (116)',3,'',7,1),(100,'2018-11-20 05:54:51.859911','115','Visiter object (115)',3,'',7,1),(101,'2018-11-20 07:39:31.764904','125','Visiter object (125)',3,'',7,1),(102,'2018-11-20 07:39:31.768195','124','Visiter object (124)',3,'',7,1),(103,'2018-11-20 07:39:31.770839','123','Visiter object (123)',3,'',7,1),(104,'2018-11-20 07:39:31.774096','122','Visiter object (122)',3,'',7,1),(105,'2018-11-20 07:39:31.778952','121','Visiter object (121)',3,'',7,1),(106,'2018-11-20 07:39:31.781836','120','Visiter object (120)',3,'',7,1),(107,'2018-11-20 07:39:31.784353','119','Visiter object (119)',3,'',7,1),(108,'2018-11-20 07:39:31.786795','118','Visiter object (118)',3,'',7,1),(109,'2018-11-20 07:39:31.789637','117','Visiter object (117)',3,'',7,1),(110,'2018-11-20 08:13:07.250383','114','Visiter object (114)',3,'',7,1),(111,'2018-11-20 08:13:07.253770','113','Visiter object (113)',3,'',7,1),(112,'2018-11-20 08:13:07.256420','112','Visiter object (112)',3,'',7,1),(113,'2018-11-20 08:13:07.258834','110','Visiter object (110)',3,'',7,1),(114,'2018-11-20 08:13:07.261495','109','Visiter object (109)',3,'',7,1),(115,'2018-11-20 08:13:07.263905','104','Visiter object (104)',3,'',7,1),(116,'2018-11-20 08:13:07.266488','100','Visiter object (100)',3,'',7,1),(117,'2018-11-20 08:13:07.269364','99','Visiter object (99)',3,'',7,1),(118,'2018-11-20 08:13:07.274936','98','Visiter object (98)',3,'',7,1),(119,'2018-11-20 08:13:07.277917','97','Visiter object (97)',3,'',7,1),(120,'2018-11-20 08:13:07.280426','96','Visiter object (96)',3,'',7,1),(121,'2018-11-20 08:13:07.282995','95','Visiter object (95)',3,'',7,1),(122,'2018-11-20 08:13:07.285745','94','Visiter object (94)',3,'',7,1),(123,'2018-11-20 08:47:20.776647','131','Visiter object (131)',3,'',7,1),(124,'2018-11-20 08:47:20.780164','130','Visiter object (130)',3,'',7,1),(125,'2018-11-20 08:47:20.783001','129','Visiter object (129)',3,'',7,1),(126,'2018-11-20 08:47:20.785916','128','Visiter object (128)',3,'',7,1),(127,'2018-11-20 08:47:20.789522','127','Visiter object (127)',3,'',7,1),(128,'2018-11-20 08:47:20.793049','126','Visiter object (126)',3,'',7,1),(129,'2018-11-20 08:55:56.569629','135','Visiter object (135)',3,'',7,1),(130,'2018-11-20 08:55:56.573128','134','Visiter object (134)',3,'',7,1),(131,'2018-11-20 08:55:56.577154','133','Visiter object (133)',3,'',7,1),(132,'2018-11-20 08:55:56.580437','132','Visiter object (132)',3,'',7,1),(133,'2018-11-20 09:17:14.073436','137','Visiter object (137)',3,'',7,1),(134,'2018-11-20 09:17:14.077202','136','Visiter object (136)',3,'',7,1),(135,'2018-11-21 22:08:18.767206','143','Visiter object (143)',3,'',7,1),(136,'2018-11-21 22:08:18.773004','141','Visiter object (141)',3,'',7,1),(137,'2018-11-21 22:08:18.775551','106','Visiter object (106)',3,'',7,1),(138,'2018-11-22 00:45:21.095154','2','Leavings object (2)',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',8,1),(139,'2018-11-22 23:33:00.380771','3','Leavings object (3)',3,'',8,1),(140,'2018-11-22 23:33:00.383890','2','Leavings object (2)',3,'',8,1),(141,'2018-11-22 23:33:00.386128','1','Leavings object (1)',3,'',8,1),(142,'2018-11-23 01:07:00.576452','151','Visiter object (151)',3,'',7,1),(143,'2018-11-23 01:07:00.580754','150','Visiter object (150)',3,'',7,1),(144,'2018-11-23 01:07:00.583509','149','Visiter object (149)',3,'',7,1),(145,'2018-11-23 01:07:00.586271','148','Visiter object (148)',3,'',7,1),(146,'2018-11-24 04:27:18.512334','156','Visiter object (156)',3,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'leavingshandle','leavings'),(6,'sessions','session'),(7,'trackself','visiter');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-14 19:46:36.773448'),(2,'auth','0001_initial','2018-11-14 19:46:37.305625'),(3,'admin','0001_initial','2018-11-14 19:46:37.437684'),(4,'admin','0002_logentry_remove_auto_add','2018-11-14 19:46:37.449700'),(5,'contenttypes','0002_remove_content_type_name','2018-11-14 19:46:37.530903'),(6,'auth','0002_alter_permission_name_max_length','2018-11-14 19:46:37.584855'),(7,'auth','0003_alter_user_email_max_length','2018-11-14 19:46:37.640487'),(8,'auth','0004_alter_user_username_opts','2018-11-14 19:46:37.650958'),(9,'auth','0005_alter_user_last_login_null','2018-11-14 19:46:37.708884'),(10,'auth','0006_require_contenttypes_0002','2018-11-14 19:46:37.712127'),(11,'auth','0007_alter_validators_add_error_messages','2018-11-14 19:46:37.722979'),(12,'auth','0008_alter_user_username_max_length','2018-11-14 19:46:37.823833'),(13,'auth','0009_alter_user_last_name_max_length','2018-11-14 19:46:37.881232'),(14,'sessions','0001_initial','2018-11-14 19:46:37.920493'),(15,'trackself','0001_initial','2018-11-14 19:46:37.946921'),(16,'trackself','0002_auto_20181117_0958','2018-11-17 01:58:53.818619'),(17,'trackself','0003_auto_20181120_0128','2018-11-19 17:31:28.109042'),(18,'trackself','0004_visiter_brows_pages','2018-11-20 07:33:10.685726'),(19,'trackself','0005_visiter_casual_user','2018-11-20 07:58:07.477739'),(20,'leavingshandle','0001_initial','2018-11-21 23:14:35.712241'),(21,'trackself','0006_visiter_ip','2018-11-24 03:49:09.034006'),(22,'trackself','0007_auto_20181124_1148','2018-11-24 03:49:09.040092'),(23,'trackself','0008_auto_20181124_1225','2018-11-24 04:26:06.320989');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('348e7yijtg9f8gi950m6nyq56yx2tsfo','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-03 17:52:44.262040'),('3orinvejomoo78liwni44rzfrori0jr6','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-03 17:30:53.048717'),('3rxon2xsn92qc3a71qr7tiv7jloxpd9c','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 05:53:05.990224'),('4aokbita68uca14tnn7406tmui6u3d31','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 10:18:49.858831'),('90a0v45oigdy8r757089zc1ktcugdkzu','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:31:13.367071'),('ad5rsb9ku0b6izwpjaux7n8af7qwhfn3','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:28:41.073071'),('ay9a5l4gzs821meyrujlovsmsipnpcz4','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 07:59:54.353643'),('e0pg98ttcqys8iomzq27h2fk6k4qbt3m','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 07:35:52.702312'),('ipfkquzhw49t2k9brm7lnr34a5njzju9','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 03:59:12.095316'),('jozrd8uyslrg7y3wwwkmpxnsorca947w','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:54:07.704433'),('kj6jae7gvc5e6tdopao9i1lcmnxek7vg','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-03 00:23:00.742192'),('lk1ejxgrsqcquhblpp52unix7pad2xel','YTQxZWZjZTFiZGMxZjRmMTYwZTYxNjgxOTkwNDhhODFlY2YxY2ZmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTE2NzU3NjcwYzFiNjE3NzlmYzRiOGE0ZTVhNjMyODZjNzVjYmQyIn0=','2018-11-28 20:30:13.952713'),('mz5ygzqfr4xonnbn25zlltallp5iwd2a','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-03 16:35:50.934441'),('oqc4xs71222cij9o86tpcdqfyg8x82os','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:12:38.976148'),('sq4u9ghmkjtn4n62wvet4ogbrcg4h44f','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:19:14.099404'),('udznw89naquwhc4b5v1nt1pe9282v1ra','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-07 01:04:25.983775'),('uiapb5wtqfvxbdytkvzl3am41g204gxn','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-04 08:44:12.871147'),('upugcwatg3k4hth2d7b9j0o9t1xu6i07','YTQxZWZjZTFiZGMxZjRmMTYwZTYxNjgxOTkwNDhhODFlY2YxY2ZmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTE2NzU3NjcwYzFiNjE3NzlmYzRiOGE0ZTVhNjMyODZjNzVjYmQyIn0=','2018-11-30 00:30:34.875105'),('vtadlqrzbw11rrob4fogavhod3w5kwun','MDY3ZDcyYzlmMDYwNjc4Y2EwODBlMGM2ZDViZDlkYzMyZDk3ZDFkZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MDYzYzVjODc2MWM3ZDZkNjEzYjk4MGYwZTIxZDUxYmQ5NmUyOWYwIn0=','2018-12-03 19:24:57.944993'),('wk5yev35j16h83qjxw440a5yompz0dkt','YTQxZWZjZTFiZGMxZjRmMTYwZTYxNjgxOTkwNDhhODFlY2YxY2ZmYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTE2NzU3NjcwYzFiNjE3NzlmYzRiOGE0ZTVhNjMyODZjNzVjYmQyIn0=','2018-11-28 19:47:45.546798');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leavingshandle_leavings`
--

DROP TABLE IF EXISTS `leavingshandle_leavings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leavingshandle_leavings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `username` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `address` varchar(512) NOT NULL,
  `address2` varchar(512) NOT NULL,
  `content` varchar(4096) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leavingshandle_leavings`
--

LOCK TABLES `leavingshandle_leavings` WRITE;
/*!40000 ALTER TABLE `leavingshandle_leavings` DISABLE KEYS */;
INSERT INTO `leavingshandle_leavings` VALUES (4,'','','','a@11.com','','',''),(5,'','','','hello@11.com','','',''),(6,'','','','hello@11.com','','',''),(7,'','','fypignfypign','hellowrld@11.com','jiangxinongye','','helloworkdjaflkjfdk\nhellworlkjfadlskfj'),(8,'','','helloworld283285356@qq.com','283285356@qq.com','jiangxi','','helloworld this is not a test');
/*!40000 ALTER TABLE `leavingshandle_leavings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trackself_visiter`
--

DROP TABLE IF EXISTS `trackself_visiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trackself_visiter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_time_visit` varchar(20) NOT NULL,
  `last_time_visit` varchar(20) NOT NULL,
  `friend_status` varchar(1) NOT NULL,
  `visit_times` int(11) NOT NULL,
  `tokens` varchar(256) NOT NULL,
  `browser` varchar(64) NOT NULL,
  `device` varchar(64) NOT NULL,
  `os` varchar(64) NOT NULL,
  `brows_pages` varchar(64) NOT NULL,
  `casual_user` tinyint(1) NOT NULL,
  `ip` char(39) NOT NULL,
  `isp` varchar(128) NOT NULL,
  `location` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trackself_visiter`
--

LOCK TABLES `trackself_visiter` WRITE;
/*!40000 ALTER TABLE `trackself_visiter` DISABLE KEYS */;
INSERT INTO `trackself_visiter` VALUES (37,'2018-11-15','2018-11-15','0',1,'bosszhipin/6.151/1004 mozilla/5.0 (iphone','default_device','default_device','default_os','*',1,'defa','',''),(48,'2018-11-15','2018-11-15','0',1,'mozilla/5.0 (macintosh','default_device','default_device','default_os','*',1,'defa','',''),(105,'2018-11-19@11:18:24','2018-11-19@11:18:24','0',1,'129d846fae71cbe98280b7fe78132962$$151306274128575602522150360088','default_device','default_device','default_os','*',1,'defa','',''),(111,'2018-11-20@11:3:59','2018-11-20@20:53:40','0',3,'01dbb01f66624c7c2e7805b205f0658d$$24121925602751742023400670358','None','HuaweiVKY-AL00VKY-AL00','None','*',1,'defa','',''),(138,'2018-11-20@17:16:45','2018-11-24@0:17:25','2',7,'8ef8c9dd5273f6af1f48588558db71b7$$m3$$233290568341877686283407758820','Chrome Mobile','GenericGeneric SmartphoneSmartphone','','fangself.com.cn/',1,'defa','',''),(139,'2018-11-20@19:21:51','2018-11-20@19:22:2','0',2,'153251bd49e90db2c799f5b9531bf440$$783100800959609886451892633','Mobile Safari','AppleiPhoneiPhone','','fangself.com.cn/cv.html',1,'defa','',''),(140,'2018-11-20@19:23:30','2018-11-20@19:23:30','0',1,'153251bd49e90db2c799f5b9531bf440$$783100800959609886451892633','Mobile Safari','AppleiPhoneiPhone','','fangself.com.cn/cv.html',0,'defa','',''),(142,'2018-11-20@20:11:16','2018-11-20@20:18:7','2',5,'08ac6aeb466ccd8f05ad37a144afe0f8$$m3$$21923284841312561543586191094','Edge','','','fangself.com.cn/',1,'defa','',''),(144,'2018-11-21@10:19:24','2018-11-21@10:19:24','0',1,'08ac6aeb466ccd8f05ad37a144afe0f8$$21923284841312561543314827722','Edge','','','fangself.com.cn/cv',1,'defa','',''),(145,'2018-11-21@11:22:49','2018-11-21@11:22:49','0',1,'79fdf9a4513e49073c81a3fe9e85b865$$330299778030203794921863314302','Mobile Safari','AppleiPhoneiPhone','','fangself.com.cn/cv.html',1,'defa','',''),(146,'2018-11-21@14:42:45','2018-11-21@14:42:45','0',1,'d1ed831a110dc29a35c1347fbb238085$$166581494732003827923830078819','Chrome','','','fangself.com.cn/cv',1,'defa','',''),(147,'2018-11-22@6:9:9','2018-11-24@12:40:19','0',2,'c402f9b394ee325de76533495f874574$$3267893572279830619870176508','Chrome','','','fangself.com.cn/',1,'defa','',''),(152,'2018-11-23@10:52:39','2018-11-23@14:14:45','0',5,'d229566d0b27288fe691e4c820af9fb4$$266911316242390432433395085858','Chrome','','','fangself.com.cn/cv.html',1,'defa','',''),(153,'2018-11-23@11:40:29','2018-11-23@13:47:6','0',2,'e0ee83d5fbed2e45b689e90f944579e9$$190969094241280328572198769553','Chrome','','','fangself.com.cn/cv',1,'defa','',''),(154,'2018-11-23@13:41:39','2018-11-23@13:47:6','0',2,'e0ee83d5fbed2e45b689e90f944579e9$$190969094241280328572198769553','Chrome','','','fangself.com.cn/',1,'defa','',''),(155,'2018-11-23@16:45:43','2018-11-23@16:45:43','0',1,'3d295b2f081da2c79e33a69f48cae506$$38823087412871706601480465031','Chrome','','','fangself.com.cn/cv.html',1,'defa','','');
/*!40000 ALTER TABLE `trackself_visiter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-24 12:58:03
