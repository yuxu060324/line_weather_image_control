import base64
import io
import sqlite3

from flask import Flask, send_file, jsonify
from datetime import datetime

from create_weather_image import create_weather_image

app = Flask(__name__)

DB_PATH = "database.sqlite"

def init_db():
	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS latest_image (
			id INTEGER PRIMARY KEY,
			filename TEXT,
			image_base64 TEXT
			)
	""")
	cur.execute("""
		INSERT OR IGNORE INTO latest_image (id, filename, image_base64)
		VALUES (1, '', '')
	""")
	conn.commit()
	conn.close()

init_db()


# def get_conn():
# 	return psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")




@app.route("/image")
def get_image():
	# conn = get_conn()
	# cur = conn.cursor()
	# cur.execute("SELECT url FROM latest_image LIMIT 1")
	# url = cur.fetchone()[0]
	# conn.close()
	# return redirect(url, code=302)

	return "VIEW_IMAGE"


@app.route("/admin/update", methods=["POST"])
def update_image():
	# data = request.json
	# url = data["url"]
	#
	# conn = get_conn()
	# cur = conn.cursor()
	# cur.execute("UPDATE latest_image SET url=%s WHERE id=1", (url,))
	# conn.commit()
	# conn.close()
	#
	# return {"status": "ok", "image_url": url}

	return "UPDATE_IMAGE"


# sleepさせないためのバッファAPI
@app.route("/")
def home():
	return "HOME"


# ---------- Render 用 ----------
if __name__ == "__main__":
	app.run()

