// Add your JavaScript code here

let selectedMovie = null;

// Function to fetch movie data from the backend API and display results
function findMovies() {
    const query = document.getElementById('movie-search-box').value.trim();

    if (query.length > 0) {
        const apiUrl = '/search-movies?query=' + encodeURIComponent(query);
        fetch(apiUrl)
            .then((response) => response.json())
            .then((data) => {
                displayMovieResults(data);
            })
            .catch((error) => {
                displayErrorMessage();
                console.error('Error fetching data:', error);
            });
    } else {
        clearMovieResults();
    }
}

// Function to display movie results
function displayMovieResults(data) {
    const movieGrid = document.getElementById('result-grid');
    movieGrid.innerHTML = '';

    if (data.results.length > 0) {
        data.results.forEach((movie) => {
            const movieItem = createMovieItem(movie);
            movieGrid.appendChild(movieItem);

            // Add click event listener to each movie item
            movieItem.addEventListener('click', () => {
                selectedMovie = movie;
                displaySelectedMovie();
            });
        });
    } else {
        displayErrorMessage();
    }
}

// Function to create a movie item element
function createMovieItem(movie) {
    // Create the elements for the movie item
    const movieItem = document.createElement('div');
    movieItem.classList.add('col-md-3', 'mt-2', 'mb-3'); // Add Bootstrap classes
    const card = document.createElement('div');
    card.classList.add('card', 'h-100');

    const moviePoster = document.createElement('img');
    moviePoster.classList.add('card-img-top');
    moviePoster.src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
    moviePoster.alt = 'Movie Poster';

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body', 'd-flex', 'flex-column');

    const cardTitleLink = document.createElement('a');
    cardTitleLink.href = `/movie/${movie.id}`; 

    const cardTitle = document.createElement('h5');
    cardTitle.classList.add('card-title');
    cardTitle.textContent = movie.title;

    const cardText = document.createElement('p');
    cardText.classList.add('card-text');
    cardText.textContent = movie.overview.substring(0, 100) + '...'; // Display first 100 characters of the overview

    cardTitleLink.appendChild(cardTitle);
    cardBody.appendChild(cardTitleLink);
    cardBody.appendChild(cardText);

    card.appendChild(moviePoster);
    card.appendChild(cardBody);
    movieItem.appendChild(card);

    return movieItem;
}


// Function to display the selected movie
function displaySelectedMovie() {
    const movieGrid = document.getElementById('result-grid');
    movieGrid.innerHTML = '';

    if (selectedMovie) {
        const movieItem = createMovieItem(selectedMovie);
        movieGrid.appendChild(movieItem);
    } else {
        displayErrorMessage();
    }
}

// Function to display error message when no results are found
function displayErrorMessage() {
    const errorMessage = document.getElementById('result-grid');
    errorMessage.innerHTML = '<p class="error-message">No results found. Please try a different search.</p>';
}


