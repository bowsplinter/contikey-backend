-- MySQL dump 10.16  Distrib 10.2.9-MariaDB, for osx10.12 (x86_64)
--
-- Host: mycontikey.cjivvjfjcng2.ap-southeast-1.rds.amazonaws.com    Database: dboard
-- ------------------------------------------------------
-- Server version	10.0.32-MariaDB

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
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `article` (
  `article_id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(500) NOT NULL,
  `caption` varchar(500) DEFAULT NULL,
  `preview_image` varchar(500) DEFAULT NULL,
  `preview_title` varchar(100) DEFAULT NULL,
  `preview_text` varchar(500) DEFAULT NULL,
  `channel_id` int(11) DEFAULT NULL,
  `shared_from_article_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `num_words` int(11) DEFAULT NULL,
  `preview_x_frame_options` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`article_id`),
  KEY `channel_id` (`channel_id`),
  KEY `shared_from_article_id` (`shared_from_article_id`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`channel_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `article_ibfk_2` FOREIGN KEY (`shared_from_article_id`) REFERENCES `article` (`article_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'https://dog.ceo/','Never seen such a reliable sites to learn more about how different breeds of dogs look like','https://dog.ceo/img/dog-fb-preview.jpg','Dog CEO. Good Dog Business.','All the latest news, expert opinion and insider tips from the dog and canine-related business world',2,NULL,'2017-12-09 16:29:57',46,NULL),(2,'https://en.wikipedia.org/wiki/Dog','Interestingly Wikipedia has a very detailed writeup about dogs','https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Collage_of_Nine_Dogs.jpg/1200px-Collage_of_Nine_Dogs.jpg','Dog - Wikipedia',NULL,2,NULL,'2017-12-09 16:30:55',91,NULL),(3,'https://www.youtube.com/watch?v=F1ka6a13S9I','Great talk by Andrew Ng about how to think about deep learning! The part about training/dev/test data is a must watch.','https://i.ytimg.com/vi/F1ka6a13S9I/maxresdefault.jpg','Nuts and Bolts of Applying Deep Learning (Andrew Ng)','The talks at the Deep Learning School on September 24/25, 2016 were amazing. I clipped out individual talks from the full live streams and provided links to ...',1,NULL,'2017-12-09 16:30:59',0,'SAMEORIGIN'),(4,'https://distill.pub/2017/feature-visualization/','Visualizing features in neural networks','https://distill.pub/2017/feature-visualization/thumbnail.jpg','Feature Visualization','How neural networks build up their understanding of images.',1,NULL,'2017-12-09 16:31:35',1514,NULL),(6,'https://nerdnomads.com/hachiko_the_dog','This is such a sad movie :(((','https://nerdnomads.com/wp-content/uploads/The-True-Story-Of-HACHIKO-3.jpg','The Amazing And True Story Of Hachiko The Dog','The amazing and true story of #Hachi, the story behind the film \"Hachiko - A Dog`s Tale\". Have you seen it? Did you cry as much as me? :D @nerdnomads @visitjapaninternational #Japan http://nerdnomads.com/hachiko_the_dog ?',2,NULL,'2017-12-09 16:32:39',8555,NULL),(7,'https://www.thisisanfield.com/2017/12/fearsome-foursome-captain-coutinho-5-talking-points-liverpool-7-0-spartak-moscow/','7 goals and we are through to the last 16 of the champions league!','https://www.thisisanfield.com/wp-content/uploads/P171206-099-Liverpool_Spartak-e1512595453590.jpg','5 talking points from Liverpool 7-0 Spartak Moscow','The fearsome foursome and captain Coutinho!',3,NULL,'2017-12-09 16:33:29',574,'SAMEORIGIN'),(8,'https://www.youtube.com/watch?v=7okOpjq6deA&hl=en-GB&gl=SG','New Christmas anthem anyone :-?','https://i.ytimg.com/vi/7okOpjq6deA/maxresdefault.jpg','DOG MUSIC - RELAX YOUR DOG! UNIQUE SOUND TECHNOLOGY RelaxMyDog ???? RMD05','DOG MUSIC - RELAX YOUR DOG! UNIQUE SOUND TECHNOLOGY RelaxMyDog Relax My Dog are experts in creating relaxing music to help calm your dog and help dogs to sle...',2,NULL,'2017-12-09 16:33:50',0,'SAMEORIGIN'),(9,'https://www.thisisanfield.com/2017/12/klopps-resplendent-reds-strong-favourites-229th-merseyside-derby-liverpool-vs-everton-preview/','Ready for the derby this weekend! YNWA','https://www.thisisanfield.com/wp-content/uploads/170401-041-Liverpool_Everton-e1512813618751.jpg','All you need to know ahead of Liverpool vs. Everton','The 229th Merseyside derby is set for Anfield.',3,NULL,'2017-12-09 16:33:56',247,'SAMEORIGIN'),(10,'http://time.com/5028171/health-benefits-owning-dog/','That\'s right baby :thumbs_up:','https://timedotcom.files.wordpress.com/2017/11/dog.jpg?quality=85','It’s Official: Dog Owners Live Longer, Healthier Lives','The benefits are especially strong for people who live alone ',2,NULL,'2017-12-09 16:34:20',503,NULL),(11,'https://www.youtube.com/watch?v=plFCDMQLGpw','The two of my loves :)','https://i.ytimg.com/vi/plFCDMQLGpw/hqdefault.jpg','\"Dogs Playing Soccer/Football Compilation\" || CFS','Dogs Playing Soccer/Football Compilation It\'s time for dogs to show some soccer/football skills. They are so good with ball, that they really need their own ...',2,NULL,'2017-12-09 16:34:46',0,'SAMEORIGIN'),(12,'http://abcnews.go.com/Lifestyle/history-dogs-pets/story?id=41671149','So cool!! Way better than listening to my owner\'s history class revision :bleh:','http://a.abcnews.com/images/Video/GTY_dog_day_jef_160826_16x9_992.jpg','The History of Dogs as Pets','In honor of National Dog Day, ABC News looked back at how our furry four-legged companions evolved from feral wolves into our best friends.\nIt was originally believed the first domesticated wolves appeared around 15,000 years ago in the Middle East. New evidence, however, suggests it was much...',2,NULL,'2017-12-09 16:36:57',153,NULL),(13,'http://www.channelnewsasia.com/news/lifestyle/art-pets-this-unusual-exhibition-singapore-cats-dogs-9264290','I want to visit this please please please please please please please please please please please please please please please (not with all those cats thou)','http://www.channelnewsasia.com/image/9264912/16x9/991/529/841fdceb8a1f1471d69a807860c5287d/zt/art-exhibition-for-pets--kelly-limerick-.jpg','Art for pets? This unusual exhibition in Singapore was made for cats and dogs','Local artists collaborated with animal behaviourists and veterinarians to create 10 pet-friendly interactive installations, including a maze for dogs and cat-like sculpture that cats can squeeze into.',2,NULL,'2017-12-09 16:39:19',507,NULL),(14,'http://www.dailymail.co.uk/health/article-3121627/Could-owning-CAT-detrimental-mental-health-Feline-parasite-increases-risk-schizophrenia-study-finds.html','See I already told owner this. Just in case he intends to bring home a sucky cat booo','http://i.dailymail.co.uk/i/pix/2015/06/12/15/2991BED300000578-0-image-a-119_1434119211262.jpg','Could your CAT increase the risk of schizophrenia?','The parasite toxoplasma gondii, which can be passed from cats to humans, could play a role in the development of schizophrenia, scientists from the Stanley Medical Research Institute said.',4,NULL,'2017-12-09 16:40:58',261,NULL),(15,'https://www.petful.com/behaviors/cat-secretly-hates-you/','You wont\' need a sign because they obviously hate everyone >:p','https://www.petful.com/wp-content/uploads/2014/08/cat-secretly-hates-you.jpg','7 Signs That Your Cat May Secretly Hate You - Petful','I know my cat can’t help coughing up a hairball. But there are days I swear he does it on purpose.',4,NULL,'2017-12-09 16:41:57',378,NULL),(16,'https://www.pbs.org/newshour/nation/cats-dont-like-human-music-play-instead','Since they dont like your music, they should not be allowed to hang out with you either ','https://d3i6fh83elv35t.cloudfront.net/newshour/app/uploads/2015/03/4241443787_31efa5a8a0_o-1024x682.jpg','Cats don\'t like human music -- play them this instead','Ever wondered why your cats don\'t share your appreciation of Johann Sebastian Bach or aren\'t as enthusiastic to rock out to an old Led Zeppelin record? Turns out, it\'s not their style.',4,NULL,'2017-12-09 16:42:48',177,NULL),(17,'https://www.newyorker.com/humor/daily-shouts/does-your-cat-hate-you','I can tell you that they do. They do hate every single one creature on this planet','https://media.newyorker.com/photos/590973fe1c7a8e33fb38f268/16:9/w_1200,h_630,c_limit/Manley-Cat-Hate-You.jpg','Does Your Cat Hate You?','The only parental force the animal recognizes is the jungle law of kill or be killed. It’s really nothing personal.',4,NULL,'2017-12-09 16:45:39',13,NULL),(18,'http://dogtime.com/puppies/255-puppies','babies are always cute, esp our babies :)','http://cdn2-www.dogtime.com/assets/uploads/2010/12/puppies.jpg','Puppies - Adorable PUPPY PICS & What to Expect','Puppies are the epitome of cuteness! A puppy is a new special part of your family and we\'re here to help you understand your pup.',2,NULL,'2017-12-09 16:46:55',140,NULL),(19,'https://www.express.co.uk/sport/football/890188/Arsenal-transfer-news-Jordi-Osei-Tutu-Joseph-Olowu','ohhhhhh, something to look forward to','https://cdn.images.express.co.uk/img/dynamic/67/750x445/890188.jpg','Arsenal make double contract announcement on official club website','ARSENAL have made a double contract annoucement on their official club website.    \n',5,NULL,'2017-12-09 16:50:03',23,NULL),(20,'http://metro.co.uk/2017/12/09/arsenal-open-provisional-contract-talks-aaron-ramsey-danny-welbeck-7145198/','What? What? How about Alexis??? And Mesut?',NULL,'Arsenal open talks with two first-team stars to avoid another Sanchez saga','Wenger won\'t repeat his mistake.',5,NULL,'2017-12-09 16:50:40',299,NULL),(21,'https://www.reddit.com/r/Breadit/','most informative website on baking! ',NULL,'Too Many Requests','we\'re sorry, but you appear to be a bot and we\'ve seen too many requests\nfrom you lately. we enforce a hard speed limit on requests that appear to come\nfrom bots to prevent abuse.',6,NULL,'2017-12-09 16:52:34',70,'SAMEORIGIN'),(22,'https://www.forbes.com/sites/leebelltech/2017/12/06/best-wearable-tech-health-fitness-gadgets-2017-updated/','This is a good guide to what to get your loved ones this Xmas :)','https://thumbor.forbes.com/thumbor/600x315/smart/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F768329812%2F960x0.jpg%3Ffit%3Dscale','Best Wearable Tech, Smartwatches, Activity Trackers And Fitness Gadgets','The top health and fitness wearables for the gym, outdoor sports or running and cycling',7,NULL,'2017-12-09 16:53:50',298,'SAMEORIGIN'),(23,'http://time.com/see-the-wearable-tech-of-the-future/','Nice graphics for a good article. 9/10','https://timedotcom.files.wordpress.com/2015/06/wearable_fb.png?w=1200&h=628&crop=1','See the wearable tech of the future','Get to know the devices you\'ll be wearing next',7,NULL,'2017-12-09 16:54:31',346,NULL),(24,'https://en.wikipedia.org/wiki/Bread','looong history of bread; so good ','https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3%B6tchen.JPG/1200px-Korb_mit_Br%C3%B6tchen.JPG','Bread - Wikipedia',NULL,6,NULL,'2017-12-09 16:54:55',0,NULL),(25,'https://www.wired.com/insights/2015/02/the-future-of-wearable-tech/','Interesting prediction?','https://www.wired.com/wp-content/themes/Phoenix/assets/images/article-icon.jpg','The Future of Wearable Tech',NULL,7,NULL,'2017-12-09 16:54:59',352,NULL),(26,'http://breadmasterguide.com/types-of-bread/','all u need is bread ','http://breadmasterguide.com/wp-content/uploads/2017/06/Types-Of-Bread.jpg','Types Of Bread: Your Guide To Choosing The Perfect Loaf','Types Of Bread: Sure you love bread. When you enter a bakeshop, it excites you because there are a lot of delicious breads to choose from.',6,NULL,'2017-12-09 16:56:13',908,NULL),(27,'http://www.mirror.co.uk/sport/football/news/arsenal-players-questioned-arsene-wengers-11662900','Hmmm?','https://i2-prod.mirror.co.uk/incoming/article11633317.ece/ALTERNATES/s1200/Arsenals-French-striker-Alexandre-Lacaz.jpg','Wenger admits Arsenal stars questioned his tactics after costly Man United loss','\"Everybody has a little bit of his own analysis — but mine counts!\" says boss following loss that all but ended title hopes',5,NULL,'2017-12-09 16:56:37',336,NULL),(28,'https://www.theguardian.com/technology/2017/oct/29/transhuman-bodyhacking-transspecies-cyborg','Oh wow. This is some cool s**t','https://i.guim.co.uk/img/media/e36237e8cb4b9cb5c817556feea41916325f5852/0_803_5061_3037/master/5061.jpg?w=1200&h=630&q=55&auto=format&usm=12&fit=crop&crop=faces%2Centropy&bm=normal&ba=bottom%2Cleft&blend64=aHR0cHM6Ly91cGxvYWRzLmd1aW0uY28udWsvMjAxNi8wNS8yNS9vdmVybGF5LWxvZ28tMTIwMC05MF9vcHQucG5n&s=905e60d2e53af4b4ffd68c5533f9d839','When man meets metal: rise of the transhumans','At the borderline of technology and biology, ‘bodyhacking’ pioneers are defying nature to redesign their own bodies. Is this really the future?',7,NULL,'2017-12-09 16:58:39',2072,'SAMEORIGIN'),(29,'http://www.goal.com/en/news/arsenal-transfer-news-the-latest-live-player-rumours-from/1rr05xvcxkle817g8xm6yrnjwo','Please please get some good talents','https://images.performgroup.com/di/library/GOAL_INTERNATIONAL/be/b9/mesut-ozil-arsenal-2016_7llhsr97rxsh1c7wubvbj6ziz.jpg?t=1336933537&quality=100&h=300','Arsenal transfer news: The latest & LIVE player rumours from the Emirates Stadium | Goal.com','Goal summarises the biggest transfer talk involving Arsenal following a summer in which they held on to Mesut Ozil and Alexis Sanchez',5,NULL,'2017-12-09 16:59:12',758,NULL),(30,'https://en.wikipedia.org/wiki/Wearable_technology','In case you dont know what they are',NULL,'Wearable technology - Wikipedia',NULL,7,NULL,'2017-12-09 17:03:51',150,NULL),(31,'https://www.quora.com/Does-a-dog-know-its-cute','Dont listen to all of the answers. We do know that we are cute :D',NULL,'5 Answers - Does a dog know it\'s cute? - Quora',NULL,2,NULL,'2017-12-09 17:06:25',447,'SAMEORIGIN'),(32,'https://www.youtube.com/watch?v=W-0xR5e_k78','Little did they know. We are giving chance only =.=','https://i.ytimg.com/vi/W-0xR5e_k78/hqdefault.jpg','CATS TERMINATING DOGS - Cats vs Dogs / Cats Fighting Dogs','These funny cats and silly cats will make you laugh. Check out these funny cat videos in this funny cats compilation 2016. Send us a link to your video if yo...',4,NULL,'2017-12-09 17:08:44',0,'SAMEORIGIN'),(33,'http://gadgetsandwearables.com/2017/12/08/winter-sports-wearables/','cool cool. New biz ideas?','http://gadgetsandwearables.com/wp-content/uploads/2017/12/Recon-Instruments-new-MOD-Live.jpg','Winter sports, a growing area for wearable technology','Winter sports, a growing area for wearable technology',7,NULL,'2017-12-09 17:23:24',249,NULL),(34,'https://www.theguardian.com/football/2017/dec/09/jack-wilshere-arsenal-contract-expiring-what-will-happen','Hmm. Got his moment but not really a good player','https://i.guim.co.uk/img/media/f20748003bc65e43946593f16e478b6df7b95140/25_88_5431_3259/master/5431.jpg?w=1200&h=630&q=55&auto=format&usm=12&fit=crop&crop=faces%2Centropy&bm=normal&ba=bottom%2Cleft&blend64=aHR0cHM6Ly91cGxvYWRzLmd1aW0uY28udWsvMjAxNi8wNS8yNS9vdmVybGF5LWxvZ28tMTIwMC05MF9vcHQucG5n&s=c5ab09ca561fc3c7beeb4e538cddf098','Jack Wilshere: ‘I have six months left, sometimes I wonder what will happen’','Jack Wilshere is pushing hard for a return to Arsenal’s first team but questions remain over whether Arsène Wenger will offer him a new contract',5,NULL,'2017-12-10 02:47:37',438,'SAMEORIGIN'),(35,'http://www.marcinsobas.com/index.php/pl/galeria/mountains/raven-341.html','Super amazing landscapes and unique style','http://www.marcinsobas.com/images/megagaleria/miniaturki/mountains_13/raven_20121212_1053924287.jpg','Raven','Raven',8,NULL,'2017-12-10 08:14:31',1,NULL),(36,'http://siyan.co/photog','My own photography ^^ check it out, comments are much appreciated!',NULL,'Photography – Teo Si-Yan','I love landscape photography - both nature and cityscapes! Here are some of my favourite photos that I’ve taken.',8,NULL,'2017-12-10 08:19:39',19,NULL),(37,'https://cardsagainsthumanityredistributesyourwealth.com/','Great work by CAH!','https://cardsagainsthumanityredistributesyourwealth.com/images/share-f169f727.jpg','Cards Against Humanity Redistributes Your Wealth','For Day Three of Cards Against Humanity Saves America, we took some of your money and redistributed it to people who need it more.',9,NULL,'2017-12-10 09:14:54',1575,NULL),(38,'https://www.youtube.com/watch?v=28xjtYY3V3Q','Hands down must watch','https://i.ytimg.com/vi/28xjtYY3V3Q/hqdefault.jpg','Top 10 Funny and Cute Dog Videos','More cute pooches here http://clikhere.co/CkJzIboX Some of the cutest and funniest puppies and dogs from the web in no particular order PLEASE THUMBS UP! Lea...',2,NULL,'2017-12-10 15:35:38',0,'SAMEORIGIN'),(39,'https://www.youtube.com/watch?v=NAzmm-vuGwE','omg this is alarming!!!!','https://i.ytimg.com/vi/NAzmm-vuGwE/maxresdefault.jpg','Cat attacks baby *must see*','Jukin Media Verified (Original) * For licensing / permission to use: Contact - licensing(at)jukinmediadotcom',4,NULL,'2017-12-10 15:37:37',0,'SAMEORIGIN'),(40,'https://www.theguardian.com/football/live/2017/dec/10/southampton-v-arsenal-premier-league-live',':(','https://i.guim.co.uk/img/media/fd2514b9eea91313cd3c99e592c08334dd6118d5/0_141_2467_1480/master/2467.jpg?w=1200&h=630&q=55&auto=format&usm=12&fit=crop&crop=faces%2Centropy&bm=normal&ba=bottom%2Cleft&blend64=aHR0cHM6Ly91cGxvYWRzLmd1aW0uY28udWsvMjAxNi8wNS8yNS9vdmVybGF5LWxvZ28tMTIwMC05MF9vcHQucG5n&s=8e0c9828df70274de2360a59144318e3','Southampton 1-1 Arsenal: Premier League – as it happened','Southampton took the lead through Charlie Austin in the third minute and led until two minutes from time when Olivier Giroud’s header grabbed a point for an under-par Arsenal',5,NULL,'2017-12-11 05:18:54',172,'SAMEORIGIN'),(41,'http://facebook.com','Hello not rlated','https://www.facebook.com/images/fb_icon_325x325.png','Facebook – log in or sign up','Please enable JavaScript in your browser or upgrade to a JavaScript-capable browser to register for Facebook.',5,NULL,'2017-12-11 06:44:19',16,'DENY'),(42,'http://www.straitstimes.com/singapore/education/more-sutd-students-securing-jobs-before-graduation','Students doing well!','http://www.straitstimes.com/sites/all/themes/custom/bootdemo/images/facebook_default_logo.jpg','More SUTD students securing jobs before graduation','More undergraduates from the Singapore University of Technology and Design (SUTD) are securing jobs before graduation, with many benefiting from Singapore\'s push towards becoming a Smart Nation.. Read more at straitstimes.com.',13,NULL,'2017-12-21 01:46:52',438,'SAMEORIGIN'),(43,'https://www.theguardian.com/football/2017/dec/22/arsenal-liverpool-premier-league-match-report','What a crazy match!!','https://i.guim.co.uk/img/media/b6858d5d8c7df569885942f745aaae623a15c4a6/0_14_3879_2328/master/3879.jpg?w=1200&h=630&q=55&auto=format&usm=12&fit=crop&crop=faces%2Centropy&bm=normal&ba=bottom%2Cleft&blend64=aHR0cHM6Ly91cGxvYWRzLmd1aW0uY28udWsvMjAxNi8wNS8yNS9vdmVybGF5LWxvZ28tMTIwMC05MF9vcHQucG5n&s=d27dc6a36f2caec5c5c1485104d3ea6a','Roberto Firmino saves point for Liverpool after Arsenal’s crazy five minutes','Roberto Firmino earned Liverpool 3-3 draw after Arsenal overturned 0-2 deficit with three goals in five minutes at the Emirates',5,NULL,'2017-12-23 04:48:41',641,'SAMEORIGIN');
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');
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
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
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
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel` (
  `channel_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `num_subscribers` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`channel_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `channel_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (1,2,'Machine Learning','All things where we teach robots to be smarter than us!','2017-12-09 16:29:16',3),(2,1,'Dogeeee','All about dogs <3','2017-12-09 16:29:19',5),(3,2,'Liverpool','My first love.','2017-12-09 16:32:24',3),(4,1,'Cat sucks ','','2017-12-09 16:39:55',3),(5,4,'Arsenal','','2017-12-09 16:49:08',4),(6,3,'best bread in the world','i love bread ','2017-12-09 16:51:47',4),(7,4,'New Age Wearables','Hi-tech stuffs. Cool stuffs','2017-12-09 16:53:05',5),(8,5,'Awesome photography','Photography inspiration and tutorials! Mostly focused on travel/landscape photography.','2017-12-10 08:11:19',3),(9,2,'General','It\'s wizardry if you don\'t know how it works','2017-12-10 09:14:35',2),(10,7,'demo','this is for demo purpose','2017-12-11 06:45:09',1),(12,9,'AI','','2017-12-21 01:46:11',0),(13,9,'SUTD','','2017-12-21 01:46:39',2);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `channel_tags`
--

DROP TABLE IF EXISTS `channel_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `channel_tags` (
  `channel_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`channel_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `channel_tags_ibfk_1` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`channel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `channel_tags_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`tag_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel_tags`
--

LOCK TABLES `channel_tags` WRITE;
/*!40000 ALTER TABLE `channel_tags` DISABLE KEYS */;
INSERT INTO `channel_tags` VALUES (2,3),(2,4),(2,5),(2,7),(2,8),(2,9),(2,11),(2,12),(2,13),(2,16),(2,17),(2,19),(2,20),(3,2),(4,3),(4,5),(4,16),(4,17),(4,19),(5,1),(5,2),(5,17),(6,11),(7,1),(7,5),(7,7),(7,12),(7,16),(7,17),(8,7),(8,9),(8,17),(8,18),(9,1),(9,3),(9,15),(10,1),(10,8),(10,9),(10,10),(10,11),(13,4),(13,7);
/*!40000 ALTER TABLE `channel_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_text` varchar(500) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `article_id` (`article_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'imagine a soccer league for dogs! would be more interesting than alot of epl games LOL',2,11,'2017-12-09 16:41:27'),(2,'dogs > cats',2,13,'2017-12-09 16:42:38'),(3,'awesome mate. Me dog appreciate it',1,13,'2017-12-09 16:43:28'),(4,'definitely!! ',1,11,'2017-12-09 16:44:05'),(5,'and we won\'t sell tickets to cat owners nor cats',1,11,'2017-12-09 16:44:17'),(6,'so cuteeeeeeeeeeee',4,18,'2017-12-09 16:48:44'),(7,'thanks mate :thumbs_up:',1,18,'2017-12-09 17:05:39'),(8,'it\'s true',1,32,'2017-12-09 17:09:22'),(9,'believe me',1,32,'2017-12-09 17:09:28'),(10,'nice! I love baguettes and bagels :D',5,26,'2017-12-10 06:33:54'),(11,'right mate',4,31,'2017-12-10 09:06:51'),(12,'awesome',4,36,'2017-12-10 09:07:03'),(13,'more photos of food plox',4,36,'2017-12-10 09:07:35'),(14,'hello its me',7,33,'2017-12-11 06:46:20'),(15,'sup mate',4,33,'2017-12-11 06:46:30');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dboard`@`%`*/ /*!50003 TRIGGER new_comment_notification AFTER INSERT ON comment
            FOR EACH ROW
            INSERT INTO notification (type, type_id, article_id, is_read, type_user_id, user_id)
            SELECT * FROM
                (SELECT 'comment' as type, NEW.article_id as type_id, NEW.article_id as article_id,
                false as is_read, NEW.user_id as type_user_id,
                (SELECT user_id from channel WHERE channel_id IN
                    (SELECT channel_id FROM article WHERE article_id = NEW.article_id)) as user_id)
            as temptable
            where temptable.user_id <> NEW.user_id */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

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
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(4,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-12-09 16:24:37.314108'),(2,'auth','0001_initial','2017-12-09 16:24:37.708207'),(3,'admin','0001_initial','2017-12-09 16:24:37.806530'),(4,'admin','0002_logentry_remove_auto_add','2017-12-09 16:24:37.831040'),(5,'user','0001_create_user_table','2017-12-09 16:24:37.885984'),(6,'channel','0001_create_channel_table','2017-12-09 16:24:37.917219'),(7,'article','0001_create_article_table','2017-12-09 16:24:37.956278'),(8,'article','0002_add_num_words_article_table','2017-12-09 16:24:37.988980'),(9,'article','0003_add_xframe_options_article_table','2017-12-09 16:24:38.022356'),(10,'contenttypes','0002_remove_content_type_name','2017-12-09 16:24:38.090367'),(11,'auth','0002_alter_permission_name_max_length','2017-12-09 16:24:38.130578'),(12,'auth','0003_alter_user_email_max_length','2017-12-09 16:24:38.173820'),(13,'auth','0004_alter_user_username_opts','2017-12-09 16:24:38.190881'),(14,'auth','0005_alter_user_last_login_null','2017-12-09 16:24:38.226738'),(15,'auth','0006_require_contenttypes_0002','2017-12-09 16:24:38.233266'),(16,'auth','0007_alter_validators_add_error_messages','2017-12-09 16:24:38.247737'),(17,'auth','0008_alter_user_username_max_length','2017-12-09 16:24:38.296149'),(18,'tag','0001_create_tag_table','2017-12-09 16:24:38.323880'),(19,'channel','0002_create_channel_tag_tables','2017-12-09 16:24:38.356202'),(20,'channel','0003_modify_channel_table','2017-12-09 16:24:38.385912'),(21,'channel','0004_modify_channel_table','2017-12-09 16:24:38.401806'),(22,'notification','0001_create_notification_table','2017-12-09 16:24:38.430091'),(23,'notification','0002_modify_notification_table','2017-12-09 16:24:38.501427'),(24,'notification','0003_add_type_user_notification_table','2017-12-09 16:24:38.570825'),(25,'comment','0001_create_comment_table','2017-12-09 16:24:38.608485'),(26,'comment','0002_comment_notification_trigger','2017-12-09 16:24:38.630891'),(27,'comment','0003_delete_comment_notification_trigger','2017-12-09 16:24:38.642421'),(28,'comment','0004_comment_notification_trigger','2017-12-09 16:24:38.663878'),(29,'comment','0005_delete_comment_trigger','2017-12-09 16:24:38.676687'),(30,'comment','0006_modify_comment_notification','2017-12-09 16:24:38.703843'),(31,'comment','0007_modify_comment_trigger','2017-12-09 16:24:38.736416'),(32,'notification','0004_modify_notification_table','2017-12-09 16:24:38.813623'),(33,'sessions','0001_initial','2017-12-09 16:24:38.849433'),(34,'stats','0001_create_stats_table','2017-12-09 16:24:38.884071'),(35,'user','0002_create_user_rship_tables','2017-12-09 16:24:38.988965'),(36,'user','0003_modify_user_attributes','2017-12-09 16:24:39.022177'),(37,'user','0004_like_notification_trigger','2017-12-09 16:24:39.045717'),(38,'user','0005_follow_notification_trigger','2017-12-09 16:24:39.068485'),(39,'user','0006_subscribe_channel_trigger','2017-12-09 16:24:39.099739'),(40,'user','0007_unsubscribe_channel_trigger','2017-12-09 16:24:39.118478'),(41,'user','0008_delete_like_notification_trigger','2017-12-09 16:24:39.142082'),(42,'user','0009_unfollow_notification_trigger','2017-12-09 16:24:39.169637'),(43,'user','0010_modify_likes_trigger','2017-12-09 16:24:39.201216'),(44,'user','0011_modify_follow_trigger','2017-12-09 16:24:39.238888');
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
INSERT INTO `django_session` VALUES ('01uzeel5ujlppjfol5nq4dnee24zzux3','OGRkNjY5NmFjNzRhOWJjZGIxZjQxMDJiMjllYTFkMDFjYWUwODFhZjp7InVzZXJfaWQiOjl9','2018-01-04 08:58:38.256082'),('0w6rb7chqlduu5923a6g1yuqymtyq4xi','ZTcwMDIyYzY3MzVkNmY1YTg1MDA0MjRjOTM2MzdlZTAyZTA0ZjFlYTp7InVzZXJfaWQiOjd9','2018-01-05 06:52:49.114226'),('14hyrhy4138f5q1m3o9klgu2kvqze0h8','ZTcwMDIyYzY3MzVkNmY1YTg1MDA0MjRjOTM2MzdlZTAyZTA0ZjFlYTp7InVzZXJfaWQiOjd9','2018-01-05 06:52:48.752396'),('a8vcns7zf7qzxig8tkqbve2rtize6qpa','MTc4MmEyNTk2NmRmNmRjZWEzNjg5OTg5M2ExMzM0ZTEzMjNjZTgyNzp7InVzZXJfaWQiOjJ9','2017-12-24 14:13:12.967136'),('c0w4nu7o8pkvfcaynntmnpun9p5sys5x','OTE3YzJhYTE5ZDFiYmUwN2RjMTc0MzgyZWQ0ODRmMzFiOWUyNjdlYzp7InVzZXJfaWQiOjR9','2017-12-25 04:52:26.059104'),('chrx1pg4aomg6ht74x5bk456garw0f1t','MTc4MmEyNTk2NmRmNmRjZWEzNjg5OTg5M2ExMzM0ZTEzMjNjZTgyNzp7InVzZXJfaWQiOjJ9','2018-01-10 11:34:13.305843'),('f5c7ghxu15eod7auzlyif3kfjya6e7p9','YmQwZjQzYWFjNDU1NGM3ZDUwOGZjMDc3ZDE1N2Y1Zjk0YzFkMWVkMzp7InVzZXJfaWQiOjh9','2017-12-25 12:42:32.029112'),('fkvmr6i3syh6t0h65qprck9zladnsj4z','Yzk2NWU0OTUwODFiYjk1M2Q2MDAzMDE4ZGFkYjRlOTY1NDQ3NzQ2Njp7InVzZXJfaWQiOjV9','2018-01-04 14:11:21.610231'),('hmkpxkh5kya69jeep58jkgw913mtsxzh','ZTcwMDIyYzY3MzVkNmY1YTg1MDA0MjRjOTM2MzdlZTAyZTA0ZjFlYTp7InVzZXJfaWQiOjd9','2017-12-25 06:41:00.156036'),('j3vfh3kqh3ike7ty0976n0iktj1hyy9w','MTc4MmEyNTk2NmRmNmRjZWEzNjg5OTg5M2ExMzM0ZTEzMjNjZTgyNzp7InVzZXJfaWQiOjJ9','2017-12-24 14:13:12.104823'),('lh5zbjo8m6zurzvhg715tbv6wpkzqlhk','MTc4MmEyNTk2NmRmNmRjZWEzNjg5OTg5M2ExMzM0ZTEzMjNjZTgyNzp7InVzZXJfaWQiOjJ9','2018-01-10 11:34:13.675748'),('m055hcb2lnrq33e5mhk6wwg921r89zbp','OTE3YzJhYTE5ZDFiYmUwN2RjMTc0MzgyZWQ0ODRmMzFiOWUyNjdlYzp7InVzZXJfaWQiOjR9','2018-01-13 05:40:21.340071'),('ng58ga1oos3sgt7zbhammn40b5ro68x2','OGRkNjY5NmFjNzRhOWJjZGIxZjQxMDJiMjllYTFkMDFjYWUwODFhZjp7InVzZXJfaWQiOjl9','2018-01-04 08:58:38.587241'),('ofu462hdn7sjbqlk734bg1cy213uifn1','OTE3YzJhYTE5ZDFiYmUwN2RjMTc0MzgyZWQ0ODRmMzFiOWUyNjdlYzp7InVzZXJfaWQiOjR9','2017-12-27 11:40:21.473316'),('suuuw7ll8eup9vciipg5ruja1n59ogaj','OGRkNjY5NmFjNzRhOWJjZGIxZjQxMDJiMjllYTFkMDFjYWUwODFhZjp7InVzZXJfaWQiOjl9','2018-01-04 01:47:06.243183'),('t41n1v8whxlc8j2ishwrkotilibw3dt4','ZjcyOWNmNWM1NTJhOWJmYzJkMWFkYmRkMjA1MzZlYmUwYmNhNzU2Mzp7InVzZXJfaWQiOjZ9','2017-12-25 04:47:07.770272'),('uz5qhm2kjuztrjh7ahxhu686chviqpul','MTc4MmEyNTk2NmRmNmRjZWEzNjg5OTg5M2ExMzM0ZTEzMjNjZTgyNzp7InVzZXJfaWQiOjJ9','2017-12-25 06:34:02.224117'),('w4ftaa3k1e00dbw1jtnb6onam9v1fi1o','ODIzMTVmNmFiMjdmNTM2ZTY1OWI1ZThhMjQ4YWNmZjJmZTIxNzg1Zjp7InVzZXJfaWQiOjN9','2017-12-24 04:14:31.743994');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `type` varchar(20) DEFAULT NULL,
  `is_read` tinyint(1) DEFAULT '0',
  `article_id` int(11) DEFAULT NULL,
  `type_user_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `channel_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`notification_id`),
  KEY `user_id` (`user_id`),
  KEY `articleFK` (`article_id`),
  KEY `type_userFK` (`type_user_id`),
  KEY `channelFK` (`channel_id`),
  CONSTRAINT `articleFK` FOREIGN KEY (`article_id`) REFERENCES `article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `channelFK` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`channel_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `type_userFK` FOREIGN KEY (`type_user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (1,1,'2017-12-09 16:40:20','like',1,11,2,11,NULL),(2,1,'2017-12-09 16:41:27','comment',1,11,2,11,NULL),(3,1,'2017-12-09 16:42:12','channel',1,NULL,2,2,2),(4,1,'2017-12-09 16:42:38','comment',1,13,2,13,NULL),(5,1,'2017-12-09 16:42:40','like',1,13,2,13,NULL),(6,2,'2017-12-09 16:43:42','channel',0,NULL,1,3,3),(7,2,'2017-12-09 16:43:48','like',0,3,1,3,NULL),(8,2,'2017-12-09 16:46:55','article',0,NULL,1,2,2),(9,1,'2017-12-09 16:48:27','channel',1,NULL,4,2,2),(10,2,'2017-12-09 16:48:29','channel',0,NULL,4,3,3),(11,1,'2017-12-09 16:48:30','channel',1,NULL,4,4,4),(12,1,'2017-12-09 16:48:35','like',1,18,4,18,NULL),(13,1,'2017-12-09 16:48:44','comment',1,18,4,18,NULL),(14,1,'2017-12-09 16:53:23','channel',1,NULL,3,2,2),(15,4,'2017-12-09 16:56:49','channel',1,NULL,3,7,7),(16,3,'2017-12-09 16:57:03','channel',0,NULL,4,6,6),(17,2,'2017-12-09 16:57:07','channel',0,NULL,3,1,1),(18,3,'2017-12-09 16:57:08','like',0,21,4,21,NULL),(19,1,'2017-12-09 16:57:14','like',1,1,4,1,NULL),(20,1,'2017-12-09 16:57:18','like',1,2,4,2,NULL),(21,2,'2017-12-09 16:57:24','like',0,3,4,3,NULL),(22,1,'2017-12-09 16:57:32','like',1,13,4,13,NULL),(23,3,'2017-12-09 16:58:39','article',0,NULL,4,7,7),(24,3,'2017-12-09 17:03:51','article',0,NULL,4,7,7),(25,2,'2017-12-09 17:06:25','article',0,NULL,1,2,2),(26,3,'2017-12-09 17:06:25','article',0,NULL,1,2,2),(27,4,'2017-12-09 17:06:25','article',1,NULL,1,2,2),(28,4,'2017-12-09 17:06:51','channel',1,NULL,1,7,7),(29,4,'2017-12-09 17:06:54','channel',1,NULL,1,5,5),(30,3,'2017-12-09 17:06:56','channel',0,NULL,1,6,6),(31,4,'2017-12-09 17:07:38','like',1,29,1,29,NULL),(32,4,'2017-12-09 17:08:44','article',1,NULL,1,4,4),(33,4,'2017-12-09 17:09:40','like',1,28,1,28,NULL),(34,4,'2017-12-09 17:10:07','like',1,20,1,20,NULL),(35,2,'2017-12-09 17:16:16','like',0,9,4,9,NULL),(36,1,'2017-12-09 17:23:24','article',1,NULL,4,7,7),(37,3,'2017-12-09 17:23:24','article',0,NULL,4,7,7),(38,2,'2017-12-09 17:24:14','like',0,4,4,4,NULL),(39,2,'2017-12-09 17:24:21','channel',0,NULL,4,1,1),(40,1,'2017-12-10 01:19:51','like',1,16,4,16,NULL),(41,1,'2017-12-10 01:20:13','like',1,31,4,31,NULL),(42,1,'2017-12-10 02:47:37','article',1,34,4,5,5),(43,3,'2017-12-10 06:32:52','channel',0,NULL,5,6,6),(44,3,'2017-12-10 06:33:10','like',0,26,5,26,NULL),(45,3,'2017-12-10 06:33:54','comment',0,26,5,26,NULL),(46,2,'2017-12-10 07:59:22','channel',0,NULL,5,1,1),(47,2,'2017-12-10 08:16:16','like',1,3,5,3,NULL),(48,5,'2017-12-10 09:05:14','like',1,36,4,36,NULL),(49,5,'2017-12-10 09:05:17','channel',1,NULL,4,8,8),(50,5,'2017-12-10 09:05:21','like',1,35,4,35,NULL),(51,1,'2017-12-10 09:06:51','comment',1,31,4,31,NULL),(52,5,'2017-12-10 09:07:03','comment',1,36,4,36,NULL),(53,5,'2017-12-10 09:07:35','comment',1,36,4,36,NULL),(54,3,'2017-12-10 09:08:20','like',0,26,4,26,NULL),(55,4,'2017-12-10 10:16:46','channel',1,NULL,5,7,7),(56,4,'2017-12-10 10:17:00','like',1,25,5,25,NULL),(57,1,'2017-12-10 10:19:11','like',1,31,5,31,NULL),(58,5,'2017-12-10 15:34:38','channel',1,NULL,1,8,8),(59,4,'2017-12-10 15:34:53','like',1,34,1,34,NULL),(60,2,'2017-12-10 15:35:38','article',0,38,1,2,2),(61,3,'2017-12-10 15:35:38','article',0,38,1,2,2),(62,4,'2017-12-10 15:35:38','article',1,38,1,2,2),(63,4,'2017-12-10 15:37:37','article',1,39,1,4,4),(64,4,'2017-12-11 04:47:37','channel',1,NULL,6,5,5),(65,1,'2017-12-11 04:53:01','like',0,38,4,38,NULL),(66,1,'2017-12-11 05:18:54','article',0,40,4,5,5),(67,6,'2017-12-11 05:18:54','article',0,40,4,5,5),(68,4,'2017-12-11 06:41:26','channel',1,NULL,7,5,5),(69,2,'2017-12-11 06:41:28','channel',1,NULL,7,9,9),(70,1,'2017-12-11 06:41:31','channel',0,NULL,7,4,4),(71,4,'2017-12-11 06:42:27','channel',1,NULL,7,7,7),(72,1,'2017-12-11 06:44:19','article',0,41,4,5,5),(73,6,'2017-12-11 06:44:19','article',0,41,4,5,5),(74,7,'2017-12-11 06:44:19','article',1,41,4,5,5),(75,4,'2017-12-11 06:46:07','like',1,33,7,33,NULL),(76,4,'2017-12-11 06:46:20','comment',1,33,7,33,NULL),(77,1,'2017-12-11 06:48:28','channel',0,NULL,7,2,2),(78,1,'2017-12-11 06:49:56','like',0,38,7,38,NULL),(79,1,'2017-12-23 04:48:41','article',0,43,4,5,5),(80,6,'2017-12-23 04:48:41','article',0,43,4,5,5),(81,7,'2017-12-23 04:48:41','article',0,43,4,5,5),(82,9,'2017-12-23 04:49:40','channel',0,NULL,4,13,13),(83,2,'2017-12-26 00:48:41','like',1,37,4,37,NULL),(84,1,'2017-12-26 00:50:05','like',0,39,4,39,NULL),(85,9,'2017-12-26 11:39:22','like',0,42,4,42,NULL);
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  PRIMARY KEY (`tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'Technology','image'),(2,'Sports','image'),(3,'Science','image'),(4,'Music','image'),(5,'Health','image'),(6,'Books','image'),(7,'Education','image'),(8,'Philosophy','image'),(9,'Art','image'),(10,'Finance','image'),(11,'Food','image'),(12,'Fashion','image'),(13,'History','image'),(14,'Economics','image'),(15,'Mathematics','image'),(16,'Humanities','image'),(17,'Culture','image'),(18,'Travel','image'),(19,'Relationships','image'),(20,'Religion','image');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `facebook_id` varchar(20) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `bio` varchar(500) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `facebook_id` (`facebook_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'121409068645229','data.quickly@gmail.com','DB Fran','https://scontent.xx.fbcdn.net/v/t1.0-1/c0.0.194.194/24296698_115224929263643_3503897240277431884_n.jpg?oh=a025ecfb4717f1d5c0a43a1b67ccc13d&oe=5ACA0CD6',NULL,'2017-12-09 16:25:34'),(2,'10156283795000101','vivek_liverpool94@hotmail.com','Vivek Kalyan','https://scontent.xx.fbcdn.net/v/t1.0-1/1476659_10152312852335101_1073622097_n.jpg?oh=5022f57f36599c971d0aaff6641129ef&oe=5AC67623',NULL,'2017-12-09 16:28:16'),(3,'10213032923091863','poppyfights@gmail.com','Pammela Ng','https://scontent.xx.fbcdn.net/v/t1.0-1/c0.50.200.200/p200x200/19224978_10211823865986191_5847446003370497390_n.jpg?oh=05d69aebb7dc5338b55bc710af9fe661&oe=5A8D38C1',NULL,'2017-12-09 16:47:29'),(4,'1265993720167636','hung.ngn.the@gmail.com','Hung Nguyen','https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/14716049_889128904520788_634030994533050311_n.jpg?oh=82d27d89bddee276b9c2a2c873c86692&oe=5ACD58A8',NULL,'2017-12-09 16:48:10'),(5,'10156039080283846','teosiyan@hotmail.com','Si-Yan Teo','https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/10922840_10153264942928846_5053000109680771715_n.jpg?oh=15109f63cdd4b94c3734d58114ed115c&oe=5A8F316F',NULL,'2017-12-10 06:20:49'),(6,'10212269015578339','jbz_1995@hotmail.com','Jonathan Beibei Bei','https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/12923206_10207191484203228_7926422443764497193_n.jpg?oh=683c0417902cbddd681e20a5f0456fe2&oe=5AC5417F',NULL,'2017-12-11 04:47:07'),(7,'10155809510269705','tyclian@hotmail.com','Joe Ng','https://scontent.xx.fbcdn.net/v/t1.0-1/c22.22.281.281/s200x200/167994_496137844704_402883_n.jpg?oh=2f0d17d99d218da5a697727415d4a8a7&oe=5AC47309',NULL,'2017-12-11 06:41:00'),(8,'885658894936601','sanjaypushparajan@gmail.com','Sanjay Pushparajan','https://scontent.xx.fbcdn.net/v/t1.0-1/c145.142.630.630/s200x200/14681611_653746414794518_8338800105384416853_n.jpg?oh=009093d37d4d22eb16c85f2b8e70a8b7&oe=5A8B7D14',NULL,'2017-12-11 08:20:35'),(9,'10156166021559789','dorien.herremans@gmail.com','Dorien Herremans','https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/13254405_10154328505399789_7214040997277470248_n.jpg?oh=1b4c6fb48c8e1163a9c5e7f4af5260ef&oe=5ACA6112',NULL,'2017-12-21 01:17:27');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_follows_channel`
--

DROP TABLE IF EXISTS `user_follows_channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_follows_channel` (
  `user_id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`channel_id`),
  KEY `channel_id` (`channel_id`),
  CONSTRAINT `user_follows_channel_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_follows_channel_ibfk_2` FOREIGN KEY (`channel_id`) REFERENCES `channel` (`channel_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_follows_channel`
--

LOCK TABLES `user_follows_channel` WRITE;
/*!40000 ALTER TABLE `user_follows_channel` DISABLE KEYS */;
INSERT INTO `user_follows_channel` VALUES (1,2,'2017-12-09 16:29:19'),(1,3,'2017-12-09 16:43:42'),(1,4,'2017-12-09 16:39:55'),(1,5,'2017-12-09 17:06:54'),(1,6,'2017-12-09 17:06:56'),(1,7,'2017-12-09 17:06:51'),(1,8,'2017-12-10 15:34:38'),(2,2,'2017-12-09 16:42:12'),(2,3,'2017-12-09 16:32:24'),(2,9,'2017-12-10 09:14:35'),(3,1,'2017-12-09 16:57:07'),(3,2,'2017-12-09 16:53:23'),(3,6,'2017-12-09 16:51:47'),(3,7,'2017-12-09 16:56:49'),(4,1,'2017-12-09 17:24:21'),(4,2,'2017-12-09 16:48:27'),(4,3,'2017-12-09 16:48:29'),(4,4,'2017-12-09 16:48:30'),(4,5,'2017-12-09 16:49:08'),(4,6,'2017-12-09 16:57:03'),(4,7,'2017-12-09 16:53:05'),(4,8,'2017-12-10 09:05:17'),(4,13,'2017-12-23 04:49:40'),(5,1,'2017-12-10 07:59:22'),(5,6,'2017-12-10 06:32:52'),(5,7,'2017-12-10 10:16:46'),(5,8,'2017-12-10 08:11:19'),(6,5,'2017-12-11 04:47:37'),(7,2,'2017-12-11 06:48:28'),(7,4,'2017-12-11 06:41:31'),(7,5,'2017-12-11 06:41:26'),(7,7,'2017-12-11 06:42:27'),(7,9,'2017-12-11 06:41:28'),(7,10,'2017-12-11 06:45:09'),(9,13,'2017-12-21 01:46:39');
/*!40000 ALTER TABLE `user_follows_channel` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dboard`@`%`*/ /*!50003 TRIGGER follow_notification AFTER INSERT ON user_follows_channel
            FOR EACH ROW
            BEGIN
            	SET @subbed_chnn = (SELECT channel_id FROM user_follows_channel
            		WHERE created_at = (SELECT max(created_at) FROM user_follows_channel));
            	UPDATE channel SET num_subscribers = num_subscribers + 1 WHERE channel_id = @subbed_chnn;
            	INSERT INTO notification (type, type_id, channel_id, is_read, type_user_id, user_id)
                SELECT * FROM
               	    (SELECT 'channel' AS type, NEW.channel_id AS type_id, NEW.channel_id AS channel_id,
               	    false AS is_read, NEW.user_id AS type_user_id,
               	    (SELECT user_id from channel WHERE channel_id = NEW.channel_id) AS user_id)
                AS temptable
                WHERE temptable.user_id <> NEW.user_id;
            END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dboard`@`%`*/ /*!50003 TRIGGER unfollow_notification AFTER DELETE ON user_follows_channel
            FOR EACH ROW
            DELETE FROM notification
            WHERE type = 'channel'
            AND type_id = OLD.channel_id
            AND channel_id = OLD.channel_id
            AND type_user_id = OLD.user_id
            AND user_id IN (
                SELECT user_id from channel WHERE channel_id = OLD.channel_id) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `user_follows_tag`
--

DROP TABLE IF EXISTS `user_follows_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_follows_tag` (
  `user_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `user_follows_tag_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_follows_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`tag_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_follows_tag`
--

LOCK TABLES `user_follows_tag` WRITE;
/*!40000 ALTER TABLE `user_follows_tag` DISABLE KEYS */;
INSERT INTO `user_follows_tag` VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10),(4,11),(4,12),(4,13),(4,14),(4,15),(4,16),(4,17),(4,18),(4,19),(4,20),(5,1),(5,2),(5,3),(5,5),(5,6),(5,7),(5,8),(5,9),(5,11),(5,18),(5,19),(6,1),(6,2),(6,3),(6,19),(7,1),(7,4),(7,5),(7,7),(7,8),(7,12),(7,13),(7,14),(7,15),(7,18),(9,4),(9,10);
/*!40000 ALTER TABLE `user_follows_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_friends`
--

DROP TABLE IF EXISTS `user_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_friends` (
  `user_id` int(11) NOT NULL DEFAULT '0',
  `friend_id` int(11) NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`friend_id`),
  KEY `friend_id` (`friend_id`),
  CONSTRAINT `user_friends_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `user_friends_ibfk_2` FOREIGN KEY (`friend_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_friends`
--

LOCK TABLES `user_friends` WRITE;
/*!40000 ALTER TABLE `user_friends` DISABLE KEYS */;
INSERT INTO `user_friends` VALUES (3,1,'2017-12-09 16:47:29'),(4,1,'2017-12-09 16:48:10'),(4,2,'2017-12-09 16:48:10'),(4,3,'2017-12-09 16:48:10'),(5,2,'2017-12-10 06:20:49'),(5,3,'2017-12-10 06:20:49'),(5,4,'2017-12-10 06:20:49'),(6,4,'2017-12-11 04:47:07'),(7,2,'2017-12-11 06:41:00'),(7,4,'2017-12-11 06:41:00'),(7,5,'2017-12-11 06:41:00'),(8,2,'2017-12-11 08:20:35'),(8,5,'2017-12-11 08:20:35'),(8,7,'2017-12-11 08:20:35');
/*!40000 ALTER TABLE `user_friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_likes_article`
--

DROP TABLE IF EXISTS `user_likes_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_likes_article` (
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `likeStatus` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`article_id`),
  KEY `article_id` (`article_id`),
  CONSTRAINT `user_likes_article_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_likes_article_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_likes_article`
--

LOCK TABLES `user_likes_article` WRITE;
/*!40000 ALTER TABLE `user_likes_article` DISABLE KEYS */;
INSERT INTO `user_likes_article` VALUES (1,1,NULL,'2017-12-09 16:31:21'),(1,2,NULL,'2017-12-09 16:31:15'),(1,3,NULL,'2017-12-09 16:43:48'),(1,11,NULL,'2017-12-09 16:35:00'),(1,13,NULL,'2017-12-09 16:43:00'),(1,18,NULL,'2017-12-09 17:05:38'),(1,20,NULL,'2017-12-09 17:10:07'),(1,28,NULL,'2017-12-09 17:09:40'),(1,29,NULL,'2017-12-09 17:07:38'),(1,31,NULL,'2017-12-09 17:07:32'),(1,32,NULL,'2017-12-09 17:09:14'),(1,34,NULL,'2017-12-10 15:34:53'),(1,38,NULL,'2017-12-10 15:37:56'),(1,39,NULL,'2017-12-10 15:37:52'),(2,11,NULL,'2017-12-09 16:40:20'),(2,13,NULL,'2017-12-09 16:42:40'),(4,1,NULL,'2017-12-09 16:57:14'),(4,2,NULL,'2017-12-09 16:57:18'),(4,3,NULL,'2017-12-09 16:57:24'),(4,4,NULL,'2017-12-09 17:24:14'),(4,9,NULL,'2017-12-09 17:16:16'),(4,13,NULL,'2017-12-09 16:57:32'),(4,16,NULL,'2017-12-10 01:19:51'),(4,18,NULL,'2017-12-09 16:48:35'),(4,19,NULL,'2017-12-09 16:55:05'),(4,20,NULL,'2017-12-09 16:56:03'),(4,21,NULL,'2017-12-09 16:57:08'),(4,22,NULL,'2017-12-09 17:20:27'),(4,23,NULL,'2017-12-09 16:59:27'),(4,26,NULL,'2017-12-10 09:08:20'),(4,27,NULL,'2017-12-09 17:20:17'),(4,28,NULL,'2017-12-09 17:16:28'),(4,29,NULL,'2017-12-10 05:14:06'),(4,30,NULL,'2017-12-09 17:23:00'),(4,31,NULL,'2017-12-10 01:20:13'),(4,33,NULL,'2017-12-09 17:23:37'),(4,34,NULL,'2017-12-10 02:47:43'),(4,35,NULL,'2017-12-10 09:05:21'),(4,36,NULL,'2017-12-10 09:05:14'),(4,37,NULL,'2017-12-26 00:48:41'),(4,38,NULL,'2017-12-11 04:53:01'),(4,39,NULL,'2017-12-26 00:50:05'),(4,40,NULL,'2017-12-15 13:27:03'),(4,41,NULL,'2017-12-17 03:37:21'),(4,42,NULL,'2017-12-26 11:39:22'),(4,43,NULL,'2017-12-23 04:50:08'),(5,3,NULL,'2017-12-10 08:16:16'),(5,25,NULL,'2017-12-10 10:17:00'),(5,26,NULL,'2017-12-10 06:33:10'),(5,31,NULL,'2017-12-10 10:19:11'),(7,33,NULL,'2017-12-11 06:46:07'),(7,38,NULL,'2017-12-11 06:49:56');
/*!40000 ALTER TABLE `user_likes_article` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dboard`@`%`*/ /*!50003 TRIGGER like_notification AFTER INSERT ON user_likes_article
            FOR EACH ROW
            INSERT INTO notification (type, type_id, article_id, is_read, type_user_id, user_id)
            SELECT * FROM
                (SELECT 'like' as type, NEW.article_id as type_id, NEW.article_id as article_id,
                false as is_read, NEW.user_id as type_user_id,
                (SELECT user_id from channel WHERE channel_id IN
                    (SELECT channel_id FROM article WHERE article_id = NEW.article_id)) as user_id)
            as temptable
            where temptable.user_id <> NEW.user_id */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`dboard`@`%`*/ /*!50003 TRIGGER delete_like_notification AFTER DELETE ON user_likes_article
            FOR EACH ROW
            DELETE FROM notification
            WHERE
                type = 'like'
            AND type_id = OLD.article_id
            AND article_id = OLD.article_id
            AND type_user_id = OLD.user_id
            AND user_id IN (
                SELECT user_id from channel WHERE channel_id IN (
                     SELECT channel_id FROM article WHERE article_id = OLD.article_id)) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `view`
--

DROP TABLE IF EXISTS `view`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `view` (
  `view_id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int(11) DEFAULT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`view_id`),
  KEY `user_id` (`user_id`),
  KEY `article_id` (`article_id`),
  CONSTRAINT `view_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `view_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `view`
--

LOCK TABLES `view` WRITE;
/*!40000 ALTER TABLE `view` DISABLE KEYS */;
INSERT INTO `view` VALUES (1,'2017-12-09 16:31:07',1,2),(2,'2017-12-09 16:31:19',1,1),(3,'2017-12-09 16:34:18',2,9),(4,'2017-12-09 16:34:53',1,11),(5,'2017-12-09 16:40:15',2,11),(6,'2017-12-09 16:41:03',1,11),(7,'2017-12-09 16:42:31',2,13),(8,'2017-12-09 16:42:53',1,13),(9,'2017-12-09 16:43:46',1,3),(10,'2017-12-09 16:43:50',1,11),(11,'2017-12-09 16:44:26',1,13),(12,'2017-12-09 16:48:33',4,18),(13,'2017-12-09 16:52:58',3,21),(14,'2017-12-09 16:55:04',4,19),(15,'2017-12-09 16:55:13',4,19),(16,'2017-12-09 16:55:28',4,20),(17,'2017-12-09 16:55:33',4,19),(18,'2017-12-09 16:55:46',4,19),(19,'2017-12-09 16:56:01',4,20),(20,'2017-12-09 16:57:04',4,21),(21,'2017-12-09 16:57:13',4,1),(22,'2017-12-09 16:57:17',4,2),(23,'2017-12-09 16:57:23',4,3),(24,'2017-12-09 16:57:23',3,21),(25,'2017-12-09 16:57:28',4,13),(26,'2017-12-09 16:59:26',4,23),(27,'2017-12-09 16:59:37',4,23),(28,'2017-12-09 17:00:02',4,23),(29,'2017-12-09 17:05:28',1,18),(30,'2017-12-09 17:06:30',1,31),(31,'2017-12-09 17:07:02',1,18),(32,'2017-12-09 17:07:11',1,13),(33,'2017-12-09 17:07:15',1,2),(34,'2017-12-09 17:07:17',1,1),(35,'2017-12-09 17:07:31',1,31),(36,'2017-12-09 17:07:37',1,29),(37,'2017-12-09 17:09:13',1,32),(38,'2017-12-09 17:09:38',1,28),(39,'2017-12-09 17:10:05',1,20),(40,'2017-12-09 17:15:52',4,21),(41,'2017-12-09 17:16:14',4,9),(42,'2017-12-09 17:16:23',4,20),(43,'2017-12-09 17:16:25',4,28),(44,'2017-12-09 17:16:32',4,29),(45,'2017-12-09 17:20:16',4,27),(46,'2017-12-09 17:20:24',4,22),(47,'2017-12-09 17:22:48',4,28),(48,'2017-12-09 17:22:59',4,30),(49,'2017-12-09 17:23:35',4,33),(50,'2017-12-09 17:24:12',4,4),(51,'2017-12-09 17:38:01',4,4),(52,'2017-12-09 17:38:05',4,33),(53,'2017-12-10 01:19:49',4,16),(54,'2017-12-10 01:20:04',4,33),(55,'2017-12-10 01:20:11',4,31),(56,'2017-12-10 01:20:23',4,27),(57,'2017-12-10 02:47:41',4,34),(58,'2017-12-10 04:15:02',3,23),(59,'2017-12-10 05:13:23',4,34),(60,'2017-12-10 05:13:32',4,28),(61,'2017-12-10 05:14:03',4,29),(62,'2017-12-10 06:20:20',NULL,26),(63,'2017-12-10 06:20:38',NULL,26),(64,'2017-12-10 06:32:58',5,24),(65,'2017-12-10 06:33:07',5,26),(66,'2017-12-10 08:14:44',5,35),(67,'2017-12-10 08:15:56',5,21),(68,'2017-12-10 08:15:59',5,4),(69,'2017-12-10 08:16:00',5,3),(70,'2017-12-10 08:19:47',5,36),(71,'2017-12-10 08:20:39',5,31),(72,'2017-12-10 08:20:39',5,32),(73,'2017-12-10 09:05:00',NULL,36),(74,'2017-12-10 09:05:20',4,35),(75,'2017-12-10 09:05:53',4,35),(76,'2017-12-10 09:06:03',4,34),(77,'2017-12-10 09:06:41',4,31),(78,'2017-12-10 09:06:57',4,36),(79,'2017-12-10 09:07:46',4,36),(80,'2017-12-10 09:08:17',4,26),(81,'2017-12-10 09:15:02',2,3),(82,'2017-12-10 09:15:11',2,37),(83,'2017-12-10 09:16:06',2,36),(84,'2017-12-10 10:16:23',5,36),(85,'2017-12-10 10:16:33',5,35),(86,'2017-12-10 10:16:49',5,25),(87,'2017-12-10 10:17:29',5,25),(88,'2017-12-10 10:17:50',5,36),(89,'2017-12-10 10:18:22',5,31),(90,'2017-12-10 14:13:24',2,3),(91,'2017-12-10 14:39:54',NULL,37),(92,'2017-12-10 14:39:54',NULL,37),(93,'2017-12-10 14:41:29',NULL,11),(94,'2017-12-10 14:41:29',NULL,11),(95,'2017-12-10 15:34:42',1,31),(96,'2017-12-10 15:34:50',1,34),(97,'2017-12-10 15:35:05',1,34),(98,'2017-12-10 15:35:07',1,31),(99,'2017-12-10 15:35:09',1,16),(100,'2017-12-10 15:37:47',1,39),(101,'2017-12-10 15:37:55',1,38),(102,'2017-12-11 04:48:38',6,34),(103,'2017-12-11 04:48:47',6,35),(104,'2017-12-11 04:52:58',4,39),(105,'2017-12-11 04:52:59',NULL,39),(106,'2017-12-11 04:52:59',4,38),(107,'2017-12-11 04:53:00',NULL,38),(108,'2017-12-11 04:53:02',4,34),(109,'2017-12-11 04:53:03',NULL,34),(110,'2017-12-11 04:53:16',4,34),(111,'2017-12-11 04:53:22',4,26),(112,'2017-12-11 04:53:22',NULL,26),(113,'2017-12-11 04:53:37',4,9),(114,'2017-12-11 04:53:37',NULL,9),(115,'2017-12-11 04:53:43',4,36),(116,'2017-12-11 04:53:43',NULL,36),(117,'2017-12-11 04:54:20',4,25),(118,'2017-12-11 04:54:20',NULL,25),(119,'2017-12-11 06:46:04',7,33),(120,'2017-12-11 06:46:05',NULL,33),(121,'2017-12-11 06:46:26',4,33),(122,'2017-12-11 06:46:38',7,41),(123,'2017-12-11 06:46:38',NULL,41),(124,'2017-12-11 06:48:18',4,39),(125,'2017-12-11 06:48:20',4,38),(126,'2017-12-11 06:48:20',NULL,38),(127,'2017-12-11 06:49:49',7,39),(128,'2017-12-11 06:49:50',NULL,39),(129,'2017-12-11 06:49:51',NULL,39),(130,'2017-12-11 06:49:54',7,38),(131,'2017-12-11 06:50:22',7,40),(132,'2017-12-11 06:50:23',NULL,40),(133,'2017-12-11 06:50:55',7,37),(134,'2017-12-11 11:17:44',4,33),(135,'2017-12-11 16:58:07',NULL,26),(136,'2017-12-15 13:26:59',4,40),(137,'2017-12-15 13:27:00',NULL,40),(138,'2017-12-15 13:31:00',NULL,40),(139,'2017-12-15 14:15:46',4,37),(140,'2017-12-15 14:15:46',NULL,37),(141,'2017-12-17 03:37:05',4,36),(142,'2017-12-17 03:37:18',4,41),(143,'2017-12-17 03:37:36',4,23),(144,'2017-12-18 05:39:41',4,40),(145,'2017-12-18 05:39:47',4,36),(146,'2017-12-21 01:47:41',9,38),(147,'2017-12-23 04:49:21',4,42),(148,'2017-12-23 04:50:06',4,43),(149,'2017-12-23 17:55:12',4,43),(150,'2017-12-23 17:55:22',4,42),(151,'2017-12-23 17:57:23',4,40),(152,'2017-12-23 17:57:26',4,43),(153,'2017-12-25 21:36:12',NULL,20),(154,'2017-12-26 00:48:12',NULL,15),(155,'2017-12-26 00:48:38',4,37),(156,'2017-12-26 00:50:03',4,39),(157,'2017-12-26 00:50:15',4,41),(158,'2017-12-26 00:50:21',4,36),(159,'2017-12-26 00:51:48',4,35),(160,'2017-12-26 00:52:21',4,1),(161,'2017-12-26 11:39:06',4,35),(162,'2017-12-26 11:39:06',NULL,35),(163,'2017-12-26 11:39:19',4,42),(164,'2017-12-26 11:39:19',NULL,42),(165,'2017-12-27 11:34:22',2,37),(166,'2017-12-28 02:22:46',4,42),(167,'2017-12-28 11:54:48',4,43),(168,'2017-12-28 11:54:59',4,40),(169,'2017-12-28 11:55:04',4,38),(170,'2017-12-28 11:55:05',NULL,38),(171,'2017-12-28 11:55:11',4,25),(172,'2017-12-28 11:55:11',NULL,25),(173,'2017-12-30 05:41:19',4,43);
/*!40000 ALTER TABLE `view` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-03 12:28:32
