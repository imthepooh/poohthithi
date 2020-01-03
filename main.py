import os 
import telegram
import datetime
from pytz import timezone

bot = telegram.Bot(token=os.environ["TOKEN"])
months = list(['jan','feb','mar','april','may','june','july','aug','sep','oct','nov','dec'])
source_data = {
	"panchangam_jan": [{
			"Thithi": "Saptami Full",
			"Nakshatram": "Purvabhadra 14:53",
			"Rahukalam": "12:11-13:24",
			"Durmuhurtam": "11:52-12:31",
			"Varjam": "None"
		},
		{
			"Thithi": " Saptami 7:30",
			"Nakshatram": "Uttarabhadra 17:50",
			"Rahukalam": "13:24-14:36",
			"Durmuhurtam": "10:36-11:14",
			"Varjam": "31:13-33:00"
		},
		{
			"Thithi": " Ashtami 09:56",
			"Nakshatram": "Revathi 20:35",
			"Rahukalam": "11:00-12:12",
			"Durmuhurtam": "09:19-09:57",
			"Varjam": "None"
		},
		{
			"Thithi": "Navami 12:02",
			"Nakshatram": "Ashwini 22:57",
			"Rahukalam": "09:48-11:00",
			"Durmuhurtam": "07:24-8:41",
			"Varjam": "18:33-20:19"
		},
		{
			"Thithi": "Dashami 13:37",
			"Nakshatram": "Bharani 24:45",
			"Rahukalam": "15:50-17:02",
			"Durmuhurtam": "15:45-16:24",
			"Varjam": "9:16-11:00"
		},
		{
			"Thithi": "Ekadashi 14:32",
			"Nakshatram": "Krittika 25:54",
			"Rahukalam": "08:36-09:49",
			"Durmuhurtam": "14:29-15:07",
			"Varjam": "13:20-15:00"
		},
		{
			"Thithi": "Dvadashi 14:44",
			"Nakshatram": "Rohini 26:21",
			"Rahukalam": "14:39-15:52",
			"Durmuhurtam": "09:20-09:58",
			"Varjam": "18:12-19:50"
		},
		{
			"Thithi": "Trayodashi 14:14",
			"Nakshatram": "Mrigashira 26:08",
			"Rahukalam": "12:14-13:27",
			"Durmuhurtam": "11:55-12:34",
			"Varjam": "07:54-11:09"
		},
		{
			"Thithi": "Chaturdashi 13:04",
			"Nakshatram": "Aardra 25:18",
			"Rahukalam": "13:28-14:40",
			"Durmuhurtam": "10:38-11:17",
			"Varjam": "10:14-11:47"
		},
		{
			"Thithi": "Purnima 11:21",
			"Nakshatram": "Punarvasu 24:00",
			"Rahukalam": "11:02-12:15",
			"Durmuhurtam": "12:35-13:14",
			"Varjam": "12:39-14:10"
		},
		{
			"Thithi": "Prathama 09:11",
			"Nakshatram": "Dvitiiya 30:42, Pushya 22:19",
			"Rahukalam": "09:49-11:02",
			"Durmuhurtam": "07:23-08:41",
			"Varjam": "07:26-08:56"
		},
		{
			"Thithi": "Tritiiya 28:02",
			"Nakshatram": "Aslesha 20:25",
			"Rahukalam": "15:56-17:09",
			"Durmuhurtam": "15:51-16:30",
			"Varjam": "10:06-11:35"
		},
		{
			"Thithi": "Chaturthi 25:19",
			"Nakshatram": "Magha 18:25",
			"Rahukalam": "08:36-09:50",
			"Durmuhurtam": "12:36-13:15",
			"Varjam": "25:46-27:14"
		},
		{
			"Thithi": "Panchami 22:40",
			"Nakshatram": "Purvaphalguni 16:27",
			"Rahukalam": "14:44-15:57",
			"Durmuhurtam": "09:20-09:59",
			"Varjam": "23:06-24:34"
		},
		{
			"Thithi": "Shashthi 20:11",
			"Nakshatram": "Uttarai 14:37",
			"Rahukalam": "12:17-13:31",
			"Durmuhurtam": "11:57-12:37",
			"Varjam": "22:27-23:56"
		},
		{
			"Thithi": "Saptami 17:58",
			"Nakshatram": "Hasta 13:00",
			"Rahukalam": "13:31-14:45",
			"Durmuhurtam": "10:39-11:18",
			"Varjam": "20:34-22:05"
		},
		{
			"Thithi": "Ashtami 16:03",
			"Nakshatram": "Chitra 11:42",
			"Rahukalam": "11:04-12:18",
			"Durmuhurtam": "09:20-10:00",
			"Varjam": "17:05-18:37"
		},
		{
			"Thithi": "Navami 14:30",
			"Nakshatram": "Swati 10:45",
			"Rahukalam": "09:50-11:04",
			"Durmuhurtam": "07:21-08:40",
			"Varjam": "16:13-17:47"
		},
		{
			"Thithi": "Dashami 13:21",
			"Nakshatram": "Vishaakha 10:11",
			"Rahukalam": "16:02-17:16",
			"Durmuhurtam": "15:57-16:37",
			"Varjam": "14:09-15:44"
		},
		{
			"Thithi": "Ekadashi 12:36",
			"Nakshatram": "Anuraadha 10:00",
			"Rahukalam": "08:35-09:49",
			"Durmuhurtam": "12:39-13:18",
			"Varjam": "15:39-17:16"
		},
		{
			"Thithi": "Dvadashi 12:15",
			"Nakshatram": "Jyeshtha 10:13",
			"Rahukalam": "14:49-16:04",
			"Durmuhurtam": "22:55-23:51",
			"Varjam": ""
		},
		{
			"Thithi": "Trayodashi 12:18",
			"Nakshatram": "Mula 10:50",
			"Rahukalam": "12:19-13:34",
			"Durmuhurtam": "11:59-12:39",
			"Varjam": "09:11-10:50"
		},
		{
			"Thithi": "Chaturdashi 12:47",
			"Nakshatram": "P.shadha 11:50",
			"Rahukalam": "13:35-14:50",
			"Durmuhurtam": "10:39-11:19",
			"Varjam": "20:19-22:01"
		},
		{
			"Thithi": "Amavasya 13:41",
			"Nakshatram": "U.shadha 13:16",
			"Rahukalam": "11:04-12:20",
			"Durmuhurtam": "09:19-09:59",
			"Varjam": "17:34-19:17 "
		},
		{
			"Thithi": "Maagha Shukla, Prathama 05:01",
			"Nakshatram": "Shravana 15:05",
			"Rahukalam": "11:04-12:21",
			"Durmuhurtam": "09:16-09:57, 12:42-13:23",
			"Varjam": "19:28-21:12"
		},
		{
			"Thithi": "26 Dvitiiya 16:45",
			"Nakshatram": "Dhanishta 17:19",
			"Rahukalam": "16:08-17:24",
			"Durmuhurtam": "16:03-16:43",
			"Varjam": "25:17-27:03"
		},
		{
			"Thithi": "Tritiiya 18:52",
			"Nakshatram": "Shatabhisha 19:53",
			"Rahukalam": "08:32-09:48",
			"Durmuhurtam": "12:41-13:21",
			"Varjam": "27:02-28:50"
		},
		{
			"Thithi": "Chaturthi 21:16",
			"Nakshatram": "Purvabhadra 22:43",
			"Rahukalam": "14:53-16:10",
			"Durmuhurtam": "09:18-09:58, 22:58-23:53",
			"Varjam": ""
		},
		{
			"Thithi": "Panchami 23:49",
			"Nakshatram": "Uttarahadra 25:42",
			"Rahukalam": "12:21-13:37",
			"Durmuhurtam": "12:01-12:41",
			"Varjam": "09:31-11:19"
		},
		{
			"Thithi": "Shashthi 26:22",
			"Nakshatram": "Revati 28:40",
			"Rahukalam": "13:38-14:55 ",
			"Durmuhurtam": "10:39-11:20",
			"Varjam": "15:11-16:59"
		},
		{
			"Thithi": "Saptami 28:41",
			"Nakshatram": "Ashwini full night",
			"Rahukalam": "11:04-12:21",
			"Durmuhurtam": "09:16-09:57",
			"Varjam": "26:56-28:43"
		}
	],
	"panchangam_feb": [{
			"Thithi": "Ashtami 30:33",
			"Nakshatram": "Ashwini 07:23",
			"Rahukalam": "09:47-11:04",
			"Durmuhurtam": "07:12-08:35",
			"Varjam": "17:54-19:40"
		},
		{
			"Thithi": "Navami full night",
			"Nakshatram": "Bharani 09:41",
			"Rahukalam": "16:14-17:32",
			"Durmuhurtam": "16:09-16:50",
			"Varjam": "22:32-24:14"
		},
		{
			"Thithi": "Navami 07:49",
			"Nakshatram": "Krittika 11:22",
			"Rahukalam": "08:28-09:46",
			"Durmuhurtam": "12:42-13:24",
			"Varjam": "28:00-29:40"
		},
		{
			"Thithi": "Dashami 08:19",
			"Nakshatram": "Rohini 12:19",
			"Rahukalam": "14:58-16:16",
			"Durmuhurtam": "09:15-09:56",
			"Varjam": "17:57-19:34"
		},
		{
			"Thithi": "Ekadashi 08:01, Dvadashi 30:53",
			"Nakshatram": "Mrigashirsha 12:28",
			"Rahukalam": "12:22-13:40",
			"Durmuhurtam": "12:01-12:43",
			"Varjam": "20:39-22:13"
		},
		{
			"Thithi": "Trayodashi 29:01",
			"Nakshatram": "Aardra 11:51",
			"Rahukalam": "13:40-14:59",
			"Durmuhurtam": "10:37-11:19",
			"Varjam": "23:11-24:41"
		},
		{
			"Thithi": "Chaturdashi 26:32",
			"Nakshatram": "Punarvasu 10:30",
			"Rahukalam": "11:03-12:22",
			"Durmuhurtam": "09:13-09:55",
			"Varjam": "17:52-19:20"
		},
		{
			"Thithi": "Purnima 23:33",
			"Nakshatram": "Pushya 08:35, Aslesha 30:13",
			"Rahukalam": "09:44-11:03",
			"Durmuhurtam": "07:06-08:30",
			"Varjam": "20:07-21:34"
		},
		{
			"Thithi": "Prathama 20:15",
			"Nakshatram": "Magha 27:35",
			"Rahukalam": "16:20-17:39",
			"Durmuhurtam": "16:15-16:57",
			"Varjam": "16:54-18:20"
		},
		{
			"Thithi": "Dvitiiya 16:48",
			"Nakshatram": "Purvapalguni 24:53",
			"Rahukalam": "08:23-09:43",
			"Durmuhurtam": "12:43-13:26",
			"Varjam": "10:41-12:06"
		},
		{
			"Thithi": "Tritiiya 13:23",
			"Nakshatram": "Uttara  22:16",
			"Rahukalam": "15:02-16:22",
			"Durmuhurtam": "09:10-09:53",
			"Varjam": "07:18-08:43"
		},
		{
			"Thithi": "Chaturthi 10:09",
			"Nakshatram": "Hasta 19:55",
			"Rahukalam": "12:22-13:42",
			"Durmuhurtam": "12:01-12:43",
			"Varjam": "27:16-28:44"
		},
		{
			"Thithi": "Panchami 07:16, Shashthi 28:51",
			"Nakshatram": "Chitra 17:57",
			"Rahukalam": "13:42-15:03",
			"Durmuhurtam": "10:35-11:18, 14:52-15:35",
			"Varjam": "23:13-24:43"
		},
		{
			"Thithi": "Saptami 26:59",
			"Nakshatram": "Swathi 16:31",
			"Rahukalam": "11:01-12:22",
			"Durmuhurtam": "09:08-09:51",
			"Varjam": "21:55-23:27"
		},
		{
			"Thithi": "Ashtami 25:44",
			"Nakshatram": "Vishaakha 15:39",
			"Rahukalam": "09:40-11:01",
			"Durmuhurtam": "06:58-08:25",
			"Varjam": "19:36-21:11"
		},
		{
			"Thithi": "Navami 25:05",
			"Nakshatram": "Anuraadha 15:23",
			"Rahukalam": "16:26-17:47",
			"Durmuhurtam": "16:20-17:03",
			"Varjam": "21:04-22:41"
		},
		{
			"Thithi": "Dashami 25:03",
			"Nakshatram": "Jyeshtha 15:44",
			"Rahukalam": "08:17-09:39",
			"Durmuhurtam": "12:44-13:27, 14:54-15:37",
			"Varjam": ""
		},
		{
			"Thithi": "Ekadashi 25:32",
			"Nakshatram": "Mula 16:36",
			"Rahukalam": "15:05-16:27",
			"Durmuhurtam": "09:06-09:49",
			"Varjam": "14:57-16:36"
		},
		{
			"Thithi": "Dvadashi 26.30",
			"Nakshatram": "Purvashadha 17:58",
			"Rahukalam": "12:22-13:44",
			"Durmuhurtam": "12:00-12:44",
			"Varjam": "26:33-28:16"
		},
		{
			"Thithi": "Trayodashi 27:51",
			"Nakshatram": "Uttarashadha 19:43",
			"Rahukalam": "13:44-15:06",
			"Durmuhurtam": "10:32-11:16",
			"Varjam": "24:04-25:49"
		},
		{
			"Thithi": "Chaturdashi 29:33",
			"Nakshatram": "Shravana 21:49",
			"Rahukalam": "10:59-12:22",
			"Durmuhurtam": "09:03-09:47",
			"Varjam": "26:13-27:59"
		},
		{
			"Thithi": "Amavasya full night",
			"Nakshatram": "Dhanishta 24:13",
			"Rahukalam": "09:36-10:58",
			"Durmuhurtam": "06:50-08:18",
			"Varjam": ""
		},
		{
			"Thithi": "Amavasya 07:31",
			"Nakshatram": "Shatabhisha 26:51",
			"Rahukalam": "16:31-17:54",
			"Durmuhurtam": "16:25-17:10",
			"Varjam": "08:12-09:59"
		},
		{
			"Thithi": "Phalguna Shukla, Prathama 09:45",
			"Nakshatram": "Purvabhadra 29:40",
			"Rahukalam": "08:11-09:34",
			"Durmuhurtam": "12:43-13:28,  14:57-15:42",
			"Varjam": "10:00-11:47"
		},
		{
			"Thithi": "Dvitiiya 12:10",
			"Nakshatram": "Uttarabhadra full night",
			"Rahukalam": "15:09-16:32",
			"Durmuhurtam": "09:00-09:45",
			"Varjam": "16:27-18:15"
		},
		{
			"Thithi": "26 Tritiiya 14:42",
			"Nakshatram": "Uttarabhadra 08:38",
			"Rahukalam": "12:21-13:45",
			"Durmuhurtam": "11:58-12:43",
			"Varjam": "22:08-23:56"
		},
		{
			"Thithi": "Chaturthi 17:14",
			"Nakshatram": "Revati 11.38",
			"Rahukalam": "13:45-15:09",
			"Durmuhurtam": "10:28-11:13, 14:58-15:43",
			"Varjam": ""
		},
		{
			"Thithi": "Panchami 19:39",
			"Nakshatram": "Ashwini 14:33",
			"Rahukalam": "10:56-12:20",
			"Durmuhurtam": "08:57-09:42",
			"Varjam": "10:04-11:51"
		},
		{
			"Thithi": "Shashthi 21:46",
			"Nakshatram": "Bharani 17:12",
			"Rahukalam": "09:30-10:55",
			"Durmuhurtam": "06:40-08:11",
			"Varjam": "30:18-32:03"
		}
	],

	"panchangam_mar": [{
			"Thithi": "Saptami 23:23",
			"Nakshatram": "Krittika 19:25",
			"Rahukalam": "16:36-18:01",
			"Durmuhurtam": "16:30-17:16",
			"Varjam": ""
		},
		{
			"Thithi": "Ashtami 24:20",
			"Nakshatram": "Rohini 21:01",
			"Rahukalam": "08:03-09:29",
			"Durmuhurtam": "12:43-13:28",
			"Varjam": "12:29-14:12"
		},
		{
			"Thithi": "Navami 24:30",
			"Nakshatram": "Mrigashirsha 21:53",
			"Rahukalam": "15:11-16:37",
			"Durmuhurtam": "08:54-09:39",
			"Varjam": "30:18-31:54"
		},
		{
			"Thithi": "Dashami 23:49",
			"Nakshatram": "Aardra 21:56",
			"Rahukalam": "12:19-13:46",
			"Durmuhurtam": "11:56-12:42",
			"Varjam": ""
		},
		{
			"Thithi": "Ekadashi 22:17",
			"Nakshatram": "Punarvasu 21:08",
			"Rahukalam": "13:46-15:12",
			"Durmuhurtam": "10:24-11:10",
			"Varjam": "09:32-11:05"
		},
		{
			"Thithi": "Dvadashi 19:59",
			"Nakshatram": "Pushya 19:35",
			"Rahukalam": "10:52-12:19",
			"Durmuhurtam": "08:51-09:37, 12:42-13:28",
			"Varjam": ""
		},
		{
			"Thithi": "Trayodashi 17:01",
			"Nakshatram": "Aslesha 17:22",
			"Rahukalam": "09:25-10:52",
			"Durmuhurtam": "06:31-08:03",
			"Varjam": "07:12-08:39"
		},
		{
			"Thithi": "Chaturdashi 14:34",
			"Nakshatram": "Magha 15:40",
			"Rahukalam": "17:41-19:08",
			"Durmuhurtam": "17:35-18:21",
			"Varjam": "22:39-24:03"
		},
		{
			"Thithi": "Purnima 10:47",
			"Nakshatram": "Purvaphalguni 12:39",
			"Rahukalam": "08:55-10:23",
			"Durmuhurtam": "13:42-14:28",
			"Varjam": "18:54-20:18"
		},
		{
			"Thithi": "Dvitiiya 27:03",
			"Nakshatram": "Uttara  09:31",
			"Rahukalam": "16:14-17:42",
			"Durmuhurtam": "09:47-10:43",
			"Varjam": "16:52-18:16"
		},
		{
			"Thithi": "Tritiiya 23:29",
			"Nakshatram": "Chitra 27:45",
			"Rahukalam": "13:18-14:46",
			"Durmuhurtam": "12:54-13:41",
			"Varjam": "13:35-15:00"
		},
		{
			"Thithi": "Chaturthi 20:20",
			"Nakshatram": "Swathi 25:29",
			"Rahukalam": "14:46-16:15",
			"Durmuhurtam": "11:19-12:07",
			"Varjam": "08:50-10:17"
		},
		{
			"Thithi": "Panchami 17:47",
			"Nakshatram": "Vishaaka 23:50",
			"Rahukalam": "11:48-13:17",
			"Durmuhurtam": "09:44-10:31",
			"Varjam": "27:40-29:13"
		},
		{
			"Thithi": "Shashthi 15:55",
			"Nakshatram": "Anuraadha 22:53",
			"Rahukalam": "10:19-11:48",
			"Durmuhurtam": "07:20-08:55",
			"Varjam": "28:27-30:02"
		},
		{
			"Thithi": "Saptami 14:49",
			"Nakshatram": "Jyeshtha 22:42",
			"Rahukalam": "17:45-19:14",
			"Durmuhurtam": "17:39-18:27",
			"Varjam": ""
		},
		{
			"Thithi": "Ashtami 14:29",
			"Nakshatram": "Mula 23:16",
			"Rahukalam": "08:47-10:17",
			"Durmuhurtam": "13:40-14:28",
			"Varjam": "21:38-23:16"
		},
		{
			"Thithi": "Navami 14:54",
			"Nakshatram": "Purvashadha 24:31",
			"Rahukalam": "16:16-17:46",
			"Durmuhurtam": "09:40-10:28",
			"Varjam": "09:22-11:03"
		},
		{
			"Thithi": "Dashami 15:56",
			"Nakshatram": "Uttarashadha 26:20",
			"Rahukalam": "13:16-14:46",
			"Durmuhurtam": "12:52-13:40",
			"Varjam": "09:07-10:50"
		},
		{
			"Thithi": "Ekadashi 17:29",
			"Nakshatram": "Shravana 28:35",
			"Rahukalam": "14:46-16:17",
			"Durmuhurtam": "11:15-12:03, 16:05-16:53",
			"Varjam": ""
		},
		{
			"Thithi": "Dvadashi 19:26",
			"Nakshatram": "Dhanishta 31:09",
			"Rahukalam": "11:44-13:15",
			"Durmuhurtam": "09:37-10:25",
			"Varjam": "09:01-10:47"
		},
		{
			"Thithi": "Trayodashi 21:38",
			"Nakshatram": "Shatabhisha full night",
			"Rahukalam": "10:12-11:44",
			"Durmuhurtam": "07:10-08:47",
			"Varjam": "15:12-16:59"
		},
		{
			"Thithi": "Chaturdashi 24:00",
			"Nakshatram": "Shatabhisha 09:57",
			"Rahukalam": "17:49-19:21",
			"Durmuhurtam": "17:43-18:32",
			"Varjam": "17:07-18:55"
		},
		{
			"Thithi": "Amavasya 26:28",
			"Nakshatram": "Purvabhhadra 12:51",
			"Rahukalam": "08:39-10:11",
			"Durmuhurtam": "13:39-14:28",
			"Varjam": "23:38-25:26"
		},
		{
			"Thithi": "Chaitra Shukla, Prathama 28:57",
			"Nakshatram": "Uttarabhadra 15:49",
			"Rahukalam": "16:18-17:50",
			"Durmuhurtam": "09:33-10:22, 24:03-24:50",
			"Varjam": "29:18-31:05"
		},
		{
			"Thithi": "Dvitiiya full night",
			"Nakshatram": "Revati 18:46",
			"Rahukalam": "13:14-:14:46",
			"Durmuhurtam": "12:49-13:38",
			"Varjam": ""
		},
		{
			"Thithi": "26 Dvitiiya 07:23",
			"Nakshatram": "Ashwini 21:39",
			"Rahukalam": "14:46-16:19",
			"Durmuhurtam": "11:10-11:59",
			"Varjam": "17:10-18:58"
		},
		{
			"Thithi": "Tritiiya 09:42",
			"Nakshatram": "Bharani 24:22",
			"Rahukalam": "11:40-13:13",
			"Durmuhurtam": "09:30-10:19",
			"Varjam": "08:20-10:07"
		},
		{
			"Thithi": "Chaturthi 11:48",
			"Nakshatram": "Krittika 26:47",
			"Rahukalam": "10:06-11:39",
			"Durmuhurtam": "06:59-08:39",
			"Varjam": "13:35-15:20"
		},
		{
			"Thithi": "Panchami 13:31",
			"Nakshatram": "Rohini 28:48",
			"Rahukalam": "17:53-19:27",
			"Durmuhurtam": "17:47-18:37",
			"Varjam": "20:08-21:52"
		},
		{
			"Thithi": "Shashthi 14:45",
			"Nakshatram": "Mrigashirsha 30:14",
			"Rahukalam": "08:30-10:04",
			"Durmuhurtam": "13:37-14:27",
			"Varjam": "10:44-12:25"
		},
		{
			"Thithi": "Saptami 15:20",
			"Nakshatram": "Aardra full night",
			"Rahukalam": "16:20-17:55",
			"Durmuhurtam": "09:26-10:16",
			"Varjam": "14:54-16:33"
		}
	],

	"panchangam_april": [{
			"Thithi": "Ashtami 15:10",
			"Nakshatram": "Aardra 06:59",
			"Rahukalam": "13:12-14:46",
			"Durmuhurtam": "12:46-13:37",
			"Varjam": "18:59-20:35"
		},
		{
			"Thithi": "Navami 14:13",
			"Nakshatram": "Punarvasu 06:58, Pushya 30:10",
			"Rahukalam": "14:46-16:21",
			"Durmuhurtam": "11:05-11:55, 16:08-16:59",
			"Varjam": "14:42-16:15"
		},
		{
			"Thithi": "Dashami 12:28",
			"Nakshatram": "Aslesha 28:38",
			"Rahukalam": "11:36-13:11",
			"Durmuhurtam": "09:23-10:23",
			"Varjam": "18:09-19:39"
		},
		{
			"Thithi": "Ekadashi 10:00",
			"Nakshatram": "Magha 26:27",
			"Rahukalam": "10:00-11:35",
			"Durmuhurtam": "06:49-08:31",
			"Varjam": "15:33-17:00"
		},
		{
			"Thithi": "Dvadashi 06:55, Trayodashi 27:22",
			"Nakshatram": "Purvaphalguni 23:46",
			"Rahukalam": "17:58-19:33",
			"Durmuhurtam": "17:51-18:42",
			"Varjam": "09:33-10:59"
		},
		{
			"Thithi": "Chaturdashi 23:31",
			"Nakshatram": "Uttara 20:45",
			"Rahukalam": "08:22-09:58",
			"Durmuhurtam": "13:36-14:27",
			"Varjam": "28:03-29:27"
		},
		{
			"Thithi": "Purnima 19:34",
			"Nakshatram": "Hasta 17:37",
			"Rahukalam": "06:23-17:59",
			"Durmuhurtam": "09:19-10:10",
			"Varjam": "24:35-25:59"
		},
		{
			"Thithi": "Prathama 15:43",
			"Nakshatram": "Chitra 14:33",
			"Rahukalam": "13:10-14:46",
			"Durmuhurtam": "12:44-13:35",
			"Varjam": "19:29-20:54"
		},
		{
			"Thithi": "Dvitiiya 12:08",
			"Nakshatram": "Swathi 11:45",
			"Rahukalam": "14:46-16:23",
			"Durmuhurtam": "11:00-11:52",
			"Varjam": "16:48-18:15"
		},
		{
			"Thithi": "Tritiiya 09:01, Chaturthi 30:31",
			"Nakshatram": "Vishaakha 09:24",
			"Rahukalam": "11:32-13:09",
			"Durmuhurtam": "09:16-10:08, 13:35-14:27",
			"Varjam": "13:07-14:36"
		},
		{
			"Thithi": "Panchami 28:45",
			"Nakshatram": "Anuraadha 07:41",
			"Rahukalam": "09:54-11:31",
			"Durmuhurtam": "06:39-08:23",
			"Varjam": "13:04-14:36"
		},
		{
			"Thithi": "Shashthi 27:48",
			"Nakshatram": "Jyeshtha 06:42, Mula 30:32",
			"Rahukalam": "18:02-19:40",
			"Durmuhurtam": "17:55-18:47",
			"Varjam": "28:57-30:32"
		},
		{
			"Thithi": "Saptami 27:41",
			"Nakshatram": "Purvashadha full night ",
			"Rahukalam": "08:14-09:52",
			"Durmuhurtam": "13:34-14:27",
			"Varjam": "16:24-18:02"
		},
		{
			"Thithi": "Ashtami 28:21",
			"Nakshatram": "Purvashadha 07:11",
			"Rahukalam": "16:25-18:03",
			"Durmuhurtam": "09:12-10:04",
			"Varjam": "15:38-17:20"
		},
		{
			"Thithi": "Navami 29:41",
			"Nakshatram": "Uttarashadha  08:34",
			"Rahukalam": "13:08-14:46",
			"Durmuhurtam": "12:41-13:34",
			"Varjam": "12:54-14:38"
		},
		{
			"Thithi": "Dashami full night",
			"Nakshatram": "Shravana 10:36",
			"Rahukalam": "14:46-16:25",
			"Durmuhurtam": "16:12-17:05",
			"Varjam": "15:01-16:47"
		},
		{
			"Thithi": "Dashami 07:34",
			"Nakshatram": "Dhanishta 13:06",
			"Rahukalam": "11:28-13:07",
			"Durmuhurtam": "09:09-10:02",
			"Varjam": "21:08-22:56"
		},
		{
			"Thithi": "Ekadashi 09:47",
			"Nakshatram": "Shatabhisha 15:55",
			"Rahukalam": "09:48-11:28",
			"Durmuhurtam": "06:29-08:15",
			"Varjam": "23:06-24:54"
		},
		{
			"Thithi": "Dvadashi 12:13",
			"Nakshatram": "Purvabhadra 18:53",
			"Rahukalam": "18:06-19:46",
			"Durmuhurtam": "18:00-18:53",
			"Varjam": "29:41-31:29"
		},
		{
			"Thithi": "Trayodashi 14:42",
			"Nakshatram": "Uttarabhadra  21:52",
			"Rahukalam": "08:07-09:47",
			"Durmuhurtam": "13:33-14:27, 16:13-17:07",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturdashi 17:07",
			"Nakshatram": "Revati 24:48",
			"Rahukalam": "16:27-18:07",
			"Durmuhurtam": "09:06-09:59",
			"Varjam": "11:20-13:08"
		},
		{
			"Thithi": "Amavasya 19:25",
			"Nakshatram": "Ashwini 27:35",
			"Rahukalam": "13:06-14:47",
			"Durmuhurtam": "12:39-13:33",
			"Varjam": "23:07-24:54"
		},
		{
			"Thithi": "Vaishaka Shukla, Prathama 21:31",
			"Nakshatram": "Bharani 30:09",
			"Rahukalam": "14:47-16:28",
			"Durmuhurtam": "10:52-11:45, 16:14-17:08",
			"Varjam": "14:12-15:59"
		},
		{
			"Thithi": "Dvitiiya 23:22",
			"Nakshatram": "Krittika full night",
			"Rahukalam": "11:25-13:06",
			"Durmuhurtam": "09:03-09:57",
			"Varjam": "19:18-21:04"
		},
		{
			"Thithi": "Tritiiya 24:53",
			"Nakshatram": "Krittika 08:28",
			"Rahukalam": "09:43-11:24",
			"Durmuhurtam": "06:20-08:08",
			"Varjam": "25:46-27:30"
		},
		{
			"Thithi": "26 Chaturthi 26:00",
			"Nakshatram": "Rohini 10:26",
			"Rahukalam": "18:11-19:52",
			"Durmuhurtam": "18:04-18:58",
			"Varjam": "16:24-18:06"
		},
		{
			"Thithi": "Panchami 26:38",
			"Nakshatram": "Mrigashirsha 11:59",
			"Rahukalam": "08:00-09:42",
			"Durmuhurtam": "13:33-14:27",
			"Varjam": "20:45-22:26"
		},
		{
			"Thithi": "Shashthi 26:42",
			"Nakshatram": "Aardra 13:03",
			"Rahukalam": "16:30-18:12",
			"Durmuhurtam": "09:00-09:55",
			"Varjam": "25:17-26:55"
		},
		{
			"Thithi": "Saptami 26:09",
			"Nakshatram": "Punarvasu 13:31",
			"Rahukalam": "13:05-14:48",
			"Durmuhurtam": "12:38-13:33",
			"Varjam": "21:28-23:04"
		},
		{
			"Thithi": "Ashtami 24:57",
			"Nakshatram": "Pushya 13:23",
			"Rahukalam": "14:48-16:30",
			"Durmuhurtam": "10:48-11:43",
			"Varjam": "25:45-27:18"
		}
	],

	"panchangam_may": [{
			"Thithi": "Navami 23:06",
			"Nakshatram": "Aslesha 12:35",
			"Rahukalam": "11:22-13:05",
			"Durmuhurtam": "08:58-09:53",
			"Varjam": "23:52-25:23"
		},
		{
			"Thithi": "Dashami 20:39",
			"Nakshatram": "Magha 11:10",
			"Rahukalam": "09:38-11:22",
			"Durmuhurtam": "06:12-08:02",
			"Varjam": "18:31-19:59"
		},
		{
			"Thithi": "Ekadashi 17:43",
			"Nakshatram": "Purvaphalguni 09:13",
			"Rahukalam": "18:15-19:59",
			"Durmuhurtam": "18:08-19:03",
			"Varjam": "15:42-17:08"
		},
		{
			"Thithi": "Dvadashi 14:24",
			"Nakshatram": "Uttara 06:49, Hasta 28:09",
			"Rahukalam": "07:54-09:37",
			"Durmuhurtam": "13:32-14:28, 16:18-17:14",
			"Varjam": "14:17-15:42"
		},
		{
			"Thithi": "Trayodashi 10:51",
			"Nakshatram": "Chitra 25:21",
			"Rahukalam": "16:32-18:16",
			"Durmuhurtam": "08:55-09:51",
			"Varjam": "11:13-12:38"
		},
		{
			"Thithi": "Chaturdashi 07:15, Purnima 27:45",
			"Nakshatram": "Swathi 22:37",
			"Rahukalam": "13:04-14:49",
			"Durmuhurtam": "12:37-13:32",
			"Varjam": "06:19-07:44"
		},
		{
			"Thithi": "Prathama 24:31",
			"Nakshatram": "Vishaakha 20:08",
			"Rahukalam": "14:49-16:33",
			"Durmuhurtam": "10:45-11:41",
			"Varjam": "23:47-25:15"
		},
		{
			"Thithi": "Dvitiiya 21:45",
			"Nakshatram": "Anuraadha 18:03",
			"Rahukalam": "11:20-13:04",
			"Durmuhurtam": "08:53-09:49",
			"Varjam": "23:18-24:48"
		},
		{
			"Thithi": "Tritiiya  19:34",
			"Nakshatram": "Jyeshtha 16:32",
			"Rahukalam": "09:35-11:19",
			"Durmuhurtam": "06:05-07:57",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturthi 18:05",
			"Nakshatram": "Mula 15:43",
			"Rahukalam": "18:20-20:05",
			"Durmuhurtam": "18:13-19:09",
			"Varjam": "14:10-15:43"
		},
		{
			"Thithi": "Panchami 17:23",
			"Nakshatram": "Purvashadha 15:40",
			"Rahukalam": "07:48-09:34",
			"Durmuhurtam": "13:32-14:29",
			"Varjam": "23:54-25:33"
		},
		{
			"Thithi": "Shashthi 17:29",
			"Nakshatram": "Uttarashadha 16:24",
			"Rahukalam": "16:35-18:21",
			"Durmuhurtam": "08:51-09:47",
			"Varjam": "20:39-22:21"
		},
		{
			"Thithi": "Saptami 18:21",
			"Nakshatram": "Shravana 17:53",
			"Rahukalam": "13:04-14:50",
			"Durmuhurtam": "12:36-13:32",
			"Varjam": "22:14-23:58"
		},
		{
			"Thithi": "Ashtami 19:52",
			"Nakshatram": "Dhanishta 20:00",
			"Rahukalam": "14:50-16:36",
			"Durmuhurtam": "10:43-11:39",
			"Varjam": "27:58-29:45"
		},
		{
			"Thithi": "Navami 21:53",
			"Nakshatram": "Shatabhisha 22:35",
			"Rahukalam": "11:18-13:04",
			"Durmuhurtam": "08:49-09:46",
			"Varjam": "29:45-31:33"
		},
		{
			"Thithi": "Dashami 24:12",
			"Nakshatram": "Purvabhadra  25:28",
			"Rahukalam": "09:31-11:18",
			"Durmuhurtam": "05:59-07:52",
			"Varjam": ""
		},
		{
			"Thithi": "Ekadashi 26:38",
			"Nakshatram": "Uttarabhadra 28:28",
			"Rahukalam": "18:24-20:11",
			"Durmuhurtam": "18:17-19:14",
			"Varjam": "12:16-14:04"
		},
		{
			"Thithi": "Dvadashi 29:01",
			"Nakshatram": "Revati full night",
			"Rahukalam": "07:44-09:31",
			"Durmuhurtam": "13:33-14:30",
			"Varjam": "17:56-19:43"
		},
		{
			"Thithi": "Trayodashi full night",
			"Nakshatram": "Revati 07:23",
			"Rahukalam": "16:38-18:25",
			"Durmuhurtam": "08:48-09:45",
			"Varjam": "29:40-31:27"
		},
		{
			"Thithi": "Trayodashi 07:12",
			"Nakshatram": "Ashwini 10:07",
			"Rahukalam": "13:04-14:52",
			"Durmuhurtam": "12:36-13:33",
			"Varjam": "20:42-22:27"
		},
		{
			"Thithi": "Chaturdashi 09:06",
			"Nakshatram": "Bharani 12:34",
			"Rahukalam": "14:52-16:39",
			"Durmuhurtam": "10:41-11:39",
			"Varjam": "25:36-27:21"
		},
		{
			"Thithi": "Amavasya 10:38",
			"Nakshatram": "Krittika 14:39",
			"Rahukalam": "11:17-13:05",
			"Durmuhurtam": "08:46-09:44, 13:33-14:31",
			"Varjam": ""
		},
		{
			"Thithi": "Jyeshtha Shukla, Prathama 11:47",
			"Nakshatram": "Rohini 16:22",
			"Rahukalam": "09:29-11:17",
			"Durmuhurtam": "05:54-07:49",
			"Varjam": "07:47-09:30"
		},
		{
			"Thithi": "Dvitiiya 12:30",
			"Nakshatram": "Mrigashirsha 17:40",
			"Rahukalam": "18:28-20:16",
			"Durmuhurtam": "18:21-19:19",
			"Varjam": "26:22-28:01"
		},
		{
			"Thithi": "Tritiiya 12:48",
			"Nakshatram": "Aardra 18:32",
			"Rahukalam": "07:41-09:29",
			"Durmuhurtam": "16:27-17:24, 13:34-14:31",
			"Varjam": ""
		},
		{
			"Thithi": "26 Chaturthi 12:39",
			"Nakshatram": "Punarvasu 18:58",
			"Rahukalam": "16:41-18:30",
			"Durmuhurtam": "08:45-09:43",
			"Varjam": "06:45-08:23"
		},
		{
			"Thithi": "Panchami 12:02",
			"Nakshatram": "Pushya 18:57",
			"Rahukalam": "13:05-14:53",
			"Durmuhurtam": "12:36-13:34",
			"Varjam": ""
		},
		{
			"Thithi": "Shashthi 10:57",
			"Nakshatram": "Aslesha 18:28",
			"Rahukalam": "14:54-16:42",
			"Durmuhurtam": "10:41-11:38",
			"Varjam": "07:29-09:03"
		},
		{
			"Thithi": "Saptami 09:25",
			"Nakshatram": "Magha 17:33",
			"Rahukalam": "11:17-13:05",
			"Durmuhurtam": "08:45-09:43, 13:34-14:32",
			"Varjam": "25:06-26:37, 06:00-07:33"
		},
		{
			"Thithi": "Ashtami 07:27, Navami 29:07",
			"Nakshatram": "Purvaphalguni 16:12",
			"Rahukalam": "09:28-11:17",
			"Durmuhurtam": "05:50-07:46",
			"Varjam": "22:54-24:23"
		},
		{
			"Thithi": "Dashami 26:27",
			"Nakshatram": "Uttaraphalguni 14:31",
			"Rahukalam": "18:32-20:21",
			"Durmuhurtam": "18:25-19:23",
			"Varjam": "22:14-23:42"
		}
	],

	"panchangam_june": [{
			"Thithi": "Ekadashi 23:34",
			"Nakshatram": "Hasta 12:33",
			"Rahukalam": "07:39-09:28",
			"Durmuhurtam": "13:35-14:33",
			"Varjam": "19:50-21:17"
		},
		{
			"Thithi": "Dvadashi 20:35",
			"Nakshatram": "Chitra 10:24",
			"Rahukalam": "16:44-18:33",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "15:30-16:57"
		},
		{
			"Thithi": "Trayodashi 17:36",
			"Nakshatram": "Swathi 08:13",
			"Rahukalam": "13:06-14:55",
			"Durmuhurtam": "12:37-13:35",
			"Varjam": "13:19-14:47"
		},
		{
			"Thithi": "Chaturdashi 14:45",
			"Nakshatram": "Vishaakha 06:06, Anuraadha 28:13",
			"Rahukalam": "14:56-16:45",
			"Durmuhurtam": "10:40-11:39, 16:30-17:29",
			"Varjam": "09:48-11:16"
		},
		{
			"Thithi": "Purnima 12:12",
			"Nakshatram": "Jyeshtha 26:42",
			"Rahukalam": "11:17-13:06",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "09:28-10:58"
		},
		{
			"Thithi": "Prathama 10:03",
			"Nakshatram": "Mula 25:41",
			"Rahukalam": "09:27-11:17",
			"Durmuhurtam": "05:48-07:45",
			"Varjam": "24:09-25:41"
		},
		{
			"Thithi": "Dvitiiya 08:25",
			"Nakshatram": "Purvashadha 25:15",
			"Rahukalam": "16:36-20:25",
			"Durmuhurtam": "18:28-19:27",
			"Varjam": "11:06-12:41"
		},
		{
			"Thithi": "Tritiiya 07:26",
			"Nakshatram": "Uttarashadha 25:30",
			"Rahukalam": "07:38-09:27",
			"Durmuhurtam": "13:36-14:35",
			"Varjam": "09:20-10:57"
		},
		{
			"Thithi": "Chaturthi 07:09",
			"Nakshatram": "Shravana 26:27",
			"Rahukalam": "16:47-18:37",
			"Durmuhurtam": "24:11-24:48, 08:44-09:42",
			"Varjam": ""
		},
		{
			"Thithi": "Panchami 07:34",
			"Nakshatram": "Dhanishta 28:05",
			"Rahukalam": "13:07-14:57",
			"Durmuhurtam": "12:38-13:37",
			"Varjam": "06:44-08:26"
		},
		{
			"Thithi": "Shashthi 08:41",
			"Nakshatram": "Shatabhisha full night ",
			"Rahukalam": "14:57-16:47",
			"Durmuhurtam": "10:41-11:40",
			"Varjam": "11:57-13:42"
		},
		{
			"Thithi": "Saptami 10:22",
			"Nakshatram": "Shatabhisha 06:18",
			"Rahukalam": "11:18-13:08",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "13:25-15:11"
		},
		{
			"Thithi": "Ashtami 12:29",
			"Nakshatram": "Purvabhadra  08:58",
			"Rahukalam": "09:28-11:18",
			"Durmuhurtam": "05:48-07:45",
			"Varjam": "19:43-21:31"
		},
		{
			"Thithi": "Navami 14:49",
			"Nakshatram": "Uttarabhadra 11:51",
			"Rahukalam": "18:38-20:29",
			"Durmuhurtam": "18:31-19:30",
			"Varjam": "25:19-27:07"
		},
		{
			"Thithi": "Dashami 17:10",
			"Nakshatram": "Revati 14:47",
			"Rahukalam": "07:38-09:28",
			"Durmuhurtam": "13:38-14:36, 16:34-17:33",
			"Varjam": ""
		},
		{
			"Thithi": "Ekadashi 19:20",
			"Nakshatram": "Ashwini 17:34",
			"Rahukalam": "16:49-18:39",
			"Durmuhurtam": "08:44-09:43",
			"Varjam": "13:06-14:53"
		},
		{
			"Thithi": "Dvadashi 21:09",
			"Nakshatram": "Bharani 20:01",
			"Rahukalam": "13:09-14:59",
			"Durmuhurtam": "12:39-13:38",
			"Varjam": ""
		},
		{
			"Thithi": "Trayodashi 22:31",
			"Nakshatram": "Krittika 22:01",
			"Rahukalam": "14:59-16:49",
			"Durmuhurtam": "10:42-11:41",
			"Varjam": "09:01-10:45"
		},
		{
			"Thithi": "Chaturdashi23:22",
			"Nakshatram": "Rohini 23:32",
			"Rahukalam": "11:19-13:09",
			"Durmuhurtam": "08:45-09:43",
			"Varjam": "15:02-16:44"
		},
		{
			"Thithi": "Amavasya 23:41",
			"Nakshatram": "Mrigashirsha 24:31",
			"Rahukalam": "09:29-11:19",
			"Durmuhurtam": "05:48-07:46",
			"Varjam": ""
		},
		{
			"Thithi": "Ashada Shukla, Prathama 23:29",
			"Nakshatram": "Aardra 25:01",
			"Rahukalam": "18:40-20:31",
			"Durmuhurtam": "18:33-19:32",
			"Varjam": "09:06-10:44"
		},
		{
			"Thithi": "Dvitiiya 22:49",
			"Nakshatram": "Punarvasu 25:03",
			"Rahukalam": "07:39-09:29",
			"Durmuhurtam": "13:39-14:38",
			"Varjam": "13:02-14:38"
		},
		{
			"Thithi": "Tritiiya 21:44",
			"Nakshatram": "Pushya 24:40",
			"Rahukalam": "16:50-18:41",
			"Durmuhurtam": "08:46-09:44",
			"Varjam": "08:55-10:30"
		},
		{
			"Thithi": "Chaturthi 20:17",
			"Nakshatram": "Aslesha 23:56",
			"Rahukalam": "13:10-15:00",
			"Durmuhurtam": "12:41-13:40",
			"Varjam": "13:05-14:38"
		},
		{
			"Thithi": "Panchami 18:33",
			"Nakshatram": "Magha 22:56",
			"Rahukalam": "15:01-16:51",
			"Durmuhurtam": "10:44-11:42",
			"Varjam": "11:26-12:58"
		},
		{
			"Thithi": "26 Shashthi 16:34",
			"Nakshatram": "Purvaphalguni 21:41",
			"Rahukalam": "11:21-13:11",
			"Durmuhurtam": "08:46-09:45",
			"Varjam": "06:31-08:02"
		},
		{
			"Thithi": "Saptami 14:23",
			"Nakshatram": "Uttara  20:16",
			"Rahukalam": "09:31-11:21",
			"Durmuhurtam": "05:51-07:48",
			"Varjam": "28:08-29:38"
		},
		{
			"Thithi": "Ashtami 12:05",
			"Nakshatram": "Hasta 18:44",
			"Rahukalam": "18:41-20:31",
			"Durmuhurtam": "18:34-19:32",
			"Varjam": "26:12-27:42"
		},
		{
			"Thithi": "Navami 09:43",
			"Nakshatram": "Chitra 17:09",
			"Rahukalam": "07:41-09:31",
			"Durmuhurtam": "13:41-14:39",
			"Varjam": "22:23-23:52"
		},
		{
			"Thithi": "Dashami 07:19, Ekadashi 28:59",
			"Nakshatram": "Swathi 15:34",
			"Rahukalam": "16:51-18:41",
			"Durmuhurtam": "08:48-09:46, 24:16-24:53",
			"Varjam": "20:49-22:19"
		}
	],

	"panchangam_july": [{
			"Thithi": "Dwadashi 26:47",
			"Nakshatram": "Vishakha 14:04",
			"Rahukalam": "13:12-15:01",
			"Durmuhurtam": "12:42-13:41",
			"Varjam": "17:51-19:21"
		},
		{
			"Thithi": "Trayodashi 24:46",
			"Nakshatram": "Anuradha 12:43",
			"Rahukalam": "15:02-16:51",
			"Durmuhurtam": "10:45-11:44",
			"Varjam": "18:04-19:36"
		},
		{
			"Thithi": "Chaturdashi 23:04",
			"Nakshatram": "Jyeshta 11:38",
			"Rahukalam": "11:22-13:12",
			"Durmuhurtam": "08:49-09:47, 13:41-14:40",
			"Varjam": ""
		},
		{
			"Thithi": "Poornima 21:44",
			"Nakshatram": "Mula 10:52",
			"Rahukalam": "09:33-11:23",
			"Durmuhurtam": "05:54-07:51",
			"Varjam": "09:19-10:52"
		},
		{
			"Thithi": "Prathama 20:52",
			"Nakshatram": "Purvashada 10:32",
			"Rahukalam": "18:41-20:30",
			"Durmuhurtam": "18:33-19:32",
			"Varjam": "18:35-20:12"
		},
		{
			"Thithi": "Dwitiya 20:32",
			"Nakshatram": "Uttarashada 10:42",
			"Rahukalam": "07:44-09:34",
			"Durmuhurtam": "13:42-14:40, 16:37-17:35",
			"Varjam": "14:49-16:28"
		},
		{
			"Thithi": "Tritiiya 20:49",
			"Nakshatram": "Shravana 11:26",
			"Rahukalam": "16:51-18:40",
			"Durmuhurtam": "08:50-09:49, 24:16-24:54",
			"Varjam": "15:39-17:20"
		},
		{
			"Thithi": "Chaturthi 21:41",
			"Nakshatram": "Dhanishta 12:45",
			"Rahukalam": "13:13-15:02",
			"Durmuhurtam": "12:44-13:42",
			"Varjam": "20:31-22:15"
		},
		{
			"Thithi": "Panchami 23:08",
			"Nakshatram": "Shatabhisha 14:39",
			"Rahukalam": "15:02-16:51",
			"Durmuhurtam": "10:47-11:46, 16:36-17:35",
			"Varjam": "21:41-23:27"
		},
		{
			"Thithi": "Shashthi 25:03",
			"Nakshatram": "Purvabhadra 17:03",
			"Rahukalam": "11:24-13:13",
			"Durmuhurtam": "08:52-09:50, 13:42-14:40",
			"Varjam": "27:45-29:32"
		},
		{
			"Thithi": "Saptami 27:18",
			"Nakshatram": "Uttarabhadra 19:48",
			"Rahukalam": "09:35-11:24",
			"Durmuhurtam": "05:58-07:54",
			"Varjam": ""
		},
		{
			"Thithi": "Ashtami 29:39",
			"Nakshatram": "Revati 22:44",
			"Rahukalam": "18:39-20:28",
			"Durmuhurtam": "18:32-19:30",
			"Varjam": "09:16-11:04"
		},
		{
			"Thithi": "Navami full night",
			"Nakshatram": "Ashwini 25:37",
			"Rahukalam": "07:48-09:36",
			"Durmuhurtam": "13:42-14:40",
			"Varjam": "12:08-22:55"
		},
		{
			"Thithi": "Navami 07:54",
			"Nakshatram": "Bharani 28:13",
			"Rahukalam": "16:50-18:39",
			"Durmuhurtam": "08:53-09:51",
			"Varjam": "12:15-14:02"
		},
		{
			"Thithi": "Dashami 09:49",
			"Nakshatram": "Krittika full night",
			"Rahukalam": "13:14-15:02",
			"Durmuhurtam": "12:45-13:42",
			"Varjam": "17:18-19:03"
		},
		{
			"Thithi": "Ekadashi 11:15",
			"Nakshatram": "Krittika 06:23",
			"Rahukalam": "15:02-16:50",
			"Durmuhurtam": "10:49-11:47",
			"Varjam": "23:26-25:08"
		},
		{
			"Thithi": "Dvadashi 12:03",
			"Nakshatram": "Rohini 07:58",
			"Rahukalam": "11:26-13:14",
			"Durmuhurtam": "08:55-09:52",
			"Varjam": "13:47-15:26"
		},
		{
			"Thithi": "Trayodashi 12:11",
			"Nakshatram": "Mrigashirsha 08:53",
			"Rahukalam": "09:38-11:26",
			"Durmuhurtam": "06:03-07:58",
			"Varjam": "17:23-19:00"
		},
		{
			"Thithi": "Chaturdashi11:40",
			"Nakshatram": "Aardra 09:10",
			"Rahukalam": "18:37-20:24",
			"Durmuhurtam": "18:29-19:27",
			"Varjam": "21:00-22:35"
		},
		{
			"Thithi": "Amavasya 10:32",
			"Nakshatram": "Punarvasu 08:50",
			"Rahukalam": "07:52-09:39",
			"Durmuhurtam": "13:42-14:40",
			"Varjam": "16:34-18:06"
		},
		{
			"Thithi": "Shravana Shukla, Prathama 08:54",
			"Nakshatram": "Pushya 08:00",
			"Rahukalam": "16:48-18:36",
			"Durmuhurtam": "08:57-09:54, 24:16-24:55",
			"Varjam": "20:08-21:39"
		},
		{
			"Thithi": "Dvitiiya 06:52",
			"Nakshatram": "Aslesha 06:45, Magha 29:14",
			"Rahukalam": "13:14-15:01",
			"Durmuhurtam": "12:45-13:42",
			"Varjam": "18:00-19:29"
		},
		{
			"Thithi": "Chaturthi 26:04",
			"Nakshatram": "Purvaphalguni 27:32",
			"Rahukalam": "15:01-16:48",
			"Durmuhurtam": "10:51-11:48",
			"Varjam": "12:40-14:09"
		},
		{
			"Thithi": "Panchami 23:32",
			"Nakshatram": "Uttara 25:48",
			"Rahukalam": "11:27-13:14",
			"Durmuhurtam": "08:58-09:55",
			"Varjam": "10:13-11:42"
		},
		{
			"Thithi": "Shashthi 21:02",
			"Nakshatram": "Hasta 24:07",
			"Rahukalam": "09:41-11:27",
			"Durmuhurtam": "06:08-08:02",
			"Varjam": "09:37-11:06"
		},
		{
			"Thithi": "26 Saptami 18:39",
			"Nakshatram": "Chitra 22:33",
			"Rahukalam": "18:33-20:19",
			"Durmuhurtam": "18:26-19:22",
			"Varjam": "07:36-09:06"
		},
		{
			"Thithi": "Ashtami 16:28",
			"Nakshatram": "Swathi 21:11",
			"Rahukalam": "07:56-09:42",
			"Durmuhurtam": "13:42-14:39",
			"Varjam": "26:31-28:03"
		},
		{
			"Thithi": "Navami 14:29",
			"Nakshatram": "Vishaakha 20:03",
			"Rahukalam": "16:46-18:31",
			"Durmuhurtam": "09:00-09:56",
			"Varjam": "23:54-25:27"
		},
		{
			"Thithi": "Dashami 12:46",
			"Nakshatram": "Anuraadha 19:10",
			"Rahukalam": "13:14-14:59",
			"Durmuhurtam": "12:46-13:42",
			"Varjam": "24:38-26:12"
		},
		{
			"Thithi": "Ekadashi 11:20",
			"Nakshatram": "Jyeshtha 18:35",
			"Rahukalam": "14:59-16:45",
			"Durmuhurtam": "10:53-11:49, 16:31-17:27",
			"Varjam": ""
		},
		{
			"Thithi": "Dvadashi 10:12",
			"Nakshatram": "Mula 18:18",
			"Rahukalam": "11:29-13:14",
			"Durmuhurtam": "09:01-09:57",
			"Varjam": "16:43-18:18"
		}
	],

	"panchangam_aug": [{
			"Thithi": "Trayodashi 09:24",
			"Nakshatram": "Purvashadha 18:22",
			"Rahukalam": "09:44-11:29",
			"Durmuhurtam": "06:14-08:06",
			"Varjam": "26:31-28:09"
		},
		{
			"Thithi": "Chaturdashi 08:59",
			"Nakshatram": "Uttarashadha 18:49",
			"Rahukalam": "18:28-20:13",
			"Durmuhurtam": "18:21-19:27",
			"Varjam": "20:57-24:37"
		},
		{
			"Thithi": "Purnima 08:58",
			"Nakshatram": "Shravana 19:41",
			"Rahukalam": "08:00-09:44",
			"Durmuhurtam": "13:41-14:37",
			"Varjam": "23:54-25:35"
		},
		{
			"Thithi": "Prathama 09:25",
			"Nakshatram": "Dhanishta 21:00",
			"Rahukalam": "16:42-18:26",
			"Durmuhurtam": "09:03-09:59",
			"Varjam": "28:45-30:28"
		},
		{
			"Thithi": "Dvitiiya 10:20",
			"Nakshatram": "Shatabhisha 22:48",
			"Rahukalam": "13:13-14:57",
			"Durmuhurtam": "12:46-13:41",
			"Varjam": "29:48-31:33"
		},
		{
			"Thithi": "Tritiiya 11:45",
			"Nakshatram": "Purvabhadra 25:03",
			"Rahukalam": "14:57-16:41",
			"Durmuhurtam": "10:55-11:50, 16:27-17:22",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturthi 13:36",
			"Nakshatram": "Uttarabhadra 27:42",
			"Rahukalam": "11:29-13:13",
			"Durmuhurtam": "09:05-10:00",
			"Varjam": "11:43-13:29"
		},
		{
			"Thithi": "Panchami 15:48",
			"Nakshatram": "Revati full night",
			"Rahukalam": "09:46-11:30",
			"Durmuhurtam": "06:20-08:10",
			"Varjam": "17:09-18:57"
		},
		{
			"Thithi": "Shashthi 18:13",
			"Nakshatram": "Revati 06:36",
			"Rahukalam": "18:22-20:05",
			"Durmuhurtam": "18:15-19:10",
			"Varjam": "29:06-30:54"
		},
		{
			"Thithi": "Saptami 20:37",
			"Nakshatram": "Ashwini 09:35",
			"Rahukalam": "08:04-09:47",
			"Durmuhurtam": "13:40-14:35",
			"Varjam": "20:20-22:07"
		},
		{
			"Thithi": "Ashtami 22:46",
			"Nakshatram": "Bharani 12:27",
			"Rahukalam": "16:38-18:20",
			"Durmuhurtam": "09:06-10:01",
			"Varjam": "25:41-27:27"
		},
		{
			"Thithi": "Navami 24:28",
			"Nakshatram": "Krittika 14:56",
			"Rahukalam": "13:12-14:55",
			"Durmuhurtam": "12:45-13:40",
			"Varjam": ""
		},
		{
			"Thithi": "Dashami 25:32",
			"Nakshatram": "Rohini 16:52",
			"Rahukalam": "14:54-16:36",
			"Durmuhurtam": "10:56-11:50",
			"Varjam": "08:13-09:57"
		},
		{
			"Thithi": "Ekadashi 25:50",
			"Nakshatram": "Mrigashirsha 18:06",
			"Rahukalam": "11:30-13:12",
			"Durmuhurtam": "09:08-10:02",
			"Varjam": "26:39-28:17"
		},
		{
			"Thithi": "Dvadashi 25:20",
			"Nakshatram": "Aardra 18:33",
			"Rahukalam": "09:49-11:30",
			"Durmuhurtam": "06:26-08:14",
			"Varjam": "30:23-31:58"
		},
		{
			"Thithi": "Trayodashi 24:05",
			"Nakshatram": "Punarvasu 18:14",
			"Rahukalam": "18:15-19:56",
			"Durmuhurtam": "18:08-19:02",
			"Varjam": "25:54-27:26"
		},
		{
			"Thithi": "Chaturdashi22:09",
			"Nakshatram": "Pushya 17:13",
			"Rahukalam": "08:08-09:49",
			"Durmuhurtam": "13:38-14:32",
			"Varjam": "29:10-30:40"
		},
		{
			"Thithi": "Amavasya 19:41",
			"Nakshatram": "Aslesha 15:38",
			"Rahukalam": "16:32-18:13",
			"Durmuhurtam": "09:09-10:03",
			"Varjam": "26:37-28:05"
		},
		{
			"Thithi": "BhadrapadaShukla, Prathama 16:49",
			"Nakshatram": "Magha 13:37",
			"Rahukalam": "13:11-14:51",
			"Durmuhurtam": "12:44-13:38",
			"Varjam": "20:52-22:18"
		},
		{
			"Thithi": "Dvitiiya 13:43",
			"Nakshatram": "Purvaphalguni 11:21",
			"Rahukalam": "14:51-16:31",
			"Durmuhurtam": "10:57-11:50",
			"Varjam": "17:50-19:17"
		},
		{
			"Thithi": "Tritiiya 10:33",
			"Nakshatram": "Uttara 08:59",
			"Rahukalam": "11:30-13:10",
			"Durmuhurtam": "09:10-10:04",
			"Varjam": "16:34-18:01"
		},
		{
			"Thithi": "Chaturthi 07:27, Panchami 28:34",
			"Nakshatram": "Hasta 06:41",
			"Rahukalam": "09:51-14:50",
			"Durmuhurtam": "06:31-08:18",
			"Varjam": "13:59-15:27"
		},
		{
			"Thithi": "Shashthi 26:01",
			"Nakshatram": "Swathi 26:50",
			"Rahukalam": "18:08-19:47",
			"Durmuhurtam": "18:01-18:54",
			"Varjam": "09:47-11:16"
		},
		{
			"Thithi": "Saptami 23:52",
			"Nakshatram": "Vishaakha 25:29",
			"Rahukalam": "08:12-09:51",
			"Durmuhurtam": "13:36-14:29",
			"Varjam": "08:07-09:38"
		},
		{
			"Thithi": "Ashtami 22:09",
			"Nakshatram": "Anuraadha 24:34",
			"Rahukalam": "16:27-18:06",
			"Durmuhurtam": "09:12-10:05",
			"Varjam": "30:04-31:38"
		},
		{
			"Thithi": "26 Navami 20:55",
			"Nakshatram": "Jyeshtha 24:07",
			"Rahukalam": "13:09-14:47",
			"Durmuhurtam": "12:43-13:35",
			"Varjam": ""
		},
		{
			"Thithi": "Dashami 20:08",
			"Nakshatram": "Mula 24:07",
			"Rahukalam": "14:47-16:25",
			"Durmuhurtam": "10:58-11:50",
			"Varjam": "22:31-24:07"
		},
		{
			"Thithi": "Ekadashi 19:47",
			"Nakshatram": "Purvashadha 24:33",
			"Rahukalam": "11:30-13:08",
			"Durmuhurtam": "09:13-10:05",
			"Varjam": "09:53-11:31"
		},
		{
			"Thithi": "Dvadashi 19:51",
			"Nakshatram": "Uttarashadha 25:22",
			"Rahukalam": "09:53-11:30",
			"Durmuhurtam": "06:37-08:21",
			"Varjam": "08:49-10:28"
		},
		{
			"Thithi": "Trayodashi 20:19",
			"Nakshatram": "Shravana 26:34",
			"Rahukalam": "18:00-19:37",
			"Durmuhurtam": "17:53-18:45",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturdashi21:09",
			"Nakshatram": "Dhanishta 28:08",
			"Rahukalam": "08:16-09:53",
			"Durmuhurtam": "13:33-14:25",
			"Varjam": "06:49-08:32"
		}
	],

	"panchangam_sep": [{
			"Thithi": "Purnima 22:21",
			"Nakshatram": "Shatabhisha 30:04",
			"Rahukalam": "16:21-17:58",
			"Durmuhurtam": "09:15-10:06",
			"Varjam": "11:54-13:38"
		},
		{
			"Thithi": "Prathama 23:57",
			"Nakshatram": "Purvabhadra full night",
			"Rahukalam": "13:07-14:43",
			"Durmuhurtam": "12:41-13:32",
			"Varjam": "13:04-14:49"
		},
		{
			"Thithi": "Dvitiiya 25:53",
			"Nakshatram": "Purvabhadra 08:21",
			"Rahukalam": "14:43-16:19",
			"Durmuhurtam": "10:58-11:49",
			"Varjam": "19:00-20:46"
		},
		{
			"Thithi": "Tritiiya 28:09",
			"Nakshatram": "Uttarabhadra 10:58",
			"Rahukalam": "11:30-13:06",
			"Durmuhurtam": "09:16-10:07",
			"Varjam": "24:24-26:12"
		},
		{
			"Thithi": "Chaturthi 30:37",
			"Nakshatram": "Revati 13:51",
			"Rahukalam": "09:54-11:30",
			"Durmuhurtam": "06:43-08:25",
			"Varjam": ""
		},
		{
			"Thithi": "Panchami full night",
			"Nakshatram": "Ashwini 16:54",
			"Rahukalam": "17:52-19:27",
			"Durmuhurtam": "17:45-18:36",
			"Varjam": "12:23-14:11"
		},
		{
			"Thithi": "Panchami 09:08",
			"Nakshatram": "Bharani 19:56",
			"Rahukalam": "08:20-09:55",
			"Durmuhurtam": "13:30-14:21, 16:03-16:53",
			"Varjam": ""
		},
		{
			"Thithi": "Shashthi 11:33",
			"Nakshatram": "Krittika 22:45",
			"Rahukalam": "16:14-17:49",
			"Durmuhurtam": "09:17-10:08",
			"Varjam": "09:20-11:08"
		},
		{
			"Thithi": "Saptami 13:36",
			"Nakshatram": "Rohini 25:09",
			"Rahukalam": "13:04-14:39",
			"Durmuhurtam": "12:39-13:30",
			"Varjam": "16:21-18:07"
		},
		{
			"Thithi": "Ashtami 15:05",
			"Nakshatram": "Mrigashirsha 26:55",
			"Rahukalam": "14:38-16:12",
			"Durmuhurtam": "10:58-11:49",
			"Varjam": "07:10-08:53"
		},
		{
			"Thithi": "Navami 15:49",
			"Nakshatram": "Aardra 27:55",
			"Rahukalam": "11:30-13:04",
			"Durmuhurtam": "09:18-10:08",
			"Varjam": "11:40-13:20"
		},
		{
			"Thithi": "Dashami 15:44",
			"Nakshatram": "Punarvasu 28:04",
			"Rahukalam": "09:56-11:30",
			"Durmuhurtam": "06:49-08:29",
			"Varjam": "15:59-17:36"
		},
		{
			"Thithi": "Ekadashi 14:46",
			"Nakshatram": "Pushya 27:22",
			"Rahukalam": "17:43-19:16",
			"Durmuhurtam": "17:37-18:26",
			"Varjam": "11:50-13:23"
		},
		{
			"Thithi": "Dvadashi 12:59",
			"Nakshatram": "Aslesha 25:55",
			"Rahukalam": "08:23-09:57",
			"Durmuhurtam": "13:27-14:17",
			"Varjam": "15:24-16:54"
		},
		{
			"Thithi": "Trayodashi 10:30",
			"Nakshatram": "Magha 23:50",
			"Rahukalam": "16:08-17:40",
			"Durmuhurtam": "09:20-10:09",
			"Varjam": "12:43-14:20"
		},
		{
			"Thithi": "Chaturdashi07:26, Amavasya 28:00",
			"Nakshatram": "Purvaphalguni 21:18",
			"Rahukalam": "13:02-14:34",
			"Durmuhurtam": "12:37-13:27",
			"Varjam": "07:00-08:25"
		},
		{
			"Thithi": "Adhika Ashwija Shukla Prathama24:20",
			"Nakshatram": "Uttara 18:30",
			"Rahukalam": "14:24-16:06",
			"Durmuhurtam": "10:59-11:48",
			"Varjam": "25:53-27:17"
		},
		{
			"Thithi": "Dvitiiya 20:40",
			"Nakshatram": "Hasta 15:36",
			"Rahukalam": "11:29-13:01",
			"Durmuhurtam": "09:21-10:10",
			"Varjam": "22:41-24:06"
		},
		{
			"Thithi": "Tritiiya 17:09",
			"Nakshatram": "Chitra 12:50",
			"Rahukalam": "09:58-11:29",
			"Durmuhurtam": "06:55-08:32",
			"Varjam": "17:52-19:18"
		},
		{
			"Thithi": "Chaturthi 13:57",
			"Nakshatram": "Swathi 10:21",
			"Rahukalam": "17:34-19:06",
			"Durmuhurtam": "17:28-18:17",
			"Varjam": "15:29-16:57"
		},
		{
			"Thithi": "Panchami 11:12",
			"Nakshatram": "Vishaakha 08:18, Anuraadha 30:48",
			"Rahukalam": "08:27-09:58",
			"Durmuhurtam": "13:24-14:13, 15:50-16:38",
			"Varjam": "12:03-13:33"
		},
		{
			"Thithi": "Shashthi 09:01",
			"Nakshatram": "Jyeshtha 29:55",
			"Rahukalam": "16:01-17:32",
			"Durmuhurtam": "09:22-10:11",
			"Varjam": "12:12-13:44"
		},
		{
			"Thithi": "Saptami 07:27, Ashtami 30:31",
			"Nakshatram": "Mula 29:39",
			"Rahukalam": "12:59-14:30",
			"Durmuhurtam": "12:35-13:24",
			"Varjam": "28:04-29:39"
		},
		{
			"Thithi": "Navami 30:13",
			"Nakshatram": "Purvashadha 30:01",
			"Rahukalam": "14:29-15:59",
			"Durmuhurtam": "10:59-11:47",
			"Varjam": "15:24-17:01"
		},
		{
			"Thithi": "Dashami 30:30",
			"Nakshatram": "Uttarashadha 30:56",
			"Rahukalam": "11:29-12:59",
			"Durmuhurtam": "09:23-10:11",
			"Varjam": "14:19-15:59"
		},
		{
			"Thithi": "26 Ekadashi fullnight",
			"Nakshatram": "Shravana full night",
			"Rahukalam": "09:59-11:29",
			"Durmuhurtam": "07:00-08:36",
			"Varjam": "11:10-12:51"
		},
		{
			"Thithi": "Ekadashi 07:16",
			"Nakshatram": "Shravana 08:20",
			"Rahukalam": "17:26-18:55",
			"Durmuhurtam": "17:20-18:07",
			"Varjam": "12:38-14:21"
		},
		{
			"Thithi": "Dvadashi 08:29",
			"Nakshatram": "Dhanishta 10:08",
			"Rahukalam": "08:31-10:00",
			"Durmuhurtam": "13:21-14:09",
			"Varjam": "17:59-19:44"
		},
		{
			"Thithi": "Trayodashi 10:03",
			"Nakshatram": "Shatabhisha 12:18",
			"Rahukalam": "15:55-17:23",
			"Durmuhurtam": "09:25-10:12",
			"Varjam": "19:21-21:07"
		},
		{
			"Thithi": "Chaturdashi11:56",
			"Nakshatram": "Purvabhadra 14:45",
			"Rahukalam": "12:57-14:25",
			"Durmuhurtam": "12:34-13:21",
			"Varjam": "25:26-27:12"
		}
	],

	"panchangam_oct": [{
			"Thithi": "Purnima 14:05",
			"Nakshatram": "Uttarabhadra 17:27",
			"Rahukalam": "14:25-15:53",
			"Durmuhurtam": "10:59-11:46",
			"Varjam": "30:54-32:41"
		},
		{
			"Thithi": "Prathama 16:26",
			"Nakshatram": "Revati 20:21",
			"Rahukalam": "11:29-12:56",
			"Durmuhurtam": "09:26-10:13, 13:20-14:07",
			"Varjam": ""
		},
		{
			"Thithi": "Dvitiiya 18:57",
			"Nakshatram": "Ashwini 23:22",
			"Rahukalam": "10:01-11:29",
			"Durmuhurtam": "07:07-08:40",
			"Varjam": "18:52-20:40"
		},
		{
			"Thithi": "Tritiiya 21:32",
			"Nakshatram": "Bharani 26:26",
			"Rahukalam": "17:17-18:44",
			"Durmuhurtam": "17:11-17:58",
			"Varjam": "10:12-12:00"
		},
		{
			"Thithi": "Chaturthi 24:02",
			"Nakshatram": "Krittika 29:24",
			"Rahukalam": "08:35-10:02",
			"Durmuhurtam": "13:19-14:05",
			"Varjam": "15:55-17:43"
		},
		{
			"Thithi": "Panchami 26:17",
			"Nakshatram": "Rohini full night",
			"Rahukalam": "15:48-17:15",
			"Durmuhurtam": "09:28-10:14",
			"Varjam": "23:12-24:58"
		},
		{
			"Thithi": "Shashthi 28:06",
			"Nakshatram": "Rohini 08:06",
			"Rahukalam": "12:55-14:21",
			"Durmuhurtam": "12:32-13:18",
			"Varjam": "14:13-15:58"
		},
		{
			"Thithi": "Saptami 29:19",
			"Nakshatram": "Mrigashirsha 10:20",
			"Rahukalam": "14:21-15:47",
			"Durmuhurtam": "11:21-15:47",
			"Varjam": "19:18-21:00"
		},
		{
			"Thithi": "Ashtami 29:46",
			"Nakshatram": "Aardra 11:57",
			"Rahukalam": "11:29-12:54",
			"Durmuhurtam": "09:29-10:15",
			"Varjam": "24:22-26:02"
		},
		{
			"Thithi": "Navami 29:23",
			"Nakshatram": "Punarvasu 12:48",
			"Rahukalam": "10:03-11:29",
			"Durmuhurtam": "07:13-08:44",
			"Varjam": "20:48-22:24"
		},
		{
			"Thithi": "Dashami 28:09",
			"Nakshatram": "Pushya 12:49",
			"Rahukalam": "17:09-18:34",
			"Durmuhurtam": "17:03-17:49",
			"Varjam": "25:10-26:43"
		},
		{
			"Thithi": "Ekadashi 26:06",
			"Nakshatram": "Aslesha 11:59",
			"Rahukalam": "08:39-10:04",
			"Durmuhurtam": "13:16-14:01",
			"Varjam": "23:12-24:42"
		},
		{
			"Thithi": "Dvadashi 23:21",
			"Nakshatram": "Magha 10:24",
			"Rahukalam": "15:42-17:07",
			"Durmuhurtam": "09:31-10:16",
			"Varjam": "17:40-19:07"
		},
		{
			"Thithi": "Trayodashi 20:03",
			"Nakshatram": "Purvaphalguni 08:11, Uttara  29:28",
			"Rahukalam": "12:53-14:17",
			"Durmuhurtam": "12:31-13:16",
			"Varjam": "14:34-15:59"
		},
		{
			"Thithi": "Chaturdashi16:22",
			"Nakshatram": "Hasta 26:28",
			"Rahukalam": "14:17-15:41",
			"Durmuhurtam": "11:01-11:46",
			"Varjam": "12:49-14:13"
		},
		{
			"Thithi": "Amavasya 12:30",
			"Nakshatram": "Chitra 23:21",
			"Rahukalam": "11:29-12:53",
			"Durmuhurtam": "09:32-10:17",
			"Varjam": "09:26-10:49"
		},
		{
			"Thithi": "Nija Ashwija Prathama 08:38, Dvitiiya 28:57",
			"Nakshatram": "Swathi 20:21",
			"Rahukalam": "10:06-11:29",
			"Durmuhurtam": "07:19-08:48",
			"Varjam": "25:19-26:44"
		},
		{
			"Thithi": "Tritiiya 25:38",
			"Nakshatram": "Vishaakha 17:38",
			"Rahukalam": "17:01-18:25",
			"Durmuhurtam": "16:56-17:40",
			"Varjam": "21:15-22:42"
		},
		{
			"Thithi": "Chaturthi 22:49",
			"Nakshatram": "Anuraadha 15:22",
			"Rahukalam": "08:44-10:07",
			"Durmuhurtam": "13:14-13:58",
			"Varjam": "20:35-22:04"
		},
		{
			"Thithi": "Panchami 20:37",
			"Nakshatram": "Jyeshtha 13:42 RK ",
			"Rahukalam": "15:37-16:59",
			"Durmuhurtam": "09:34-10:18, 23:34-24:26",
			"Varjam": ""
		},
		{
			"Thithi": "Shashthi 19:09",
			"Nakshatram": "Mula 12:43",
			"Rahukalam": "12:52-14:14",
			"Durmuhurtam": "12:30-13:14",
			"Varjam": "11:11-12:43"
		},
		{
			"Thithi": "Saptami 18:27",
			"Nakshatram": "Purvashadha 22:28",
			"Rahukalam": "14:14-15:36",
			"Durmuhurtam": "11:03-11:46",
			"Varjam": "20:38-22:16"
		},
		{
			"Thithi": "Ashtami 18:29",
			"Nakshatram": "Uttarashadha 12:58",
			"Rahukalam": "11:30-12:52",
			"Durmuhurtam": "09:36-10:19",
			"Varjam": "17:09-18:50"
		},
		{
			"Thithi": "Navami 19:12",
			"Nakshatram": "Shravana 14:08",
			"Rahukalam": "10:09-11:30",
			"Durmuhurtam": "07:26-08:53",
			"Varjam": "18:25-20:08"
		},
		{
			"Thithi": "Dashami 20:30",
			"Nakshatram": "Dhanishta 15:53",
			"Rahukalam": "16:55-18:16",
			"Durmuhurtam": "16:49-17:32",
			"Varjam": "23:45-25:30"
		},
		{
			"Thithi": "26 Ekadashi 22:16",
			"Nakshatram": "Shatabhisha 18:06",
			"Rahukalam": "08:49-10:10",
			"Durmuhurtam": "13:13-13:56",
			"Varjam": "25:12-26:58"
		},
		{
			"Thithi": "Dvadashi 24:24",
			"Nakshatram": "Purvabhadra 20:41",
			"Rahukalam": "15:32- 16:53",
			"Durmuhurtam": "09:38-10:21",
			"Varjam": "31:25-33:12"
		},
		{
			"Thithi": "Trayodashi 26:45",
			"Nakshatram": "Uttarabhadra 23:30",
			"Rahukalam": "12:51-14:11",
			"Durmuhurtam": "12:30-13:13",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturdashi29:15",
			"Nakshatram": "Revati 26:27",
			"Rahukalam": "14:11-15:31",
			"Durmuhurtam": "11:04-11:47",
			"Varjam": "12:58-14:46"
		},
		{
			"Thithi": "Purnima full night",
			"Nakshatram": "Ashwini 29:28",
			"Rahukalam": "11:31-12:51",
			"Durmuhurtam": "09:40-10:22",
			"Varjam": "24:58-26:46"
		},
		{
			"Thithi": "Purnima 07:49",
			"Nakshatram": "Bharani full night",
			"Rahukalam": "10:12-11:32",
			"Durmuhurtam": "07:33-08:58",
			"Varjam": "16:15-18:03"
		}
	],

	"panchangam_nov": [{
			"Thithi": "Prathama 09:20",
			"Nakshatram": "Bharani 07:27",
			"Rahukalam": "15:49-17:08",
			"Durmuhurtam": "15:43-16:26",
			"Varjam": "20:53-22:41"
		},
		{
			"Thithi": "Dvitiiya 11:44",
			"Nakshatram": "Krittika 10:20",
			"Rahukalam": "07:54-09:13",
			"Durmuhurtam": "12:12-12:54",
			"Varjam": "28:06-29:53"
		},
		{
			"Thithi": "Tritiiya 13:54",
			"Nakshatram": "Rohini 13:00",
			"Rahukalam": "14:28-15:47",
			"Durmuhurtam": "08:42-09:24",
			"Varjam": "19:09-20:54"
		},
		{
			"Thithi": "Chaturthi 15:44",
			"Nakshatram": "Mrigashirsha 15:21",
			"Rahukalam": "11:51-13:09",
			"Durmuhurtam": "11:30-12:12",
			"Varjam": "24:25-26:08"
		},
		{
			"Thithi": "Panchami 17:06",
			"Nakshatram": "Aardra 17:15",
			"Rahukalam": "13:09-14:27",
			"Durmuhurtam": "10:07-10:48",
			"Varjam": "29:55-31:36"
		},
		{
			"Thithi": "Shashthi 17:53",
			"Nakshatram": "Punarvasu 18:35",
			"Rahukalam": "10:33-11:51",
			"Durmuhurtam": "08:44-09:26",
			"Varjam": "26:48-28:27"
		},
		{
			"Thithi": "Saptami 17:59",
			"Nakshatram": "Pushya 19:15",
			"Rahukalam": "09:16-10:33",
			"Durmuhurtam": "06:40-08:03",
			"Varjam": ""
		},
		{
			"Thithi": "Ashtami 17:21",
			"Nakshatram": "Aslesha 19:12",
			"Rahukalam": "15:44-17:01",
			"Durmuhurtam": "15:38-16:20",
			"Varjam": "08:02-09:38"
		},
		{
			"Thithi": "Navami 15:58",
			"Nakshatram": "Magha 18:26",
			"Rahukalam": "08:00-09:17",
			"Durmuhurtam": "12:12-12:53, 14:15-14:57",
			"Varjam": "06:49-08:22"
		},
		{
			"Thithi": "Dashami 13:52",
			"Nakshatram": "Purvaphalguni 16:58",
			"Rahukalam": "14:25-15:42",
			"Durmuhurtam": "08:47-09:28, 22:29-23:24",
			"Varjam": "23:33-25:01"
		},
		{
			"Thithi": "Ekadashi 11:11",
			"Nakshatram": "Uttara  14:55",
			"Rahukalam": "11:52-13:08",
			"Durmuhurtam": "11:31-12:12",
			"Varjam": "22:26-23:52"
		},
		{
			"Thithi": "Dvadashi 08:00, Trayodashi 28:29",
			"Nakshatram": "Hasta 12:24",
			"Rahukalam": "13:08-14:25",
			"Durmuhurtam": "10:10-10:50, 14:14-14:55",
			"Varjam": "19:28-20:53"
		},
		{
			"Thithi": "Chaturdashi24:48",
			"Nakshatram": "Chitra 09:35, Swathi 30:39",
			"Rahukalam": "10:36-11:52",
			"Durmuhurtam": "08:49-09:29",
			"Varjam": "14:30-15:55"
		},
		{
			"Thithi": "Amavasya 21:07",
			"Nakshatram": "Vishaakha 27:46",
			"Rahukalam": "09:20-10:36",
			"Durmuhurtam": "06:48-08:09",
			"Varjam": "11:34-12:59"
		},
		{
			"Thithi": "Karthika Shukla Prathama 17:36",
			"Nakshatram": "Anuraadha 25:06",
			"Rahukalam": "15:40-16:55",
			"Durmuhurtam": "15:35-16:15",
			"Varjam": "07:19-08:44"
		},
		{
			"Thithi": "Dvitiiya 14:27",
			"Nakshatram": "Jyeshtha 22:51",
			"Rahukalam": "08:06-09:21",
			"Durmuhurtam": "12:13-12:53, 14:14-14:54",
			"Varjam": ""
		},
		{
			"Thithi": "Tritiiya 11:47",
			"Nakshatram": "Mula 21:10",
			"Rahukalam": "14:23-15:39",
			"Durmuhurtam": "08:52-09:32",
			"Varjam": "19:40-21:10"
		},
		{
			"Thithi": "Chaturthi 09:46",
			"Nakshatram": "Purvashadha 20:08",
			"Rahukalam": "11:53-13:08",
			"Durmuhurtam": "11:33-12:13",
			"Varjam": "28:03-29:38"
		},
		{
			"Thithi": "Panchami 08:29",
			"Nakshatram": "Uttarashadha 19:52",
			"Rahukalam": "13:08-14:23",
			"Durmuhurtam": "10:13-10:53",
			"Varjam": "23:57-25:36"
		},
		{
			"Thithi": "Shashthi 08:00",
			"Nakshatram": "Shravana 20:23",
			"Rahukalam": "10:38-11:53",
			"Durmuhurtam": "08:54-09:34",
			"Varjam": "24:36-26:17"
		},
		{
			"Thithi": "Saptami 08:18",
			"Nakshatram": "Dhanishta 21:39",
			"Rahukalam": "09:24-10:39",
			"Durmuhurtam": "06:55-08:15",
			"Varjam": "29:26-31:09"
		},
		{
			"Thithi": "Ashtami 09:21",
			"Nakshatram": "Shatabhisha 23:35",
			"Rahukalam": "15:37-16:51",
			"Durmuhurtam": "15:32-16:12",
			"Varjam": "30:38-32:24"
		},
		{
			"Thithi": "Navami 11:02",
			"Nakshatram": "Purvabhadra 26:02",
			"Rahukalam": "08:11-09:26",
			"Durmuhurtam": "12:14-12:53, 14:13-14:52",
			"Varjam": ""
		},
		{
			"Thithi": "Dashami 13:12",
			"Nakshatram": "Uttarabhadra 28:50",
			"Rahukalam": "14:22-15:37",
			"Durmuhurtam": "08:57-09:36",
			"Varjam": "12:45-14:32"
		},
		{
			"Thithi": "Ekadashi 15:40",
			"Nakshatram": "Revati full night",
			"Rahukalam": "11:55-13:09",
			"Durmuhurtam": "11:35-12:14",
			"Varjam": "18:20-20:08"
		},
		{
			"Thithi": "26 Dvadashi 18:16",
			"Nakshatram": "Revati 07:50",
			"Rahukalam": "13:09-14:22",
			"Durmuhurtam": "10:17-10:56",
			"Varjam": "30:22-32-10"
		},
		{
			"Thithi": "Trayodashi 20:51",
			"Nakshatram": "Ashwini 10:53",
			"Rahukalam": "10:42-11:55",
			"Durmuhurtam": "08:59-09:38",
			"Varjam": "21:39-23:27"
		},
		{
			"Thithi": "Chaturdashi23:17",
			"Nakshatram": "Bharani 13:49",
			"Rahukalam": "09:29-10:42",
			"Durmuhurtam": "07:02-8:20",
			"Varjam": "27:11-28:58"
		},
		{
			"Thithi": "Purnima 25:29",
			"Nakshatram": "Krittika 16:33",
			"Rahukalam": "15:36-16:49",
			"Durmuhurtam": "15:31-16:10",
			"Varjam": ""
		},
		{
			"Thithi": "Prathama 27:22",
			"Nakshatram": "Rohini 19:01",
			"Rahukalam": "08:17-09:30",
			"Durmuhurtam": "12:16-12:55",
			"Varjam": "10:11-11:57"
		}
	],

	"panchangam_dec": [{
			"Thithi": "Dwitiya 28:52",
			"Nakshatram": "Mrigashira 21:08",
			"Rahukalam": "14:23-15:36",
			"Durmuhurtam": "09:02-09:41",
			"Varjam": "30:08-31:51"
		},
		{
			"Thithi": "Tritiya 29:57",
			"Nakshatram": "Aardra 22:51",
			"Rahukalam": "11:57-13:10",
			"Durmuhurtam": "11:38-12:17",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturthi 30:33",
			"Nakshatram": "Punarvasu 24:09",
			"Rahukalam": "13:10-14:23",
			"Durmuhurtam": "10:21-10:59",
			"Varjam": "11:30-13:11"
		},
		{
			"Thithi": "Panchami 30:40",
			"Nakshatram": "Pushya 24:58",
			"Rahukalam": "10:45-11:58",
			"Durmuhurtam": "09:04-09:43",
			"Varjam": "08:25-10:04"
		},
		{
			"Thithi": "Shashthi 30:15",
			"Nakshatram": "Aslesha 25:16",
			"Rahukalam": "09:34-10:46",
			"Durmuhurtam": "07:09-08:26",
			"Varjam": "13:55-15:32"
		},
		{
			"Thithi": "Saptami 29:17",
			"Nakshatram": "Magha 25:02",
			"Rahukalam": "15:36-16:48",
			"Durmuhurtam": "15:31-16:10",
			"Varjam": "13:09-14:44"
		},
		{
			"Thithi": "Ashtami 27:47",
			"Nakshatram": "Purvaphalguni 24:17",
			"Rahukalam": "08:23-09:35",
			"Durmuhurtam": "12:19-12:57, 14:14-14:53",
			"Varjam": "08:47-10:20"
		},
		{
			"Thithi": "Navami 25:47",
			"Nakshatram": "Uttara  23:02",
			"Rahukalam": "14:24-15:36",
			"Durmuhurtam": "09:07-09:45",
			"Varjam": "30:51-32:20"
		},
		{
			"Thithi": "Dashami 23:21",
			"Nakshatram": "Hasta 21:21",
			"Rahukalam": "12:00-13:12",
			"Durmuhurtam": "11:41-12:19",
			"Varjam": "28:40-30:08"
		},
		{
			"Thithi": "Ekadashi 20:34",
			"Nakshatram": "Chitra 19:18",
			"Rahukalam": "13:13-14:25",
			"Durmuhurtam": "10:25-11:03",
			"Varjam": "24:22-25:49"
		},
		{
			"Thithi": "Dvadashi 17:32",
			"Nakshatram": "Swathi 17:00",
			"Rahukalam": "10:49-12:01",
			"Durmuhurtam": "09:09-09:47",
			"Varjam": "22:02-23:28"
		},
		{
			"Thithi": "Trayodashi 14:23",
			"Nakshatram": "Vishaakha 14:34",
			"Rahukalam": "09:38-10:50",
			"Durmuhurtam": "07:14-08:31",
			"Varjam": "18:10-19:37"
		},
		{
			"Thithi": "Chaturdashi11:14",
			"Nakshatram": "Anuraadha 12:10",
			"Rahukalam": "15:37-16:49",
			"Durmuhurtam": "15:33-16:11",
			"Varjam": "17:15-18:42"
		},
		{
			"Thithi": "Amavasya 08:16, Margasira Shukla Prathama 29:36",
			"Nakshatram": "Jyeshtha 09:56",
			"Rahukalam": "08:27-09:39",
			"Durmuhurtam": "12:22-13:00, 14:17-14:55",
			"Varjam": "08:47-10:20"
		},
		{
			"Thithi": "Dvitiiya 27:24",
			"Nakshatram": "Mula 08:01, Purvashadha 30:34",
			"Rahukalam": "14:26-15:38",
			"Durmuhurtam": "09:11-09:49",
			"Varjam": "17:02-18:32"
		},
		{
			"Thithi": "Tritiiya 25:47",
			"Nakshatram": "Uttarashadha 29:43",
			"Rahukalam": "12:04-13:15",
			"Durmuhurtam": "11:44-12:23",
			"Varjam": "14:17-15:49"
		},
		{
			"Thithi": "Chaturthi 24:53",
			"Nakshatram": "Shravana 29:34",
			"Rahukalam": "13:16-14:27",
			"Durmuhurtam": "10:29-11:07, 14:18-14:56",
			"Varjam": "09:41-11:17"
		},
		{
			"Thithi": "Panchami 24:44",
			"Nakshatram": "Dhanishta 30:10",
			"Rahukalam": "10:53-12:05",
			"Durmuhurtam": "09:13-09:51",
			"Varjam": "09:40-11:18"
		},
		{
			"Thithi": "Shashthi 25:22",
			"Nakshatram": "Shatabhisha full night",
			"Rahukalam": "09:42-10:54",
			"Durmuhurtam": "07:19-08:35",
			"Varjam": "13:46-15:28"
		},
		{
			"Thithi": "Saptami 26:45",
			"Nakshatram": "Shatabhisha 07:31",
			"Rahukalam": "15:40-16:52",
			"Durmuhurtam": "15:36-16:14",
			"Varjam": "14:28-16:12"
		},
		{
			"Thithi": "Ashtami 28:44",
			"Nakshatram": "Purvabhadra 09:33",
			"Rahukalam": "08:31-09:43",
			"Durmuhurtam": "12:25-13:03, 14:20-14:58",
			"Varjam": "20:11-21:57"
		},
		{
			"Thithi": "Navami 31:09",
			"Nakshatram": "Uttarabhadra 12:07",
			"Rahukalam": "14:30-15:41",
			"Durmuhurtam": "09:15-09:53, 22:40-23:38",
			"Varjam": "25:35-27:23"
		},
		{
			"Thithi": "Dashami full night ",
			"Nakshatram": "Revati 15:03",
			"Rahukalam": "12:07-13:19",
			"Durmuhurtam": "11:48-12:26",
			"Varjam": ""
		},
		{
			"Thithi": "Dashami 09:47",
			"Nakshatram": "Ashwini 18:06",
			"Rahukalam": "13:19-14:31",
			"Durmuhurtam": "10:32-11:10, 14:21-15:00",
			"Varjam": "13:36-15:24"
		},
		{
			"Thithi": "Ekadashi 12:24",
			"Nakshatram": "Bharani 21:05",
			"Rahukalam": "10:56-12:08",
			"Durmuhurtam": "09:16-09:54, 12:27-13:05",
			"Varjam": ""
		},
		{
			"Thithi": "26 Dvadashi 14:48",
			"Nakshatram": "Krittika 23:49",
			"Rahukalam": "09:45-10:57",
			"Durmuhurtam": "07:22- 08:38",
			"Varjam": "10:27-12:14"
		},
		{
			"Thithi": "Trayodashi 16:50",
			"Nakshatram": "Rohini 26:09",
			"Rahukalam": "15:44-16:56",
			"Durmuhurtam": "15:40-16:18",
			"Varjam": "17:23-19:08"
		},
		{
			"Thithi": "Chaturdashi18:24",
			"Nakshatram": "Mrigashirsha 28:02",
			"Rahukalam": "08:34-09:46",
			"Durmuhurtam": "08:34-09:46, 14:24-15:02",
			"Varjam": "08:12-09:55"
		},
		{
			"Thithi": "Purnima 19:28",
			"Nakshatram": "Aardra 29:25",
			"Rahukalam": "14:34-15:46",
			"Durmuhurtam": "09:18-09:56, 22:44-23:41",
			"Varjam": "12:55-14:37"
		},
		{
			"Thithi": "Prathama 20:00",
			"Nakshatram": "Punarvasu 30:19",
			"Rahukalam": "12:11-13:22",
			"Durmuhurtam": "11:51-12:30",
			"Varjam": "17:52-19:31"
		},
		{
			"Thithi": "Dvitiiya 20:03",
			"Nakshatram": "Pushya 30:45",
			"Rahukalam": "13:23-14:35",
			"Durmuhurtam": "10:35-11:13, 14:25-15:04",
			"Varjam": "14:27-16:05"
		}
	]
}

def thithi(request):
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(request),bot)
        chat_id = update.message.chat_id
        complete_message = update.message.text.split(' ')
        if complete_message[0] == '/tithi':
            try:
                #date_string = f"{datetime.datetime.today().date():%m-%d-%Y}" if str.upper(complete_message[1]) == 'TODAY' else complete_message[1]
                if len(complete_message) == 1:
                    date_string = f"{datetime.datetime.now(timezone('US/Pacific')):%m-%d-%Y}"
                elif str.upper(complete_message[1]) == 'TODAY':
                    date_string = f"{datetime.datetime.now(timezone('US/Pacific')):%m-%d-%Y}"
                else:
                    date_string = complete_message[1]
                #print("date received: ", date_string)
                date_check = datetime.datetime.strptime(date_string,"%m-%d-%Y")
            except:
                res_text = 'Please enter a valid date in mm-dd-yyyy format'
            else:
                r_date = date_string.split('-')
                if(r_date[2] != '2020'):
                   res_text = 'I can only give you 2020 details'
                else:
                   try:
                       r_d = int(r_date[1]) - 1
                       r_m = int(r_date[0]) - 1
                   except:
                       res_text = 'Invalid date in the request, please use /help'
                   else:
                       ar = "panchangam_" + months[r_m]
                       i_data = "   Date:  " + date_string + "\n"
                       t_data = "Thithi: " + source_data[ar][r_d]['Thithi'] +  "\n" 
                       n_data = "Nakshatram: " + source_data[ar][r_d]['Nakshatram'] +  "\n"
                       r_data = "Rahukalam: " + source_data[ar][r_d]['Rahukalam'] +  "\n"
                       d_data = "Durmuhurtam: " + source_data[ar][r_d]['Durmuhurtam'] +  "\n"
                       v_data = "Varjam: " + source_data[ar][r_d]['Varjam'] +  "\n"
                       res_text = i_data + t_data + n_data + r_data + d_data + v_data
        elif complete_message[0] == '/start':
            res_text = 'Hello! I am bot, please use /help to know what I can do'
        elif complete_message[0] == '/help':
            res_text = '\nI give the Tithi,  Nakshatra and other details for the given date of the current year(2020).\n To request send a command as /tithi <mm-dd-yyyy> \n If no date is provided, it will use current date in PST zone.\n\n All the times mentioned are in PST'
        else:
            res_text = 'Invalid command entered, please use /help'
            
        bot.sendMessage(chat_id=chat_id,text=res_text)
    return f'ok'