import os
import sqlite3

from flask import Flask, send_file, jsonify
from datetime import datetime

from image_common import *
from common_global import *
from create_weather_image import create_weather_image

app = Flask(__name__)

DB_PATH = "database.sqlite"

def init_db():
	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS latest_image (
			id INTEGER PRIMARY KEY,
			filename TEXT
		)
	""")
	cur.execute("""
		INSERT OR IGNORE INTO latest_image (id, filename)
		VALUES (1, '')
	""")
	conn.commit()
	conn.close()


init_db()


@app.route("/get_image_filename")
def get_image_filename():
	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()
	cur.execute("SELECT filename FROM latest_image WHERE id = 1")
	row = cur.fetchone()
	conn.close()

	if not row or not row[0]:
		logger.warning(f'データベースに値が登録されていないです: {row[0]}')
		return OUT_DEFAULT_WEATHER_IMAGE_FILE_NAME

	file_path = os.path.join(OUTPUT_FILE_PATH, row[0])
	logger.debug(f'filename: {row[0]}')

	if not os.path.exists(file_path):
		logger.warning(f'ファイルが存在しません: {file_path}')
		return OUT_DEFAULT_WEATHER_IMAGE_FILE_NAME

	return row[0]


@app.route("/image/<filename>")
def get_image(filename):
	file_path = os.path.join(OUTPUT_FILE_PATH, filename)

	# 画像がない場合は、サンプル画像を返却する
	if not os.path.exists(file_path):
		return send_file(OUT_DEFAULT_WEATHER_IMAGE_PATH, mimetype="image/png")

	return send_file(file_path, mimetype="image/png")


@app.route("/admin/update", methods=["POST"])
def update_image():

	filename = create_weather_image(place_code="130000")

	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()
	cur.execute(
		"UPDATE latest_image SET filename = ? WHERE id = 1",
		(filename,)
	)
	conn.commit()
	conn.close()

	logger.debug(f'saved filename: {filename}')

	return jsonify({
		"status": "ok",
		"filename": filename
	})


# sleepさせないためのバッファAPI
@app.route("/")
def home():
	return "HOME"


# ---------- Render 用 ----------
if __name__ == "__main__":
	app.run(debug=True)

