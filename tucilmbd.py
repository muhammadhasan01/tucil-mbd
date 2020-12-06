import psycopg2
host = "SG-tucilmbd-1357-pgsql-master.servers.mongodirector.com" # ganti dengan host masing-masing
matkul = "mbd"
point = 0

# Modul 1
def test1():
	db = psycopg2.connect(dbname=matkul, host=host, user="mahasiswa", password=matkul)
	cursor = db.cursor()
	try:
		cursor.execute('SELECT * FROM penilaian')
		cursor.execute("commit")
	except:
		cursor.execute("rollback")
	cursor.execute('SELECT nim, nama FROM penilaian')
	print(cursor.fetchone())

# Modul 2
def test2():
	db = psycopg2.connect(dbname=matkul, host=host, user="dosen", password=matkul)
	cursor = db.cursor()
	cursor.execute("SELECT * FROM information_schema.role_table_grants WHERE table_name='penilaian'")
	for data in cursor.fetchall():
		print(data)
	print()
	cursor.execute("SELECT r.rolname, r.rolinherit, r.rolcreaterole, r.rolcanlogin,\
  	ARRAY(SELECT b.rolname \
		FROM pg_catalog.pg_auth_members m \
		JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid) \
		WHERE m.member = r.oid) as memberof \
	FROM pg_catalog.pg_roles r \
	WHERE r.rolname NOT LIKE 'pg%%'  \
	ORDER BY 1")
	for data in cursor.fetchall():
		print(data)

test1()
test2()