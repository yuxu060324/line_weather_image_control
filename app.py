from flask import Flask, request, redirect
import psycopg2
import os

app = Flask(__name__)

def get_conn():
	return psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

@app.route("/image")
def get_image():
	conn = get_conn()
	cur = conn.cursor()
	cur.execute("SELECT url FROM latest_image LIMIT 1")
	url = cur.fetchone()[0]
	conn.close()
	return redirect(url, code=302)

@app.route("/admin/update", methods=["POST"])
def update_image():
	data = request.json
	url = data["url"]

	conn = get_conn()
	cur = conn.cursor()
	cur.execute("UPDATE latest_image SET url=%s WHERE id=1", (url,))
	conn.commit()
	conn.close()

	return {"status": "ok", "image_url": url}
