import os 
import telegram
import datetime

bot = telegram.Bot(token=os.environ["TOKEN"])
months = list(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
source_data = {
	"panchangam_jan": [{
			"Thithi": "Ekadashi 11:58",
			"Nakshatram": "Vishakha 08:10",
			"Rahukalam": "14:34-15:45",
			"Durmuhurtam": "09:21-09:59",
			"Varjam": "24:24-26:06"
		},
		{
			"Thithi": "Dwadashi 12:40",
			"Nakshatram": "Anuradha 21:33",
			"Rahukalam": "12:12-13:24",
			"Durmuhurtam": "11:53-12:31",
			"Varjam": "27:35-29:18"
		},
		{
			"Thithi": "Trayodashi 13:51",
			"Nakshatram": "Jyeshta 23:23",
			"Rahukalam": "13:24-14:37",
			"Durmuhurtam": "10:36-11:14",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturdashi 15:27",
			"Nakshatram": "Mula 25:37",
			"Rahukalam": "11:00-12:13",
			"Durmuhurtam": "09:19-09:58",
			"Varjam": "23:52-25-37"
		},
		{
			"Thithi": "Amavasya 17:28",
			"Nakshatram": "Purvashada 28:13",
			"Rahukalam": "09:48-11:01",
			"Durmuhurtam": "07:24-08:41",
			"Varjam": "12:15-14:02"
		},
		{
			"Thithi": "Pausha Shukla, Prathama 19:48",
			"Nakshatram": "Uttarashada 31:06",
			"Rahukalam": "15:51-17:04",
			"Durmuhurtam": "15:46-16:25",
			"Varjam": "13:10-14:58"
		},
		{
			"Thithi": "Dwitiya 22:24",
			"Nakshatram": "Shravana Full Night",
			"Rahukalam": "08:36-09:49",
			"Durmuhurtam": "12:33-13:12",
			"Varjam": "11:36-13:25"
		},
		{
			"Thithi": "Tritiya 25:08",
			"Nakshatram": "Shravana 10:10",
			"Rahukalam": "14:40-15:53",
			"Durmuhurtam": "09:20-09:59",
			"Varjam": "14:42-16:30"
		},
		{
			"Thithi": "Chaturthi 27:52",
			"Nakshatram": "Dhanishta 13:19",
			"Rahukalam": "12:15-13:28",
			"Durmuhurtam": "11:55-12:34",
			"Varjam": "21:27-23:15"
		},
		{
			"Thithi": "Panchami 30:24",
			"Nakshatram": "Sathabhisha 16:24",
			"Rahukalam": "13:28-14:41",
			"Durmuhurtam": "10:38-11:17",
			"Varjam": "23:33-25:20"
		},
		{
			"Thithi": "Shashti Full Night",
			"Nakshatram": "Purvabhadra 19:13",
			"Rahukalam": "11:03-12:16",
			"Durmuhurtam": "09:20-09:59, 12:35-13:14",
			"Varjam": ""
		},
		{
			"Thithi": "Shashti 08:34",
			"Nakshatram": "Uttarabhadra 21:36",
			"Rahukalam": "09:50-11:03",
			"Durmuhurtam": "07:23-08:41",
			"Varjam": "None"
		},
		{
			"Thithi": "Saptami 10:12",
			"Nakshatram": "Revati 23:22",
			"Rahukalam": "15:57-17:10",
			"Durmuhurtam": "15:52-16:31",
			"Varjam": "10:29-12:12"
		},
		{
			"Thithi": "Ashtami 11:07",
			"Nakshatram": "Ashvini 24:26",
			"Rahukalam": "08:36-09:50",
			"Durmuhurtam": "12:36-13:16",
			"Varjam": "20:15-21:55"
		},
		{
			"Thithi": "Navami 11:15",
			"Nakshatram": "Bharani 24:42",
			"Rahukalam": "14:45-15:59",
			"Durmuhurtam": "09:20-10:00",
			"Varjam": "10:08-11:45"
		},
		{
			"Thithi": "Dashami 10:33",
			"Nakshatram": "Krittika 24:10",
			"Rahukalam": "12:18-13:32",
			"Durmuhurtam": "11:58-12:37",
			"Varjam": "12:26-14:00"
		},
		{
			"Thithi": "Ekadashi 09:04, Dwadashi 30:52",
			"Nakshatram": "Rohini 22:55",
			"Rahukalam": "",
			"Durmuhurtam": "10:39-11:19",
			"Varjam": "15:20-16:51"
		},
		{
			"Thithi": "Trayodashi 28:04",
			"Nakshatram": "Mrigashira 21:01",
			"Rahukalam": "11:04-12:18",
			"Durmuhurtam": "09:20-10:00, 12:38-13:18",
			"Varjam": ""
		},
		{
			"Thithi": "Chaturdashi 24:49",
			"Nakshatram": "Aardra 18:37",
			"Rahukalam": "09:50-11:04",
			"Durmuhurtam": "07:21-08:40",
			"Varjam": "29:14-30:39"
		},
		{
			"Thithi": "Purnima 21:15",
			"Nakshatram": "Punarvasu 15:52",
			"Rahukalam": "16:03-17:18",
			"Durmuhurtam": "15:58-16:38",
			"Varjam": "22:54-24:18"
		},
		{
			"Thithi": "Pratipath 17:34",
			"Nakshatram": "Pushya 12:57",
			"Rahukalam": "08:34-09:49",
			"Durmuhurtam": "12:39-13:19",
			"Varjam": "24:11-25:36"
		},
		{
			"Thithi": "Dwitiya 13:56",
			"Nakshatram": "Ashlesha 10:01, Magha 31:16",
			"Rahukalam": "14:50-16:05",
			"Durmuhurtam": "09:19-09:59",
			"Varjam": "20:39-22:04"
		},
		{
			"Thithi": "Tritiya 10:29",
			"Nakshatram": "Purvaphalguni 28:51",
			"Rahukalam": "12:20-13:35",
			"Durmuhurtam": "12:00-12:40",
			"Varjam": "14:28-15:54"
		},
		{
			"Thithi": "Chaturthi 07:23, Panchami 28:48",
			"Nakshatram": "Uttara 26:55",
			"Rahukalam": "13:35-14:51",
			"Durmuhurtam": "10:39-11:20",
			"Varjam": "11:28-12:56"
		},
		{
			"Thithi": "Shashti 26:49",
			"Nakshatram": "Hasta 25:34",
			"Rahukalam": "11:04-12:20",
			"Durmuhurtam": "09:18-09:59",
			"Varjam": "10:50-12:21"
		},
		{
			"Thithi": "Saptami 25:32",
			"Nakshatram": "Chitra 24:54",
			"Rahukalam": "09:48-11:04",
			"Durmuhurtam": "07:17-08:38",
			"Varjam": "09:21-10:54"
		},
		{
			"Thithi": "Ashtami 24:59",
			"Nakshatram": "Swathi 24:58",
			"Rahukalam": "16:09-17:25",
			"Durmuhurtam": "16:04-16:45",
			"Varjam": "30:45-32:24"
		},
		{
			"Thithi": "Navami 25:10",
			"Nakshatram": "Vishakha 25:44",
			"Rahukalam": "08:32-09:48",
			"Durmuhurtam": "12:41-13:22",
			"Varjam": "29:58-31:40"
		},
		{
			"Thithi": "Dashami 26:03",
			"Nakshatram": "Anuradha 27:10",
			"Rahukalam": "14:54-16:11",
			"Durmuhurtam": "09:17-09:58",
			"Varjam": "None"
		},
		{
			"Thithi": "Ekadashi 27:31",
			"Nakshatram": "Jyeshta 29:10",
			"Rahukalam": "12:21-13:38",
			"Durmuhurtam": "12:01-12:42",
			"Varjam": "09:14-10:58"
		},
		{
			"Thithi": "Dwadashi 29:29",
			"Nakshatram": "Mula Full Night",
			"Rahukalam": "13:38-14:55",
			"Durmuhurtam": "10:38-11:20",
			"Varjam": "29:51-31:37"
		}
	],

	"panchangam_feb": [{
			"Thithi": "Trayodashi Full N",
			"Nakshatram": "Mula 07:37",
			"Rahukalam": "11:04-12:21",
			"Durmuhurtam": "09:16-09:57",
			"Varjam": "18:20-20:07"
		},
		{
			"Thithi": "Trayodashi 07:48",
			"Nakshatram": "Purvashada 10:24",
			"Rahukalam": "09:46-11:04",
			"Durmuhurtam": "07:11-08:34",
			"Varjam": "19:24-21:12"
		},
		{
			"Thithi": "Chaturdashi 10:22",
			"Nakshatram": "Uttarashada 13:25",
			"Rahukalam": "16:15-17:33",
			"Durmuhurtam": "16:10-16:51",
			"Varjam": "17:56-19:44"
		},
		{
			"Thithi": "Amavasya 13:03",
			"Nakshatram": "Shravana 16:31",
			"Rahukalam": "08:28-09:46",
			"Durmuhurtam": "12:43-13:24",
			"Varjam": "21:02-22:51"
		},
		{
			"Thithi": "Magha Shukla Pratipath 15:45",
			"Nakshatram": "Dhanishta 19:38",
			"Rahukalam": "14:59-16:17",
			"Durmuhurtam": "09:14-09:56",
			"Varjam": "27:44-29:32"
		},
		{
			"Thithi": "Dwitiya 18:22",
			"Nakshatram": "Satabhisha 22:39",
			"Rahukalam": "12:22-13:41",
			"Durmuhurtam": "12:01-12:43",
			"Varjam": "29:48-31:35"
		},
		{
			"Thithi": "Tritiya 20:48",
			"Nakshatram": "Purvabhadra 25:28",
			"Rahukalam": "",
			"Durmuhurtam": "Dur",
			"Varjam": "Var"
		},
		{
			"Thithi": "Chaturthi 22:55",
			"Nakshatram": "Uttarabhadra 28:00",
			"Rahukalam": "11:03-12:22",
			"Durmuhurtam": "09:12-09:54",
			"Varjam": "12:05-13:51"
		},
		{
			"Thithi": "Panchami 24:39",
			"Nakshatram": "Revathi 30:07",
			"Rahukalam": "09:43-11:03",
			"Durmuhurtam": "07:05-08:29",
			"Varjam": "17:03-18:48"
		},
		{
			"Thithi": "Shashti 25:50",
			"Nakshatram": "Ashwini Full Night",
			"Rahukalam": "16:21-17:41",
			"Durmuhurtam": "16:16-16:58",
			"Varjam": "27:26-29:09"
		},
		{
			"Thithi": "Saptami 26:24",
			"Nakshatram": "Ashwini 07:42",
			"Rahukalam": "08:22-09:42",
			"Durmuhurtam": "12:43-13:26",
			"Varjam": "17:42-19:21"
		},
		{
			"Thithi": "Ashtami 26:16",
			"Nakshatram": "Bharani 08:40",
			"Rahukalam": "15:02-16:23",
			"Durmuhurtam": "09:10-09:52",
			"Varjam": "20:49-22:26"
		},
		{
			"Thithi": "Navami 25:24",
			"Nakshatram": "Krittika 08:57",
			"Rahukalam": "12:22-13:43",
			"Durmuhurtam": "12:01-12:44",
			"Varjam": "24:40-26:14"
		},
		{
			"Thithi": "Dashami 23:48",
			"Nakshatram": "Rohini 08:31",
			"Rahukalam": "13:43-15:03",
			"Durmuhurtam": "10:34-11:17",
			"Varjam": "13:51-15:22"
		},
		{
			"Thithi": "Ekadashi 21:32",
			"Nakshatram": "Mrigashira 07:22, Aardra 29:35",
			"Rahukalam": "11:01-12:22",
			"Durmuhurtam": "09:08-09:51",
			"Varjam": "15:09-16:38"
		},
		{
			"Thithi": "Dwadashi 18:40",
			"Nakshatram": "Punarvasu 27:15",
			"Rahukalam": "09:39-11:01",
			"Durmuhurtam": "06:57-08:24",
			"Varjam": "16:25-17:52"
		},
		{
			"Thithi": "Trayodashi 15:20",
			"Nakshatram": "Pushya 24:31",
			"Rahukalam": "16:27-17:48",
			"Durmuhurtam": "16:21-17:05",
			"Varjam": "10:21-11:46"
		},
		{
			"Thithi": "Chaturdashi 11:41",
			"Nakshatram": "Ashlesha 21:33",
			"Rahukalam": "08:16-09:38",
			"Durmuhurtam": "12:44-13:27",
			"Varjam": "11:44-13:08"
		},
		{
			"Thithi": "Poornima 07:53, Prathama 28:06",
			"Nakshatram": "Magha 18:30",
			"Rahukalam": "15:06-16:28",
			"Durmuhurtam": "09:05-09:48",
			"Varjam": "08:01-09:25"
		},
		{
			"Thithi": "Dwitiya 24:31",
			"Nakshatram": "Pubba 15:34",
			"Rahukalam": "12:22-13:44",
			"Durmuhurtam": "12:00-12:44",
			"Varjam": "21:58-23:24"
		},
		{
			"Thithi": "Tritiya 21:20",
			"Nakshatram": "Uttara 12:56",
			"Rahukalam": "13:44-15:07",
			"Durmuhurtam": "10:31-11:15",
			"Varjam": "20:35-22:02"
		},
		{
			"Thithi": "Chaturthi 18:40",
			"Nakshatram": "Hasta 10:47",
			"Rahukalam": "10:58-12:21",
			"Durmuhurtam": "09:02-09:46",
			"Varjam": "18:17-19:47"
		},
		{
			"Thithi": "Panchami 16:43",
			"Nakshatram": "Chitra 09:17",
			"Rahukalam": "09:35-10:58",
			"Durmuhurtam": "06:48-08:17",
			"Varjam": "14:42-16:15"
		},
		{
			"Thithi": "Shashti 15:34",
			"Nakshatram": "Swathi 08:32",
			"Rahukalam": "16:32-17:55",
			"Durmuhurtam": "16:26-17:11",
			"Varjam": "14:09-15:46"
		},
		{
			"Thithi": "Saptami 15:16",
			"Nakshatram": "Vishakha 08:38",
			"Rahukalam": "08:09-09:33",
			"Durmuhurtam": "12:43-13:28",
			"Varjam": "12:47-14:27"
		},
		{
			"Thithi": "Ashtami 15:50",
			"Nakshatram": "Anuradha 09:33",
			"Rahukalam": "15:09-16:33",
			"Durmuhurtam": "08:59-09:44",
			"Varjam": "15:33-17:16"
		},
		{
			"Thithi": "Navami 17:10",
			"Nakshatram": "Jyeshta 11:15",
			"Rahukalam": "12:21-13:45",
			"Durmuhurtam": "11:58-12:43",
			"Varjam": "None"
		},
		{
			"Thithi": "Dashami 19:09",
			"Nakshatram": "Mula 13:36",
			"Rahukalam": "13:45-15:10",
			"Durmuhurtam": "10:27-11:13",
			"Varjam": "11:50-13:36"
		}
	],


	"panchangam_mar": [{
			"Thithi": "Ekadashi 21:34",
			"Nakshatram": "Purvashada 16:24",
			"Rahukalam": "10:55-12:20",
			"Durmuhurtam": "08:56-09:42",
			"Varjam": "25:26-27:14"
		},
		{
			"Thithi": "Dwadashi 24:14",
			"Nakshatram": "Uttarashada 19:29",
			"Rahukalam": "09:29-10:55",
			"Durmuhurtam": "06:39-08:10",
			"Varjam": "24:01-25:50"
		},
		{
			"Thithi": "Trayodashi 26:58",
			"Nakshatram": "Sravana 22:40",
			"Rahukalam": "16:37-18:02",
			"Durmuhurtam": "16:31-17:17",
			"Varjam": "27:11-28:59"
		},
		{
			"Thithi": "Chaturdashi 29:37",
			"Nakshatram": "Dhanishta 25:46",
			"Rahukalam": "08:02-09:28",
			"Durmuhurtam": "12:43-13:28",
			"Varjam": "None"
		},
		{
			"Thithi": "Amavasya Full Night",
			"Nakshatram": "Shatabhisha 28:43",
			"Rahukalam": "15:12-16:38",
			"Durmuhurtam": "08:52-09:38",
			"Varjam": "09:51-11:39"
		},
		{
			"Thithi": "Amavasya 08:03",
			"Nakshatram": "Purvabhadra Full Night",
			"Rahukalam": "12:19-13:46",
			"Durmuhurtam": "11:56-12:42",
			"Varjam": "11:50-13:36"
		},
		{
			"Thithi": "Phalguna Shukla Pratipath 10:13",
			"Nakshatram": "Purvabhadra 07:24",
			"Rahukalam": "13:46-15:13",
			"Durmuhurtam": "10:23-11:09",
			"Varjam": "17:57-19:42"
		},
		{
			"Thithi": "Dwitiya 12:04",
			"Nakshatram": "Uttarabhadra 09:46",
			"Rahukalam": "10:52-12:19",
			"Durmuhurtam": "08:50-09:36",
			"Varjam": "22:47-24:31"
		},
		{
			"Thithi": "Tritiya 13:32",
			"Nakshatram": "Revati 11:48",
			"Rahukalam": "09:24-10:51",
			"Durmuhurtam": "06:29-08:02",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturthi 15:36",
			"Nakshatram": "Ashwini 14:27",
			"Rahukalam": "17:41-19:09",
			"Durmuhurtam": "17:35-18:22",
			"Varjam": "10:10-11:53"
		},
		{
			"Thithi": "Panchami 16:13",
			"Nakshatram": "Bharani 15:40",
			"Rahukalam": "08:54-10:22",
			"Durmuhurtam": "13:41-14:28",
			"Varjam": "28:01-29:40"
		},
		{
			"Thithi": "Shashti 16:19",
			"Nakshatram": "Krittika 16:23",
			"Rahukalam": "16:14-17:43",
			"Durmuhurtam": "09:46-10:33",
			"Varjam": "None"
		},
		{
			"Thithi": "Saptami 15:53",
			"Nakshatram": "Rohini 16:35",
			"Rahukalam": "13:17-14:46",
			"Durmuhurtam": "12:54-13:41",
			"Varjam": "08:31-10:07"
		},
		{
			"Thithi": "Ashtami 14:51",
			"Nakshatram": "Mrigashira 16:12",
			"Rahukalam": "14:46-16:15",
			"Durmuhurtam": "11:19-12:06 16:03-16:51",
			"Varjam": ""
		},
		{
			"Thithi": "Navami 13:14",
			"Nakshatram": "Aardra 15:14",
			"Rahukalam": "11:48-13:17",
			"Durmuhurtam": "09:43-10:30",
			"Varjam": "26:28-27:58"
		},
		{
			"Thithi": "Dashami 11:02",
			"Nakshatram": "Punarvasu 13:43",
			"Rahukalam": "10:18-11:47",
			"Durmuhurtam": "07:18-08:54",
			"Varjam": "21:02-22:30"
		},
		{
			"Thithi": "Ekadashi 08:20, Dwadashi 29:13",
			"Nakshatram": "Pushya 11:41",
			"Rahukalam": "17:46-19:16",
			"Durmuhurtam": "17:40-18:28",
			"Varjam": "23:12-24:38"
		},
		{
			"Thithi": "Trayodashi 25:48",
			"Nakshatram": "Ashlesha 09:16, Magha 30:35",
			"Rahukalam": "08:46-10:16",
			"Durmuhurtam": "13:40-14:28",
			"Varjam": "19:55-21:20"
		},
		{
			"Thithi": "Chaturdashi 22:14",
			"Nakshatram": "Purvaphalguni 27:47",
			"Rahukalam": "16:17:17:47",
			"Durmuhurtam": "09:39-10:27",
			"Varjam": "13:39-15:03"
		},
		{
			"Thithi": "Purnima 18:42",
			"Nakshatram": "Uttara 25:04",
			"Rahukalam": "13:15-14:46",
			"Durmuhurtam": "12:51-13:40",
			"Varjam": "10:10-11:35"
		},
		{
			"Thithi": "Prathama 15:22",
			"Nakshatram": "Hasta 22:36",
			"Rahukalam": "14:46-16:17",
			"Durmuhurtam": "11:14-12:02",
			"Varjam": "08:36-10:02"
		},
		{
			"Thithi": "Dwitiya 12:25",
			"Nakshatram": "Chitra 20:35",
			"Rahukalam": "11:43-13:15",
			"Durmuhurtam": "09:36-10:24",
			"Varjam": "25:51-27:22"
		},
		{
			"Thithi": "Tritiya 10:02",
			"Nakshatram": "Swati 19:11",
			"Rahukalam": "10:11-11:43",
			"Durmuhurtam": "07:08-08:46",
			"Varjam": "24:38-26:12"
		},
		{
			"Thithi": "Chaturthi 08:21",
			"Nakshatram": "Vishakha 18:33",
			"Rahukalam": "17:50-19:22",
			"Durmuhurtam": "17:44-18:33",
			"Varjam": "22:35-24:12"
		},
		{
			"Thithi": "Panchami 07:30",
			"Nakshatram": "Anuradha 18:45",
			"Rahukalam": "08:37-10:09",
			"Durmuhurtam": "13:38-14:28",
			"Varjam": "24:36-26:16"
		},
		{
			"Thithi": "Shashti 07:31",
			"Nakshatram": "Jyeshta 19:49",
			"Rahukalam": "16:19-17:51",
			"Durmuhurtam": "09:32-10:21",
			"Varjam": "None"
		},
		{
			"Thithi": "Saptami 08:25",
			"Nakshatram": "Mula 21:40",
			"Rahukalam": "13:13-14:46",
			"Durmuhurtam": "12:49-13:38",
			"Varjam": "19:57-21:40"
		},
		{
			"Thithi": "Ashtami 10:04",
			"Nakshatram": "Purvashada 24:11",
			"Rahukalam": "14:46-16:19",
			"Durmuhurtam": "11:09-11:58",
			"Varjam": "08:16-10:02"
		},
		{
			"Thithi": "Navami 12:18",
			"Nakshatram": "Uttarashada 27:07",
			"Rahukalam": "11:39-13:13",
			"Durmuhurtam": "09:28-10:18",
			"Varjam": "09:10-10:57"
		},
		{
			"Thithi": "Dashami 14:53",
			"Nakshatram": "Shravana 30:16",
			"Rahukalam": "10:05-11:39",
			"Durmuhurtam": "06:57-08:37",
			"Varjam": "07:39-09:28"
		},
		{
			"Thithi": "Ekadashi 17:34",
			"Nakshatram": "Dhanishta Full Night",
			"Rahukalam": "17:54-19:28",
			"Durmuhurtam": "17:48-18:38",
			"Varjam": "10:48-12:36"
		}
	],

	"panchangam_april": [{
			"Thithi": "Dwadashi 20:08",
			"Nakshatram": "Dhanishta 09:24",
			"Rahukalam": "08:29-10:03",
			"Durmuhurtam": "13:37-14:27",
			"Varjam": "17:29-19:16"
		},
		{
			"Thithi": "Trayodashi 22:26",
			"Nakshatram": "Shatabhisha 12:19",
			"Rahukalam": "16:21-17:55",
			"Durmuhurtam": "09:24-10:15",
			"Varjam": "19:25-21:11"
		},
		{
			"Thithi": "Chaturdashi 24:21",
			"Nakshatram": "Purvabhadra 14:54",
			"Rahukalam": "13:11-14:46",
			"Durmuhurtam": "12:46-13:37",
			"Varjam": "25:23-27:08"
		},
		{
			"Thithi": "Amavasya 25:50",
			"Nakshatram": "Uttarabhadra 17:06",
			"Rahukalam": "14:46-16:21",
			"Durmuhurtam": "11:04-11:55",
			"Varjam": "29:59-31:42"
		},
		{
			"Thithi": "Chaitra Shukla, Prathama 26:53",
			"Nakshatram": "Revathi 18:52",
			"Rahukalam": "11:35-13:11",
			"Durmuhurtam": "09:21-10:12, 13:36-14:27",
			"Varjam": ""
		},
		{
			"Thithi": "Dwitiya 27:31",
			"Nakshatram": "Ashwini 20:14",
			"Rahukalam": "09:59-11:35",
			"Durmuhurtam": "06:47-08:29",
			"Varjam": "16:00-17:42"
		},
		{
			"Thithi": "Tritiya 27:45",
			"Nakshatram": "Bharani 21:13",
			"Rahukalam": "17:58-19:34",
			"Durmuhurtam": "17:52-18:43",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturthi 27:37",
			"Nakshatram": "Krittika 21:49",
			"Rahukalam": "08:21-09:57",
			"Durmuhurtam": "13:36-14:27",
			"Varjam": "09:31-11:09"
		},
		{
			"Thithi": "Panchami 27:06",
			"Nakshatram": "Rohini 22:03",
			"Rahukalam": "16:23-18:00",
			"Durmuhurtam": "09:17-10:09",
			"Varjam": "13:59-15:35"
		},
		{
			"Thithi": "Shashti 26:11",
			"Nakshatram": "Mrigashira 21:55",
			"Rahukalam": "13:09-14:46",
			"Durmuhurtam": "12:43-13:35",
			"Varjam": "30:08-31:42"
		},
		{
			"Thithi": "Saptami 24:53",
			"Nakshatram": "Ardra 21:24",
			"Rahukalam": "14:46-16:24",
			"Durmuhurtam": "10:59-11:51 16:11-17:02",
			"Varjam": ""
		},
		{
			"Thithi": "Ashtami 23:11",
			"Nakshatram": "Punarvasu 20:28",
			"Rahukalam": "11:31-13:09",
			"Durmuhurtam": "09:15-10:07",
			"Varjam": "08:56-10:28"
		},
		{
			"Thithi": "Navami 21:05",
			"Nakshatram": "Pushya 19:10",
			"Rahukalam": "09:53-11:31",
			"Durmuhurtam": "06:37-08:21",
			"Varjam": "None"
		},
		{
			"Thithi": "Dashami 18:38",
			"Nakshatram": "Ashlesha 17:29",
			"Rahukalam": "18:03-19:41",
			"Durmuhurtam": "17:56-18:48",
			"Varjam": "07:04-08:33"
		},
		{
			"Thithi": "Ekadashi 15:53",
			"Nakshatram": "Magha 15:31",
			"Rahukalam": "08:13-09:51",
			"Durmuhurtam": "13:34-14:27",
			"Varjam": "22:47-24:15"
		},
		{
			"Thithi": "Dwadashi 12:56",
			"Nakshatram": "Purvaphalguni 13:20",
			"Rahukalam": "16:25-18:04",
			"Durmuhurtam": "09:11-10:04",
			"Varjam": "19:52-21:19"
		},
		{
			"Thithi": "Trayodashi 09:54",
			"Nakshatram": "Uttara 11:05",
			"Rahukalam": "13:08-14:46",
			"Durmuhurtam": "12:41-13:34",
			"Varjam": "18:44-20:11"
		},
		{
			"Thithi": "Chaturdashi 06:56, Purnima 28:12",
			"Nakshatram": "Hasta 08:55",
			"Rahukalam": "14:47-16:26",
			"Durmuhurtam": "10:55-11:48",
			"Varjam": "16:16-17:45"
		},
		{
			"Thithi": "Prathama 25:50",
			"Nakshatram": "Chitra 06:59, Swathi 29:28",
			"Rahukalam": "11:28-13:07",
			"Durmuhurtam": "09:08-10:01",
			"Varjam": "12:14-13:44"
		},
		{
			"Thithi": "Dwitiya 24:02",
			"Nakshatram": "Vishakha 28:31",
			"Rahukalam": "09:47-11:27",
			"Durmuhurtam": "06:28-08:14",
			"Varjam": "10:51-12:23"
		},
		{
			"Thithi": "Tritiya 22:55",
			"Nakshatram": "Anuradha 28:15",
			"Rahukalam": "18:07-19:47",
			"Durmuhurtam": "18:00-18:54",
			"Varjam": "08:28-10:03"
		},
		{
			"Thithi": "Chaturthi 22:34",
			"Nakshatram": "Jyeshta 28:46",
			"Rahukalam": "08:05-09:46",
			"Durmuhurtam": "13:33-14:27",
			"Varjam": "09:58-11:36"
		},
		{
			"Thithi": "Panchami 23:02",
			"Nakshatram": "Mula 30:05",
			"Rahukalam": "16:28-18:08",
			"Durmuhurtam": "09:05-09:58",
			"Varjam": "28:24-30:05"
		},
		{
			"Thithi": "Shashti 24:16",
			"Nakshatram": "Purvashada Full Night",
			"Rahukalam": "13:06-14:47",
			"Durmuhurtam": "12:39-13:33",
			"Varjam": "16:30-18:14"
		},
		{
			"Thithi": "Saptami 26:10",
			"Nakshatram": "Purvashada 08:07",
			"Rahukalam": "14:47-16:28",
			"Durmuhurtam": "10:51-11:45",
			"Varjam": "16:59-18:46"
		},
		{
			"Thithi": "Ashtami 28:31",
			"Nakshatram": "Uttarashada 10:44",
			"Rahukalam": "11:24-13:06",
			"Durmuhurtam": "09:02-09:56",
			"Varjam": "15:14-17:02"
		},
		{
			"Thithi": "Navami Full Night",
			"Nakshatram": "Shravana 13:42",
			"Rahukalam": "09:42-11:24",
			"Durmuhurtam": "06:19-08:07",
			"Varjam": "18:13-20:02"
		},
		{
			"Thithi": "Navami 07:04",
			"Nakshatram": "Dhanishta 16:47",
			"Rahukalam": "18:11-19:53",
			"Durmuhurtam": "18:05-18:59",
			"Varjam": "24:53-26:40"
		},
		{
			"Thithi": "Dashami 09:34",
			"Nakshatram": "Shatabhisha 19:45",
			"Rahukalam": "07:59-09:41",
			"Durmuhurtam": "13:33-14:27",
			"Varjam": "26:51-28:37"
		},
		{
			"Thithi": "Ekadashi 11:47",
			"Nakshatram": "Purvabhadra 22:22",
			"Rahukalam": "16:30-18:13",
			"Durmuhurtam": "08:59-09:54",
			"Varjam": "None"
		}
	],

	"panchangam_may": [{
			"Thithi": "Dwadashi 13:05",
			"Nakshatram": "Uttarabhadra 24:32",
			"Rahukalam": "13:05-14:48",
			"Durmuhurtam": "12:38-13:32",
			"Varjam": "08:50-10:34"
		},
		{
			"Thithi": "Trayodashi 14:51",
			"Nakshatram": "Revathi 26:10",
			"Rahukalam": "14:48-16:31",
			"Durmuhurtam": "10:48-11:43",
			"Varjam": "13:21-15:03"
		},
		{
			"Thithi": "Chaturdashi 15:33",
			"Nakshatram": "Ashwini 27:17",
			"Rahukalam": "11:22-13:05",
			"Durmuhurtam": "08:57-09:52",
			"Varjam": "23:06-24:46"
		},
		{
			"Thithi": "Amavasya 15:45",
			"Nakshatram": "Bharani 27:54",
			"Rahukalam": "09:38-11:21",
			"Durmuhurtam": "06:11-08:01",
			"Varjam": "13:08-14:46"
		},
		{
			"Thithi": "Vaishakha Shukla, Prathipath 15:28",
			"Nakshatram": "Krittika 28:06",
			"Rahukalam": "18:16-20:00",
			"Durmuhurtam": "18:09-19:04",
			"Varjam": "16:00-17:37"
		},
		{
			"Thithi": "Dwitiya 14:48",
			"Nakshatram": "Rohini 27:57",
			"Rahukalam": "07:53-09:37",
			"Durmuhurtam": "13:32-14:28",
			"Varjam": "20:00-21:35"
		},
		{
			"Thithi": "Tritiya 13:47",
			"Nakshatram": "Mrigashira 27:29",
			"Rahukalam": "16:33-18:17",
			"Durmuhurtam": "08:54-09:50",
			"Varjam": "09:27-11:01"
		},
		{
			"Thithi": "Chaturthi 12:29",
			"Nakshatram": "Ardra 26:47",
			"Rahukalam": "13:04-14:49",
			"Durmuhurtam": "12:37-13:32",
			"Varjam": "11:39-13:12"
		},
		{
			"Thithi": "Panchami 10:56",
			"Nakshatram": "Punarvasu 25:51",
			"Rahukalam": "14:49-16:34",
			"Durmuhurtam": "10:45-11:41",
			"Varjam": "14:19-15:51"
		},
		{
			"Thithi": "Shashti 09:11",
			"Nakshatram": "Pushya 24:43",
			"Rahukalam": "11:19-13:04",
			"Durmuhurtam": "08:52-09:48",
			"Varjam": "09:28-11:00"
		},
		{
			"Thithi": "Saptami 07:14, Ashtami 29:07",
			"Nakshatram": "Ashlesha 23:25",
			"Rahukalam": "09:34-11:19",
			"Durmuhurtam": "06:04-07:56",
			"Varjam": "12:49-14:20"
		},
		{
			"Thithi": "Navami 26:51",
			"Nakshatram": "Magha 21:57",
			"Rahukalam": "18:20-20:06",
			"Durmuhurtam": "18:13-19:10",
			"Varjam": "10:41-12:11"
		},
		{
			"Thithi": "Dashami 24:29",
			"Nakshatram": "Purva 20:23",
			"Rahukalam": "07:47-09:33",
			"Durmuhurtam": "13:32-14:29",
			"Varjam": "27:06-28:35"
		},
		{
			"Thithi": "Ekadashi 22:05",
			"Nakshatram": "Uttara 18:46",
			"Rahukalam": "16:36-18:22",
			"Durmuhurtam": "08:50-09:47",
			"Varjam": "26:37-28:07"
		},
		{
			"Thithi": "Dwadashi 19:45",
			"Nakshatram": "Hasta 17:12",
			"Rahukalam": "13:04-14:50",
			"Durmuhurtam": "12:36-13:33",
			"Varjam": "24:43-26:13"
		},
		{
			"Thithi": "Trayodashi 17:34",
			"Nakshatram": "Chitra 15:46",
			"Rahukalam": "14:51-16:37",
			"Durmuhurtam": "10:43-11:39",
			"Varjam": "21:06-22:37"
		},
		{
			"Thithi": "Chaturdashi 15:40",
			"Nakshatram": "Swathi 14:37",
			"Rahukalam": "11:18-13:04",
			"Durmuhurtam": "08:49-09:46",
			"Varjam": "20:02-21:35"
		},
		{
			"Thithi": "Purnima 14:11",
			"Nakshatram": "Vishakha 13:52",
			"Rahukalam": "09:31-11:18",
			"Durmuhurtam": "05:58-07:51",
			"Varjam": "17:49-19:24"
		},
		{
			"Thithi": "Prathama 13:12",
			"Nakshatram": "Anuradha 13:37",
			"Rahukalam": "18:25-20:12",
			"Durmuhurtam": "18:18-19:15",
			"Varjam": "19:18-20:56"
		},
		{
			"Thithi": "Dwitiya 12:51",
			"Nakshatram": "Jyeshta 13:59",
			"Rahukalam": "07:43-09:30",
			"Durmuhurtam": "13:33-14:30, 16:24-17:21",
			"Varjam": ""
		},
		{
			"Thithi": "Tritiya 13:10",
			"Nakshatram": "Mula 15:01",
			"Rahukalam": "16:39-18:26",
			"Durmuhurtam": "08:47-09:44",
			"Varjam": "13:21-15:01"
		},
		{
			"Thithi": "Chaturthi 14:10",
			"Nakshatram": "Purvashada 16:43",
			"Rahukalam": "13:05-14:52",
			"Durmuhurtam": "12:36-13:33",
			"Varjam": "25:29-27:14"
		},
		{
			"Thithi": "Panchami 15:48",
			"Nakshatram": "Uttarashada 19:00",
			"Rahukalam": "14:52-16:40",
			"Durmuhurtam": "10:41-11:39",
			"Varjam": "23:28-25:15"
		},
		{
			"Thithi": "Shashti 17:55",
			"Nakshatram": "Shravana 21:45",
			"Rahukalam": "11:17-13:05",
			"Durmuhurtam": "08:46-09:44",
			"Varjam": "26:14-28:02"
		},
		{
			"Thithi": "Saptami 20:19",
			"Nakshatram": "Dhanishta 24:44",
			"Rahukalam": "09:29-11:17",
			"Durmuhurtam": "05:53-07:48",
			"Varjam": "None"
		},
		{
			"Thithi": "Ashtami 22:46",
			"Nakshatram": "Sathabhisha 27:43",
			"Rahukalam": "18:29-20:17",
			"Durmuhurtam": "18:22-19:20",
			"Varjam": "08:49-10:37"
		},
		{
			"Thithi": "Navami 20:01",
			"Nakshatram": "Purvabhadra Full Night",
			"Rahukalam": "07:40-09:29",
			"Durmuhurtam": "13:34-14:32",
			"Varjam": "10:51-12:38"
		},
		{
			"Thithi": "Dashami 26:51",
			"Nakshatram": "Purvabhadra 06:28",
			"Rahukalam": "16:42-18:30",
			"Durmuhurtam": "08:45-09:43",
			"Varjam": "17:00-18:45"
		},
		{
			"Thithi": "Ekadashi 28:08",
			"Nakshatram": "Uttarabhadra 08:48",
			"Rahukalam": "13:05-14:54",
			"Durmuhurtam": "12:36-13:34",
			"Varjam": "21:41-23:24"
		},
		{
			"Thithi": "Dwadashi 28:46",
			"Nakshatram": "Revathi 10:33",
			"Rahukalam": "14:54-16:43",
			"Durmuhurtam": "10:40-11:38",
			"Varjam": "None"
		},
		{
			"Thithi": "Trayodashi 28:46",
			"Nakshatram": "Ashwini 11:42",
			"Rahukalam": "11:17-13:06",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "07:30-09:11"
		}
	],


	"panchangam_june": [{
			"Thithi": "Chaturdashi 28:10",
			"Nakshatram": "Bharani 12:12",
			"Rahukalam": "09:28-11:17",
			"Durmuhurtam": "05:50-07:46",
			"Varjam": "24:10-25:46"
		},
		{
			"Thithi": "Amavasya 27:01",
			"Nakshatram": "Krittika 12:08",
			"Rahukalam": "18:33-20:22",
			"Durmuhurtam": "18:26-19:24",
			"Varjam": "27:46-29:20"
		},
		{
			"Thithi": "Jyeshta Shukla, Prathama 25:27",
			"Nakshatram": "Rohini 11:35",
			"Rahukalam": "07:38-09:28",
			"Durmuhurtam": "13:35-14:33",
			"Varjam": "16:58-18:30"
		},
		{
			"Thithi": "Dwitiya 23:33",
			"Nakshatram": "Mrigashira 10:38",
			"Rahukalam": "16:45-18:34",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "18:36-20:07"
		},
		{
			"Thithi": "Tritiya 21:25",
			"Nakshatram": "Aardra 09:24",
			"Rahukalam": "13:06-14:56",
			"Durmuhurtam": "12:37-13:35",
			"Varjam": "20:41-22:11"
		},
		{
			"Thithi": "Chaturthi 19:07",
			"Nakshatram": "Punarvasu 07:58",
			"Rahukalam": "14:56-16:45",
			"Durmuhurtam": "10:40-11:39",
			"Varjam": "15:27-16:57"
		},
		{
			"Thithi": "Panchami 16:46",
			"Nakshatram": "Pushya 06:26, Ashlesha 28:52",
			"Rahukalam": "11:17-13:07",
			"Durmuhurtam": "08:44-09:42, 13:36-14:34",
			"Varjam": "18:24-19:53"
		},
		{
			"Thithi": "Shashti 14:25",
			"Nakshatram": "Magha 27:19",
			"Rahukalam": "09:27-11:17",
			"Durmuhurtam": "05:48-07:45",
			"Varjam": "16:05-17:35"
		},
		{
			"Thithi": "Saptami 12:06",
			"Nakshatram": "Purvaphalguni 25:51",
			"Rahukalam": "18:36-20:26",
			"Durmuhurtam": "18:29-19:28",
			"Varjam": "10:49-12:20"
		},
		{
			"Thithi": "Ashtami 09:53",
			"Nakshatram": "Uttara 24:30",
			"Rahukalam": "07:38-09:28",
			"Durmuhurtam": "13:37-14:35",
			"Varjam": "08:39-10:09"
		},
		{
			"Thithi": "Navami 07:49",
			"Nakshatram": "Hasta 23:21",
			"Rahukalam": "16:47-18:37",
			"Durmuhurtam": "08:44-09:42",
			"Varjam": "08:30-10:01"
		},
		{
			"Thithi": "Dashami 05:57, Ekadashi 28:19",
			"Nakshatram": "Chitra 22:25",
			"Rahukalam": "13:08-14:58",
			"Durmuhurtam": "10:41-11:40",
			"Varjam": "07:02-08:34"
		},
		{
			"Thithi": "Dwadashi 27:00",
			"Nakshatram": "Swathi 21:46",
			"Rahukalam": "14:58-16:48",
			"Durmuhurtam": "10:41-11:40",
			"Varjam": "27:18-28:53"
		},
		{
			"Thithi": "Trayodashi 26:03",
			"Nakshatram": "Vishakha 21:29",
			"Rahukalam": "11:18-13:08",
			"Durmuhurtam": "08:44-09:43",
			"Varjam": "25:30-27:07"
		},
		{
			"Thithi": "Chaturdashi 25:32",
			"Nakshatram": "Anuradha 21:37",
			"Rahukalam": "09:28-11:18",
			"Durmuhurtam": "05:48-07:45",
			"Varjam": "27:21-29:00"
		},
		{
			"Thithi": "Purnima 25:30",
			"Nakshatram": "Jyeshta 22:13",
			"Rahukalam": "18:39-20:29",
			"Durmuhurtam": "18:32-19:30",
			"Varjam": "None"
		},
		{
			"Thithi": "Prathama 26:00",
			"Nakshatram": "Mula 23:20",
			"Rahukalam": "07:38-09:28",
			"Durmuhurtam": "13:38-14:37",
			"Varjam": "21:40-23:20"
		},
		{
			"Thithi": "Dwitiya 27:04",
			"Nakshatram": "Purvashada 24:59",
			"Rahukalam": "16:49-18:39",
			"Durmuhurtam": "08:44-09:43",
			"Varjam": "09:36-11:18"
		},
		{
			"Thithi": "Tritiya 28:38",
			"Nakshatram": "Uttarashada 27:09",
			"Rahukalam": "13:09-14:59",
			"Durmuhurtam": "12:40-13:38",
			"Varjam": "09:43-11:27"
		},
		{
			"Thithi": "Chaturthi Full N",
			"Nakshatram": "Shravana 29:44",
			"Rahukalam": "14:59-16:50",
			"Durmuhurtam": "10:42-11:41",
			"Varjam": "07:35-09:21"
		},
		{
			"Thithi": "Chaturthi 06:38",
			"Nakshatram": "Dhanishta Full Night",
			"Rahukalam": "11:19-13:09",
			"Durmuhurtam": "08:45-09:44",
			"Varjam": "10:13-12:01"
		},
		{
			"Thithi": "Panchami 08:57",
			"Nakshatram": "Dhanishta 08:37",
			"Rahukalam": "09:29-11:19",
			"Durmuhurtam": "05:49-07:46",
			"Varjam": "16:43-18:31"
		},
		{
			"Thithi": "Shashti 11:22",
			"Nakshatram": "Shatabhisha 11:37",
			"Rahukalam": "18:41-20:31",
			"Durmuhurtam": "18:33-19:32",
			"Varjam": "18:48-20:35"
		},
		{
			"Thithi": "Saptami 13:42",
			"Nakshatram": "Purvabhadra 14:32",
			"Rahukalam": "07:39-09:30",
			"Durmuhurtam": "13:39-14:38",
			"Varjam": "25:10-26:56"
		},
		{
			"Thithi": "Ashtami 15:43",
			"Nakshatram": "Uttarabhadra 17:07",
			"Rahukalam": "16:51-18:41",
			"Durmuhurtam": "08:46-09:45",
			"Varjam": "None"
		},
		{
			"Thithi": "Navami 17:14",
			"Nakshatram": "Revathi 19:13",
			"Rahukalam": "13:10-15:01",
			"Durmuhurtam": "12:41-13:40",
			"Varjam": "06:10-07:55"
		},
		{
			"Thithi": "Dashami 18:06",
			"Nakshatram": "Ashwini 20:41",
			"Rahukalam": "15:01-16:51",
			"Durmuhurtam": "10:44-11:43",
			"Varjam": "16:27-18:08"
		},
		{
			"Thithi": "Ekadashi 18:15",
			"Nakshatram": "Bharani 21:27",
			"Rahukalam": "11:21-13:11",
			"Durmuhurtam": "08:47-09:45",
			"Varjam": "06:36-08:15"
		},
		{
			"Thithi": "Dwadashi 17:41",
			"Nakshatram": "Krittika 21:31",
			"Rahukalam": "09:31-11:21",
			"Durmuhurtam": "05:51-07:48",
			"Varjam": "09:29-11:05"
		},
		{
			"Thithi": "Trayodashi 16:26",
			"Nakshatram": "Rohini 20:55",
			"Rahukalam": "18:41-20:31",
			"Durmuhurtam": "18:34-19:32",
			"Varjam": "13:07-14:40"
		}
	],



	"panchangam_july": [{
			"Thithi": "Chaturdashi 14:35",
			"Nakshatram": "Mrigashira 19:44",
			"Rahukalam": "07:42-09:32",
			"Durmuhurtam": "13:41-14:39",
			"Varjam": "27:34-29:03"
		},
		{
			"Thithi": "Amavasya 12:16",
			"Nakshatram": "Aardra 18:06",
			"Rahukalam": "16:51-18:41",
			"Durmuhurtam": "08:48-09:47",
			"Varjam": "29:07-30:35"
		},
		{
			"Thithi": "Ashada Shukla Prathama 09:34",
			"Nakshatram": "Punarvasu 16:09",
			"Rahukalam": "13:12-15:02",
			"Durmuhurtam": "12:43-13:41",
			"Varjam": "23:26-24:53"
		},
		{
			"Thithi": "Dwitiya 06:39, Tritiya 27:39",
			"Nakshatram": "Pushya 14:00",
			"Rahukalam": "15:02-16:51",
			"Durmuhurtam": "10:46-11:44",
			"Varjam": "25:37-27:05"
		},
		{
			"Thithi": "Chaturthi 24:39",
			"Nakshatram": "Ashlesha 11:48",
			"Rahukalam": "11:23-13:12",
			"Durmuhurtam": "08:49-09:48",
			"Varjam": "22:44-24:11"
		},
		{
			"Thithi": "Panchami 21:48",
			"Nakshatram": "Magha 09:40",
			"Rahukalam": "09:33-11:23",
			"Durmuhurtam": "05:54-07:51",
			"Varjam": "17:01-18:29"
		},
		{
			"Thithi": "Shashti 19:12",
			"Nakshatram": "Purvaphalguni 07:43",
			"Rahukalam": "18:41-20:30",
			"Durmuhurtam": "18:33-19:32",
			"Varjam": "14:25-15:55"
		},
		{
			"Thithi": "Saptami 16:54",
			"Nakshatram": "Uttara 06:03, Hasta 28:45",
			"Rahukalam": "07:45-09:34",
			"Durmuhurtam": "13:42-14:40, 16:37-17:35",
			"Varjam": "14:00-15:31"
		},
		{
			"Thithi": "Ashtami 15:00",
			"Nakshatram": "Chitra 27:52",
			"Rahukalam": "16:51-18:40",
			"Durmuhurtam": "08:51-09:49",
			"Varjam": "12:27-14:00"
		},
		{
			"Thithi": "Navami 13:32",
			"Nakshatram": "Swati 27:25",
			"Rahukalam": "13:13-15:02",
			"Durmuhurtam": "12:44-13:42",
			"Varjam": "09:21-10:56"
		},
		{
			"Thithi": "Dashami 12:32",
			"Nakshatram": "Vishakha 27:27",
			"Rahukalam": "15:02-16:51",
			"Durmuhurtam": "10:48-11:46",
			"Varjam": "09:01-10:38"
		},
		{
			"Thithi": "Ekadashi 12:01",
			"Nakshatram": "Anuradha 27:57",
			"Rahukalam": "11:24-13:13",
			"Durmuhurtam": "08:52-09:50",
			"Varjam": "07:32-09:10"
		},
		{
			"Thithi": "Dwadashi 11:58",
			"Nakshatram": "Jyeshta 28:56",
			"Rahukalam": "09:36-11:25",
			"Durmuhurtam": "05:59-07:55",
			"Varjam": "09:47-11:27"
		},
		{
			"Thithi": "Trayodashi 12:24",
			"Nakshatram": "Mula Full Night",
			"Rahukalam": "18:39-20:27",
			"Durmuhurtam": "18:32-19:29",
			"Varjam": "28:40-30:21"
		},
		{
			"Thithi": "Chaturdashi 13:18",
			"Nakshatram": "Mula 06:21",
			"Rahukalam": "07:48-09:37",
			"Durmuhurtam": "13:42-14:40",
			"Varjam": "16:42-18:26"
		},
		{
			"Thithi": "Purnima 14:38",
			"Nakshatram": "Purvashada 08:13",
			"Rahukalam": "16:50-18:38",
			"Durmuhurtam": "08:54-09:52",
			"Varjam": "16:58-18:43"
		},
		{
			"Thithi": "Prathama 16:21",
			"Nakshatram": "Uttarashada 10:28",
			"Rahukalam": "13:14-15:02",
			"Durmuhurtam": "12:45-13:42",
			"Varjam": "14:54-16:41"
		},
		{
			"Thithi": "Dwitiya 18:25",
			"Nakshatram": "Shravana 13:04",
			"Rahukalam": "15:02-16:49",
			"Durmuhurtam": "10:50-11:47",
			"Varjam": "17:32-19:20"
		},
		{
			"Thithi": "Tritiya 20:43",
			"Nakshatram": "Dhanishta 15:55",
			"Rahukalam": "11:26-13:14",
			"Durmuhurtam": "08:55-09:53",
			"Varjam": "24:01-25:49"
		},
		{
			"Thithi": "Chaturthi 23:09",
			"Nakshatram": "Satabhisha 18:55",
			"Rahukalam": "09:39-11:26",
			"Durmuhurtam": "06:04-07:58",
			"Varjam": "26:07-27:55"
		},
		{
			"Thithi": "Panchami 25:34",
			"Nakshatram": "Purvabhadra 21:54",
			"Rahukalam": "18:36-20:23",
			"Durmuhurtam": "18:29-19:26",
			"Varjam": "None"
		},
		{
			"Thithi": "Shashti 27:46",
			"Nakshatram": "Uttarabhadra 24:44",
			"Rahukalam": "07:52-09:40",
			"Durmuhurtam": "13:42-14:40",
			"Varjam": "08:38-10:25"
		},
		{
			"Thithi": "Saptami 29:35",
			"Nakshatram": "Revathi 27:12",
			"Rahukalam": "16:48-18:35",
			"Durmuhurtam": "08:57-09:54",
			"Varjam": "13:58-15:44"
		},
		{
			"Thithi": "Ashtami Full N",
			"Nakshatram": "Ashwini 29:09",
			"Rahukalam": "13:14-15:01",
			"Durmuhurtam": "12:45-13:42",
			"Varjam": "24:49-26:33"
		},
		{
			"Thithi": "Ashtami 06:51",
			"Nakshatram": "Bharani Full Night",
			"Rahukalam": "15:01-16:47",
			"Durmuhurtam": "10:52-11:49",
			"Varjam": "15:16-16:57"
		},
		{
			"Thithi": "Navami 07:26",
			"Nakshatram": "Bharani 06:26",
			"Rahukalam": "11:28-13:14",
			"Durmuhurtam": "08:59-09:55",
			"Varjam": "18:43-20:21"
		},
		{
			"Thithi": "Dashami 07:16",
			"Nakshatram": "Krittika 07:00",
			"Rahukalam": "09:42-11:28",
			"Durmuhurtam": "06:09-08:02",
			"Varjam": "22:52-24:27"
		},
		{
			"Thithi": "Ekadashi 06:19, Dwadashi 28:39",
			"Nakshatram": "Rohini 06:48",
			"Rahukalam": "18:32-20:18",
			"Durmuhurtam": "18:25-19:21",
			"Varjam": "12:11-13:43"
		},
		{
			"Thithi": "Trayodashi 26:19",
			"Nakshatram": "Aardra 28:17",
			"Rahukalam": "07:57-09:42",
			"Durmuhurtam": "13:42-14:38",
			"Varjam": "13:43-15:12"
		},
		{
			"Thithi": "Chaturdashi 23:27",
			"Nakshatram": "Punarvasu 26:11",
			"Rahukalam": "16:45-18:31",
			"Durmuhurtam": "09:00-09:57",
			"Varjam": "15:14-16:41"
		},
		{
			"Thithi": "Amavasya 20:11",
			"Nakshatram": "Pushya 23:41",
			"Rahukalam": "13:14-14:59",
			"Durmuhurtam": "12:46-13:42",
			"Varjam": "09:21-10:47"
		}
	],

	"panchangam_aug": [{
			"Thithi": "Shravana Shukla, Prathama 16:41",
			"Nakshatram": "Ashlesha 20:59",
			"Rahukalam": "14:59-16:44",
			"Durmuhurtam": "10:54-11:50, 16:30-17:26",
			"Varjam": "11:03-12:28"
		},
		{
			"Thithi": "Dwitiya 13:06",
			"Nakshatram": "Magha 18:14",
			"Rahukalam": "18:14-11:29",
			"Durmuhurtam": "09:02-09:58",
			"Varjam": "07:36-09:01"
		},
		{
			"Thithi": "Tritiya 09:35",
			"Nakshatram": "Purvaphalguni 15:35",
			"Rahukalam": "09:44-11:29",
			"Durmuhurtam": "06:15-08:07",
			"Varjam": "22:05-23:31"
		},
		{
			"Thithi": "Chaturthi 06:18, Panchami 27:24",
			"Nakshatram": "Uttaraphalguni 13:14",
			"Rahukalam": "18:27-20:11",
			"Durmuhurtam": "18:20-19:16",
			"Varjam": "20:57-22:25"
		},
		{
			"Thithi": "Shashti 25:00",
			"Nakshatram": "Hasta 11:17",
			"Rahukalam": "08:01-09:45",
			"Durmuhurtam": "13:41-14:37",
			"Varjam": "18:49-20:19"
		},
		{
			"Thithi": "Saptami 23:10",
			"Nakshatram": "Chitra 09:53",
			"Rahukalam": "16:41-18:25",
			"Durmuhurtam": "09:04-09:59",
			"Varjam": "15:18-16:51"
		},
		{
			"Thithi": "Ashtami 22:00",
			"Nakshatram": "Swathi 09:05",
			"Rahukalam": "13:13-14:57",
			"Durmuhurtam": "12:45-13:41",
			"Varjam": "14:40-16:15"
		},
		{
			"Thithi": "Navami 21:30",
			"Nakshatram": "Vishakha 08:57",
			"Rahukalam": "14:56-16:40",
			"Durmuhurtam": "10:55-11:50",
			"Varjam": "13:02-14:40"
		},
		{
			"Thithi": "Dashami 21:38",
			"Nakshatram": "Anuradha 09:28",
			"Rahukalam": "11:30-13:13",
			"Durmuhurtam": "09:05-10:00",
			"Varjam": "15:20-17:00"
		},
		{
			"Thithi": "Ekadashi 22:22",
			"Nakshatram": "Jyeshta 10:35",
			"Rahukalam": "09:47-11:30",
			"Durmuhurtam": "06:21-08:11",
			"Varjam": "None"
		},
		{
			"Thithi": "Dwadashi 23:36",
			"Nakshatram": "Mula 12:15",
			"Rahukalam": "18:21-20:04",
			"Durmuhurtam": "18:14-19:09",
			"Varjam": "10:32-12:15, 22:41-24:26"
		},
		{
			"Thithi": "Trayodashi 25:16",
			"Nakshatram": "Purvashada 14:21",
			"Rahukalam": "08:05-09:47",
			"Durmuhurtam": "13:40-14:34",
			"Varjam": "23:10-24:56"
		},
		{
			"Thithi": "Chaturdashi 27:15",
			"Nakshatram": "Uttarashada 16:49",
			"Rahukalam": "16:37-18:19",
			"Durmuhurtam": "09:07-10:01",
			"Varjam": "21:16-23:03"
		},
		{
			"Thithi": "Purnima 29:29",
			"Nakshatram": "Shravana 19:32",
			"Rahukalam": "13:12-14:54",
			"Durmuhurtam": "12:45-13:39",
			"Varjam": "24:01-25:48"
		},
		{
			"Thithi": "Prathama Full N",
			"Nakshatram": "Dhanishta 22:26",
			"Rahukalam": "14:54-16:35",
			"Durmuhurtam": "10:56-11:50",
			"Varjam": "None"
		},
		{
			"Thithi": "Prathama 07:51",
			"Nakshatram": "Satabhisha 25:25",
			"Rahukalam": "11:30-13:12",
			"Durmuhurtam": "09:08-10:02",
			"Varjam": "06:31-08:19"
		},
		{
			"Thithi": "Dwitiya 10:18",
			"Nakshatram": "Purvabhadra 28:25",
			"Rahukalam": "09:49-11:30",
			"Durmuhurtam": "06:27-08:15",
			"Varjam": "08:37-10:25"
		},
		{
			"Thithi": "Tritiya 12:43",
			"Nakshatram": "Uttarabhadra Full Night",
			"Rahukalam": "18:14-19:55",
			"Durmuhurtam": "18:07-19:01",
			"Varjam": "15:10-16:58"
		},
		{
			"Thithi": "Chaturthi 15:00",
			"Nakshatram": "Uttarabhadra 07:18",
			"Rahukalam": "08:09-09:50",
			"Durmuhurtam": "13:38-14:31",
			"Varjam": "20:38-22:25"
		},
		{
			"Thithi": "Panchami 17:00",
			"Nakshatram": "Revathi 09:58",
			"Rahukalam": "16:31-18:12",
			"Durmuhurtam": "09:10-10:03",
			"Varjam": "None"
		},
		{
			"Thithi": "Shashti 18:36",
			"Nakshatram": "Ashwini 12:17",
			"Rahukalam": "13:10-14:51",
			"Durmuhurtam": " 22:37-24:20",
			"Varjam": "07:54-09:39"
		},
		{
			"Thithi": "Saptami 19:39",
			"Nakshatram": "Bharani 14:06",
			"Rahukalam": "14:50-16:30",
			"Durmuhurtam": "10:57-11:50",
			"Varjam": "26:42-28:22"
		},
		{
			"Thithi": "Ashtami 20:02",
			"Nakshatram": "Krittika 15:17",
			"Rahukalam": "11:30-13:10",
			"Durmuhurtam": "09:11-10:04",
			"Varjam": "None"
		},
		{
			"Thithi": "Navami 19:40",
			"Nakshatram": "Rohini 15:46",
			"Rahukalam": "09:51-11:30",
			"Durmuhurtam": " 21:18-22:53",
			"Varjam": "07:36-09:14"
		},
		{
			"Thithi": "Dashami 18:32",
			"Nakshatram": "Mrigashira 15:29",
			"Rahukalam": "18:06-19:45",
			"Durmuhurtam": "18:00-18:53",
			"Varjam": "23:31-25:03"
		},
		{
			"Thithi": "Ekadashi 16:39",
			"Nakshatram": "Ardra 14:26",
			"Rahukalam": "08:13-09:52",
			"Durmuhurtam": "13:35-14:28",
			"Varjam": "25:35-27:04"
		},
		{
			"Thithi": "Dwadashi 14:06",
			"Nakshatram": "Punarvasu 12:43",
			"Rahukalam": "16:26-18:04",
			"Durmuhurtam": "09:13-10:05",
			"Varjam": "19:57-21:24"
		},
		{
			"Thithi": "Trayodashi 10:58",
			"Nakshatram": "Pushya 10:25",
			"Rahukalam": "13:09-14:47",
			"Durmuhurtam": "12:42-13:35",
			"Varjam": "21:45-23:10"
		},
		{
			"Thithi": "Chaturdashi 07:25, Amavasya 27:37",
			"Nakshatram": "Ashlesha 07:41",
			"Rahukalam": "14:46-16:24",
			"Durmuhurtam": "10:58-11:50",
			"Varjam": "18:11-19:35"
		},
		{
			"Thithi": "Bhadrapada Shukla Prathama 23:43",
			"Nakshatram": "Purvaphalguni 25:37",
			"Rahukalam": "11:30-13:08",
			"Durmuhurtam": "09:14-10:06",
			"Varjam": "11:40-13:03"
		},
		{
			"Thithi": "Dwitiya 19:56",
			"Nakshatram": "Uttara 22:40",
			"Rahukalam": "09:53-11:30",
			"Durmuhurtam": "06:38-08:22",
			"Varjam": "07:56-09:20"
		}
	],

	"panchangam_sep": [{
			"Thithi": "Tritiya 16:26",
			"Nakshatram": "Hasta 20:02",
			"Rahukalam": "17:58-19:35",
			"Durmuhurtam": "17:52-18:44",
			"Varjam": "27:20-28:47"
		},
		{
			"Thithi": "Chaturthi 13:23",
			"Nakshatram": "Chitra 17:54",
			"Rahukalam": "08:17-09:53",
			"Durmuhurtam": "13:33-14:24",
			"Varjam": "23:09-24:39"
		},
		{
			"Thithi": "Panchami 10:57",
			"Nakshatram": "Swathi 16:23",
			"Rahukalam": "16:20-17:56",
			"Durmuhurtam": "09:15-10:07",
			"Varjam": "21:48-23:21"
		},
		{
			"Thithi": "Shashti 09:14",
			"Nakshatram": "Vishakha 15:37",
			"Rahukalam": "13:06-14:43",
			"Durmuhurtam": "12:41-13:32",
			"Varjam": "19:37-21:13"
		},
		{
			"Thithi": "Saptami 08:19",
			"Nakshatram": "Anuradha 15:39",
			"Rahukalam": "14:42-16:18",
			"Durmuhurtam": "10:58-11:49",
			"Varjam": "21:26-23:05"
		},
		{
			"Thithi": "Ashtami 08:13",
			"Nakshatram": "Jyeshta 16:27",
			"Rahukalam": "11:30-13:06",
			"Durmuhurtam": "09:16-10:07",
			"Varjam": "None"
		},
		{
			"Thithi": "Navami 08:52",
			"Nakshatram": "Mula 17:59",
			"Rahukalam": "09:55-11:30",
			"Durmuhurtam": "06:44-08:26",
			"Varjam": "16:17-17:59"
		},
		{
			"Thithi": "Dashami 10:11",
			"Nakshatram": "Purvashada 20:06",
			"Rahukalam": "17:50-19:25",
			"Durmuhurtam": "17:44-18:34",
			"Varjam": "28:57-30:43"
		},
		{
			"Thithi": "Ekadashi 12:01",
			"Nakshatram": "Uttarashada 22:39",
			"Rahukalam": "08:20-09:55",
			"Durmuhurtam": "13:30-14:20",
			"Varjam": "27:07-28:55"
		},
		{
			"Thithi": "Dwadashi 14:12",
			"Nakshatram": "Shravana 25:29",
			"Rahukalam": "16:13-17:48",
			"Durmuhurtam": "09:18-10:08",
			"Varjam": "29:59-31:47"
		},
		{
			"Thithi": "Trayodashi 16:36",
			"Nakshatram": "Dhanishta 28:28",
			"Rahukalam": "13:04-14:38",
			"Durmuhurtam": "12:39-13:29",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturdashi 19:05",
			"Nakshatram": "Satabhisha Full Night",
			"Rahukalam": "14:37-16:11",
			"Durmuhurtam": "10:58-11:48",
			"Varjam": "12:34-14:22"
		},
		{
			"Thithi": "Purnima 21:32",
			"Nakshatram": "Satabhisha 07:28",
			"Rahukalam": "11:30-13:03",
			"Durmuhurtam": "09:19-10:09",
			"Varjam": "14:40-16:27"
		},
		{
			"Thithi": "Prathama 23:53",
			"Nakshatram": "Purvabhadra 10:25",
			"Rahukalam": "09:56-11:30",
			"Durmuhurtam": "06:50-08:29",
			"Varjam": "21:09-22:56"
		},
		{
			"Thithi": "Dwitiya 26:05",
			"Nakshatram": "Uttarabhadra 13:14",
			"Rahukalam": "17:41-19:14",
			"Durmuhurtam": "17:35-18:25",
			"Varjam": "26:33-28:20"
		},
		{
			"Thithi": "Tritiya 28:02",
			"Nakshatram": "Revathi 15:52",
			"Rahukalam": "08:24-09:57",
			"Durmuhurtam": "13:27-14:16",
			"Varjam": "None"
		},
		{
			"Thithi": "Chaturthi 29:41",
			"Nakshatram": "Ashwini 18:14",
			"Rahukalam": "16:07-17:39",
			"Durmuhurtam": "09:20-10:09",
			"Varjam": "13:50-15:36"
		},
		{
			"Thithi": "Panchami Full N",
			"Nakshatram": "Bharani 20:15",
			"Rahukalam": "13:01-14:34",
			"Durmuhurtam": "12:37-13:26",
			"Varjam": "None"
		},
		{
			"Thithi": "Panchami 06:56",
			"Nakshatram": "Krittika 21:49",
			"Rahukalam": "14:33-16:05",
			"Durmuhurtam": "10:59-11:48",
			"Varjam": "09:02-10:44"
		},
		{
			"Thithi": "Shashti 07:41",
			"Nakshatram": "Rohini 22:52",
			"Rahukalam": "11:29-13:01",
			"Durmuhurtam": "09:21-10:10",
			"Varjam": "14:31-16:11"
		},
		{
			"Thithi": "Saptami 07:50",
			"Nakshatram": "Mrigashira 23:16",
			"Rahukalam": "09:58-11:29",
			"Durmuhurtam": "06:56-08:33",
			"Varjam": "None"
		},
		{
			"Thithi": "Ashtami 07:20, Navami 30:07",
			"Nakshatram": "Aardra 22:59",
			"Rahukalam": "17:33-19:04",
			"Durmuhurtam": "17:27-18:15",
			"Varjam": "07:34-09:09"
		},
		{
			"Thithi": "Dashami 28:12",
			"Nakshatram": "Punarvasu 22:01",
			"Rahukalam": "08:28-09:58",
			"Durmuhurtam": "13:24-14:12",
			"Varjam": "10:30-12:02"
		},
		{
			"Thithi": "Ekadashi 25:38",
			"Nakshatram": "Pushya 20:23",
			"Rahukalam": "16:00-17:30",
			"Durmuhurtam": "09:23-10:11",
			"Varjam": "None"
		},
		{
			"Thithi": "Dwadashi 22:32",
			"Nakshatram": "Ashlesha 18:10",
			"Rahukalam": "12:59-14:29",
			"Durmuhurtam": "12:35-13:23",
			"Varjam": "08:00-09:27"
		},
		{
			"Thithi": "Trayodashi 19:01",
			"Nakshatram": "Magha 15:31",
			"Rahukalam": "14:28-15:58",
			"Durmuhurtam": "10:59-11:47",
			"Varjam": "22:32-23:56"
		},
		{
			"Thithi": "Chaturdashi 15:16",
			"Nakshatram": "Purvaphalguni 12:34",
			"Rahukalam": "11:29-12:58",
			"Durmuhurtam": "09:24-10:11",
			"Varjam": "18:52-20:16"
		},
		{
			"Thithi": "Amavasya 11:26",
			"Nakshatram": "Uttara 09:32, Hasta 30:36",
			"Rahukalam": "10:00-11:29",
			"Durmuhurtam": "07:02-08:37",
			"Varjam": "16:55-18:19"
		},
		{
			"Thithi": "Ashwija Shukla Prathama 07:43, Dwitiya 28:19",
			"Nakshatram": "Chitra 27:59",
			"Rahukalam": "17:24-18:53",
			"Durmuhurtam": "17:18-18:06",
			"Varjam": "13:44-15:09"
		},
		{
			"Thithi": "Tritiya 25:25",
			"Nakshatram": "Swati 25:51",
			"Rahukalam": "08:32-10:00",
			"Durmuhurtam": "13:21-14:08",
			"Varjam": "09:05-10:32"
		}
	],

	"panchangam_oct": [{
			"Thithi": "Chaturthi 23:09",
			"Nakshatram": "Vishakha 24:22",
			"Rahukalam": "15:53-17:22",
			"Durmuhurtam": "09:25-10:12",
			"Varjam": "07:06-08:36"
		},
		{
			"Thithi": "Panchami 21:41",
			"Nakshatram": "Anuradha 23:40",
			"Rahukalam": "12:57-14:25",
			"Durmuhurtam": "12:33-13:20",
			"Varjam": "29:18-30:55"
		},
		{
			"Thithi": "Shashti 21:05",
			"Nakshatram": "Jyeshta 23:49",
			"Rahukalam": "14:24-15:52",
			"Durmuhurtam": "11:00-11:46",
			"Varjam": "None"
		},
		{
			"Thithi": "Saptami 21:20",
			"Nakshatram": "Mula 24:48",
			"Rahukalam": " 11:29-12:56",
			"Durmuhurtam": "09:26-10:13",
			"Varjam": "23:08-24:48"
		},
		{
			"Thithi": "Ashtami 22:24",
			"Nakshatram": "Purvashada 26:33",
			"Rahukalam": "10:02-11:29",
			"Durmuhurtam": "07:08-08:40",
			"Varjam": "11:06-12:49"
		},
		{
			"Thithi": "Navami 24:07",
			"Nakshatram": "Uttarashada 28:55",
			"Rahukalam": "17:16-18:42",
			"Durmuhurtam": "17:10-17:56",
			"Varjam": "11:21-13:06"
		},
		{
			"Thithi": "Dashami 26:20",
			"Nakshatram": "Shravana Full Night",
			"Rahukalam": "08:36-10:02",
			"Durmuhurtam": "13:18-14:04",
			"Varjam": "09:23-11:10"
		},
		{
			"Thithi": "Ekadashi 28:48",
			"Nakshatram": "Shravana 07:42",
			"Rahukalam": "15:47-17:13",
			"Durmuhurtam": "09:28-10:14",
			"Varjam": "12:12-14:00"
		},
		{
			"Thithi": "Dwadashi Full N",
			"Nakshatram": "Dhanishta 10:42",
			"Rahukalam": "12:55-14:20",
			"Durmuhurtam": "12:32-13:17",
			"Varjam": "18:48-20:37"
		},
		{
			"Thithi": "Dwadashi 07:21",
			"Nakshatram": "Sathabhisha 13:44",
			"Rahukalam": "14:20-15:45",
			"Durmuhurtam": "11:00-11:46",
			"Varjam": "20:55-22:42"
		},
		{
			"Thithi": "Trayodashi 09:50",
			"Nakshatram": "Purvabhadra 16:39",
			"Rahukalam": "11:29-12:54",
			"Durmuhurtam": "09:29-10:15",
			"Varjam": "27:21-29:08"
		},
		{
			"Thithi": "Chaturdashi 12:06",
			"Nakshatram": "Uttarabhadra 19:23",
			"Rahukalam": "10:04-11:29",
			"Durmuhurtam": "07:14-08:45",
			"Varjam": "None"
		},
		{
			"Thithi": "Purnima 14:07",
			"Nakshatram": "Revathi 21:50",
			"Rahukalam": "17:08-18:32",
			"Durmuhurtam": "17:02-17:47",
			"Varjam": "08:36-10:22"
		},
		{
			"Thithi": "Prathama 15:50",
			"Nakshatram": "Ashwini 24:00",
			"Rahukalam": "08:40-10:05",
			"Durmuhurtam": "13:16-14:01",
			"Varjam": "19:38-21:23"
		},
		{
			"Thithi": "Dwitiya 17:14",
			"Nakshatram": "Bharani 25:51",
			"Rahukalam": "15:41-17:05",
			"Durmuhurtam": "09:31-10:16",
			"Varjam": "10:21-12:04"
		},
		{
			"Thithi": "Tritiya 18:18",
			"Nakshatram": "Krittika 27:22",
			"Rahukalam": "12:53-14:17",
			"Durmuhurtam": "12:31-13:15",
			"Varjam": "14:36-16:18"
		},
		{
			"Thithi": "Chaturthi 18:58",
			"Nakshatram": "Rohini 28:29",
			"Rahukalam": "14:16-15:40",
			"Durmuhurtam": "11:01-11:46",
			"Varjam": "20:06-21:47"
		},
		{
			"Thithi": "Panchami 19:13",
			"Nakshatram": "Mrigashira 29:10",
			"Rahukalam": "11:29-12:52",
			"Durmuhurtam": "09:33-10:17",
			"Varjam": "10:15-11:53"
		},
		{
			"Thithi": "Shashti 19:00",
			"Nakshatram": "Ardra 29:22",
			"Rahukalam": "10:06-11:29",
			"Durmuhurtam": "07:20-08:49",
			"Varjam": "13:38-15:15"
		},
		{
			"Thithi": "Saptami 18:14",
			"Nakshatram": "Punarvasu 29:02",
			"Rahukalam": "17:00-18:23",
			"Durmuhurtam": "16:55-17:39",
			"Varjam": "17:12-18:47"
		},
		{
			"Thithi": "Ashtami 16:55",
			"Nakshatram": "Pushya 28:08",
			"Rahukalam": "08:45-10:07",
			"Durmuhurtam": "13:14-13:58",
			"Varjam": "12:44-14:17"
		},
		{
			"Thithi": "Navami 15:02",
			"Nakshatram": "Ashlesha 26:43",
			"Rahukalam": "15:36-16:58",
			"Durmuhurtam": "09:35-10:19",
			"Varjam": "16:11-17:41"
		},
		{
			"Thithi": "Dashami 12:39",
			"Nakshatram": "Magha 24:48",
			"Rahukalam": "12:52-14:14",
			"Durmuhurtam": "12:30-13:13",
			"Varjam": "13:45-15:14"
		},
		{
			"Thithi": "Ekadashi 09:48, Dwadashi 30:38",
			"Nakshatram": "Purvaphalguni 22:30",
			"Rahukalam": "14:13-15:35",
			"Durmuhurtam": "11:03-11:46",
			"Varjam": "08:02-09:29"
		},
		{
			"Thithi": "Trayodashi 27:16",
			"Nakshatram": "Uttara 19:57",
			"Rahukalam": "11:30-12:51",
			"Durmuhurtam": "09:36-10:20",
			"Varjam": "27:26-28:51"
		},
		{
			"Thithi": "Chaturdashi 23:53",
			"Nakshatram": "Hasta 17:19",
			"Rahukalam": "10:09-11:30",
			"Durmuhurtam": "07:27-08:54",
			"Varjam": "24:28:25:54"
		},
		{
			"Thithi": "Amavasya 20:38",
			"Nakshatram": "Chitra 14:46",
			"Rahukalam": "16:53-18:14",
			"Durmuhurtam": "16:48-17:31",
			"Varjam": "19:51-21:17"
		},
		{
			"Thithi": "Karthika Shukla, Prathama 17:43",
			"Nakshatram": "Swathi 12:30",
			"Rahukalam": "08:50-10:10",
			"Durmuhurtam": "13:13-13:56, 15:21-16:04",
			"Varjam": "17:41-19:09"
		},
		{
			"Thithi": "Dwitiya 15:17",
			"Nakshatram": "Vishakha 10:41",
			"Rahukalam": "15:31-16:52",
			"Durmuhurtam": "09:39-10:21",
			"Varjam": "14:29-16:00"
		},
		{
			"Thithi": "Tritiya 13:31",
			"Nakshatram": "Anuradha 09:29",
			"Rahukalam": "12:51-14:11",
			"Durmuhurtam": "12:30-13:12",
			"Varjam": "14:58-16:33"
		},
		{
			"Thithi": "Chaturthi 12:31",
			"Nakshatram": "Jyeshta 09:01",
			"Rahukalam": "14:11-15:30",
			"Durmuhurtam": "11:05-11:47",
			"Varjam": "None"
		}
	],

	"panchangam_nov": [{
			"Thithi": "Panchami 12:21",
			"Nakshatram": "Mula 09:22",
			"Rahukalam": "11:32-12:51",
			"Durmuhurtam": "09:40-10:23",
			"Varjam": "07:44-09:22"
		},
		{
			"Thithi": "Shashti 13:01",
			"Nakshatram": "Purvashada 10:31",
			"Rahukalam": "10:13-11:32",
			"Durmuhurtam": "07:34-08:59",
			"Varjam": "19:09-20:53"
		},
		{
			"Thithi": "Saptami 13:26",
			"Nakshatram": "Uttarashada 11:25",
			"Rahukalam": "15:48-17:06",
			"Durmuhurtam": "15:42-16:24",
			"Varjam": "15:49-17:35"
		},
		{
			"Thithi": "Ashtami 15:27",
			"Nakshatram": "Shravana 13:53",
			"Rahukalam": "07:55-09:14",
			"Durmuhurtam": "12:12-12:54",
			"Varjam": "18:22-20:09"
		},
		{
			"Thithi": "Navami 17:51",
			"Nakshatram": "Dhanishta 16:45",
			"Rahukalam": "14:28-15:46",
			"Durmuhurtam": "08:43-09:25",
			"Varjam": "24:51-26:39"
		},
		{
			"Thithi": "Dashami 20:24",
			"Nakshatram": "Satabhisha 19:45",
			"Rahukalam": "11:51-13:09",
			"Durmuhurtam": "11:30-12:12",
			"Varjam": "26:56-28:44"
		},
		{
			"Thithi": "Ekadashi 22:54",
			"Nakshatram": "Purvabhadra 22:42",
			"Rahukalam": "13:09:14:27",
			"Durmuhurtam": "10:07-10:49",
			"Varjam": "None"
		},
		{
			"Thithi": "Dwadashi 25:09",
			"Nakshatram": "Uttarabhadra 25:26",
			"Rahukalam": "10:34-11:51",
			"Durmuhurtam": "08:45-09:26",
			"Varjam": "09:24-11:10"
		},
		{
			"Thithi": "Trayodashi 27:03",
			"Nakshatram": "Revathi 27:48",
			"Rahukalam": "09:16-10:34",
			"Durmuhurtam": "06:42-08:04",
			"Varjam": "14:37-16:23"
		},
		{
			"Thithi": "Chaturdashi 28:31",
			"Nakshatram": "Ashwini 29:47",
			"Rahukalam": "15:43-17:00",
			"Durmuhurtam": "15:38-16:19",
			"Varjam": "25:27-27:11"
		},
		{
			"Thithi": "Purnima 29:34",
			"Nakshatram": "Bharani Full Night",
			"Rahukalam": "08:01-09:18",
			"Durmuhurtam": "12:12-12:53",
			"Varjam": "16:01-17:43"
		},
		{
			"Thithi": "Prathama 30:11",
			"Nakshatram": "Bharani 07:21",
			"Rahukalam": "14:25-15:42",
			"Durmuhurtam": "08:48-09:28",
			"Varjam": "19:56-21:36"
		},
		{
			"Thithi": "Dwitiya 30:24",
			"Nakshatram": "Krittika 08:31",
			"Rahukalam": "11:52-13:08",
			"Durmuhurtam": "11:31-12:12",
			"Varjam": "25:02-26:41"
		},
		{
			"Thithi": "Tritiya 30:17",
			"Nakshatram": "Rohini 09:17",
			"Rahukalam": "13:08-14:24",
			"Durmuhurtam": "10:10-10:51",
			"Varjam": "14:59-16:37"
		},
		{
			"Thithi": "Chaturthi 29:44",
			"Nakshatram": "Mrigashira 09:42",
			"Rahukalam": "10:36-11:52",
			"Durmuhurtam": "08:50-09:30",
			"Varjam": "18:07-19:43"
		},
		{
			"Thithi": "Panchami 28:52",
			"Nakshatram": "Aardra 09:46",
			"Rahukalam": "09:21-10:36",
			"Durmuhurtam": "06:49-08:10",
			"Varjam": "21:37-23:12"
		},
		{
			"Thithi": "Shashti 27:39",
			"Nakshatram": "Punarvasu 09:29",
			"Rahukalam": "15:39-16:55",
			"Durmuhurtam": "15:34-16:14",
			"Varjam": "17:16-18:49"
		},
		{
			"Thithi": "Saptami 26:05",
			"Nakshatram": "Pushya 08:51",
			"Rahukalam": "08:07-09:22",
			"Durmuhurtam": "12:13-12:53",
			"Varjam": "21:08-22:40"
		},
		{
			"Thithi": "Ashtami 24:11",
			"Nakshatram": "Ashlesha 07:52, Magha 30:34",
			"Rahukalam": "14:23-15:38",
			"Durmuhurtam": "08:52-09:33, 22:29-23:25",
			"Varjam": "19:13-20:44"
		},
		{
			"Thithi": "Navami 21:58",
			"Nakshatram": "Purvaphalguni 28:59",
			"Rahukalam": "11:53-13:08",
			"Durmuhurtam": "11:33-12:13",
			"Varjam": "14:03-15:32"
		},
		{
			"Thithi": "Dashami 19:31",
			"Nakshatram": "Uttara 27:11",
			"Rahukalam": "13:08-14:23",
			"Durmuhurtam": "10:14-10:54",
			"Varjam": "11:39-13:07"
		},
		{
			"Thithi": "Ekadashi 16:54",
			"Nakshatram": "Hasta 25:14",
			"Rahukalam": "10:39-11:54",
			"Durmuhurtam": "08:55-09:34",
			"Varjam": "10:54-12:22"
		},
		{
			"Thithi": "Dwadashi 14:13",
			"Nakshatram": "Chitra 23:17",
			"Rahukalam": "09:25-10:39",
			"Durmuhurtam": "06:56-08:16",
			"Varjam": "08:35-10:04"
		},
		{
			"Thithi": "Trayodashi 11:35",
			"Nakshatram": "Swathi 21:27",
			"Rahukalam": "15:37-16:51",
			"Durmuhurtam": "15:32-16:11",
			"Varjam": "26:41-28:11"
		},
		{
			"Thithi": "Chaturdashi 09:10",
			"Nakshatram": "Vishakha 19:52",
			"Rahukalam": "08:12-09:26",
			"Durmuhurtam": "12:14-12:54",
			"Varjam": "23:41-25:12"
		},
		{
			"Thithi": "Amavasya 07:05, Prathama 29:29",
			"Nakshatram": "Anuradha 18:42",
			"Rahukalam": "14:22-15:36",
			"Durmuhurtam": "08:58-09:37, 22:30-23:27",
			"Varjam": "24:09-25:42"
		},
		{
			"Thithi": "Dwitiya 28:28",
			"Nakshatram": "Jyeshta 18:04",
			"Rahukalam": "11:55-13:09",
			"Durmuhurtam": "11:35-12:15",
			"Varjam": "None"
		},
		{
			"Thithi": "Tritiya 28:09",
			"Nakshatram": "Mula 18:03",
			"Rahukalam": "13:09-14:22",
			"Durmuhurtam": "10:17-10:57",
			"Varjam": "16:27-18:03"
		},
		{
			"Thithi": "Chaturthi 28:34",
			"Nakshatram": "Purvashada 18:45",
			"Rahukalam": "10:42-11:56",
			"Durmuhurtam": "09:00-09:39",
			"Varjam": "27:14-28:55"
		},
		{
			"Thithi": "Panchami 29:43",
			"Nakshatram": "Uttarashada 20:10",
			"Rahukalam": "09:30-10:43",
			"Durmuhurtam": "07:03-08:21",
			"Varjam": "24:30-26:15"
		}
	],

	"panchangam_dec": [{
			"Thithi": "Shashti Full N",
			"Nakshatram": "Shravana 22:13",
			"Rahukalam": "15:36-16:49",
			"Durmuhurtam": "15:31-16:10",
			"Varjam": "26:38-28:25"
		},
		{
			"Thithi": "Shashti 07:29",
			"Nakshatram": "Dhanishta 24:46",
			"Rahukalam": "08:18-09:31",
			"Durmuhurtam": "12:16-12:55",
			"Varjam": "None"
		},
		{
			"Thithi": "Saptami 09:44",
			"Nakshatram": "Satabhisha 27:40",
			"Rahukalam": "14:23-15:36",
			"Durmuhurtam": "09:03-09:41",
			"Varjam": "08:50-10:38"
		},
		{
			"Thithi": "Ashtami 12:14",
			"Nakshatram": "Purvabhadra 30:37",
			"Rahukalam": "11:58-13:10",
			"Durmuhurtam": "11:38-12:17",
			"Varjam": "10:51-12:38"
		},
		{
			"Thithi": "Navami 14:45",
			"Nakshatram": "Uttarabhadra Full Night",
			"Rahukalam": "13:11-14:23",
			"Durmuhurtam": "10:21-11:00",
			"Varjam": "17:21-19:09"
		},
		{
			"Thithi": "Dashami 17:04",
			"Nakshatram": "Uttarabhadra 09:27",
			"Rahukalam": "10:46-11:59",
			"Durmuhurtam": "09:05-09:43",
			"Varjam": "22:42-24:28"
		},
		{
			"Thithi": "Ekadashi 18:59",
			"Nakshatram": "Revathi 11:58",
			"Rahukalam": "09:34-10:47",
			"Durmuhurtam": "07:10-08:27",
			"Varjam": "None"
		},
		{
			"Thithi": "Dwadashi 20:23",
			"Nakshatram": "Ashwini 14:00",
			"Rahukalam": "15:36-16:48",
			"Durmuhurtam": " 24:12-25:54",
			"Varjam": "09:40-11:24"
		},
		{
			"Thithi": "Trayodashi 21",
			"Nakshatram": "Bharani 15:30",
			"Rahukalam": "08:23-09:36",
			"Durmuhurtam": "12:19-12:58",
			"Varjam": "27:59-29:38"
		},
		{
			"Thithi": "Chaturdashi 21:29",
			"Nakshatram": "Krittika 16:27",
			"Rahukalam": "14:24-15:36",
			"Durmuhurtam": "09:07-09:46",
			"Varjam": "None"
		},
		{
			"Thithi": "Purnima 21:12",
			"Nakshatram": "Rohini 16:52",
			"Rahukalam": "12:01-13:13",
			"Durmuhurtam": " 08:44-10:21",
			"Varjam": "08:44-10:21"
		},
		{
			"Thithi": "Prathama 20:26",
			"Nakshatram": "Mrigashira 16:48",
			"Rahukalam": "13:13-14:25",
			"Durmuhurtam": "10:25-11:04",
			"Varjam": "25:02-26:37"
		},
		{
			"Thithi": "Dwitiya 19:17",
			"Nakshatram": "Aardra 16:20",
			"Rahukalam": "10:50-12:02",
			"Durmuhurtam": "09:09-09:48",
			"Varjam": "27:57-29:30"
		},
		{
			"Thithi": "Tritiya 17:48",
			"Nakshatram": "Punarvasu 15:33",
			"Rahukalam": "09:39-10:50",
			"Durmuhurtam": "07:15-08:32",
			"Varjam": "23:12-24:44"
		},
		{
			"Thithi": "Chaturthi 16:04",
			"Nakshatram": "Pushya 14:30",
			"Rahukalam": "15:38-16:50",
			"Durmuhurtam": "15:33-16:11",
			"Varjam": "26:39-28:10"
		},
		{
			"Thithi": "Panchami 14:09",
			"Nakshatram": "Ashlesha 13:17",
			"Rahukalam": "08:28-09:40",
			"Durmuhurtam": "12:22-13:01",
			"Varjam": "24:36-26:07"
		},
		{
			"Thithi": "Shashti 12:07",
			"Nakshatram": "Magha 11:56",
			"Rahukalam": "14:27-15:39",
			"Durmuhurtam": "09:12-09:50",
			"Varjam": "19:27-20:58"
		},
		{
			"Thithi": "Saptami 10:00",
			"Nakshatram": "Purvaphalguni 10:30",
			"Rahukalam": "12:04-13:16",
			"Durmuhurtam": "11:45-12:23",
			"Varjam": "17:16-18:47"
		},
		{
			"Thithi": "Ashtami 07:53, Navami 29:46",
			"Nakshatram": "Uttara 09:04",
			"Rahukalam": "13:16-14:28",
			"Durmuhurtam": "10:29-11:07, 14:18-14:57",
			"Varjam": "16:58-18:28"
		},
		{
			"Thithi": "Dashami 27:45",
			"Nakshatram": "Hasta 07:39, Chitra 30:19",
			"Rahukalam": "10:54-12:05",
			"Durmuhurtam": "09:13-09:52, 12:24-13:02",
			"Varjam": "15:12-16:43"
		},
		{
			"Thithi": "Ekadashi 25:52",
			"Nakshatram": "Swathi 29:08",
			"Rahukalam": "09:43-10:54",
			"Durmuhurtam": "07:19-08:36",
			"Varjam": "11:38-13:09"
		},
		{
			"Thithi": "Dwadashi 24:11",
			"Nakshatram": "Vishakha 28:09",
			"Rahukalam": "15:41-16:53",
			"Durmuhurtam": "15:36-16:14",
			"Varjam": "10:30-12:02"
		},
		{
			"Thithi": "Trayodashi 22:48",
			"Nakshatram": "Anuradha 27:29",
			"Rahukalam": "08:32-09:44",
			"Durmuhurtam": "12:26-13:04",
			"Varjam": "08:03-09:36"
		},
		{
			"Thithi": "Chaturdashi 21:47",
			"Nakshatram": "Jyeshta 27:11",
			"Rahukalam": "14:30-15:42",
			"Durmuhurtam": "09:15-09:54",
			"Varjam": "09:01-10:36"
		},
		{
			"Thithi": "Amavasya 21:12",
			"Nakshatram": "Mula 27:20",
			"Rahukalam": "12:08-13:19",
			"Durmuhurtam": "11:49-12:27",
			"Varjam": "25:43-27:20"
		},
		{
			"Thithi": "Pousha Shukla, Prathama 21:09",
			"Nakshatram": "Purvashada 28:00",
			"Rahukalam": "13:20-14:32",
			"Durmuhurtam": "10:33-11:11, 14:22-15:00",
			"Varjam": "13:12-14:51"
		},
		{
			"Thithi": "Dwitiya 21:40",
			"Nakshatram": "Uttarashada 29:13",
			"Rahukalam": "10:57-12:09",
			"Durmuhurtam": "09:17-09:55",
			"Varjam": "12:24-14:05"
		},
		{
			"Thithi": "Tritiya 22:45",
			"Nakshatram": "Shravana 31:00",
			"Rahukalam": "09:46-10:57",
			"Durmuhurtam": "07:22-08:39",
			"Varjam": "09:31-11:14"
		},
		{
			"Thithi": "Chaturthi 24:24",
			"Nakshatram": "Dhanishta Full Night",
			"Rahukalam": "15:45-16:57",
			"Durmuhurtam": "15:40-16:19",
			"Varjam": "11:22-13:07"
		},
		{
			"Thithi": "Panchami 26:31",
			"Nakshatram": "Dhanishta 09:16",
			"Rahukalam": "08:35-:09:47",
			"Durmuhurtam": "12:29-13:08",
			"Varjam": "17:17-19:04"
		},
		{
			"Thithi": "Shashti 28:57",
			"Nakshatram": "Satabhisha 11:57",
			"Rahukalam": "14:35-15:46",
			"Durmuhurtam": "09:18-09:56",
			"Varjam": "19:08-20:56"
		}
	]
}

def thithi(request):
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(request),bot)
        chat_id = update.message.chat.id
        complete_message = update.message.text.split(' ')
        if complete_message[0] == '/tithi':
            try:
                print("date received: ", complete_message[1])
                date_check = datetime.datetime.strptime(complete_message[1],"%m-%d-%Y")
                r_date = complete_message[1].split('-')
                if(r_date[2] != '2019'):
                   res_text = 'I can only give you 2019 details'
                else:
                   r_d = int(r_date[1]) - 1
                   r_m = int(r_date[0]) - 1
                   ar = "panchangam_" + months[r_m]
                   t_data = "Thithi: " + source_data[ar][r_d]['Thithi'] +  "\n" 
                   n_data = "Nakshatram: " + source_data[ar][r_d]['Nakshatram'] +  "\n"
                   r_data = "Rahukalam: " + source_data[ar][r_d]['Rahukalam'] +  "\n"
                   d_data = "Durmuhurtam: " + source_data[ar][r_d]['Durmuhurtam'] +  "\n"
                   v_data = "Varjam: " + source_data[ar][r_d]['Varjam'] +  "\n"
                   res_text = t_data + n_data + r_data + d_data + v_data
            except:
                   res_text = 'Please enter a valid date in mm-dd-yyyy format'
        elif complete_message[0] == '/start':
            res_text = 'Hello! I am bot, please use /help to know what I can do'
        elif complete_message[0] == '/help':
            res_text = 'I give the Tithi,  Nakshatra and other details for the given date of the current year(2019).\n To request send a command as /tithi <mm-dd-yyyy> \n The times mentioned are in PST'
        else:
            res_text = 'Invalid command entered, please use /help'
            
        bot.sendMessage(chat_id=chat_id,text=res_text)
    return f'ok'