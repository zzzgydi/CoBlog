/*
    创建数据库
*/

-- create DATABASE `conote`;
/*
alias 存放用户主页需要跳转的地址
flag  记录用户主页是否需要跳转
*/
create table `user` (
    `uid` int UNSIGNED not null AUTO_INCREMENT,
    `account` varchar(128) not null,
    `password` varchar(128) not null,
    `name` varchar(128),
    `avatar` varchar(256),
    `backimg` varchar(256),
    `alias` varchar(256),
    `flag` tinyint default 0,
    primary key (`uid`)
);

create table `note` (
    `nid` varchar(64) not null,
    `author` int UNSIGNED not null,
    `label` varchar(256),
    `title` varchar(512),
    `content` text,
    `modified` bigint UNSIGNED,
    `state` varchar(32) not null,
    `look` int UNSIGNED not null,
    primary key (`nid`)
);

create table `label` (
    `l_id` int UNSIGNED not null AUTO_INCREMENT,
    `user` int UNSIGNED not null,
    `value` varchar(128) not null,
    `color` varchar(128),
    primary key (`l_id`)
);

create table `favurl` (
    `fid` int UNSIGNED not null AUTO_INCREMENT,
    `user` int UNSIGNED not null,
    `title` varchar(512),
    `url` text,
    `remark` text,
    `modified` bigint UNSIGNED,
    primary key (`fid`)
);

create table `image` (
    `id` int UNSIGNED not null AUTO_INCREMENT,
    `user` int UNSIGNED not null,
    `url` varchar(256) not null,
    `filename` varchar(256) not null,
    `hash` varchar(256) not null,
    `modified` bigint UNSIGNED,
    `remark` varchar(64),
    primary key (`id`)
);

ALTER TABLE `user` ADD `avatar` VARCHAR(256) NULL AFTER `name`;
ALTER TABLE `user` ADD `backimg` VARCHAR(256) NULL AFTER `avatar`;
ALTER TABLE `user` ADD `alias` VARCHAR(256) NULL AFTER `backimg`;
ALTER TABLE `user` ADD `flag` TINYINT NOT NULL DEFAULT '0' AFTER `alias`;
