import sqlite3

conn = sqlite3.connect("games.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS sent_games (
    store TEXT,
    game_id TEXT,
    PRIMARY KEY (store, game_id)
)
""")
conn.commit()

def already_sent(store, game_id):
    c.execute(
        "SELECT 1 FROM sent_games WHERE store=? AND game_id=?",
        (store, game_id)
    )
    return c.fetchone() is not None

def mark_sent(store, game_id):
    c.execute(
        "INSERT OR IGNORE INTO sent_games VALUES (?,?)",
        (store, game_id)
    )
    conn.commit()
