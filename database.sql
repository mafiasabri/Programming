BEGIN TRANSACTION;
CREATE TABLE "NS-Reizigers" (
	`Reizigers-ID`	INTEGER,
	`Naam`	TEXT,
	`OV-nummer`	INTEGER,
	`Beginstation`	TEXT,
	`Eindstation`	TEXT
);
COMMIT;
