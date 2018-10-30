#! /usr/bin/env python3

import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

cursor.execute(

	"SELECT articles.title, COUNT(log.path) FROM log INNER JOIN articles ON log.path LIKE '%' || articles.slug GROUP BY articles.title ORDER BY COUNT(log.path) DESC LIMIT 3")

print('Most Popular Articles: \n')

for results in cursor.fetchall():

	print('Article: ', results[0])
	print('Amount of Views: ', results[1])

cursor.execute(

	"SELECT name, COUNT(log.path) FROM authors, log, articles WHERE authors.id = articles.author AND log.path LIKE '%' || articles.slug GROUP BY authors.name ORDER BY COUNT(log.path) DESC")

print('\n Most Popular Authors: \n')

for results in cursor.fetchall():

	print('Author: ', results[0])
	print('Amount of Views: ', results[1])

cursor.execute(

	"SELECT requests.date, total_requests, error_requests FROM (SELECT DATE_TRUNC('day', time) AS date, COUNT(*) AS total_requests FROM log GROUP BY date) AS requests, (SELECT DATE_TRUNC('day', time) AS date, COUNT(*) AS error_requests FROM log WHERE status NOT LIKE '2%' GROUP BY date) AS errors WHERE requests.date = errors.date ORDER BY requests.date DESC;")

for results in cursor.fetchall():

	PercentError = float(results[2]) / float(results[1]) * 100 

	if PercentError > 1.0: 
		print('\n Date(s) >1% of requests led to errors: \n')
		print('Date', str(results[0])[:10])
		print('Percent of errors: ', round(PercentError,1))

db.close()