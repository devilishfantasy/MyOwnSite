async function loadMovies() {
    try {
        const response = await fetch('movies.json');
        const movies = await response.json();
        
        const grid = document.querySelector('.grid-movies');
        grid.innerHTML = movies.map(m => `
            <a href="${m.link}" class="card">
                <img src="${m.image}" alt="poster" class="film-poster">
                <span class="body">
                    <span class="film-title">${m.title}</span>
                    <span class="film-votes">${m.kp_rating ?? '—'} / ${m.imdb_rating ?? '—'}</span>
                </span>
            </a>
        `).join('');
    } catch (err) {
        console.error('Не удалось загрузить фильмы:', err);
    }
}

document.addEventListener('DOMContentLoaded', loadMovies);