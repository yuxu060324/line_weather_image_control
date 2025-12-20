import os
import sys
import json
import logging
from logging import StreamHandler
try:
	import urlparse
except ImportError:
	import urllib.parse as urlparse

RUN_ENV = "LOCAL"
HOME_ABSPATH = os.path.dirname(os.path.abspath(__file__))
log_file_name = "project"

# logger
def getMyLogger(name):

	my_logger = logging.getLogger(name)

	# デプロイ環境
	if RUN_ENV == "RENDER":
		my_logger.setLevel(logging.DEBUG)

		handler = logging.StreamHandler(sys.stdout)
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('[%(filename)s:%(lineno)d %(funcName)s] %(message)s')

		handler.setFormatter(formatter)
		my_logger.addHandler(handler)

	# デバッグ環境
	else:

		log_file_path = os.path.join(HOME_ABSPATH, "log", f'{log_file_name}.log')
		my_logger.setLevel(logging.DEBUG)

		# ディレクトリの存在確認
		if not os.path.isdir(os.path.join(HOME_ABSPATH, "log")):
			# ディレクトリの作成
			os.makedirs(os.path.join(HOME_ABSPATH, "log"))
			# ファイルの存在確認
			if not os.path.isfile(log_file_path):
				# ファイルの作成
				with open(log_file_path, "w"):
					pass

		handler = logging.FileHandler(log_file_path, encoding="utf-8")
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(levelname)-9s %(asctime)s [%(filename)s:%(lineno)d %(funcName)s] %(message)s')

		handler.setFormatter(formatter)
		my_logger.addHandler(handler)

	return my_logger


# loggerの定義
logger = getMyLogger(__name__)

