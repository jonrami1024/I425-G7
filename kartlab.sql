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
(1, 'Baby Peach', 1, 'images/drivers/baby_peach.png'),
(2, 'Baby Daisy', 1, 'images/drivers/baby_daisy.png'),
(3, 'Baby Rosalina', 2, 'images/drivers/baby_rosalina.png'),
(4, 'Lemmy', 2, 'images/drivers/lemmy.png'),
(5, 'Baby Mario', 3, 'images/drivers/baby_mario.png'),
(6, 'Baby Luigi', 3, 'images/drivers/baby_luigi.png'),
(7, 'Dry Bones', 3, 'images/drivers/dry_bones.png'),
(8, 'Mii (Light)', 3, 'images/drivers/mii_light.png'),
(9, 'Koopa Troopa', 4, 'images/drivers/koopa_troopa.png'),
(10, 'Lakitu', 4, 'images/drivers/lakitu.png'),
(11, 'Bowser Jr.', 4, 'images/drivers/bowser_jr.png'),
(12, 'Toadette', 5, 'images/drivers/toadette.png'),
(13, 'Wendy', 5, 'images/drivers/wendy.png'),
(14, 'Isabelle', 5, 'images/drivers/isabelle.png'),
(15, 'Toad', 6, 'images/drivers/toad.png'),
(16, 'Shy Guy', 6, 'images/drivers/shy_guy.png'),
(17, 'Larry', 6, 'images/drivers/larry.png'),
(18, 'Cat Peach', 7, 'images/drivers/cat_peach.png'),
(19, 'Inkling Girl', 7, 'images/drivers/inkling_girl.png'),
(20, 'Villager (Female)', 7, 'images/drivers/villager_female.png'),
(21, 'Diddy Kong', 7, 'images/drivers/diddy_kong.png'),
(22, 'Peach', 8, 'images/drivers/peach.png'),
(23, 'Daisy', 8, 'images/drivers/daisy.png'),
(24, 'Yoshi', 8, 'images/drivers/yoshi.png'),
(25, 'Birdo', 8, 'images/drivers/birdo.png'),
(26, 'Peachette', 8, 'images/drivers/peachette.png'),
(27, 'Tanooki Mario', 9, 'images/drivers/tanooki_mario.png'),
(28, 'Inkling Boy', 9, 'images/drivers/inkling_boy.png'),
(29, 'Villager (Male)', 9, 'images/drivers/villager_male.png'),
(30, 'Mario', 10, 'images/drivers/mario.png'),
(31, 'Ludwig', 10, 'images/drivers/ludwig.png'),
(32, 'Mii (Medium)', 10, 'images/drivers/mii_medium.png'),
(33, 'Luigi', 11, 'images/drivers/luigi.png'),
(34, 'Iggy', 11, 'images/drivers/iggy.png'),
(35, 'Kamek', 11, 'images/drivers/kamek.png'),
(36, 'Metal Mario', 12, 'images/drivers/metal_mario.png'),
(37, 'Gold Mario', 12, 'images/drivers/gold_mario.png'),
(38, 'Pink Gold Peach', 12, 'images/drivers/pink_gold_peach.png'),
(39, 'Wiggler', 13, 'images/drivers/wiggler.png'),
(40, 'Rosalina', 14, 'images/drivers/rosalina.png'),
(41, 'King Boo', 14, 'images/drivers/king_boo.png'),
(42, 'Link', 14, 'images/drivers/link.png'),
(43, 'Link (BotW)', 14, 'images/drivers/link_botw.png'),
(44, 'Pauline', 14, 'images/drivers/pauline.png'),
(45, 'Petey Piranha', 15, 'images/drivers/petey_piranha.png'),
(46, 'Waluigi', 16, 'images/drivers/waluigi.png'),
(47, 'Donkey Kong', 16, 'images/drivers/donkey_kong.png'),
(48, 'Roy', 16, 'images/drivers/roy.png'),
(49, 'Wario', 17, 'images/drivers/wario.png'),
(50, 'Dry Bowser', 17, 'images/drivers/dry_bowser.png'),
(51, 'Funky Kong', 17, 'images/drivers/funky_kong.png'),
(52, 'Mii (Heavy)', 17, 'images/drivers/mii_heavy.png'),
(53, 'Bowser', 18, 'images/drivers/bowser.png'),
(54, 'Morton', 18, 'images/drivers/morton.png');

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
(1, 'Biddybuggy', 'Kart', 1, 'images/bodies/biddybuggy.png'),
(2, 'Mr. Scooty', 'Standard Bike', 1, 'images/bodies/mr_scooty.png'),
(3, 'Streetle', 'Kart', 2, 'images/bodies/streetle.png'),
(4, 'Landship', 'Kart', 3, 'images/bodies/landship.png'),
(5, 'Pipe Frame', 'Kart', 4, 'images/bodies/pipe_frame.png'),
(6, 'Varmint', 'Standard Bike', 5, 'images/bodies/varmint.png'),
(7, 'City Tripper', 'Standard Bike', 5, 'images/bodies/city_tripper.png'),
(8, 'Cat Cruiser', 'Kart', 6, 'images/bodies/cat_cruiser.png'),
(9, 'Comet', 'Sport Bike', 6, 'images/bodies/comet.png'),
(10, 'Yoshi Bike', 'Sport Bike', 7, 'images/bodies/yoshi_bike.png'),
(11, 'Teddy Buggy', 'ATV', 8, 'images/bodies/teddy_buggy.png'),
(12, 'W 25 Silver Arrow', 'Kart', 9, 'images/bodies/w_25_silver_arrow.png'),
(13, 'Wild Wiggler', 'ATV', 9, 'images/bodies/wild_wiggler.png'),
(14, 'Standard Bike', 'Standard Bike', 9, 'images/bodies/standard_bike.png'),
(15, 'Flame Rider', 'Standard Bike', 9, 'images/bodies/flame_rider.png'),
(16, 'Mach 8', 'Kart', 10, 'images/bodies/mach_8.png'),
(17, 'Sports Coupe', 'Kart', 10, 'images/bodies/sports_coupe.png'),
(18, 'Inkstriker', 'ATV', 11, 'images/bodies/inkstriker.png'),
(19, 'Tanooki Kart', 'Kart', 12, 'images/bodies/tanooki_kart.png'),
(20, 'Koopa Clown', 'Kart', 13, 'images/bodies/koopa_clown.png'),
(21, 'Master Cycle Zero', 'Standard Bike', 13, 'images/bodies/master_cycle_zero.png'),
(22, '300 SL Roadster', 'Kart', 14, 'images/bodies/300_sl_roadster.png'),
(23, 'Standard Kart', 'Kart', 15, 'images/bodies/standard_kart.png'),
(24, 'The Duke', 'Standard Bike', 15, 'images/bodies/the_duke.png'),
(25, 'Blue Falcon', 'Kart', 16, 'images/bodies/blue_falcon.png'),
(26, 'Splat Buggy', 'ATV', 17, 'images/bodies/splat_buggy.png'),
(27, 'Prancer', 'Kart', 18, 'images/bodies/prancer.png'),
(28, 'Sport Bike', 'Sport Bike', 19, 'images/bodies/sport_bike.png'),
(29, 'Jet Bike', 'Sport Bike', 19, 'images/bodies/jet_bike.png'),
(30, 'Sneeker', 'Kart', 20, 'images/bodies/sneeker.png'),
(31, 'Gold Standard', 'Kart', 21, 'images/bodies/gold_standard.png'),
(32, 'Master Cycle', 'Sport Bike', 22, 'images/bodies/master_cycle.png'),
(33, 'Steel Driver', 'Kart', 23, 'images/bodies/steel_driver.png'),
(34, 'Tri-Speeder', 'Kart', 23, 'images/bodies/tri_speeder.png'),
(35, 'Bone Rattler', 'ATV', 24, 'images/bodies/bone_rattler.png'),
(36, 'Circuit Special', 'Kart', 25, 'images/bodies/circuit_special.png'),
(37, 'B Dasher', 'Kart', 25, 'images/bodies/b_dasher.png'),
(38, 'P-Wing', 'Kart', 25, 'images/bodies/p_wing.png'),
(39, 'Badwagon', 'Kart', 26, 'images/bodies/badwagon.png'),
(40, 'GLA', 'Kart', 26, 'images/bodies/gla.png'),
(41, 'Standard ATV', 'ATV', 27, 'images/bodies/standard_atv.png');

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
(1, 'Roller', 1, 'images/tires/roller.png'),
(2, 'Azure Roller', 1, 'images/tires/azure_roller.png'),
(3, 'Button', 2, 'images/tires/button.png'),
(4, 'Leaf Tires', 2, 'images/tires/leaf_tires.png'),
(5, 'Cushion', 3, 'images/tires/cushion.png'),
(6, 'Sponge', 4, 'images/tires/sponge.png'),
(7, 'GLA Tires', 5, 'images/tires/gla_tires.png'),
(8, 'Standard', 6, 'images/tires/standard.png'),
(9, 'Blue Standard', 6, 'images/tires/blue_standard.png'),
(10, 'Slim', 7, 'images/tires/slim.png'),
(11, 'Crimson Slim', 7, 'images/tires/crimson_slim.png'),
(12, 'Wood', 7, 'images/tires/wood.png'),
(13, 'Monster', 8, 'images/tires/monster.png'),
(14, 'Hot Monster', 8, 'images/tires/hot_monster.png'),
(15, 'Ancient Tires', 9, 'images/tires/ancient_tires.png'),
(16, 'Off-Road', 10, 'images/tires/off_road.png'),
(17, 'Retro Off-Road', 10, 'images/tires/retro_off_road.png'),
(18, 'Triforce Tires', 10, 'images/tires/triforce_tires.png'),
(19, 'Slick', 11, 'images/tires/slick.png'),
(20, 'Cyber Slick', 11, 'images/tires/cyber_slick.png'),
(21, 'Metal', 12, 'images/tires/metal.png'),
(22, 'Gold Tires', 13, 'images/tires/gold_tires.png');

INSERT INTO gliders (glider_id, name, image_file, speed, acceleration, weight, handling, traction, mini_turbo, invincibility) VALUES
(1, 'Cloud Glider', 'images/gliders/cloud_glider.png', 0, 2, 0, 1, 1, 2, 0),
(2, 'Parachute', 'images/gliders/parachute.png', 0, 2, 0, 1, 1, 2, 0),
(3, 'Flower Glider', 'images/gliders/flower_glider.png', 0, 2, 0, 1, 1, 2, 0),
(4, 'Paper Glider', 'images/gliders/paper_glider.png', 0, 2, 0, 1, 1, 2, 0),
(5, 'Peach Parasol', 'images/gliders/peach_parasol.png', 0, 2, 1, 1, 0, 2, 0),
(6, 'Parafoil', 'images/gliders/parafoil.png', 0, 2, 1, 1, 0, 2, 0),
(7, 'Bowser Kite', 'images/gliders/bowser_kite.png', 0, 2, 1, 1, 0, 2, 0),
(8, 'MKTV Parafoil', 'images/gliders/mktv_parafoil.png', 0, 2, 1, 1, 0, 2, 0),
(9, 'Wario Wing', 'images/gliders/wario_wing.png', 1, 1, 2, 1, 0, 1, 1),
(10, 'Plane Glider', 'images/gliders/plane_glider.png', 1, 1, 2, 1, 0, 1, 1),
(11, 'Gold Glider', 'images/gliders/gold_glider.png', 1, 1, 2, 1, 0, 1, 1),
(12, 'Paraglider', 'images/gliders/paraglider.png', 1, 1, 2, 1, 0, 1, 1),
(13, 'Super Glider', 'images/gliders/super_glider.png', 1, 1, 1, 1, 1, 1, 1),
(14, 'Waddle Wing', 'images/gliders/waddle_wing.png', 1, 1, 1, 1, 1, 1, 1),
(15, 'Hylian Kite', 'images/gliders/hylian_kite.png', 1, 1, 1, 1, 1, 1, 1);

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
