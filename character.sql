CREATE TABLE characters (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
    name text NOT NULL DEFAULT '',
    intelligence VARCHAR(10) NOT NULL DEFAULT '',
    strength VARCHAR(10) NOT NULL DEFAULT '',
    speed VARCHAR(10) NOT NULL DEFAULT '',
    durability VARCHAR(10) NOT NULL DEFAULT '',
    power VARCHAR(10) NOT NULL DEFAULT '',
    combat VARCHAR(10) NOT NULL DEFAULT '',
    height VARCHAR(24) NOT NULL DEFAULT '',
    weight VARCHAR(24) NOT NULL DEFAULT ''
);
