CREATE TABLE Team (
  team_id INT PRIMARY KEY,
  team_name VARCHAR(30),
  mascot VARCHAR(30)
);
CREATE TABLE Player (
  player_id INT PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  team_id INT,
  FOREIGN KEY (team_id) REFERENCES Team(team_id)
);