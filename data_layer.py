from pathlib import Path

from chainlit.data.sql_alchemy import SQLAlchemyDataLayer

DB_PATH = Path(__file__).parent / "chat_history.db"
DB_URL = f"sqlite+aiosqlite:///{DB_PATH}"

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    "id"         TEXT PRIMARY KEY,
    "identifier" TEXT NOT NULL UNIQUE,
    "createdAt"  TEXT,
    "metadata"   TEXT
);
CREATE TABLE IF NOT EXISTS threads (
    "id"             TEXT PRIMARY KEY,
    "createdAt"      TEXT,
    "name"           TEXT,
    "userId"         TEXT,
    "userIdentifier" TEXT,
    "tags"           TEXT,
    "metadata"       TEXT
);
CREATE TABLE IF NOT EXISTS steps (
    "id"            TEXT PRIMARY KEY,
    "name"          TEXT,
    "type"          TEXT,
    "threadId"      TEXT,
    "parentId"      TEXT,
    "streaming"     INTEGER,
    "waitForAnswer" INTEGER,
    "isError"       INTEGER,
    "metadata"      TEXT,
    "tags"          TEXT,
    "input"         TEXT,
    "output"        TEXT,
    "createdAt"     TEXT,
    "start"         TEXT,
    "end"           TEXT,
    "generation"    TEXT,
    "showInput"     TEXT,
    "language"      TEXT
);
CREATE TABLE IF NOT EXISTS feedbacks (
    "id"      TEXT PRIMARY KEY,
    "forId"   TEXT,
    "value"   INTEGER,
    "comment" TEXT
);
CREATE TABLE IF NOT EXISTS elements (
    "id"           TEXT PRIMARY KEY,
    "threadId"     TEXT,
    "type"         TEXT,
    "chainlitKey"  TEXT,
    "url"          TEXT,
    "objectKey"    TEXT,
    "name"         TEXT,
    "display"      TEXT,
    "size"         TEXT,
    "language"     TEXT,
    "page"         INTEGER,
    "forId"        TEXT,
    "mime"         TEXT,
    "props"        TEXT
);
"""


def init_database() -> None:
    import sqlite3
    conn = sqlite3.connect(str(DB_PATH))
    conn.executescript(_SCHEMA_SQL)
    conn.commit()
    conn.close()


def make_data_layer() -> SQLAlchemyDataLayer:
    return SQLAlchemyDataLayer(conninfo=DB_URL)
