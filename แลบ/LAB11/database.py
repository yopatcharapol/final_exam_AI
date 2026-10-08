import sqlite3
from datetime import datetime


DATABASE_NAME = "chat.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (chat_id) REFERENCES chats(id)
        )
    """)

    connection.commit()
    connection.close()


def create_chat(title="New Chat"):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO chats (title, created_at)
        VALUES (?, ?)
        """,
        (title, datetime.now().isoformat())
    )

    chat_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return chat_id


def get_chats():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM chats
        ORDER BY id DESC
    """)

    chats = cursor.fetchall()

    connection.close()

    return [dict(chat) for chat in chats]


def get_chat(chat_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM chats WHERE id = ?",
        (chat_id,)
    )

    chat = cursor.fetchone()

    connection.close()

    if chat:
        return dict(chat)

    return None


def add_message(chat_id, role, content):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (chat_id, role, content, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            chat_id,
            role,
            content,
            datetime.now().isoformat()
        )
    )

    connection.commit()
    connection.close()


def get_messages(chat_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM messages
        WHERE chat_id = ?
        ORDER BY id ASC
        """,
        (chat_id,)
    )

    messages = cursor.fetchall()

    connection.close()

    return [dict(message) for message in messages]


def update_chat_title(chat_id, title):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE chats
        SET title = ?
        WHERE id = ?
        """,
        (title, chat_id)
    )

    connection.commit()
    connection.close()
