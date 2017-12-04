def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    "Return one row from a cursor as a dict"
    return dictfetchall(cursor)[0]

def listfetchall(cursor):
    "Return list of the first entry in each row from a cursor (eg. for getting list of ids)"
    return [row[0] for row in cursor.fetchall()]