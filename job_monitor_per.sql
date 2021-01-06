/*
Navicat MySQL Data Transfer

Source Server         : 172.16.8.208
Source Server Version : 50729
Source Host           : 172.16.8.208:3306
Source Database       : bd_ads_test

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-06-19 22:44:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for job_monitor_per
-- ----------------------------
DROP TABLE IF EXISTS `job_monitor_per`;
CREATE TABLE `job_monitor_per` (
  `name` varchar(20) DEFAULT NULL,
  `sname` varchar(20) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dutydate` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of job_monitor_per
-- ----------------------------
INSERT INTO `job_monitor_per` VALUES (' 戴飞俊', 'daifeijun', '18101972375', null, '星期一');
INSERT INTO `job_monitor_per` VALUES ('高响', 'gaoxiang', '13122225313', null, '星期二');
INSERT INTO `job_monitor_per` VALUES ('高明明', 'gaomingming', '17356762434', null, '星期三');
INSERT INTO `job_monitor_per` VALUES ('张昭', 'zhangzhao', '18658263365', null, '星期四');
INSERT INTO `job_monitor_per` VALUES ('金熙', 'jinxi', '18521510944', null, '星期五');
INSERT INTO `job_monitor_per` VALUES ('史可', 'shike', '18717718913', null, '星期六');
INSERT INTO `job_monitor_per` VALUES ('李强', 'liqiang', '18621884244', null, '星期天');
