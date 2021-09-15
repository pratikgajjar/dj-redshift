# dj-redshift

This project aims to make existing postgres/postgis compatible django model definition with redshift.

## Postgres
```shell
$ python manage.py sqlmigrate main 0001_initial
```

```shell
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE TABLE "channels" ("id" serial NOT NULL PRIMARY KEY, "channel_id" varchar(30) NOT NULL UNIQUE, "name" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "uid" uuid NULL, "extra_data" jsonb NULL); (params None)
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE TABLE "videos" ("id" serial NOT NULL PRIMARY KEY, "video_id" varchar(11) NOT NULL UNIQUE, "title" varchar(200) NOT NULL, "description" text NOT NULL, "published_at" timestamp with time zone NOT NULL, "created_at" timestamp with time zone NOT NULL, "channel_id" integer NOT NULL); (params None)
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE INDEX "channels_channel_id_62d7be56_like" ON "channels" ("channel_id" varchar_pattern_ops); (params ())
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] ALTER TABLE "videos" ADD CONSTRAINT "videos_channel_id_769c9045_fk_channels_id" FOREIGN KEY ("channel_id") REFERENCES "channels" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE INDEX "videos_video_id_c3c7a99b_like" ON "videos" ("video_id" varchar_pattern_ops); (params ())
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE INDEX "videos_title_fca84e28" ON "videos" ("title"); (params ())
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE INDEX "videos_title_fca84e28_like" ON "videos" ("title" varchar_pattern_ops); (params ())
[14/Sep/2021 23:51:39] DEBUG [django.db.backends.schema:124] CREATE INDEX "videos_channel_id_769c9045" ON "videos" ("channel_id"); (params ())
BEGIN;
--
-- Create model Channel
--
CREATE TABLE "channels" ("id" serial NOT NULL PRIMARY KEY, "channel_id" varchar(30) NOT NULL UNIQUE, "name" varchar(200) NOT NULL, "created_at" timestamp with time zone NOT NULL, "uid" uuid NULL, "extra_data" jsonb NULL);
--
-- Create model Video
--
CREATE TABLE "videos" ("id" serial NOT NULL PRIMARY KEY, "video_id" varchar(11) NOT NULL UNIQUE, "title" varchar(200) NOT NULL, "description" text NOT NULL, "published_at" timestamp with time zone NOT NULL, "created_at" timestamp with time zone NOT NULL, "channel_id" integer NOT NULL);
CREATE INDEX "channels_channel_id_62d7be56_like" ON "channels" ("channel_id" varchar_pattern_ops);
ALTER TABLE "videos" ADD CONSTRAINT "videos_channel_id_769c9045_fk_channels_id" FOREIGN KEY ("channel_id") REFERENCES "channels" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "videos_video_id_c3c7a99b_like" ON "videos" ("video_id" varchar_pattern_ops);
CREATE INDEX "videos_title_fca84e28" ON "videos" ("title");
CREATE INDEX "videos_title_fca84e28_like" ON "videos" ("title" varchar_pattern_ops);
CREATE INDEX "videos_channel_id_769c9045" ON "videos" ("channel_id");
COMMIT;
```
## Redshift
```shell
[14/Sep/2021 23:49:42] DEBUG [django.db.backends.schema:124] CREATE TABLE "channels" ("id" integer identity(1, 1) NULL, "channel_id" varchar(30) NULL UNIQUE, "name" varchar(200) NULL, "created_at" timestamp with time zone NULL, "uid" varchar(40) NULL, "extra_data" SUPER NULL) ; (params None)
[14/Sep/2021 23:49:42] DEBUG [django.db.backends.schema:124] CREATE TABLE "videos" ("id" integer identity(1, 1) NULL, "video_id" varchar(11) NULL UNIQUE, "title" varchar(200) NULL, "description" varchar(max) NULL, "published_at" timestamp with time zone NULL, "created_at" timestamp with time zone NULL, "channel_id" integer NULL) ; (params None)
[14/Sep/2021 23:49:42] DEBUG [django.db.backends.schema:124] ALTER TABLE "videos" ADD CONSTRAINT "videos_channel_id_769c9045_fk_channels_id" FOREIGN KEY ("channel_id") REFERENCES "channels" ("id"); (params ())
BEGIN;
--
-- Create model Channel
--
CREATE TABLE "channels" ("id" integer identity(1, 1) NULL, "channel_id" varchar(30) NULL UNIQUE, "name" varchar(200) NULL, "created_at" timestamp with time zone NULL, "uid" varchar(40) NULL, "extra_data" SUPER NULL) ;
--
-- Create model Video
--
CREATE TABLE "videos" ("id" integer identity(1, 1) NULL, "video_id" varchar(11) NULL UNIQUE, "title" varchar(200) NULL, "description" varchar(max) NULL, "published_at" timestamp with time zone NULL, "created_at" timestamp with time zone NULL, "channel_id" integer NULL) ;
ALTER TABLE "videos" ADD CONSTRAINT "videos_channel_id_769c9045_fk_channels_id" FOREIGN KEY ("channel_id") REFERENCES "channels" ("id");
COMMIT;
```