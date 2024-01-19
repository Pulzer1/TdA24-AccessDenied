DROP TABLE IF EXISTS lecturer_tags;
DROP TABLE IF EXISTS lecturer;
DROP TABLE IF EXISTS tag;

CREATE TABLE IF NOT EXISTS contact_info (
    id INTEGER PRIMARY KEY,
    telephone_numbers BLOB,
    emails BLOB
);

CREATE TABLE IF NOT EXISTS lecturer (
    uuid TEXT PRIMARY KEY,
    title_before TEXT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    title_after TEXT,
    picture_url TEXT,
    location TEXT,
    claim TEXT,
    bio TEXT,
    price_per_hour INTEGER,
    contact_id INTEGER,
    FOREIGN KEY (contact_id) REFERENCES contact_info(id)
);




CREATE TABLE IF NOT EXISTS tag (
    uuid TEXT PRIMARY KEY, 
    name TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS lecturer_tags (
    lecturer_uuid TEXT,
    tag_uuid TEXT, 
    PRIMARY KEY (lecturer_uuid, tag_uuid),
    FOREIGN KEY (lecturer_uuid) REFERENCES lecturer (uuid),
    FOREIGN KEY (tag_uuid) REFERENCES tag (uuid)
);