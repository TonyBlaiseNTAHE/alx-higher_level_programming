-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name 'genre', COUNT(tv_shows.id) 'number_of_shows' FROM tv_show_genres LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC; 
