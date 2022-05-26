-- non so come metteremo queste cose nella presentazione
-- per ora metto le tabelle create in sql 
-- la mia idea è fare come ha fatto lui:
-- mettere le tabelle fatte in sql e le classi (o solo le intestazioni)

CREATE TABLE Modello(
	tipo VARCHAR(24) PRIMARY KEY, 
	marca VARCHAR(24),
	modello VARCHAR(24),
	costoOrario DECIMAL(2, 2),
	costoGiornaliero DECIMAL(2, 2)
);

CREATE TABLE Mezzo(
	numeroMatricola CHAR(7) PRIMARY KEY, 
	modello VARCHAR(24) REFERENCES Modello,
	tipologia VARCHAR(24) CHECK (tipologia IN ('bicicletta', 'bicicletta elettrica', 'scoter elettrico',
									 'scooter a benzina', 'monopattino elettrico')),
	stato VARCHAR(24) CHECK (stato IN ('disponibile', 'prenotato', 'noleggiato',
									 'guasto', 'inOperazione', 'radiato')),
	kmPercorsi DECIMAL(5,2),
	targa VARCHAR(12) UNIQUE,
	capacitaSerbatoio DECIMAL(2,2),
	litriPresenti DECIMAL(2),
	caricaBatterie SMALLINT
);

-- in tipo non metto 'cliente registrato' e 'cliente non registrato' perche si capisce dal
-- fatto se ha la password settata o meno
CREATE TABLE Utente(
	CF CHAR(16) PRIMARY KEY,
	tipo VARCHAR(24) CHECK (tipo IN ('amministratore', 'operatore', 'cliente')),
	password VARCHAR(32),
	mail VARCHAR(24),
	telefono CHAR(10),
	luogoNascita VARCHAR(32),
	dataNascita DATE,
	via VARCHAR(24),
	numero SMALLINT,
	CAP CHAR(5),
	cita VARCHAR(24),
	abilitato BOOL
);

CREATE TABLE Prenotazione(
	CFCliente CHAR(16) REFERENCES Utente,
	nrMatricolaMezzo CHAR(7) REFERENCES Mezzo,
	dataPrenotazione DATE, 
	dataRitiro TIMESTAMP,
	dataConsegnaPrevista TIMESTAMP,
	dataConsegnaEffettiva TIMESTAMP,
	PRIMARY KEY(CFCliente, nrMatricolaMezzo, dataRitiro)
);

CREATE TABLE Operazione(
	idOperazione SERIAL PRIMARY KEY,
	nrMatricolaMezzo CHAR(7) REFERENCES Mezzo,
	dataInizio DATE, 
	dataFine TIMESTAMP,
	tipoIntervento VARCHAR(50),
	costo DECIMAL (4,2),
	officina VARCHAR(24)
);

CREATE TABLE Attesa(
	idAttesa SERIAL PRIMARY KEY,
	CFCliente CHAR(16) REFERENCES Utente,
	modelloMezzo VARCHAR(24) REFERENCES Modello,
	dataInizioAttesa TIMESTAMP, 
	dataRitiroPrevista TIMESTAMP
);