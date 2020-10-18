CREATE TABLE `tbl_Voces` (
  `id` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `SO` int(11) DEFAULT NULL,
  `idAudio` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
