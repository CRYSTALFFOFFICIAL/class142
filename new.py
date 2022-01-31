from flask import Flask, jsonify, request
import csv
from demographic import output

all_movies = []

with open('Movie_Recommendation.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie_route():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie_route():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch_route():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-movies")
def popular_route():
    movies = []
    for i in output:
        d = {
            "title":i[0],
            "poster_link": i[1],
            "release_date": i[2],
            "duration":  i[3],
            "rating": i[4],
            "overview": i[5]
        }
        movies.append(d)
    return jsonify({
        "data":movies,
        "status":"success"
    }),200

if __name__ == "__main__":
  app.run()