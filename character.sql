CREATE TABLE characters (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
    name text NOT NULL DEFAULT '',
    intelligence INTEGER NOT NULL DEFAULT 0,
    strength VARCHAR(10) NOT NULL DEFAULT '',
    speed INTEGER NOT NULL DEFAULT 0,
    durability INTEGER NOT NULL DEFAULT 0,
    power INTEGER NOT NULL DEFAULT 0,
    speed INTEGER NOT NULL DEFAULT 0,
    height VARCHAR(24) NOT NULL DEFAULT '',
    weight VARCHAR(24) NOT NULL DEFAULT ''
);
