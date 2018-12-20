#! /usr/bin/env python3

import psycopg2

try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Error: could not connect to news database.")

cursor = db.cursor()

cursor.execute(

    """SELECT articles.title, COUNT(log.path)
            FROM log
                INNER JOIN articles ON log.path
                LIKE '%' || articles.slug
                GROUP BY articles.title
                ORDER BY COUNT(log.path)
                DESC LIMIT 3""")

print('Most Popular Articles: \n')

for article, views in cursor.fetchall():

    print('Article: ', article)
    print('Amount of Views: ', views)

cursor.execute(

    """SELECT name, COUNT(log.path)
            FROM authors, log, articles
                WHERE authors.id = articles.author
                AND log.path LIKE '%' || articles.slug
                GROUP BY authors.name
                ORDER BY COUNT(log.path) DESC""")

print('\n Most Popular Authors: \n')

for author, views in cursor.fetchall():

    print('Author: ', author)
    print('Amount of Views: ', views)

cursor.execute(

    """SELECT TO_CHAR(requests.date, 'Mon DD, YYYY'),
                     (error_requests * 100 / total_requests)
            FROM (SELECT DATE_TRUNC('day', time) AS date,
                         COUNT(*) AS total_requests
                FROM log GROUP BY date) AS requests,
                (SELECT DATE_TRUNC('day', time) AS date,
                        COUNT(*) AS error_requests
                FROM log WHERE status NOT LIKE '2%' GROUP BY date) AS errors
                WHERE requests.date = errors.date
                AND error_requests * 100 / total_requests > 1.0;""")

print('\n Date(s) >1% of requests led to errors: \n')

for date, percentErrors in cursor.fetchall():
    print('Date: ', date)
    print('Percent of errors: ', percentErrors)

db.close()
