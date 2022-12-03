-- SQLite
DROP TABLE transactions




Create table transactions (
    transactionid INTEGER Primary Key AUTOINCREMENT,
    accountid integer,
    amount real NOT NULL
);