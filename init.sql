
GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;
CREATE TABLE IF NOT EXISTS temp(
    id varchar(512) not null primary key
);
CREATE TABLE IF NOT EXISTS user(
    username varchar(512) not null,
    name varchar(512) not null,
    email varchar(512) not null,
    phone varchar(20) not null,
    is_active boolean not null,
    is_stuff boolean not null,
);