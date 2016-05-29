attach "cs183db.db" as db1;

CREATE TABLE IF NOT EXISTS db1.app(
    id INT PRIMARY KEY,
    version TEXT,
    name TEXT);

CREATE TABLE IF NOT EXISTS db1.bugreport(
    id INT PRIMARY KEY,
    report TEXT,
    appid INT,
    FOREIGN KEY(appid) REFERENCES app(id));
