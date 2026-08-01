import sqlite3

DATABASE_NAME = "media.db"


def get_connection():
    """Creates and returns a database connection."""
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    """Creates the media table if it doesn't already exist."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS media(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            media_type TEXT NOT NULL,
            name TEXT NOT NULL,
            genre TEXT NOT NULL,
            rating INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_media(media):
    """Adds a Movie or Show to the database."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO media(media_type, name, genre, rating)
        VALUES (?, ?, ?, ?)
    """, media.to_tuple())

    conn.commit()
    conn.close()


def get_all_media():
    """Returns every record ordered by name."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, media_type, name, genre, rating
        FROM media
        ORDER BY name
    """)

    records = cursor.fetchall()

    conn.close()

    return records


def update_media(media_id, media):
    """Updates an existing record."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE media
        SET
            media_type = ?,
            name = ?,
            genre = ?,
            rating = ?
        WHERE id = ?
    """, (
        media.media_type,
        media.name,
        media.genre,
        media.rating,
        media_id
    ))

    conn.commit()
    conn.close()


def delete_media(media_id):
    """Deletes a record by ID."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM media
        WHERE id = ?
    """, (media_id,))

    conn.commit()
    conn.close()


def search_media(search_text):
    """Searches by name."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, media_type, name, genre, rating
        FROM media
        WHERE LOWER(name) LIKE ?
        ORDER BY name
    """, (f"%{search_text.lower()}%",))

    results = cursor.fetchall()

    conn.close()

    return results


def get_movies():
    """Returns only movies."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, media_type, name, genre, rating
        FROM media
        WHERE media_type = 'Movie'
        ORDER BY name
    """)

    movies = cursor.fetchall()

    conn.close()

    return movies


def get_shows():
    """Returns only shows."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, media_type, name, genre, rating
        FROM media
        WHERE media_type = 'Show'
        ORDER BY name
    """)

    shows = cursor.fetchall()

    conn.close()

    return shows