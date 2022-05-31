-- non so come metteremo queste cose nella presentazione
-- per ora metto le tabelle create in sql 
-- la mia idea è fare come ha fatto lui:
-- mettere le tabelle fatte in sql e le classi (o solo le intestazioni)

CREATE TABLE StrutturaNoleggio(
	IBAN CHAR(27) PRIMARY KEY,
	via VARCHAR(24),
	numero SMALLINT,
	CAP CHAR(5),
	cita VARCHAR(24),
	ragioneSociale VARCHAR(50)
);


CREATE TABLE Modello(
	idModello SERIAL PRIMARY KEY,
	tipologia VARCHAR(24) NOT NULL CHECK (tipologia IN ('bicicletta', 'bicicletta elettrica', 'scoter elettrico',
									 'scooter a benzina', 'monopattino elettrico')),
	marca VARCHAR(24) NOT NULL,
	tipoModello VARCHAR(24) NOT NULL,
	costoOrario DECIMAL(2, 2) NOT NULL,
	costoGiornaliero DECIMAL(2, 2) NOT NULL
);

CREATE TABLE Mezzo(
	numeroMatricola CHAR(7) PRIMARY KEY, 
	modello INTEGER NOT NULL REFERENCES Modello,
	stato VARCHAR(24) NOT NULL CHECK (stato IN ('disponibile', 'prenotato', 'noleggiato',
									 'guasto', 'inOperazione', 'radiato')),
	kmPercorsi DECIMAL(5,2),
	oreNoleggio DECIMAL(5,2),
	targa VARCHAR(12) UNIQUE,
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
	noleggio CHAR(27) REFERENCES StrutturaNoleggio,
	abilitato BOOL
);

CREATE TABLE Sconto(
	codSconto SERIAL PRIMARY KEY,
	modello INTEGER NOT NULL REFERENCES Modello,
	dataInizio DATE NOT NULL,
	percentuale SMALLINT,
	dataFine DATE NOT NULL
);

CREATE TABLE Prenotazione(
	idPrenotazione SERIAL PRIMARY KEY,
	CFCliente CHAR(16) REFERENCES Utente,
	nrMatricolaMezzo CHAR(7) REFERENCES Mezzo,
	dataPrenotazione DATE NOT NULL, 
	dataRitiro TIMESTAMP NOT NULL,
	dataConsegnaPrevista TIMESTAMP NOT NULL,
	dataConsegnaEffettiva TIMESTAMP,
	codiceSconto INTEGER REFERENCES Sconto
);

CREATE TABLE Pagamento(
	idPagamento SERIAL PRIMARY KEY,
	idPrenotazione INTEGER REFERENCES Prenotazione NOT NULL,
	importo DECIMAL(4,2) CHECK (importo > 0) NOT NULL,
	casuale VARCHAR(20) NOT NULL,
	descrizione VARCHAR(200)
);

CREATE TABLE Fattura(
	idPagamento INTEGER PRIMARY KEY REFERENCES Pagamento,
	protocollo VARCHAR(24) NOT NULL,
	nomeFile VARCHAR(32) NOT NULL,
	dataEmissione DATE NOT NULL
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

CREATE TABLE ClienteInAttesa(
	idAttesa SERIAL PRIMARY KEY,
	CFCliente CHAR(16) NOT NULL REFERENCES Utente,
	modelloMezzo SERIAL NOT NULL REFERENCES Modello,
	dataInizioAttesa TIMESTAMP NOT NULL, 
	dataRitiroPrevista TIMESTAMP NOT NULL,
	dataConsegnaPrevista TIMESTAMP NOT NULL
);