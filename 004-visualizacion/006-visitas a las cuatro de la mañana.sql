SELECT strftime('%H', datetime(utc, 'unixepoch')) AS hora,*
           
    FROM registros
	WHERE hora LIKE '%04%'
    