-- phpMyAdmin SQL Dump
-- version 3.5.8.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost:3306
-- 生成日期: 2013 年 12 月 05 日 19:37
-- 服务器版本: 5.1.69
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `dkzz`
--

-- --------------------------------------------------------

--
-- 表的结构 `game_detail`
--

CREATE TABLE IF NOT EXISTS `game_detail` (
  `game_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `player_num` tinyint(11) NOT NULL,
  `game_status` tinyint(11) NOT NULL DEFAULT '-1' COMMENT 'bitmap,default value is -1',
  `total_player` tinyint(11) NOT NULL DEFAULT '5',
  `owner_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `game_detail`
--

INSERT INTO `game_detail` (`game_id`, `player_num`, `game_status`, `total_player`, `owner_id`) VALUES
('a09e3a50-5d8f-11e3-9183-60a44c34b055', 1, -1, 3, '1-2-3-4'),
('d6e4910e-5d8f-11e3-bbba-60a44c34b055', 2, -1, 6, '1-2-3-4-5');

-- --------------------------------------------------------

--
-- 表的结构 `game_player`
--

CREATE TABLE IF NOT EXISTS `game_player` (
  `player_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `game_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `player_identity` tinyint(4) NOT NULL DEFAULT '-1',
  `player_card` tinyint(4) NOT NULL DEFAULT '-1',
  `player_vote` tinyint(4) NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `game_player`
--

INSERT INTO `game_player` (`player_id`, `game_id`, `player_identity`, `player_card`, `player_vote`) VALUES
('1-2-3', '4511f796-5d74-11e3-b327-60a44c34b055', 0, -1, 0),
('2-3-4', 'd6e4910e-5d8f-11e3-bbba-60a44c34b055', -1, -1, 0),
('1-2-3-4-5', 'd6e4910e-5d8f-11e3-bbba-60a44c34b055', -1, -1, 0),
('1-2-3-4', 'a09e3a50-5d8f-11e3-9183-60a44c34b055', -1, -1, 0);

-- --------------------------------------------------------

--
-- 表的结构 `player_detail`
--

CREATE TABLE IF NOT EXISTS `player_detail` (
  `player_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `player_nickname` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
