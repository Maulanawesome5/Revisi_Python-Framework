-- Active: 1667427687682@@127.0.0.1@3306@django_project
USE django_project;
SHOW TABLES;
SELECT * FROM blog_post;
DESCRIBE blog_post;

ALTER TABLE blog_post
DROP COLUMN author_username;
ALTER TABLE blog_post
DROP COLUMN date_post;
