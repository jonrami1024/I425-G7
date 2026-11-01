-- KartLab: Mario Kart 8 Deluxe Build Planner

-- Stats are stored as integer points (levels), the way the game stores them.
-- A build's level for a stat = driver + body + tire + glider points.
-- The value shown in the game's stat bars = (level + 3) / 4.0
-- Stat data source: Super Mario Wiki, "Mario Kart 8 Deluxe in-game statistics"
-- (ground speed and ground handling are used for speed and handling).

PRAGMA foreign_keys = ON;

DROP VIEW  IF EXISTS build_stats;
DROP TRIGGER IF EXISTS no_self_rating_insert;
DROP TRIGGER IF EXISTS no_self_rating_update;
DROP TABLE IF EXISTS build_ratings;
DROP TABLE IF EXISTS builds;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS gliders;
DROP TABLE IF EXISTS tires;
DROP TABLE IF EXISTS tire_groups;
DROP TABLE IF EXISTS bodies;
DROP TABLE IF EXISTS body_groups;
DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS driver_groups;

-- Independent entities: stat groups and users
-- Parts in the same group share the exact same stats in the game.

CREATE TABLE driver_groups (
    driver_group_id INTEGER PRIMARY KEY,
    label          TEXT    NOT NULL UNIQUE,
    size           TEXT    NOT NULL CHECK (size IN ('Small','Medium','Large')),
    speed          INTEGER NOT NULL CHECK (speed BETWEEN 0 AND 20),
    acceleration   INTEGER NOT NULL CHECK (acceleration BETWEEN 0 AND 20),
    weight         INTEGER NOT NULL CHECK (weight BETWEEN 0 AND 20),
    handling       INTEGER NOT NULL CHECK (handling BETWEEN 0 AND 20),
    traction       INTEGER NOT NULL CHECK (traction BETWEEN 0 AND 20),
    mini_turbo     INTEGER NOT NULL CHECK (mini_turbo BETWEEN 0 AND 20),
    invincibility  INTEGER NOT NULL CHECK (invincibility BETWEEN 0 AND 20)
);

CREATE TABLE body_groups (
    body_group_id INTEGER PRIMARY KEY,
    label          TEXT    NOT NULL UNIQUE,
    speed          INTEGER NOT NULL CHECK (speed BETWEEN 0 AND 20),
    acceleration   INTEGER NOT NULL CHECK (acceleration BETWEEN 0 AND 20),
    weight         INTEGER NOT NULL CHECK (weight BETWEEN 0 AND 20),
    handling       INTEGER NOT NULL CHECK (handling BETWEEN 0 AND 20),
    traction       INTEGER NOT NULL CHECK (traction BETWEEN 0 AND 20),
    mini_turbo     INTEGER NOT NULL CHECK (mini_turbo BETWEEN 0 AND 20),
    invincibility  INTEGER NOT NULL CHECK (invincibility BETWEEN 0 AND 20)
);

CREATE TABLE tire_groups (
    tire_group_id INTEGER PRIMARY KEY,
    label          TEXT    NOT NULL UNIQUE,
    speed          INTEGER NOT NULL CHECK (speed BETWEEN 0 AND 20),
    acceleration   INTEGER NOT NULL CHECK (acceleration BETWEEN 0 AND 20),
    weight         INTEGER NOT NULL CHECK (weight BETWEEN 0 AND 20),
    handling       INTEGER NOT NULL CHECK (handling BETWEEN 0 AND 20),
    traction       INTEGER NOT NULL CHECK (traction BETWEEN 0 AND 20),
    mini_turbo     INTEGER NOT NULL CHECK (mini_turbo BETWEEN 0 AND 20),
    invincibility  INTEGER NOT NULL CHECK (invincibility BETWEEN 0 AND 20)
);

CREATE TABLE users (
    user_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username       TEXT    NOT NULL UNIQUE CHECK (length(trim(username)) > 0),
    email          TEXT    NOT NULL UNIQUE
);

-- Gliders keep their stats directly: the game has only 4 glider stat groups,
-- which is below the 5-row minimum for a separate group table.
CREATE TABLE gliders (
    glider_id      INTEGER PRIMARY KEY,
    name           TEXT    NOT NULL UNIQUE,
    image_file     TEXT,
    speed          INTEGER NOT NULL CHECK (speed BETWEEN 0 AND 20),
    acceleration   INTEGER NOT NULL CHECK (acceleration BETWEEN 0 AND 20),
    weight         INTEGER NOT NULL CHECK (weight BETWEEN 0 AND 20),
    handling       INTEGER NOT NULL CHECK (handling BETWEEN 0 AND 20),
    traction       INTEGER NOT NULL CHECK (traction BETWEEN 0 AND 20),
    mini_turbo     INTEGER NOT NULL CHECK (mini_turbo BETWEEN 0 AND 20),
    invincibility  INTEGER NOT NULL CHECK (invincibility BETWEEN 0 AND 20)
);

-- Dependent entities: parts

CREATE TABLE drivers (
    driver_id       INTEGER PRIMARY KEY,
    name            TEXT    NOT NULL UNIQUE,
    driver_group_id INTEGER NOT NULL,
    image_file      TEXT,
    FOREIGN KEY (driver_group_id) REFERENCES driver_groups(driver_group_id) ON DELETE RESTRICT
);

CREATE TABLE bodies (
    body_id         INTEGER PRIMARY KEY,
    name            TEXT    NOT NULL UNIQUE,
    vehicle_type    TEXT    NOT NULL CHECK (vehicle_type IN ('Kart','Standard Bike','Sport Bike','ATV')),
    body_group_id   INTEGER NOT NULL,
    image_file      TEXT,
    FOREIGN KEY (body_group_id) REFERENCES body_groups(body_group_id) ON DELETE RESTRICT
);

CREATE TABLE tires (
    tire_id         INTEGER PRIMARY KEY,
    name            TEXT    NOT NULL UNIQUE,
    tire_group_id   INTEGER NOT NULL,
    image_file      TEXT,
    FOREIGN KEY (tire_group_id) REFERENCES tire_groups(tire_group_id) ON DELETE RESTRICT
);



-- Dependent entities: user content

CREATE TABLE builds (
    build_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      INTEGER NOT NULL,
    driver_id    INTEGER NOT NULL,
    body_id      INTEGER NOT NULL,
    tire_id      INTEGER NOT NULL,
    glider_id    INTEGER NOT NULL,
    build_name   TEXT    NOT NULL CHECK (length(trim(build_name)) > 0),
    FOREIGN KEY (user_id)   REFERENCES users(user_id)     ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE RESTRICT,
    FOREIGN KEY (body_id)   REFERENCES bodies(body_id)    ON DELETE RESTRICT,
    FOREIGN KEY (tire_id)   REFERENCES tires(tire_id)     ON DELETE RESTRICT,
    FOREIGN KEY (glider_id) REFERENCES gliders(glider_id) ON DELETE RESTRICT
);

CREATE TABLE build_ratings (
    rating_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    build_id     INTEGER NOT NULL,
    user_id      INTEGER NOT NULL,
    score        INTEGER NOT NULL CHECK (score BETWEEN 1 AND 5),
    FOREIGN KEY (build_id) REFERENCES builds(build_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id)  REFERENCES users(user_id)   ON DELETE CASCADE,
    UNIQUE (build_id, user_id)
);

-- Sample data

INSERT INTO driver_groups (driver_group_id, label, size, speed, acceleration, weight, handling, traction, mini_turbo, invincibility) VALUES
(1, 'Baby Peach class', 'Small', 1, 4, 0, 10, 5, 5, 6),
(2, 'Baby Rosalina class', 'Small', 1, 5, 0, 9, 3, 5, 6),
(3, 'Baby Mario class', 'Small', 2, 5, 1, 8, 4, 5, 5),
(4, 'Koopa Troopa class', 'Small', 3, 4, 2, 8, 5, 4, 4),
(5, 'Toadette class', 'Small', 3, 5, 2, 7, 2, 4, 3),
(6, 'Toad class', 'Small', 4, 4, 3, 7, 4, 4, 3),
(7, 'Cat Peach class', 'Medium', 5, 4, 3, 6, 3, 4, 3),
(8, 'Peach class', 'Medium', 6, 3, 4, 5, 3, 4, 1),
(9, 'Tanooki Mario class', 'Medium', 6, 3, 5, 5, 1, 4, 1),
(10, 'Mario class', 'Medium', 7, 2, 6, 4, 2, 3, 3),
(11, 'Luigi class', 'Medium', 7, 2, 6, 5, 1, 3, 3),
(12, 'Metal Mario class', 'Medium', 8, 1, 10, 3, 1, 1, 3),
(13, 'Wiggler class', 'Medium', 9, 1, 8, 2, 0, 1, 4),
(14, 'Rosalina class', 'Large', 8, 1, 7, 3, 3, 2, 4),
(15, 'Petey Piranha class', 'Large', 8, 1, 10, 3, 1, 1, 6),
(16, 'Waluigi class', 'Large', 9, 1, 8, 2, 0, 1, 4),
(17, 'Wario class', 'Large', 10, 0, 9, 1, 1, 0, 5),
(18, 'Bowser class', 'Large', 10, 0, 10, 0, 0, 0, 6);

INSERT INTO drivers (driver_id, name, driver_group_id, image_file) VALUES
(1, 'Baby Peach', 1, 'img/character/image8.webp'),
(2, 'Baby Daisy', 1, 'img/character/image5.webp'),
(3, 'Baby Rosalina', 2, 'img/character/image9.webp'),
(4, 'Lemmy', 2, 'img/character/image26.webp'),
(5, 'Baby Mario', 3, 'img/character/image7.webp'),
(6, 'Baby Luigi', 3, 'img/character/image6.webp'),
(7, 'Dry Bones', 3, 'img/character/image15.webp'),
(8, 'Mii (Light)', 3, 'img/character/image51.png'),
(9, 'Koopa Troopa', 4, 'img/character/image23.webp'),
(10, 'Lakitu', 4, 'img/character/image24.webp'),
(11, 'Bowser Jr.', 4, 'img/character/image2.webp'),
(12, 'Toadette', 5, 'img/character/image43.webp'),
(13, 'Wendy', 5, 'img/character/image46.webp'),
(14, 'Isabelle', 5, 'img/character/image20.webp'),
(15, 'Toad', 6, 'img/character/image42.webp'),
(16, 'Shy Guy', 6, 'img/character/image40.webp'),
(17, 'Larry', 6, 'img/character/image25.webp'),
(18, 'Cat Peach', 7, 'img/character/image11.webp'),
(19, 'Inkling Girl', 7, 'img/character/image17.webp'),
(20, 'Villager (Female)', 7, 'img/character/image49.webp'),
(21, 'Diddy Kong', 7, 'img/character/image13.webp'),
(22, 'Peach', 8, 'img/character/image34.webp'),
(23, 'Daisy', 8, 'img/character/image12.webp'),
(24, 'Yoshi', 8, 'img/character/image48.webp'),
(25, 'Birdo', 8, 'img/character/image3.webp'),
(26, 'Peachette', 8, 'img/character/image35.webp'),
(27, 'Tanooki Mario', 9, 'img/character/image41.webp'),
(28, 'Inkling Boy', 9, 'img/character/image50.webp'),
(29, 'Villager (Male)', 9, 'img/character/image29.webp'),
(30, 'Mario', 10, 'img/character/image30.webp'),
(31, 'Ludwig', 10, 'img/character/image27.webp'),
(32, 'Mii (Medium)', 10, 'img/character/image52.png'),
(33, 'Luigi', 11, 'img/character/image28.webp'),
(34, 'Iggy', 11, 'img/character/image19.webp'),
(35, 'Kamek', 11, 'img/character/image21.webp'),
(36, 'Metal Mario', 12, 'img/character/image31.webp'),
(37, 'Gold Mario', 12, 'img/character/image54.webp'),
(38, 'Pink Gold Peach', 12, 'img/character/image37.webp'),
(39, 'Wiggler', 13, 'img/character/image47.webp'),
(40, 'Rosalina', 14, 'img/character/image38.webp'),
(41, 'King Boo', 14, 'img/character/image22.webp'),
(42, 'Link', 14, 'img/character/image4.webp'),
(43, 'Link (BotW)', 14, 'img/character/image4.webp'),
(44, 'Pauline', 14, 'img/character/image33.webp'),
(45, 'Petey Piranha', 15, 'img/character/image36.webp'),
(46, 'Waluigi', 16, 'img/character/image44.webp'),
(47, 'Donkey Kong', 16, 'img/character/image14.webp'),
(48, 'Roy', 16, 'img/character/image39.webp'),
(49, 'Wario', 17, 'img/character/image45.webp'),
(50, 'Dry Bowser', 17, 'img/character/image16.webp'),
(51, 'Funky Kong', 17, 'img/character/image18.webp'),
(52, 'Mii (Heavy)', 17, 'img/character/image53.png'),
(53, 'Bowser', 18, 'img/character/image10.webp'),
(54, 'Morton', 18, 'img/character/image32.webp');

INSERT INTO body_groups (body_group_id, label, speed, acceleration, weight, handling, traction, mini_turbo, invincibility) VALUES
(1, 'Biddybuggy class', 0, 7, 0, 5, 4, 7, 0),
(2, 'Streetle class', 2, 6, 0, 4, 6, 6, 3),
(3, 'Landship class', 2, 6, 0, 4, 6, 6, 2),
(4, 'Pipe Frame class', 2, 6, 1, 5, 4, 6, 3),
(5, 'Varmint class', 2, 6, 1, 5, 4, 6, 2),
(6, 'Cat Cruiser class', 2, 5, 2, 4, 3, 6, 3),
(7, 'Yoshi Bike class', 2, 5, 2, 4, 3, 6, 2),
(8, 'Teddy Buggy class', 2, 5, 2, 4, 3, 6, 1),
(9, 'W 25 Silver Arrow class', 2, 5, 1, 4, 5, 5, 4),
(10, 'Mach 8 class', 3, 3, 3, 2, 4, 5, 3),
(11, 'Inkstriker class', 3, 3, 3, 2, 4, 5, 1),
(12, 'Tanooki Kart class', 3, 2, 3, 4, 7, 5, 4),
(13, 'Koopa Clown class', 3, 2, 3, 4, 7, 5, 3),
(14, '300 SL Roadster class', 3, 4, 2, 3, 3, 5, 4),
(15, 'Standard Kart class', 3, 4, 2, 3, 3, 5, 3),
(16, 'Blue Falcon class', 4, 3, 0, 2, 3, 4, 4),
(17, 'Splat Buggy class', 4, 3, 0, 2, 3, 4, 3),
(18, 'Prancer class', 4, 2, 1, 3, 2, 4, 5),
(19, 'Sport Bike class', 4, 2, 1, 3, 2, 4, 3),
(20, 'Sneeker class', 4, 2, 2, 3, 0, 4, 5),
(21, 'Gold Standard class', 4, 2, 2, 3, 0, 4, 4),
(22, 'Master Cycle class', 4, 2, 2, 3, 0, 4, 3),
(23, 'Steel Driver class', 4, 1, 4, 1, 3, 3, 6),
(24, 'Bone Rattler class', 4, 1, 4, 1, 3, 3, 5),
(25, 'Circuit Special class', 5, 1, 3, 1, 1, 3, 6),
(26, 'Badwagon class', 5, 0, 4, 0, 5, 3, 7),
(27, 'Standard ATV class', 5, 0, 4, 0, 5, 3, 6);

INSERT INTO bodies (body_id, name, vehicle_type, body_group_id, image_file) VALUES
(1, 'Biddybuggy', 'Kart', 1, 'img/kart/image3.webp'),
(2, 'Mr. Scooty', 'Standard Bike', 1, 'img/kart/image24.webp'),
(3, 'Streetle', 'Kart', 2, 'img/kart/image23.webp'),
(4, 'Landship', 'Kart', 3, 'img/kart/image11.webp'),
(5, 'Pipe Frame', 'Kart', 4, 'img/kart/image25.webp'),
(6, 'Varmint', 'Standard Bike', 5, 'img/kart/image36.webp'),
(7, 'City Tripper', 'Standard Bike', 5, 'img/kart/image13.webp'),
(8, 'Cat Cruiser', 'Kart', 6, 'img/kart/image4.webp'),
(9, 'Comet', 'Sport Bike', 6, 'img/kart/image10.webp'),
(10, 'Yoshi Bike', 'Sport Bike', 7, 'img/kart/image40.webp'),
(11, 'Teddy Buggy', 'ATV', 8, 'img/kart/image34.webp'),
(12, 'W 25 Silver Arrow', 'Kart', 9, 'img/kart/image38.webp'),
(13, 'Wild Wiggler', 'ATV', 9, 'img/kart/image39.webp'),
(14, 'Standard Bike', 'Standard Bike', 9, 'img/kart/image31.webp'),
(15, 'Flame Rider', 'Standard Bike', 9, 'img/kart/image7.webp'),
(16, 'Mach 8', 'Kart', 10, 'img/kart/image12.webp'),
(17, 'Sports Coupe', 'Kart', 10, 'img/kart/image29.webp'),
(18, 'Inkstriker', 'ATV', 11, 'img/kart/image18.webp'),
(19, 'Tanooki Kart', 'Kart', 12, 'img/kart/image26.webp'),
(20, 'Koopa Clown', 'Kart', 13, 'img/kart/image19.webp'),
(21, 'Master Cycle Zero', 'Standard Bike', 13, 'img/kart/image17.webp'),
(22, '300 SL Roadster', 'Kart', 14, 'img/kart/image1.webp'),
(23, 'Standard Kart', 'Kart', 15, 'img/kart/image32.webp'),
(24, 'The Duke', 'Standard Bike', 15, 'img/kart/image30.webp'),
(25, 'Blue Falcon', 'Kart', 16, 'img/kart/image5.webp'),
(26, 'Splat Buggy', 'ATV', 17, 'img/kart/image20.webp'),
(27, 'Prancer', 'Kart', 18, 'img/kart/image2.webp'),
(28, 'Sport Bike', 'Sport Bike', 19, 'img/kart/image28.webp'),
(29, 'Jet Bike', 'Sport Bike', 19, 'img/kart/image35.webp'),
(30, 'Sneeker', 'Kart', 20, 'img/kart/image27.webp'),
(31, 'Gold Standard', 'Kart', 21, 'img/kart/image9.webp'),
(32, 'Master Cycle', 'Sport Bike', 22, 'img/kart/image21.webp'),
(33, 'Steel Driver', 'Kart', 23, 'img/kart/image33.webp'),
(34, 'Tri-Speeder', 'Kart', 23, 'img/kart/image14.webp'),
(35, 'Bone Rattler', 'ATV', 24, 'img/kart/image37.webp'),
(36, 'Circuit Special', 'Kart', 25, 'img/kart/image41.webp'),
(37, 'B Dasher', 'Kart', 25, 'img/kart/image15.webp'),
(38, 'P-Wing', 'Kart', 25, 'img/kart/image22.webp'),
(39, 'Badwagon', 'Kart', 26, 'img/kart/image16.webp'),
(40, 'GLA', 'Kart', 26, 'img/kart/image8.webp'),
(41, 'Standard ATV', 'ATV', 27, 'img/kart/image6.webp');

INSERT INTO tire_groups (tire_group_id, label, speed, acceleration, weight, handling, traction, mini_turbo, invincibility) VALUES
(1, 'Roller class', 0, 6, 0, 4, 4, 6, 0),
(2, 'Button class', 1, 5, 0, 3, 3, 5, 3),
(3, 'Cushion class', 1, 4, 1, 2, 6, 5, 6),
(4, 'Sponge class', 1, 4, 1, 2, 6, 5, 4),
(5, 'GLA Tires class', 2, 4, 2, 3, 5, 4, 5),
(6, 'Standard class', 2, 4, 2, 3, 5, 4, 4),
(7, 'Slim class', 3, 2, 2, 4, 1, 3, 5),
(8, 'Monster class', 3, 2, 4, 0, 7, 3, 6),
(9, 'Ancient Tires class', 3, 2, 4, 0, 7, 3, 5),
(10, 'Off-Road class', 3, 3, 3, 1, 6, 3, 6),
(11, 'Slick class', 4, 1, 3, 2, 0, 2, 5),
(12, 'Metal class', 4, 0, 4, 2, 2, 2, 6),
(13, 'Gold Tires class', 4, 0, 4, 2, 2, 2, 5);

INSERT INTO tires (tire_id, name, tire_group_id, image_file) VALUES
(1, 'Roller', 1, 'img/tires/image17.webp'),
(2, 'Azure Roller', 1, 'img/tires/image1.webp'),
(3, 'Button', 2, 'img/tires/image3.webp'),
(4, 'Leaf Tires', 2, 'img/tires/image10.webp'),
(5, 'Cushion', 3, 'img/tires/image5.webp'),
(6, 'Sponge', 4, 'img/tires/image20.webp'),
(7, 'GLA Tires', 5, 'img/tires/image7.webp'),
(8, 'Standard', 6, 'img/tires/image21.webp'),
(9, 'Blue Standard', 6, 'img/tires/image2.webp'),
(10, 'Slim', 7, 'img/tires/image19.webp'),
(11, 'Crimson Slim', 7, 'img/tires/image4.webp'),
(12, 'Wood', 7, 'img/tires/image22.webp'),
(13, 'Monster', 8, 'img/tires/image14.webp'),
(14, 'Hot Monster', 8, 'img/tires/image9.webp'),
(15, 'Ancient Tires', 9, 'img/tires/image12.webp'),
(16, 'Off-Road', 10, 'img/tires/image15.webp'),
(17, 'Retro Off-Road', 10, 'img/tires/image16.webp'),
(18, 'Triforce Tires', 10, 'img/tires/image13.webp'),
(19, 'Slick', 11, 'img/tires/image18.webp'),
(20, 'Cyber Slick', 11, 'img/tires/image6.webp'),
(21, 'Metal', 12, 'img/tires/image11.webp'),
(22, 'Gold Tires', 13, 'img/tires/image8.webp');

INSERT INTO gliders (glider_id, name, image_file, speed, acceleration, weight, handling, traction, mini_turbo, invincibility) VALUES
(1, 'Cloud Glider', 'img/glider/image2.webp', 0, 2, 0, 1, 1, 2, 0),
(2, 'Parachute', 'img/glider/image9.webp', 0, 2, 0, 1, 1, 2, 0),
(3, 'Flower Glider', 'img/glider/image3.webp', 0, 2, 0, 1, 1, 2, 0),
(4, 'Paper Glider', 'img/glider/image8.webp', 0, 2, 0, 1, 1, 2, 0),
(5, 'Peach Parasol', 'img/glider/image11.webp', 0, 2, 1, 1, 0, 2, 0),
(6, 'Parafoil', 'img/glider/image10.webp', 0, 2, 1, 1, 0, 2, 0),
(7, 'Bowser Kite', 'img/glider/image1.webp', 0, 2, 1, 1, 0, 2, 0),
(8, 'MKTV Parafoil', 'img/glider/image7.webp', 0, 2, 1, 1, 0, 2, 0),
(9, 'Wario Wing', 'img/glider/image15.webp', 1, 1, 2, 1, 0, 1, 1),
(10, 'Plane Glider', 'img/glider/image12.webp', 1, 1, 2, 1, 0, 1, 1),
(11, 'Gold Glider', 'img/glider/image4.webp', 1, 1, 2, 1, 0, 1, 1),
(12, 'Paraglider', 'img/glider/image5.webp', 1, 1, 2, 1, 0, 1, 1),
(13, 'Super Glider', 'img/glider/image13.webp', 1, 1, 1, 1, 1, 1, 1),
(14, 'Waddle Wing', 'img/glider/image14.webp', 1, 1, 1, 1, 1, 1, 1),
(15, 'Hylian Kite', 'img/glider/image6.webp', 1, 1, 1, 1, 1, 1, 1);

INSERT INTO users (username, email) VALUES
('shellshocked',  'shellshocked@example.com'),
('bananapeel99',  'bananapeel99@example.com'),
('rainbowroad',   'rainbowroad@example.com'),
('bluesheller',   'bluesheller@example.com'),
('driftking',     'driftking@example.com');

-- 1: Mario / Teddy Buggy / Roller / Cloud Glider
-- 2: Bowser / Mach 8 / Slick / Wario Wing
-- 3: Baby Peach / Biddybuggy / Roller / Peach Parasol
-- 4: Wario / Badwagon / Monster / Plane Glider
-- 5: Rosalina / Wild Wiggler / Roller / Cloud Glider
-- 6: Toad / Mr. Scooty / Button / Paraglider
INSERT INTO builds (user_id, driver_id, body_id, tire_id, glider_id, build_name) VALUES
(1, 30, 11, 1, 1, 'Balanced Teddy'),
(2, 53, 16, 19, 9, 'Max Speed Bowser'),
(3, 1, 1, 1, 5, 'Baby Peach Handler'),
(4, 49, 39, 13, 10, 'Heavy Tank'),
(5, 40, 13, 1, 1, 'Rosalina Drift'),
(1, 15, 2, 3, 12, 'Toad Scooter');

INSERT INTO build_ratings (build_id, user_id, score) VALUES
(1, 2, 5),
(1, 3, 4),
(2, 1, 4),
(3, 4, 5),
(4, 5, 2),
(5, 2, 5),
(6, 3, 3);

-- Rule: users cannot rate their own builds
CREATE TRIGGER no_self_rating_insert
BEFORE INSERT ON build_ratings
WHEN NEW.user_id = (SELECT user_id FROM builds WHERE build_id = NEW.build_id)
BEGIN
    SELECT RAISE(ABORT, 'Users cannot rate their own builds');
END;

CREATE TRIGGER no_self_rating_update
BEFORE UPDATE OF build_id, user_id ON build_ratings
WHEN NEW.user_id = (SELECT user_id FROM builds WHERE build_id = NEW.build_id)
BEGIN
    SELECT RAISE(ABORT, 'Users cannot rate their own builds');
END;

-- Combined stats for every build (calculated, not stored)
CREATE VIEW build_stats AS
SELECT
    b.build_id,
    dg.speed + bg.speed + tg.speed + g.speed AS speed_level,
    (dg.speed + bg.speed + tg.speed + g.speed + 3) / 4.0 AS speed_value,
    dg.acceleration + bg.acceleration + tg.acceleration + g.acceleration AS acceleration_level,
    (dg.acceleration + bg.acceleration + tg.acceleration + g.acceleration + 3) / 4.0 AS acceleration_value,
    dg.weight + bg.weight + tg.weight + g.weight AS weight_level,
    (dg.weight + bg.weight + tg.weight + g.weight + 3) / 4.0 AS weight_value,
    dg.handling + bg.handling + tg.handling + g.handling AS handling_level,
    (dg.handling + bg.handling + tg.handling + g.handling + 3) / 4.0 AS handling_value,
    dg.traction + bg.traction + tg.traction + g.traction AS traction_level,
    (dg.traction + bg.traction + tg.traction + g.traction + 3) / 4.0 AS traction_value,
    dg.mini_turbo + bg.mini_turbo + tg.mini_turbo + g.mini_turbo AS mini_turbo_level,
    (dg.mini_turbo + bg.mini_turbo + tg.mini_turbo + g.mini_turbo + 3) / 4.0 AS mini_turbo_value,
    dg.invincibility + bg.invincibility + tg.invincibility + g.invincibility AS invincibility_level,
    (dg.invincibility + bg.invincibility + tg.invincibility + g.invincibility + 3) / 4.0 AS invincibility_value
FROM builds b
JOIN drivers d        ON d.driver_id = b.driver_id
JOIN driver_groups dg ON dg.driver_group_id = d.driver_group_id
JOIN bodies bo        ON bo.body_id = b.body_id
JOIN body_groups bg   ON bg.body_group_id = bo.body_group_id
JOIN tires t          ON t.tire_id = b.tire_id
JOIN tire_groups tg   ON tg.tire_group_id = t.tire_group_id
JOIN gliders g        ON g.glider_id = b.glider_id;
