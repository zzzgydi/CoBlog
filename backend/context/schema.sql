/*
    创建数据库
*/

-- create DATABASE `conote`;

create table `user` (
    `uid` int UNSIGNED not null AUTO_INCREMENT,
    `account` varchar(128) not null,
    `password` varchar(128) not null,
    `name` varchar(128),
    primary key (`uid`)
);

create table `note` (
    `nid` varchar(64) not null,
    `author` int UNSIGNED not null,
    `label` varchar(256),
    `title` varchar(512),
    `content` text,
    `modified` int UNSIGNED,
    `state` varchar(32) not null,
    primary key (`nid`)
);

create table `label` (
    `l_id` int UNSIGNED not null AUTO_INCREMENT,
    `user` int UNSIGNED not null,
    `value` varchar(128) not null,
    `color` varchar(128),
    primary key (`l_id`)
);
