import app as app_module

class FakeRedis:
    def __init__(self):
        self.n = 0

    def incr(self, key):
        self.n += 1
        return self.n

def test_counter_increments(monkeypatch):
    monkeypatch.setattr(app_module, "r", FakeRedis())
    client = app_module.app.test_client()
    assert b"1 fois" in client.get("/").data
    assert b"2 fois" in client.get("/").data