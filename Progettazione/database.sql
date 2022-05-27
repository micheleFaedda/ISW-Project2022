-- non so come metteremo queste cose nella presentazione
-- per ora metto le tabelle create in sql 
-- la mia idea è fare come ha fatto lui:
-- mettere le tabelle fatte in sql e le classi (o solo le intestazioni)

CREATE TABLE Modello(
	tipo VARCHAR(24) PRIMARY KEY, 
	marca VARCHAR(24) NOT NULL,
	tipologiaModello VARCHAR(24) NOT NULL,
	costoOrario DECIMAL(2, 2) NOT NULL,
	costoGiornaliero DECIMAL(2, 2) NOT NULL
);

CREATE TABLE Mezzo(
	numeroMatricola CHAR(7) PRIMARY KEY, 
	modello VARCHAR(24) NOT NULL REFERENCES Modello,
	tipologia VARCHAR(24) CHECK (tipologia IN ('bicicletta', 'bicicletta elettrica', 'scoter elettrico',
									 'scooter a benzina', 'monopattino elettrico')),
	stato VARCHAR(24) NOT NULL CHECK (stato IN ('disponibile', 'prenotato', 'noleggiato',
									 'guasto', 'inOperazione', 'radiato')),
	kmPercorsi DECIMAL(5,2) NOT NULL,
	targa VARCHAR(12) UNIQUE ,
	capacitaSerbatoio DECIMAL(2,2),
	litriPresenti DECIMAL(2),
	caricaBatterie SMALLINT
);

-- in tipo non metto 'cliente registrato' e 'cliente non registrato' perche si capisce dal
-- fatto se ha la password settata o meno
CREATE TABLE Utente(
	CF CHAR(16) PRIMARY KEY,
	nome VARCHAR(16) NOT NULL,
	cognome VARCHAR(16) NOT NULL,
	tipo VARCHAR(24) NOT NULL CHECK (tipo IN ('amministratore', 'operatore', 'cliente')),
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
	dataPrenotazione DATE NOT NULL, 
	dataRitiro TIMESTAMP,
	dataConsegnaPrevista TIMESTAMP NOT NULL,
	dataConsegnaEffettiva TIMESTAMP,
	PRIMARY KEY(CFCliente, nrMatricolaMezzo, dataRitiro)
);

CREATE TABLE Operazione(
	idOperazione SERIAL PRIMARY KEY,
	nrMatricolaMezzo CHAR(7) NOT NULL REFERENCES Mezzo,
	dataInizio DATE NOT NULL, 
	dataFine TIMESTAMP,
	tipoIntervento VARCHAR(50) CHECK (tipoIntervento in ('manutenzione', 'riparazione')),
	descizioneOperazione VARCHAR(100),
	costo DECIMAL (4,2),
	officina VARCHAR(24) NOT NULL
);

CREATE TABLE Attesa(
	idAttesa SERIAL PRIMARY KEY,
	CFCliente CHAR(16) NOT NULL REFERENCES Utente,
	modelloMezzo VARCHAR(24) NOT NULL REFERENCES Modello,
	dataInizioAttesa TIMESTAMP NOT NULL, 
	dataRitiroPrevista TIMESTAMP NOT NULL,
	dataConsegnaPrevista TIMESTAMP NOT NULL
);