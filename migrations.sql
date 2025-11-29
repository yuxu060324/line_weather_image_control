CREATE TABLE IF NOT EXISTS latest_image (
  id INTEGER PRIMARY KEY,
  url TEXT NOT NULL
);

INSERT INTO latest_image (id, url)
VALUES (1, 'https://example.com/initial.jpg')
ON CONFLICT (id) DO NOTHING;
