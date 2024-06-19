-- lists all genres in the database by their rating
SELECT tv_genres.name, SUM(rate) AS rating FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;