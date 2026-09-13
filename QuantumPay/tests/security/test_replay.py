from backend.auth.challenges import create_challenge, consume_challenge
from backend.database import SessionLocal

def test_challenge_replay_is_rejected():
    db = SessionLocal()
    try:
        item = create_challenge(db, "replay_user", "login")
        assert consume_challenge(db, "replay_user", item.challenge, "login") is True
        assert consume_challenge(db, "replay_user", item.challenge, "login") is False
    finally:
        db.close()
