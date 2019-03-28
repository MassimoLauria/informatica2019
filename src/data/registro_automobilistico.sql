-- Registro automobilistico


create table Veicoli (
       Targa            nvarchar(10) primary key,
       Cilindrata       integer,
       Cavalli_Fiscali  integer,
       Velocità         integer,
       Posti            integer,
       Immatricolazione date,

       Cod_Categoria      nchar(2) references Categorie(Cod_Categoria),
       Cod_Combustibile   nchar(2) references Combustibili(Cod_Combustibile),
       Cod_Modello        nchar(3) references Modelli(Cod_Modello)
);

insert into Veicoli(Targa,Cilindrata,Cavalli_Fiscali,
                    Velocità, Posti, Immatricolazione,
                    Cod_Categoria, Cod_Combustibile, Cod_Modello) values
       ('A123456X', 1796, 85, 195,  5, '1998-12-30', '01', '01', '004'),
       ('B256787Y', 708,  10, 120,  5, '1989-09-21', '01', '02', '001'),
       ('C76589AG', 1106, 54, 130,  5, '1998-08-13', '01', '01', '001'),
       ('C78905GT', 1998, 117, 212, 4, '1994-11-06', '01', '01', '009'),
       ('C845905Z', NULL,NULL,NULL, 3, '1995-04-11', '04', '03', '006'),
       ('CFT340VB', 1390, 75, 170,  5, '1995-01-12', '01', '02', '007'),
       ('D239765W', NULL,NULL,NULL, 2, '1997-08-12', '03', '01', '002'),
       ('DD4567XX', 1581, 17, NULL, 5, '1997-06-05', '01', '01', '003'),
       ('DGH789JC', 1590, 114, 170, 5, '1995-10-05', '01', '02', '014'),
       ('DH79567H', 1589, 107, 170, 5, NULL,         '01', '04', '011'),
       ('ERG567NM', 1598, 107, 175, 5, '1997-12-18', '01', '04', '013'),
       ('F96154NH', 1781, 125, 185, 5, '1992-03-08', '01', '03', '010'),
       ('FGH673FV', 899, 39, 140,   5, '1998-08-09', '01', '01', '012'),
       ('XCH56GJK', 1918, 110, 210, 5, '1998-09-04', '01', '01', '005'),
       ('XF5789CY', 1587, 107, 175, 5, '1996-05-05', '01', '01', '008');


create table Categorie (
       Cod_Categoria  nchar(2) primary key,
       Nome_Categoria nvarchar(30)
);

insert into Categorie values
       ('01','Autovettura'),
       ('02','Rimorchio'),
       ('03','Motociclo'),
       ('04','Furgone');

create table Combustibili (
       Cod_Combustibile nchar(2) primary key,
       Descrizione_Combustibile nvarchar(30)
);


insert into Combustibili values
       ('01', 'Benzina'),
       ('02', 'Gasolio'),
       ('03', 'GPL'),
       ('04', 'Metano');

create table Modelli (
       Cod_Modello  nchar(3) primary key,
       Nome_Modello nvarchar(30),
       Cod_Fabbrica  nchar(3) references Fabbriche(Cod_Fabbrica),
       Numero_Versioni integer
);

insert into Modelli values
       ('001','Panda','001',3),
       ('002','Vespa','004',4),
       ('003','Brava','001',2),
       ('004','Mondeo','003',3),
       ('005','V-10','005',2),
       ('006','Ducato','001',5),
       ('007','Clio','006',5),
       ('008','Corolla','007',4),
       ('009','Coupè','001',1),
       ('010','Golf','008',4),
       ('011','Megane','006',2),
       ('012','Seicento','001',2),
       ('013','Laguna','006',2),
       ('014','Civic','009',3);




create table Fabbriche (
       Cod_Fabbrica   nchar(3) primary key,
       Nome_Fabbrica  nvarcvhar(30)
);

insert into Fabbriche values
       ('001','Fiat'),
       ('003','Ford'),
       ('004','Piaggio'),
       ('005','Volvo'),
       ('006','Renault'),
       ('007','Toyota'),
       ('008','Volkswagen'),
       ('009','Honda');


create table Proprietari (
       Cod_Proprietario nchar(5) primary key,
       Cognome nvarchar(30),
       Nome    nvarchar(30),
       Indirizzo nvarchar(30),
       Provincia nchar(30)
);

insert into Proprietari values
       ('00001', 'Lucchini','Valentina','Viale Pavia, 3','LO'),
       ('00002', 'Farese','Giulia','Viale Italia, 9','LO'),
       ('00003', 'Giovanolla','Filippo','Via G.Galilei, 4','LO'),
       ('00004', 'Spoldi','Diego','Via Croce, 12','LO'),
       ('00005', 'Spoldi','Simona','Via S.Angelo, 11','LO'),
       ('00006', 'Bernocchi','Giuseppina','Via Pascoli, 1','LO'),
       ('00007', 'Cottarelli','Cristian','Via Cannero, 18','MI');


create table Proprietà (
       Targa nvarchar(10) references Veicolo(Targa),
       Cod_Proprietario nchar(5) references Proprietari(Cod_Proprietario),
       Data_Acquisto date,
       Data_Cessione date,
       primary key (Targa,Cod_Proprietario)
);

insert into Proprietà values
       ('A123456X','00001','1994/6/20','2001/12/13'),
       ('B256787Y','00001','1996/4/20','2001/7/12'),
       ('C76589AG','00002','1999/7/31','2003/5/27'),
       ('F5789CY', '00002','2000/1/25','2005/12/13'),
       ('C78905GT','00003','1994/6/23','2003/2/17'),
       ('C845905Z','00003','1993/11/30','2001/1/6'),
       ('CFT340VB','00004','1996/9/16','2002/8/31'),
       ('D239765W','00004','1998/6/20','2005/5/25'),
       ('DD4567XX','00005','1994/6/9','2003/12/13'),
       ('DGH789JC','00005','1994/5/21','2003/5/28'),
       ('DH79567H','00006','1990/9/16','2007/12/16'),
       ('ERG567NM','00006','1999/10/11','2007/5/23'),
       ('F96154NH','00007','2000/3/15','2008/9/16'),
       ('FGH673FV','00007','1995/2/28','2005/12/25'),
       ('XCH56GJX','00004','1994/2/29','2001/4/13');


