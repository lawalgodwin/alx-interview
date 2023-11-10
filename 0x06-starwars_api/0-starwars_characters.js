#!/usr/bin/node

const request = require('request');
const promisify = require('util').promisify;

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';

request.get = promisify(request.get);

const getMovieID = () => {
  try {
    return process.argv[2];
  } catch (error) {
    console.error(error);
  }
};

const getFilmUrl = (modieID) => {
  try {
    const movieId = parseInt(modieID);
    return `${baseUrl}${movieId}`;
  } catch (e) {
    console.error(e);
  }
};

const getMovieData = async (modieID) => {
  const filmUrl = getFilmUrl(modieID);
  try {
    const movideData = await request.get(filmUrl);
    return (JSON.parse(movideData.body));
  } catch (error) {
    console.error(error);
  }
};

const getMovieCharacters = async (movieId) => {
  const data = await getMovieData(movieId);
  for (const link of data.characters) {
    const subData = await request.get(`${link}`);
    console.log(JSON.parse(subData.body).name);
  }
};

const movieID = getMovieID();
getMovieCharacters(movieID);
