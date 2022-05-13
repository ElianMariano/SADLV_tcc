-- Create all the database tables
CREATE TABLE uf(
	uf   VARCHAR(2)  NOT NULL,
	nome VARCHAR(20) NOT NULL,
	CONSTRAINT pk_uf
		PRIMARY KEY (uf)
);

CREATE TABLE cidade(
	id_cidade INTEGER     NOT NULL,
	cidade    VARCHAR(40) NOT NULL,
	uf        VARCHAR(2)  NOT NULL,
	CONSTRAINT pk_cidade
		PRIMARY KEY (id_cidade),
	CONSTRAINT fk_uf
		FOREIGN KEY (uf)
		REFERENCES uf(uf)
);

CREATE TABLE profissional(
	cpf             VARCHAR(14)  NOT NULL,
	nome            VARCHAR(100) NOT NULL,
	nascimento      DATE         NOT NULL,
	email           VARCHAR(100) NOT NULL,
	bairro          VARCHAR(100) NOT NULL,
	cidade          INTEGER      NOT NULL,
	senha           VARCHAR(30)  NOT NULL,
	CONSTRAINT pk_profissional
		PRIMARY KEY (cpf),
	CONSTRAINT fk_cidade
		FOREIGN KEY (cidade)
		REFERENCES cidade(id_cidade)
);

CREATE TABLE paciente(
	cpf VARCHAR(14) NOT NULL,
	nome VARCHAR(100) NOT NULL,
	nascimento DATE NOT NULL,
	email     VARCHAR(100) NOT NULL,
	bairro VARCHAR(100) NOT NULL,
	cidade INTEGER NOT NULL,
	senha VARCHAR(30) NOT NULL,
	profissional VARCHAR(14) NOT NULL,
	CONSTRAINT pk_paciente
		PRIMARY KEY (cpf),
	CONSTRAINT fk_cidade
		FOREIGN KEY (cidade)
		REFERENCES cidade(id_cidade),
	CONSTRAINT fk_profissional
		FOREIGN KEY (profissional)
		REFERENCES profissional(cpf)
);

CREATE TABLE grupo(
	id_grupo INTEGER NOT NULL,
	titulo VARCHAR(30) NOT NULL,
	nivel VARCHAR(50) NOT NULL,
	CONSTRAINT pk_grupo
		PRIMARY KEY (id_grupo)
);

CREATE TABLE exercicio(
	id_exercicio INTEGER NOT NULL,
	exercicio VARCHAR(50) NOT NULL,
	dia DATE NOT NULL,
	CONSTRAINT pk_exercicio
		PRIMARY KEY (id_exercicio)
);

CREATE TABLE plano(
	id_plano INTEGER NOT NULL,
	paciente VARCHAR(14) NOT NULL,
	tipo VARCHAR(30) NOT NULL,
	observacao VARCHAR(300) NOT NULL,
	CONSTRAINT pk_plano
		PRIMARY KEY (id_plano),
	CONSTRAINT fk_paciente
		FOREIGN KEY (paciente)
		REFERENCES paciente(cpf)
);

CREATE TABLE plano_exercicio(
	id_plano_exercicio INTEGER NOT NULL,
	plano INTEGER NOT NULL,
	exercicio INTEGER NOT NULL,
	CONSTRAINT pk_plano_exercicio
		PRIMARY KEY (id_plano_exercicio),
	CONSTRAINT fk_plano
		FOREIGN KEY (plano)
		REFERENCES plano(id_plano),
	CONSTRAINT fk_exercicio
		FOREIGN KEY (exercicio)
		REFERENCES exercicio(id_exercicio)
);

CREATE TABLE tentativa(
	id_tentativa INTEGER NOT NULL,
	audio VARCHAR(100) NOT NULL,
	plano_exercicio INTEGER NOT NULL,
	dia DATE NOT NULL,
	acertou BOOLEAN,
	observacao VARCHAR(300),
	analise_preliminar VARCHAR(300),
	CONSTRAINT pk_tentativa
		PRIMARY KEY (id_tentativa),
	CONSTRAINT fk_plano_exercicio
		FOREIGN KEY (plano_exercicio)
		REFERENCES plano_exercicio(id_plano_exercicio)
);