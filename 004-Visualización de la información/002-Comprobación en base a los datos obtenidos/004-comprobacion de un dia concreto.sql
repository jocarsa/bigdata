SELECT strftime('%Y-%m-%d', datetime(utc, 'unixepoch')) AS dia,*
           
    FROM registros
	WHERE dia LIKE '2022-12-01'
    
    ORDER BY dia