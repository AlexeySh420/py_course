# Lecture 15 05.04.2026

# SQL
# CREATE

CREATE TABLE "user" (
    "u_id" INTEGER NOT NULL UNIQUE,
    "u_name" TEXT NOT NULL,
    "u_email" TEXT NOT NULL,
    "u_phone" TEXT NOT NULL,
    PRIMARY KEY("u_id" AUTOINCREMENT)
    );

CREATE TABLE "task" (
    "t_id" INTEGER NOT NULL UNIQUE,
    "t_name" TEXT NOT NULL,
    "t_priority" TEXT NOT NULL,
    "u_id_fk" INTEGER NOT NULL,
    PRIMARY KEY("t_id" AUTOINCREMENT),
    FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
    );


# INSERT

INSERT INTO user (u_name, u_email, u_phone) VALUES ("Дима", "@123","123");
INSERT INTO user (u_name, u_email, u_phone) VALUES ("Витя", "@12","123");
INSERT INTO user (u_name, u_email, u_phone) VALUES ("Катя", "@13","123");
INSERT INTO user (u_name, u_email, u_phone) VALUES ("Стас", "@12343","123");
INSERT INTO user (u_name, u_email, u_phone) VALUES ("Вадим", "@13433","123");

INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег",1, 1);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("есть",2, 2);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("спать",11, 3);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег1",123, 4);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег2",10, 5);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег3",9, 6);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег4",5, 2);
INSERT INTO task (t_name, t_priority, u_id_fk) VALUES ("бег5",16,3);


# DELETE
DELETE FROM task WHERE t_id=5;


# Python Implementation

import sqlite3

with sqlite3.connect("text_todolist.db") as c:
    print(c)
    print(type(c))

cur = c.cursor()
print(cur)
print(type(cur))

with sqlite3.connect("text_todolist.db") as c:
    cur = c.cursor()


with sqlite3.connect("text_todolist.db") as c:
    cur = c.cursor()
    q_text = """CREATE TABLE IF NOT EXISTS "user" (
            "u_id" INTEGER NOT NULL UNIQUE,
            "u_name" TEXT NOT NULL,
            PRIMARY KEY("u_id" AUTOINCREMENT));"""
    cur.execute(q_text)

q_text = """CREATE TABLE IF NOT EXISTS "task" (
        "t_id" INTEGER NOT NULL UNIQUE,
        "t_name" TEXT NOT NULL,
        "u_id_fk" INTEGER NOT NULL,
        PRIMARY KEY("t_id" AUTOINCREMENT),
        FOREIGN KEY(u_id_fk) REFERENCES user(u_id));"""
cur.execute(q_text)
c.commit()
