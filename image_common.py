import os
import datetime

try:
	import urlparse
except ImportError:
	import urllib.parse as urlparse

HOME_ABSPATH = os.path.dirname(os.path.abspath(__file__))

icon_folder_name = "images/"
weather_icon_folder_name = "weather/"
output_folder_name = "out/"

# 天候コードをまとめているJSONファイル名
weather_code_list_file_name = "weatherCodeList.json"


OUTPUT_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "image", "out")
FONT_FILE_PATH_MEIRYO = os.path.join(HOME_ABSPATH, "Font", "meiryo.ttc")
WEATHER_CODE_LIST_FILE_NAME = os.path.join(HOME_ABSPATH, "jsons", weather_code_list_file_name)

WEATHER_PATH = os.path.join(HOME_ABSPATH, icon_folder_name, weather_icon_folder_name)		# 天気の画像が保存されているPATH
OUT_DEFAULT_WEATHER_IMAGE_FILE_NAME = "out_weather_image_default.png"						# エラー時に返す天気画像のファイル名

ICON_WEATHER_FILE = {
	"sunny": {
		"url": os.path.join(WEATHER_PATH, "sunny.png"),
		"bg_color": "#ff7f50"
	},
	"cloudy": {
		"url": os.path.join(WEATHER_PATH, "cloudy.png"),
		"bg_color": "#c0c0c0"
	},
	"rain": {
		"url": os.path.join(WEATHER_PATH, "rain.png"),
		"bg_color": "#4169e1"
	},
	"snow": {
		"url": os.path.join(WEATHER_PATH, "snow.png"),
		"bg_color": "#afeeee"
	},
	"thunder": {
		"url": os.path.join(WEATHER_PATH, "thunderstorm.png"),
		"bg_color": "#ffd700"
	},
	"other": {
		"url": os.path.join(WEATHER_PATH, "sunny.png"),
		"bg_color": "#777777"
	}
}

WEATHER_CODE = {
	"1": "sunny",
	"2": "cloudy",
	"3": "rain",
	"4": "snow",
	"5": "thunder"
}

OUT_FOLDER_PATH = os.path.join(HOME_ABSPATH, icon_folder_name, output_folder_name)

HERO_SIZE = (480, 270)

WEATHER_FORECAST_MAP_SIZE = (320, 180)
TEMPERATURE_SIZE = (HERO_SIZE[0]-WEATHER_FORECAST_MAP_SIZE[0], WEATHER_FORECAST_MAP_SIZE[1])
WEATHER_NAME_SIZE = (HERO_SIZE[0], HERO_SIZE[1]-WEATHER_FORECAST_MAP_SIZE[1])

HERO_POSITION_WEATHER_MAP = (0, 0)
HERO_POSITION_TEMPERATURE = (WEATHER_FORECAST_MAP_SIZE[0], 0)
HERO_POSITION_DETAIL_WEATHER = (0, WEATHER_FORECAST_MAP_SIZE[1])

# ファイル名
out_file_name_hero = "out_weather_"

# 最高/最低気温の背景/枠 の色
TEMPERATURE_MAX_BG_COLOR = "#ffc0c0"		# 最高気温の背景色
TEMPERATURE_MAX_FG_COLOR = "#ff0000"		# 最高気温の枠/文字の色
TEMPERATURE_MIN_BG_COLOR = "#c0c0ff"		# 最低気温の背景色
TEMPERATURE_MIN_FG_COLOR = "#0000ff"		# 最低気温の枠/文字の色
