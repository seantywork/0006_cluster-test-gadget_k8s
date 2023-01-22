CREATE USER 'seantywork'@'%' IDENTIFIED BY 'youdonthavetoknow';

GRANT ALL PRIVILEGES ON *.* TO 'seantywork'@'%';

CREATE DATABASE test;

USE test;

CREATE TABLE counter (user VARCHAR(255), count INT);

INSERT INTO counter(user, count) values('youdonthavetoknow',0);

COMMIT;

