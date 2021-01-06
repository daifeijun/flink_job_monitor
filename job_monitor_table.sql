/*
Navicat MySQL Data Transfer

Source Server         : 172.16.8.208
Source Server Version : 50729
Source Host           : 172.16.8.208:3306
Source Database       : bd_ads_test

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-06-19 22:45:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for job_monitor_table
-- ----------------------------
DROP TABLE IF EXISTS `job_monitor_table`;
CREATE TABLE `job_monitor_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jobname` varchar(100) DEFAULT NULL,
  `jobtype` varchar(10) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL COMMENT '0:running;1:失败；2:其他',
  `statusname` varchar(20) DEFAULT NULL,
  `jobowner` varchar(20) DEFAULT NULL,
  `jobstatuscom` varchar(500) DEFAULT NULL COMMENT '获取状态的yarn application -list ',
  `jobstatuscom1` varchar(500) DEFAULT NULL,
  `jobruncom` varchar(500) DEFAULT NULL COMMENT '执行job的命令 python脚本文件',
  `detection_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
