-- Active: 1667427687682@@127.0.0.1@3306@django_project
USE django_project;
SHOW TABLES;
SELECT * FROM blog_post; SELECT * FROM auth_user;
DESCRIBE blog_post; DESCRIBE auth_user;

ALTER TABLE blog_post
DROP COLUMN author_username;
ALTER TABLE blog_post
DROP COLUMN date_post;

-- Delete table. Terdapat error karena ada nama table kembar dengan nama kolom
DROP TABLE blog_post;


CREATE TABLE blog_post_copy (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    email VARCHAR(254) NOT NULL DEFAULT "user@domain.com",
    posting_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

SELECT * FROM blog_post_copy; DESCRIBE blog_post_copy;
