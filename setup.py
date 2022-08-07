from requirements.functions import sql_connect

conn = sql_connect('requirements')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS "magazin" (
	"son"	INTEGER,
	"type"	TEXT,
	"from"	INTEGER,
	"title"	TEXT,
	"amount"	INTEGER,
	"soum_price"	INTEGER,
	"currency"	TEXT,
	"selled"	INTEGER,
	"game_type"	TEXT,
	"photo"	TEXT,
	"status"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "qiwi_payments" (
	"son"	INTEGER,
	"payment_id"	TEXT,
	"telegram_id"	TEXT,
	"account"	TEXT,
	"amount"	TEXT,
	"comment"	TEXT,
	"sana"	TEXT,
	"soum_amount"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "rubl_kursi" (
	"son"	INTEGER,
	"kurs"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "selled_history" (
	"son"	INTEGER,
	"user_id"	INTEGER,
	"amount"	INTEGER,
	"price"	TEXT,
	"currency"	TEXT,
	"sended"	TEXT,
	"payed_status"	TEXT,
	"game_id"	TEXT,
	"sana"	TEXT,
	"keshbek"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "send_users" (
	"son"	INTEGER,
	"user_id"	INTEGER,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "settings" (
	"son"	INTEGER,
	"type"	TEXT,
	"status"	TEXT,
	"item1"	TEXT,
	"item2"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "users" (
	"son"	INTEGER,
	"user_id"	TEXT,
	"rubl_money"	TEXT,
	"soum_money"	TEXT,
	"soat"	TEXT,
	"sana"	TEXT,
	"mobile_number"	TEXT,
	"lang"	TEXT,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS "uzcard_payments" (
	"son"	INTEGER,
	"user_id"	INTEGER,
	"uzcard_number"	INTEGER,
	"cheque_id"	TEXT,
	"amount"	INTEGER,
	"sana"	INTEGER,
	PRIMARY KEY("son" AUTOINCREMENT)
);""")

check_uzcard = cur.execute("SELECT * FROM settings WHERE `type`='uzcard_auto'").fetchone()
check_qiwi = cur.execute("SELECT * FROM settings WHERE `type`='qiwi_auto'").fetchone()
check_magazin = cur.execute("SELECT * FROM settings WHERE `type`='magazin'").fetchone()
check_kurs = cur.execute("SELECT * FROM rubl_kursi").fetchone()
check_keshbek = cur.execute("SELECT * FROM settings WHERE `type`='keshbek'").fetchone()
check_keshbek_foiz = cur.execute("SELECT * FROM settings WHERE `type`='keshbek_foiz'").fetchone()

if not check_uzcard:
    cur.execute("INSERT INTO settings (type, status) VALUES ('uzcard_auto', 'yoniq')")
if not check_qiwi:
    cur.execute("INSERT INTO settings (type, status) VALUES ('qiwi_auto', 'yoniq')")
if not check_magazin:
    cur.execute("INSERT INTO settings (type, status) VALUES ('magazin', 'yoniq')")
if not check_kurs:
    cur.execute("INSERT INTO rubl_kursi (kurs) VALUES ('140')")
if not check_keshbek:
    cur.execute("INSERT INTO settings (type, status) VALUES ('keshbek', 'yoniq')")
if not check_keshbek_foiz:
    cur.execute("INSERT INTO settings (type, status) VALUES ('keshbek_foiz', '1')")

conn.commit()
conn.close()