import os 
import telegram
import datetime
from pytz import timezone

bot = telegram.Bot(token=os.environ["TOKEN"])
months = list(['jan','feb','mar','april','may','june','july','aug','sep','oct','nov','dec'])
source_data = {
    "panchangam_jan": [{
            "Thithi": "Chaturdashi 14:11",
            "Nakshatram": "Mula 26:53",
            "Rahukalam": "09:47-10:59",
            "Durmuhurtam": "07:22-08:40",
            "Varjam": "12:50-14:14"
        },
        {
            "Thithi": "Amavasya 10:32, Prathama 31:01",
            "Nakshatram": "Purvashada 24:03",
            "Rahukalam": "15:50-17:02",
            "Durmuhurtam": "15:45-16:23",
            "Varjam": "11:21-12:46"
        },
        {
            "Thithi": "Dwitiya 27:49",
            "Nakshatram": "Uttarashada 21:27",
            "Rahukalam": "08:35-09:48",
            "Durmuhurtam": "12:32-13:11",
            "Varjam": "25:05-26:32"
        },
        {
            "Thithi": "Tritiya 25:04",
            "Nakshatram": "Shravana 19:16",
            "Rahukalam": "14:38-15:51",
            "Durmuhurtam": "09:19-09:58",
            "Varjam": "23:00-24:30"
        },
        {
            "Thithi": "Chaturthi 22:59",
            "Nakshatram": "Dhanishta 17:41",
            "Rahukalam": "12:14-13:26",
            "Durmuhurtam": "11:54-12:33",
            "Varjam": "24:38-26:11"
        },
        {
            "Thithi": "Panchami 21:40",
            "Nakshatram": "Satabhisha 16:51",
            "Rahukalam": "13:27-14:40",
            "Durmuhurtam": "10:37-11:16",
            "Varjam": "23:14-24:50"
        },
        {
            "Thithi": "Shashti 21:12",
            "Nakshatram": "Purvabhadra 16:50",
            "Rahukalam": "11:02-12:15",
            "Durmuhurtam": "09:19-09:58",
            "Varjam": "26:46-28:25"
        },
        {
            "Thithi": "Saptami 21:38",
            "Nakshatram": "Uttarabhadra 17:40",
            "Rahukalam": "09:49-11:02",
            "Durmuhurtam": "07:23-08:41",
            "Varjam": "None"
        },
        {
            "Thithi": "Ashtami 22:54",
            "Nakshatram": "Revathi 19:20",
            "Rahukalam": "15:55-17:08",
            "Durmuhurtam": "15:50-16:29",
            "Varjam": "None"
        },
        {
            "Thithi": "Navami 24:51",
            "Nakshatram": "Ashwini 21:40",
            "Rahukalam": "08:36-09:49",
            "Durmuhurtam": "12:35-13:14",
            "Varjam": "17:16-19:02"
        },
        {
            "Thithi": "Dashami 27:19",
            "Nakshatram": "Bharani 24:30",
            "Rahukalam": "14:43-15:57",
            "Durmuhurtam": "09:20-09:59",
            "Varjam": "08:24-10:11"
        },
        {
            "Thithi": "Ekadashi 30:02",
            "Nakshatram": "Krittika 27:37",
            "Rahukalam": "12:17-13:30",
            "Durmuhurtam": "11:57-12:36",
            "Varjam": "None"
        },
        {
            "Thithi": "Dwadashi Full",
            "Nakshatram": "Rohini 30:48",
            "Rahukalam": "13:31-14:45",
            "Durmuhurtam": "10:39-11:18",
            "Varjam": "21:44-23:33"
        },
        {
            "Thithi": "Dwadashi 08:49",
            "Nakshatram": "Mrigashira Full Night",
            "Rahukalam": "11:03-12:17",
            "Durmuhurtam": "09:20-09:59",
            "Varjam": "13:07-14:55"
        },
        {
            "Thithi": "Trayodashi 11:27",
            "Nakshatram": "Mrigashira 09:51",
            "Rahukalam": "09:49-11:04",
            "Durmuhurtam": "07:21-08:40",
            "Varjam": "19:14-21:01"
        },
        {
            "Thithi": "Chaturdashi 13:48",
            "Nakshatram": "Aardra 12:39",
            "Rahukalam": "16:01-17:15",
            "Durmuhurtam": "15:56-16:36",
            "Varjam": "25:53-27:39"
        },
        {
            "Thithi": "Poornima 15:47",
            "Nakshatram": "Punarvasu 15:07",
            "Rahukalam": "08:35-09:49",
            "Durmuhurtam": "12:38-13:18",
            "Varjam": "23:49-25:33"
        },
        {
            "Thithi": "Prathama 17:23",
            "Nakshatram": "Pushya 17:13",
            "Rahukalam": "14:48-16:03",
            "Durmuhurtam": "09:20-09:59",
            "Varjam": "None"
        },
        {
            "Thithi": "Dwitiya 18:34",
            "Nakshatram": "Ashlesha 18:54",
            "Rahukalam": "12:19-13:34",
            "Durmuhurtam": "11:59-12:39",
            "Varjam": "None"
        },
        {
            "Thithi": "Tritiya 19:21",
            "Nakshatram": "Magha 20:13",
            "Rahukalam": "13:34-14:49",
            "Durmuhurtam": "10:39-11:19",
            "Varjam": "07:34-09:15"
        },
        {
            "Thithi": "Chaturthi 19:44",
            "Nakshatram": "Purva Phalguni 21:08",
            "Rahukalam": "11:04-12:20",
            "Durmuhurtam": "09:19-09:59",
            "Varjam": "28:30-30:08"
        },
        {
            "Thithi": "Panchami 19:42",
            "Nakshatram": "Uttara 21:39",
            "Rahukalam": "09:49-11:04",
            "Durmuhurtam": "07:18-08:39",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 19:13",
            "Nakshatram": "Hasta 21:45",
            "Rahukalam": "16:07-17:23",
            "Durmuhurtam": "16:02-16:42",
            "Varjam": "29:38-31:13"
        },
        {
            "Thithi": "Saptami 18:18",
            "Nakshatram": "Chitra 21:25",
            "Rahukalam": "08:33-09:49, 14:42-15:22",
            "Durmuhurtam": "12:41-13:21",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 16:55",
            "Nakshatram": "Swathi 20:37",
            "Rahukalam": "14:53-16:09",
            "Durmuhurtam": "09:18-09:59",
            "Varjam": "25:55-27:26"
        },
        {
            "Thithi": "Navami 15:04",
            "Nakshatram": "Vishakha 19:21",
            "Rahukalam": "12:21-13:37",
            "Durmuhurtam": "12:01-12:41",
            "Varjam": "None"
        },
        {
            "Thithi": "Dashami 12:46",
            "Nakshatram": "Anuradha 17:40",
            "Rahukalam": "13:38-14:54",
            "Durmuhurtam": "10:39-11:20",
            "Varjam": "22:48-24:16"
        },
        {
            "Thithi": "Ekadashi 10:05",
            "Nakshatram": "Dwadashi 31:07",
            "Rahukalam": "Jyeshta 15:38",
            "Durmuhurtam": "09:17-09:58, 12:42-13:23",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 27:58",
            "Nakshatram": "Mula 13:19",
            "Rahukalam": "09:48-11:04",
            "Durmuhurtam": "07:14-08:36",
            "Varjam": "11:52-13:19"
        },
        {
            "Thithi": "Chaturdashi 24:48",
            "Nakshatram": "Purvashada 10:53",
            "Rahukalam": "16:13-17:30",
            "Durmuhurtam": "Sunrise 07:13",
            "Varjam": "16:08-16:49"
        },
        {
            "Thithi": "Amavasya 21:45",
            "Nakshatram": "Uttarashada 08:27, Shravana 30:14",
            "Rahukalam": "RK 08:29-09:47",
            "Durmuhurtam": "12:42-13:24",
            "Varjam": "12:05-13:32"
        }
    ],
    "panchangam_feb": [{
            "Thithi": "Magha Shukla, Prathama 19:01",
            "Nakshatram": "Dhanishta 28:23",
            "Rahukalam": "14:57-16:15",
            "Durmuhurtam": "09:15-09:57",
            "Varjam": "09:56-11:24"
        },
        {
            "Thithi": "Dwitiya 16:45",
            "Nakshatram": "Sathabhisha 27:05",
            "Rahukalam": "12:22-13:40",
            "Durmuhurtam": "12:01-12:43",
            "Varjam": "11:12-12:42"
        },
        {
            "Thithi": "Tritiya 15:08",
            "Nakshatram": "Purvabhadra 26:28",
            "Rahukalam": "13:40-14:59",
            "Durmuhurtam": "10:38-11:20",
            "Varjam": "09:19-10:52"
        },
        {
            "Thithi": "Chaturthi 14:17",
            "Nakshatram": "Uttarabhadra 26:39",
            "Rahukalam": "11:04-12:22",
            "Durmuhurtam": "09:14-09:56",
            "Varjam": "12:08-13:45"
        },
        {
            "Thithi": "Panchami 14:16",
            "Nakshatram": "Revathi 27:40",
            "Rahukalam": "09:45-11:04",
            "Durmuhurtam": "07:08-08:32",
            "Varjam": "15:09-16:49"
        },
        {
            "Thithi": "Shashti 15:07",
            "Nakshatram": "Ashwini 29:29",
            "Rahukalam": "16:19-17:38",
            "Durmuhurtam": "16:14-16:56",
            "Varjam": ""
        },
        {
            "Thithi": "Saptami 16:45",
            "Nakshatram": "Bharani Full Night",
            "Rahukalam": "08:25-09:44",
            "Durmuhurtam": "12:44-13:26",
            "Varjam": "16:04-17:50"
        },
        {
            "Thithi": "Ashtami 19:00",
            "Nakshatram": "Bharani 07:57",
            "Rahukalam": "15:01-16:21",
            "Durmuhurtam": "09:12-09:54",
            "Varjam": "21:25-23:13"
        },
        {
            "Thithi": "Navami 21:38",
            "Nakshatram": "Krittika 10:53",
            "Rahukalam": "12:23-13:42",
            "Durmuhurtam": "12:01-12:44",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 24:22",
            "Nakshatram": "Rohini 14:02",
            "Rahukalam": "13:43-15:03",
            "Durmuhurtam": "10:36-11:19",
            "Varjam": "20:21-22:10"
        },
        {
            "Thithi": "Ekadashi 26:57",
            "Nakshatram": "Mrigashira 17:08",
            "Rahukalam": "11:02-12:23, 12:44-13:27",
            "Durmuhurtam": "09:10-09:53",
            "Varjam": ""
        },
        {
            "Thithi": "Dwadashi 29:12",
            "Nakshatram": "Aardra 19:58",
            "Rahukalam": "09:42-11:02",
            "Durmuhurtam": "07:00-08:26",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 30:58",
            "Nakshatram": "Punarvasu 22:23",
            "Rahukalam": "16:25-17:46",
            "Durmuhurtam": "16:20-17:03",
            "Varjam": "09:10-10:56"
        },
        {
            "Thithi": "Chaturdashi Full Night",
            "Nakshatram": "Pushya 24:19",
            "Rahukalam": "08:19-09:40",
            "Durmuhurtam": "12:44-13:27",
            "Varjam": "07:01-08:45"
        },
        {
            "Thithi": "Chaturdashi 08:12",
            "Nakshatram": "Ashlesha 25:44",
            "Rahukalam": "15:05-16:27",
            "Durmuhurtam": "09:07-09:51",
            "Varjam": "13:52-15:34"
        },
        {
            "Thithi": "Purnima 08:55",
            "Nakshatram": "Magha 26:41",
            "Rahukalam": "12:22-13:44",
            "Durmuhurtam": "12:01-12:44",
            "Varjam": "14:12-15:52"
        },
        {
            "Thithi": "Prathama 09:10",
            "Nakshatram": "Purvaphalguni 27:12",
            "Rahukalam": "13:44-15:06",
            "Durmuhurtam": "10:33-11:17",
            "Varjam": "10:51-12:29"
        },
        {
            "Thithi": "Dwitiya 08:59",
            "Nakshatram": "Uttara 27:22",
            "Rahukalam": "11:00-12:22",
            "Durmuhurtam": "09:05-09:49",
            "Varjam": "10:27-12:03"
        },
        {
            "Thithi": "Tritiya 08:26",
            "Nakshatram": "Hasta 27:12",
            "Rahukalam": "09:37-11:00",
            "Durmuhurtam": "06:52-08:20",
            "Varjam": "11:42-13:18"
        },
        {
            "Thithi": "Chaturthi 07:35",
            "Nakshatram": "Panchami 30:27",
            "Rahukalam": "16:30-17:53",
            "Durmuhurtam": "16:25-17:09",
            "Varjam": "11:04-12:38"
        },
        {
            "Thithi": "Shashti 29:04",
            "Nakshatram": "Swathi 26:06",
            "Rahukalam": "08:13-09:36",
            "Durmuhurtam": "12:44-13:28",
            "Varjam": "08:13-09:47"
        },
        {
            "Thithi": "Saptami 27:26",
            "Nakshatram": "Vishakha 25:11",
            "Rahukalam": "15:09-16:32",
            "Durmuhurtam": "09:02-09:46",
            "Varjam": "07:29-09:01"
        },
        {
            "Thithi": "Ashtami 25:33",
            "Nakshatram": "Anuradha 24:01",
            "Rahukalam": "12:22-13:45",
            "Durmuhurtam": "11:59-12:44",
            "Varjam": "None"
        },
        {
            "Thithi": "Navami 23:27",
            "Nakshatram": "Jyeshta 22:37",
            "Rahukalam": "13:46-15:09, 14:58-15:43",
            "Durmuhurtam": "10:30-11:14",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 21:09",
            "Nakshatram": "Mula 21:02",
            "Rahukalam": "10:57-12:21",
            "Durmuhurtam": "08:59-09:44",
            "Varjam": "19:33-21:02"
        },
        {
            "Thithi": "Ekadashi 18:42",
            "Nakshatram": "Purvashada 19:19",
            "Rahukalam": "09:32-10:57",
            "Durmuhurtam": "06:43-08:13",
            "Varjam": "26:43-28:12"
        },
        {
            "Thithi": "Dwadashi 16:12",
            "Nakshatram": "Uttarashada 17:32",
            "Rahukalam": "16:36-18:00",
            "Durmuhurtam": "16:30-17:15",
            "Varjam": "21:15-22:44"
        },
        {
            "Thithi": "Trayodashi 13:46",
            "Nakshatram": "Shravana 15:49",
            "Rahukalam": "08:06-09:31",
            "Durmuhurtam": "15:00-15:45",
            "Varjam": "19:34-21:04"
        }
    ],
    "panchangam_mar": [{
            "Thithi": "Chaturdashi 11:30",
            "Nakshatram": "Dhanishta 14:18",
            "Rahukalam": "15:12-16:37",
            "Durmuhurtam": "08:56-09:41",
            "Varjam": "21:09-22:40"
        },
        {
            "Thithi": "Amavasya 09:34",
            "Nakshatram": "Satabhisha 13:07",
            "Rahukalam": "12:21-13:46",
            "Durmuhurtam": "11:58-12:43",
            "Varjam": "19:20-20:54"
        },
        {
            "Thithi": "Phalguna Shukla, Prathama 08:06",
            "Nakshatram": "Purvabhadra 12:26",
            "Rahukalam": "13:46-15:12",
            "Durmuhurtam": "10:26-11:12",
            "Varjam": "22:00-11:36"
        },
        {
            "Thithi": "Dwitiya 07:15",
            "Nakshatram": "Uttarabhadra 12:22",
            "Rahukalam": "10:54-12:20, 12:43-13:29",
            "Durmuhurtam": "08:53-09:39",
            "Varjam": ""
        },
        {
            "Thithi": "Tritiya 07:05",
            "Nakshatram": "Revathi 12:59",
            "Rahukalam": "09:27-10:53",
            "Durmuhurtam": "06:34-08:06",
            "Varjam": "10:31-12:10"
        },
        {
            "Thithi": "Chaturthi 07:41",
            "Nakshatram": "Ashwini 14:21",
            "Rahukalam": "16:40-18:07",
            "Durmuhurtam": "16:35-17:21",
            "Varjam": "10:07-11:49"
        },
        {
            "Thithi": "Panchami 09:02",
            "Nakshatram": "Bharani 16:24",
            "Rahukalam": "07:58-09:25, 15:02-15:49",
            "Durmuhurtam": "12:43-13:29",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 11:01",
            "Nakshatram": "Krittika 19:01",
            "Rahukalam": "15:14-16:42",
            "Durmuhurtam": "08:49-09:36",
            "Varjam": "16:22-18:08"
        },
        {
            "Thithi": "Saptami 13:26",
            "Nakshatram": "Rohini 22:00",
            "Rahukalam": "12:19-13:47",
            "Durmuhurtam": "11:56-12:42",
            "Varjam": "13:01-14:49"
        },
        {
            "Thithi": "Ashtami 16:04",
            "Nakshatram": "Mrigashira 25:06",
            "Rahukalam": "13:47-15:15, 15:03-15:50",
            "Durmuhurtam": "10:21-11:08",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 18:37",
            "Nakshatram": "Aardra 28:02",
            "Rahukalam": "10:50-12:18",
            "Durmuhurtam": "08:46-09:33",
            "Varjam": "10:31-12:19"
        },
        {
            "Thithi": "Dashami 20:51",
            "Nakshatram": "Punarvasu",
            "Rahukalam": "09:21-10:49",
            "Durmuhurtam": "06:23-07:58",
            "Varjam": "17:19-19:05"
        },
        {
            "Thithi": "Ekadashi 23:35",
            "Nakshatram": "Punarvasu 07:36",
            "Rahukalam": "17:45-19:14",
            "Durmuhurtam": "17:39-18:26",
            "Varjam": "16:17-18:01"
        },
        {
            "Thithi": "Dwadashi 24:42",
            "Nakshatram": "Pushya 09:38",
            "Rahukalam": "08:50-10:19, 16:04-16:52",
            "Durmuhurtam": "13:41-14:29",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 25:09",
            "Nakshatram": "Ashlesha 11:03",
            "Rahukalam": "16:17-17:46",
            "Durmuhurtam": "09:21-11:03",
            "Varjam": "23:27-25:06"
        },
        {
            "Thithi": "Chaturdashi 24:59",
            "Nakshatram": "Magha 11:51",
            "Rahukalam": "13:17-14:47",
            "Durmuhurtam": "12:53-13:41",
            "Varjam": "19:55-21:32"
        },
        {
            "Thithi": "Purnima 24:17",
            "Nakshatram": "Purvaphalguni 12:04",
            "Rahukalam": "14:47-16:17",
            "Durmuhurtam": "11:17-12:05",
            "Varjam": "19:11-20:46"
        },
        {
            "Thithi": "Prathama 23:07",
            "Nakshatram": "Uttara 11:48",
            "Rahukalam": "11:46-13:16",
            "Durmuhurtam": "09:39-10:28",
            "Varjam": "19:58-21:31"
        },
        {
            "Thithi": "Dwitiya 21:36",
            "Nakshatram": "Hasta 11:08",
            "Rahukalam": "08:01-08:50",
            "Durmuhurtam": "07:13-08:50",
            "Varjam": "18:49-20:21"
        },
        {
            "Thithi": "Tritiya 19:50",
            "Nakshatram": "Chitra 10:10",
            "Rahukalam": "17:49-19:20",
            "Durmuhurtam": "17:43-18:32",
            "Varjam": "15:30-17:01"
        },
        {
            "Thithi": "Chaturthi 17:54",
            "Nakshatram": "Swathi 09:01",
            "Rahukalam": "08:41-10:13",
            "Durmuhurtam": "13:40-14:29",
            "Varjam": "14:19-15:50"
        },
        {
            "Thithi": "Panchami 15:51",
            "Nakshatram": "VIshakha 07:44",
            "Rahukalam": "16:19-17:50",
            "Durmuhurtam": "09:35-10:24",
            "Varjam": "11:30-13:01"
        },
        {
            "Thithi": "Shashti 13:46",
            "Nakshatram": "Jyeshta 29:00",
            "Rahukalam": "13:15-14:47",
            "Durmuhurtam": "12:50-13:40",
            "Varjam": "11:39-13:10"
        },
        {
            "Thithi": "Saptami 11:39",
            "Nakshatram": "Mula 27:37",
            "Rahukalam": "14:47-16:16",
            "Durmuhurtam": "11:12-12:01",
            "Varjam": "12:32-14:03"
        },
        {
            "Thithi": "Ashtami 09:34",
            "Nakshatram": "Purvashada 26:17",
            "Rahukalam": "11:42-13:14",
            "Durmuhurtam": "09:32-10:22",
            "Varjam": "12:41-14:12"
        },
        {
            "Thithi": "Navami 07:31, Dashami. 29:34",
            "Nakshatram": "Uttarashada 25:02",
            "Rahukalam": "10:08-11:41",
            "Durmuhurtam": "07:03-08:42",
            "Varjam": "09:52-11:23"
        },
        {
            "Thithi": "Ekadashi 27:45",
            "Nakshatram": "Shravana 23:54",
            "Rahukalam": "17:53-19:27",
            "Durmuhurtam": "17:47-18:37",
            "Varjam": "27:45-29:17"
        },
        {
            "Thithi": "Dwadashi 26:08",
            "Nakshatram": "Dhanishta 22:58",
            "Rahukalam": "08:33-10:07, 16:08-16:58",
            "Durmuhurtam": "13:38-14:28",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 24:49",
            "Nakshatram": "Shatabhisha 22:19",
            "Rahukalam": "16:21-17:55",
            "Durmuhurtam": "09:28-10:18",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturdashi 23:52",
            "Nakshatram": "Purvabhadra 22:01",
            "Rahukalam": "13:13-14:47",
            "Durmuhurtam": "12:48-13:38",
            "Varjam": ""
        },
        {
            "Thithi": "Amavasya 23:23",
            "Nakshatram": "Uttara 22:10",
            "Rahukalam": "14:47-16:21",
            "Durmuhurtam": "11:07-11:57",
            "Varjam": "07:40-09:17"
        }
    ],
    "panchangam_april": [{
            "Thithi": "Chitra Shukla, Prathama 23:28",
            "Nakshatram": "Revathi 22:51",
            "Rahukalam": "11:38-13:12",
            "Durmuhurtam": "09:25-10:16, 13:38-14:28",
            "Varjam": "10:30-12:09"
        },
        {
            "Thithi": "Dwitiya 24:08",
            "Nakshatram": "Ashwini 24:07",
            "Rahukalam": "10:02-11:37",
            "Durmuhurtam": "06:52-08:33",
            "Varjam": "19:54-21:36"
        },
        {
            "Thithi": "Tritiya 25:25",
            "Nakshatram": "Bharani 25:59",
            "Rahukalam": "17:58-19:33",
            "Durmuhurtam": "17:51-18:42",
            "Varjam": "10:28-12:11"
        },
        {
            "Thithi": "Chaturthi 27:15",
            "Nakshatram": "Krittika 28:22",
            "Rahukalam": "08:25-10:00",
            "Durmuhurtam": "13:37-14:28, 16:10-17:01",
            "Varjam": "15:10-16:56"
        },
        {
            "Thithi": "Panchami 29:31",
            "Nakshatram": "Rohini Full Night",
            "Rahukalam": "16:23-17:59",
            "Durmuhurtam": "09:21-10:12",
            "Varjam": "22:14-24:01"
        },
        {
            "Thithi": "Shashti Full Night",
            "Nakshatram": "Rohini 07:10",
            "Rahukalam": "13:11-14:47",
            "Durmuhurtam": "08:22-09:59",
            "Varjam": "13:28-15:16"
        },
        {
            "Thithi": "Shashti 08:02",
            "Nakshatram": "Mrigashira 10:12",
            "Rahukalam": "14:47-16:24",
            "Durmuhurtam": "11:02-11:53, 16:11-17:02",
            "Varjam": "19:39-21:27"
        },
        {
            "Thithi": "Saptami 10:35",
            "Nakshatram": "Aardra 13:13",
            "Rahukalam": "11:34-13:10, 13:36-14:28",
            "Durmuhurtam": "09:18-10:10",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 12:53",
            "Nakshatram": "Punarvasu 16:01",
            "Rahukalam": "09:56-11:33",
            "Durmuhurtam": "06:42-08:25",
            "Varjam": "24:48-26:33"
        },
        {
            "Thithi": "Navami 14:45",
            "Nakshatram": "Pushya 18:21",
            "Rahukalam": "18:02-19:39",
            "Durmuhurtam": "17:55-18:47",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 16:00",
            "Nakshatram": "Ashlesha 20:05",
            "Rahukalam": "08:17-09:54",
            "Durmuhurtam": "13:36-14:28, 16:12-17:04",
            "Varjam": "08:04-09:47"
        },
        {
            "Thithi": "Ekadashi 16:32",
            "Nakshatram": "Magha 21:07",
            "Rahukalam": "16:25-18:03",
            "Durmuhurtam": "09:14-10:06",
            "Varjam": "08:36-10:16"
        },
        {
            "Thithi": "Dwadashi 16:19",
            "Nakshatram": "Purvaphalguni 21:26",
            "Rahukalam": "13:09-14:47",
            "Durmuhurtam": "12:43-13:35",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 15:25",
            "Nakshatram": "Uttara 21:05",
            "Rahukalam": "14:47-16:26",
            "Durmuhurtam": "10:57-11:13, 16:13-17:05",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturdashi 13:55",
            "Nakshatram": "Hasta 20:10",
            "Rahukalam": "11:30-13:08",
            "Durmuhurtam": "09:11-10:04, 13:35-14:28",
            "Varjam": ""
        },
        {
            "Thithi": "Purnima 11:54",
            "Nakshatram": "Chitra 18:47",
            "Rahukalam": "09:50-11:29",
            "Durmuhurtam": "06:32-08:18",
            "Varjam": "23:59-25:28"
        },
        {
            "Thithi": "Prathama 09:31",
            "Nakshatram": "Swathi 17:04",
            "Rahukalam": "18:06-19:45",
            "Durmuhurtam": "17:59-18:52",
            "Varjam": "22:13-23:41"
        },
        {
            "Thithi": "Dwitiya 06:53, Tritiya 28:08",
            "Nakshatram": "Vishakha 15:09",
            "Rahukalam": "08:09-09:49",
            "Durmuhurtam": "16:14-17:07",
            "Varjam": "18:49-20:17"
        },
        {
            "Thithi": "Chaturthi 25:22",
            "Nakshatram": "Anuradha 13:09",
            "Rahukalam": "16:27-18:07",
            "Durmuhurtam": "09:08-10:01",
            "Varjam": "18:17-19:46"
        },
        {
            "Thithi": "Panchami 22:42",
            "Nakshatram": "Jyeshta 11:11",
            "Rahukalam": "13:07-14:48",
            "Durmuhurtam": "12:41-13:34",
            "Varjam": "18:35-20:03"
        },
        {
            "Thithi": "Shashti 20:12",
            "Nakshatram": "Mula 09:22",
            "Rahukalam": "14:48-16:28",
            "Durmuhurtam": "10:53-11:47",
            "Varjam": "07:53-09:22"
        },
        {
            "Thithi": "Saptami 17:57",
            "Nakshatram": "Purvashada 07:44",
            "Rahukalam": "11:26-13:07",
            "Durmuhurtam": "09:05-09:59",
            "Varjam": "15:17-16:48"
        },
        {
            "Thithi": "Ashtami 15:59",
            "Nakshatram": "Uttarashada 06:24",
            "Rahukalam": "09:45-11:26",
            "Durmuhurtam": "06:23-08:10",
            "Varjam": "10:13-11:45"
        },
        {
            "Thithi": "Navami 14:22",
            "Nakshatram": "Dhanishta 28:43",
            "Rahukalam": "18:10-19:52",
            "Durmuhurtam": "18:04-18:58",
            "Varjam": "09:16-10:49"
        },
        {
            "Thithi": "Dashami 13:08",
            "Nakshatram": "Sathabhisha 28:26",
            "Rahukalam": "08:02-09:43",
            "Durmuhurtam": "13:33-14:28, 16:16-17:10",
            "Varjam": "11:50-13:25"
        },
        {
            "Thithi": "Ekadashi 12:17",
            "Nakshatram": "Purvabhadra 28:35",
            "Rahukalam": "16:30-18:12",
            "Durmuhurtam": "09:02-9:56",
            "Varjam": "10:53-12:29"
        },
        {
            "Thithi": "Dwadashi 11:53",
            "Nakshatram": "Uttarabhadra 29:10",
            "Rahukalam": "13:06-14:48",
            "Durmuhurtam": "12:39-13:33",
            "Varjam": "14:25-16:04"
        },
        {
            "Thithi": "Trayodashi 11:56",
            "Nakshatram": "Revathi 30:13",
            "Rahukalam": "14:48-16:31",
            "Durmuhurtam": "10:49-11:44",
            "Varjam": "17:41-19:22"
        },
        {
            "Thithi": "Chaturdashi 12:27",
            "Nakshatram": "Ashwini Full Night",
            "Rahukalam": "11:23-13:06",
            "Durmuhurtam": "09:00-09:54, 13:33-14:28",
            "Varjam": ""
        },
        {
            "Thithi": "Amavasya 13:27",
            "Nakshatram": "Ashwini 07:43",
            "Rahukalam": "09:40-11:23",
            "Durmuhurtam": "06:14-08:04",
            "Varjam": "18:06-19:50"
        }
    ],
    "panchangam_may": [{
            "Thithi": "Vaishakha Shukla, Prathama 14:55",
            "Nakshatram": "Bharani 09:41",
            "Rahukalam": "18:15-19:58",
            "Durmuhurtam": "18:08-19:03",
            "Varjam": "22:52-24:38"
        },
        {
            "Thithi": "Dwitiya 16:48",
            "Nakshatram": "Krittika 12:04",
            "Rahukalam": "07:55-09:39",
            "Durmuhurtam": "13:33-14:28, 16:18-17:14",
            "Varjam": ""
        },
        {
            "Thithi": "Tritiya 19:02",
            "Nakshatram": "Rohini 14:48",
            "Rahukalam": "16:33-18:16",
            "Durmuhurtam": "08:57-09:52",
            "Varjam": "21:06-22:54"
        },
        {
            "Thithi": "Chaturthi 21:30",
            "Nakshatram": "Mrigashira 17:47",
            "Rahukalam": "13:05-14:49",
            "Durmuhurtam": "12:38-13:33",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 24:02",
            "Nakshatram": "Aardra 20:50",
            "Rahukalam": "14:49-16:33",
            "Durmuhurtam": "10:46-11:42",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 26:26",
            "Nakshatram": "Punarvasu 23:48",
            "Rahukalam": "11:21-13:05",
            "Durmuhurtam": "08:55-09:50",
            "Varjam": "10:19-12:07"
        },
        {
            "Thithi": "Saptami 28:30",
            "Nakshatram": "Pushya 26:28",
            "Rahukalam": "09:36-11:20",
            "Durmuhurtam": "06:07-07:58",
            "Varjam": "08:41-10:28"
        },
        {
            "Thithi": "Ashtami 30:02",
            "Nakshatram": "Ashlesha 28:38",
            "Rahukalam": "18:19-20:04",
            "Durmuhurtam": "18:12-19:08",
            "Varjam": "16:25-18:10"
        },
        {
            "Thithi": "Navami Full Night",
            "Nakshatram": "Magha Full Night",
            "Rahukalam": "07:50-09:35",
            "Durmuhurtam": "13:33-14:29",
            "Varjam": "17:24-19:06"
        },
        {
            "Thithi": "Navami 06:54",
            "Nakshatram": "Magha 06:10",
            "Rahukalam": "16:35-18:21",
            "Durmuhurtam": "08:52-09:48",
            "Varjam": "14:26-16:05"
        },
        {
            "Thithi": "Dashami 07:01",
            "Nakshatram": "Puravaphalguni 06:58",
            "Rahukalam": "13:05-14:50",
            "Durmuhurtam": "12:37-13:33",
            "Varjam": "14:10-15:47"
        },
        {
            "Thithi": "Ekadashi 06:21, Dwadashi 28:57",
            "Nakshatram": "Uttara 07:00",
            "Rahukalam": "14:51-16:36",
            "Durmuhurtam": "10:44-11:40",
            "Varjam": "15:09-16:43"
        },
        {
            "Thithi": "Trayodashi 26:52",
            "Nakshatram": "Hasta 06:18",
            "Rahukalam": "11:19-13:05",
            "Durmuhurtam": "08:50-09:47",
            "Varjam": "13:52-15:22"
        },
        {
            "Thithi": "Chaturdashi 24:15",
            "Nakshatram": "Swathi 27:05",
            "Rahukalam": "09:32-11:19",
            "Durmuhurtam": "06:00-07:53",
            "Varjam": "10:07-11:36"
        },
        {
            "Thithi": "Purnima 21:13",
            "Nakshatram": "Vishakha 24:48",
            "Rahukalam": "18:24-20:10",
            "Durmuhurtam": "18:17-19:14",
            "Varjam": "08:09-09:36"
        },
        {
            "Thithi": "Prathama 17:55",
            "Nakshatram": "Anuradha 22:16",
            "Rahukalam": "07:45-09:32",
            "Durmuhurtam": "13:33-14:30, 16:24-17:21",
            "Varjam": ""
        },
        {
            "Thithi": "Dwitiya 14:30",
            "Nakshatram": "Jyeshta 19:40",
            "Rahukalam": "16:38-18:25",
            "Durmuhurtam": "08:48-09:45",
            "Varjam": "26:49-28:15"
        },
        {
            "Thithi": "Tritiya 11:06",
            "Nakshatram": "Mula 17:07",
            "Rahukalam": "13:05-14:52",
            "Durmuhurtam": "12:36-13:33",
            "Varjam": "15:41-17:07"
        },
        {
            "Thithi": "Chaturthi 07:53",
            "Nakshatram": "Panchami 28:58",
            "Rahukalam": "14:52-16:39",
            "Durmuhurtam": "10:42-11:39, 16:25-17:22",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 26:29",
            "Nakshatram": "Uttarashada 12:48",
            "Rahukalam": "11:18-13:05",
            "Durmuhurtam": "08:47-09:44, 13:34-14:31",
            "Varjam": "16:33-18:03"
        },
        {
            "Thithi": "Saptami 24:29",
            "Nakshatram": "Shravana 11:16",
            "Rahukalam": "09:30-11:17",
            "Durmuhurtam": "05:55-07:49",
            "Varjam": "15:06-16:38"
        },
        {
            "Thithi": "Ashtami 23:04",
            "Nakshatram": "Dhanishta 10:17",
            "Rahukalam": "18:28-20:16",
            "Durmuhurtam": "18:21-19:19",
            "Varjam": "17:21-18:56"
        },
        {
            "Thithi": "Navami 22:15",
            "Nakshatram": "Satabhisha 09:52",
            "Rahukalam": "07:41-09:29",
            "Durmuhurtam": "13:34-14:31",
            "Varjam": "16:19-17:56"
        },
        {
            "Thithi": "Dashami 22:02",
            "Nakshatram": "Purvabhadra 10:03",
            "Rahukalam": "16:41-18:30",
            "Durmuhurtam": "08:46-09:43",
            "Varjam": "19:58-21:37"
        },
        {
            "Thithi": "Ekadashi 22:24",
            "Nakshatram": "Uttarabhadra 10:50",
            "Rahukalam": "13:05-14:54",
            "Durmuhurtam": "13:05-14:54",
            "Varjam": "23:36-25:10"
        },
        {
            "Thithi": "Dwadashi 23:17",
            "Nakshatram": "Revathi 12:09",
            "Rahukalam": "14:54-16:42",
            "Durmuhurtam": "10:41-11:39, 16:28-17:26",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 24:39",
            "Nakshatram": "Ashwini 13:56",
            "Rahukalam": "11:17-13:06",
            "Durmuhurtam": "08:45-09:43",
            "Varjam": "09:39-11:22"
        },
        {
            "Thithi": "Chaturdashi 26:24",
            "Nakshatram": "Bharani 16:09",
            "Rahukalam": "09:28-11:17",
            "Durmuhurtam": "05:51-07:47",
            "Varjam": ""
        },
        {
            "Thithi": "Amavasya 28:29",
            "Nakshatram": "Krittika 18:42",
            "Rahukalam": "18:32-20:21",
            "Durmuhurtam": "18:25-19:23",
            "Varjam": ""
        },
        {
            "Thithi": "Jyeshta Shukla, Prathama Full Night",
            "Nakshatram": "Rohini Full Night",
            "Rahukalam": "07:39-09:28",
            "Durmuhurtam": "13:35-14:33",
            "Varjam": "12:35-14:22"
        },
        {
            "Thithi": "Prathama 06:48",
            "Nakshatram": "Mrigashira 24:31",
            "Rahukalam": "16:44-18:34",
            "Durmuhurtam": "08:44-09:42",
            "Varjam": ""
        }
    ],
    "panchangam_june": [{
            "Thithi": "Dwitiya 09:16",
            "Nakshatram": "Aardra 27:34",
            "Rahukalam": "13:06-14:55",
            "Durmuhurtam": "12:37-13:35",
            "Varjam": "09:59-11:47"
        },
        {
            "Thithi": "Tritiya 11:47",
            "Nakshatram": "Punarvasu Full Night",
            "Rahukalam": "14:56-16:45",
            "Durmuhurtam": "10:40-11:39",
            "Varjam": "17:05-18:53"
        },
        {
            "Thithi": "Chaturthi 14:11",
            "Nakshatram": "Punarvasu 06:35",
            "Rahukalam": "11:17-13:06",
            "Durmuhurtam": "08:44-09:42",
            "Varjam": "15:32-17:19"
        },
        {
            "Thithi": "Panchami 16:22",
            "Nakshatram": "Pushya 09:25",
            "Rahukalam": "09:27-11:17",
            "Durmuhurtam": "05:48-07:45",
            "Varjam": "23:33-25:19"
        },
        {
            "Thithi": "Shashti 18:09",
            "Nakshatram": "Ashlesha 11:55",
            "Rahukalam": "18:36-20:26",
            "Durmuhurtam": "18:29-19:27",
            "Varjam": "24:55-26:40"
        },
        {
            "Thithi": "Saptami 19:24",
            "Nakshatram": "Magha 13:56",
            "Rahukalam": "07:37-09:27",
            "Durmuhurtam": "16:32-17:31",
            "Varjam": "22:24-24:05"
        },
        {
            "Thithi": "Ashtami 20:00",
            "Nakshatram": "Purvaphalguni 15:20",
            "Rahukalam": "16:47-18:37",
            "Durmuhurtam": "08:43-09:42",
            "Varjam": "22:44-24:23"
        },
        {
            "Thithi": "Navami 19:51",
            "Nakshatram": "Uttara 16:01",
            "Rahukalam": "13:07-14:57",
            "Durmuhurtam": "12:38-13:37",
            "Varjam": "24:23-25:59"
        },
        {
            "Thithi": "Dashami 18:55",
            "Nakshatram": "Hasta 15:56",
            "Rahukalam": "14:58-16:48",
            "Durmuhurtam": "10:41-11:39, 16:33-17:32",
            "Varjam": ""
        },
        {
            "Thithi": "Ekadashi 17:15",
            "Nakshatram": "Chitra 15:07",
            "Rahukalam": "11:18-13:08",
            "Durmuhurtam": "08:43-09:42",
            "Varjam": "20:21-21:51"
        },
        {
            "Thithi": "Dwadashi 14:53",
            "Nakshatram": "Swathi 13:35",
            "Rahukalam": "09:27-11:18",
            "Durmuhurtam": "05:47-07:44",
            "Varjam": "18:42-20:09"
        },
        {
            "Thithi": "Trayodashi 11:56",
            "Nakshatram": "Vishakha 11:28",
            "Rahukalam": "18:39-20:29",
            "Durmuhurtam": "18:32-19:31",
            "Varjam": "15:03-16:28"
        },
        {
            "Thithi": "Chaturdashi 08:32, Purnima 28:51",
            "Nakshatram": "Anuradha 08:54",
            "Rahukalam": "07:37-09:28",
            "Durmuhurtam": "13:38-14:37",
            "Varjam": "13:50-15:15"
        },
        {
            "Thithi": "Prathama 25:01",
            "Nakshatram": "Jyeshta 06:02, Mula 27:03",
            "Rahukalam": "16:49-18:40",
            "Durmuhurtam": "08:43-09:42",
            "Varjam": "13:02-14:26"
        },
        {
            "Thithi": "Dwitiya 21:14",
            "Nakshatram": "Purvashada 24:07",
            "Rahukalam": "13:09-14:59",
            "Durmuhurtam": "12:39-13:38",
            "Varjam": "11:29-12:53"
        },
        {
            "Thithi": "Tritiya 17:40",
            "Nakshatram": "Uttarashada 21:26",
            "Rahukalam": "14:59-16:50",
            "Durmuhurtam": "10:42-11:41",
            "Varjam": "07:13-08:39"
        },
        {
            "Thithi": "Chaturthi 14:29",
            "Nakshatram": "Shravana 19:09",
            "Rahukalam": "11:19-13:09",
            "Durmuhurtam": "08:44-09:43",
            "Varjam": "22:52-24:21"
        },
        {
            "Thithi": "Panchami 11:49",
            "Nakshatram": "Dhanishta 17:26",
            "Rahukalam": "09:28-11:19",
            "Durmuhurtam": "05:47-07:45",
            "Varjam": "24:19-25:51"
        },
        {
            "Thithi": "Shashti 09:48",
            "Nakshatram": "Sathabhisha 16:23",
            "Rahukalam": "18:41-20:32",
            "Durmuhurtam": "18:34-19:33",
            "Varjam": "22:42-24:17"
        },
        {
            "Thithi": "Saptami 08:31",
            "Nakshatram": "Purvabhadra 16:05",
            "Rahukalam": "07:38-09:29",
            "Durmuhurtam": "13:39-14:38, 16:36-17:35",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 08:00",
            "Nakshatram": "Uttarabhadra 16:33",
            "Rahukalam": "16:51-18:42",
            "Durmuhurtam": "08:45-09:44",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 08:15",
            "Nakshatram": "Revathi 17:44",
            "Rahukalam": "13:10-15:01",
            "Durmuhurtam": "12:41-13:40",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 09:11",
            "Nakshatram": "Ashwini 19:34",
            "Rahukalam": "15:01-16:51",
            "Durmuhurtam": "10:43-11:42",
            "Varjam": "15:16-16:59"
        },
        {
            "Thithi": "Ekadashi 10:42",
            "Nakshatram": "Bharani 21:54",
            "Rahukalam": "11:20-13:11",
            "Durmuhurtam": "08:45-09:44",
            "Varjam": "06:06-07:51"
        },
        {
            "Thithi": "Dwadashi 12:39",
            "Nakshatram": "Krittika 24:36",
            "Rahukalam": "09:30-11:20",
            "Durmuhurtam": "05:49-07:47",
            "Varjam": "11:15-13:02"
        },
        {
            "Thithi": "Trayodashi 14:55",
            "Nakshatram": "Rohini 27:32",
            "Rahukalam": "18:42-20:33",
            "Durmuhurtam": "18:35-19:34",
            "Varjam": "18:34-20:21"
        },
        {
            "Thithi": "Chaturdashi 17:22",
            "Nakshatram": "Mrigashira Full Night",
            "Rahukalam": "07:40-09:30",
            "Durmuhurtam": "13:41-14:40",
            "Varjam": "09:51-11:39"
        },
        {
            "Thithi": "Amavasya 19:51",
            "Nakshatram": "Mrigashira 06:35",
            "Rahukalam": "16:52-18:43",
            "Durmuhurtam": "08:46-09:45",
            "Varjam": "16:03-17:52"
        },
        {
            "Thithi": "Ashada Shukla, Prathama 22:19",
            "Nakshatram": "Ardra 09:39",
            "Rahukalam": "13:12-15:02",
            "Durmuhurtam": "12:42-13:41",
            "Varjam": "23:08-24:56"
        },
        {
            "Thithi": "Dwitiya 24:39",
            "Nakshatram": "Punarvasu 12:37",
            "Rahukalam": "15:02-16:52",
            "Durmuhurtam": "10:45-11:44",
            "Varjam": "21:34-23:21"
        }
    ],
    "panchangam_july": [{
            "Thithi": "Tritiya 26:46",
            "Nakshatram": "Pushya 15:26",
            "Rahukalam": "11:22-13:12",
            "Durmuhurtam": "08:47-09:46, 13:41-14:40",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturthi 28:36",
            "Nakshatram": "Ashlesha 18:00",
            "Rahukalam": "09:32-11:22",
            "Durmuhurtam": "05:52-07:49",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami Full Night",
            "Nakshatram": "Magha 20:14",
            "Rahukalam": "18:42-20:32",
            "Durmuhurtam": "18:35-19:34",
            "Varjam": "07:07-08:52"
        },
        {
            "Thithi": "Panchami 06:02",
            "Nakshatram": "Purvaphalguni 22:00",
            "Rahukalam": "07:43-09:33",
            "Durmuhurtam": "13:42-14:40",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 06:58",
            "Nakshatram": "Uttara 23:14",
            "Rahukalam": "16:52-18:42",
            "Durmuhurtam": "08:49-09:48",
            "Varjam": ""
        },
        {
            "Thithi": "Saptami 07:18",
            "Nakshatram": "Hasta 23:50",
            "Rahukalam": "13:13-15:03",
            "Durmuhurtam": "12:44-13:42",
            "Varjam": "07:51-09:29"
        },
        {
            "Thithi": "Ashtami 06:58, Navami 29:55",
            "Nakshatram": "Chitra 23:44",
            "Rahukalam": "15:03-16:52",
            "Durmuhurtam": "10:47-11:45",
            "Varjam": "07:48-09:23"
        },
        {
            "Thithi": "Dashami 28:09",
            "Nakshatram": "Swathi 22:55",
            "Rahukalam": "11:24-13:13",
            "Durmuhurtam": "08:50-09:49",
            "Varjam": "28:10-29:40"
        },
        {
            "Thithi": "Ekadashi 25:43",
            "Nakshatram": "Vishakha 21:25",
            "Rahukalam": "09:34-11:24",
            "Durmuhurtam": "05:55-07:52",
            "Varjam": "25:04-26:32"
        },
        {
            "Thithi": "Dwadashi 22:43",
            "Nakshatram": "Anuradha 19:20",
            "Rahukalam": "18:41-20:31",
            "Durmuhurtam": "18:34-19:32",
            "Varjam": "24:20-25:45"
        },
        {
            "Thithi": "Trayodashi 19:16",
            "Nakshatram": "Jyeshta 16:45",
            "Rahukalam": "07:46-09:35",
            "Durmuhurtam": "13:43-14:41",
            "Varjam": "23:47-25:12"
        },
        {
            "Thithi": "Chaturdashi 15:30",
            "Nakshatram": "Mula 13:51",
            "Rahukalam": "16:52-18:41",
            "Durmuhurtam": "08:52-09:50",
            "Varjam": "12:27-13:51"
        },
        {
            "Thithi": "Purnima 11:36",
            "Nakshatram": "Purvashada 10:48",
            "Rahukalam": "13:14-15:03",
            "Durmuhurtam": "12:45-13:43",
            "Varjam": "17:48-19:12"
        },
        {
            "Thithi": "Prathama 07:46, Dwitiya 28:09",
            "Nakshatram": "Uttarashada 07:48",
            "Rahukalam": "15:03-16:51",
            "Durmuhurtam": "",
            "Varjam": ""
        },
        {
            "Thithi": "Tritiya 24:57",
            "Nakshatram": "Dhanishta 26:40",
            "Rahukalam": "11:25-13:14",
            "Durmuhurtam": "08:53-09:51",
            "Varjam": "08:38-10:04"
        },
        {
            "Thithi": "Chaturthi 22:19",
            "Nakshatram": "Sathabhisha 24:55",
            "Rahukalam": "09:37-11:26",
            "Durmuhurtam": "06:00-06:58",
            "Varjam": "09:21-10:50"
        },
        {
            "Thithi": "Pachami 20:24",
            "Nakshatram": "Purvabhadra 23:54",
            "Rahukalam": "18:39-20:27",
            "Durmuhurtam": "18:32-19:30",
            "Varjam": "07:03-08:34"
        },
        {
            "Thithi": "Shashti 19:19",
            "Nakshatram": "Uttarabhadra 23:42",
            "Rahukalam": "07:50-09:38",
            "Durmuhurtam": "13:43-14:41",
            "Varjam": "09:25-11:00"
        },
        {
            "Thithi": "Saptami 19:05",
            "Nakshatram": "Revathi 24:20",
            "Rahukalam": "16:50-18:38",
            "Durmuhurtam": "08:55-09:53",
            "Varjam": "12:01-13:40"
        },
        {
            "Thithi": "Ashtami 19:42",
            "Nakshatram": "Ashwini 25:47",
            "Rahukalam": "13:14-15:02",
            "Durmuhurtam": "12:46-13:43",
            "Varjam": "21:33-23:15"
        },
        {
            "Thithi": "Navami 21:02",
            "Nakshatram": "Bharani 27:55",
            "Rahukalam": "15:02-16:50",
            "Durmuhurtam": "10:51-11:48",
            "Varjam": "12:14-13:59"
        },
        {
            "Thithi": "Dashami 22:57",
            "Nakshatram": "Krittika Full night",
            "Rahukalam": "11:27-13:14",
            "Durmuhurtam": "08:57-09:54",
            "Varjam": "17:14-19:01"
        },
        {
            "Thithi": "Ekadashi 25:15",
            "Nakshatram": "Krittika 06:33",
            "Rahukalam": "09:40-11:27",
            "Durmuhurtam": "06:05-08:00",
            "Varjam": "24:31-26:19"
        },
        {
            "Thithi": "Dwadashi 27:45",
            "Nakshatram": "Rohini 09:30",
            "Rahukalam": "18:36-20:23",
            "Durmuhurtam": "18:28-19:26",
            "Varjam": "15:50-17:38"
        },
        {
            "Thithi": "Trayodashi Full Night",
            "Nakshatram": "Mrigashira 12:36",
            "Rahukalam": "07:54-09:41",
            "Durmuhurtam": "13:43-14:40",
            "Varjam": "22:04-23:52"
        },
        {
            "Thithi": "Trayodashi 06:16",
            "Nakshatram": "Aardra 15:39",
            "Rahukalam": "16:48-18:34",
            "Durmuhurtam": "08:58-09:55",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturdashi 08:41",
            "Nakshatram": "Punarvasu 18:35",
            "Rahukalam": "13:14-15:01",
            "Durmuhurtam": "12:46-13:43",
            "Varjam": "27:29-29:16"
        },
        {
            "Thithi": "Amavasya 10:54",
            "Nakshatram": "Pushya 21:17",
            "Rahukalam": "15:01-16:47",
            "Durmuhurtam": "10:53-11:49, 16:33-17:29",
            "Varjam": ""
        },
        {
            "Thithi": "Shravana Shukla, Prathama 12:51",
            "Nakshatram": "Ashlesha 23:43",
            "Rahukalam": "11:28-13:14",
            "Durmuhurtam": "09:00-09:56, 13:43-14:39",
            "Varjam": "11:23-13:08"
        },
        {
            "Thithi": "Dwitiya 14:29",
            "Nakshatram": "Magha 25:50",
            "Rahukalam": "09:43-11:29",
            "Durmuhurtam": "06:11-08:04",
            "Varjam": "12:46-14:31"
        },
        {
            "Thithi": "Tritiya 15:48",
            "Nakshatram": "Purvaphalguni 27:36",
            "Rahukalam": "18:31-20:17",
            "Durmuhurtam": "18:24-19:20",
            "Varjam": "10:26-12:09"
        }
    ],
    "panchangam_aug": [{
            "Thithi": "Chaturthi 16:43",
            "Nakshatram": "Uttara 28:59",
            "Rahukalam": "07:58-09:43",
            "Durmuhurtam": "13:42-14:39",
            "Varjam": "11:13-12:55"
        },
        {
            "Thithi": "Panchami 17:11",
            "Nakshatram": "Hasta 29:54",
            "Rahukalam": "16:44-18:30",
            "Durmuhurtam": "09:02-09:58",
            "Varjam": "13:42-15:22"
        },
        {
            "Thithi": "Shashti 17:10",
            "Nakshatram": "Chitra Full Night",
            "Rahukalam": "13:14-14:59",
            "Durmuhurtam": "12:46-13:42",
            "Varjam": "14:02-15:39"
        },
        {
            "Thithi": "Saptami 16:36",
            "Nakshatram": "Chitra 06:18",
            "Rahukalam": "14:59-16:43",
            "Durmuhurtam": "10:54-11:50",
            "Varjam": "11:51-13:27"
        },
        {
            "Thithi": "Ashtami 15:26",
            "Nakshatram": "Vishakha 29:22",
            "Rahukalam": "11:29-13:14",
            "Durmuhurtam": "09:03-09:29",
            "Varjam": "11:33-13:06"
        },
        {
            "Thithi": "Navami 13:41",
            "Nakshatram": "Anuradha 28:00",
            "Rahukalam": "09:45-11:30",
            "Durmuhurtam": "06:17-08:08",
            "Varjam": "09:08-10:39"
        },
        {
            "Thithi": "Dashami 11:20",
            "Nakshatram": "Jyeshta 26:07",
            "Rahukalam": "18:26-20:10",
            "Durmuhurtam": "18:19-19:14",
            "Varjam": "09:10-10:38"
        },
        {
            "Thithi": "Ekadashi 08:30, Dwadashi 29:15",
            "Nakshatram": "Mula 23:48",
            "Rahukalam": "08:02-09:46",
            "Durmuhurtam": "13:41-14:37",
            "Varjam": "09:21-10:47"
        },
        {
            "Thithi": "Trayodashi 25:45",
            "Nakshatram": "Purvashada 21:10",
            "Rahukalam": "16:40-18:24",
            "Durmuhurtam": "09:05-10:00",
            "Varjam": "08:20-09:46"
        },
        {
            "Thithi": "Chaturdashi 22:08",
            "Nakshatram": "Uttarashada 18:23",
            "Rahukalam": "13:13-14:56",
            "Durmuhurtam": "12:46-13:41",
            "Varjam": "21:55-23:20"
        },
        {
            "Thithi": "Purnima 18:35",
            "Nakshatram": "Shravana 15:37",
            "Rahukalam": "14:56-16:39",
            "Durmuhurtam": "16:25-17:20",
            "Varjam": "19:12-20:38"
        },
        {
            "Thithi": "Prathama 15:16",
            "Nakshatram": "Dhanishta 13:06",
            "Rahukalam": "11:30-13:13",
            "Durmuhurtam": "09:06-10:01",
            "Varjam": "19:39-21:07"
        },
        {
            "Thithi": "Dwitiya 12:23",
            "Nakshatram": "Satabhisha 10:58",
            "Rahukalam": "09:48-11:30",
            "Durmuhurtam": "06:23-08:12",
            "Varjam": "16:58-18:27"
        },
        {
            "Thithi": "Tritiya 10:05",
            "Nakshatram": "Purvabhadra 09:26",
            "Rahukalam": "18:19-20:01",
            "Durmuhurtam": "18:12-19:07",
            "Varjam": "18:42-20:15"
        },
        {
            "Thithi": "Chaturthi 08:31",
            "Nakshatram": "Uttarabhadra 08:37",
            "Rahukalam": "08:07-09:48",
            "Durmuhurtam": "13:40-14:34",
            "Varjam": "20:37-22:13"
        },
        {
            "Thithi": "Panchami 07:47",
            "Nakshatram": "Revathi 08:37",
            "Rahukalam": "16:36-18:17",
            "Durmuhurtam": "09:08-10:02",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 07:54",
            "Nakshatram": "Ashwini 09:27",
            "Rahukalam": "13:12-14:53",
            "Durmuhurtam": "12:45-13:39",
            "Varjam": "19:43-21:25"
        },
        {
            "Thithi": "Saptami 08:50",
            "Nakshatram": "Bharani 11:05",
            "Rahukalam": "14:53-16:34",
            "Durmuhurtam": "10:57-11:51, 16:21-17:14",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 10:29",
            "Nakshatram": "Krittika 13:23",
            "Rahukalam": "11:31-13:11",
            "Durmuhurtam": "09:09-10:03, 13:38-14:32",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 12:38",
            "Nakshatram": "Rohini 16:10",
            "Rahukalam": "09:50-11:31",
            "Durmuhurtam": "06:29-08:16",
            "Varjam": "07:14-09:01"
        },
        {
            "Thithi": "Dashami 15:05",
            "Nakshatram": "Mrigashira 19:11",
            "Rahukalam": "18:12-19:52",
            "Durmuhurtam": "18:05-18:59",
            "Varjam": "28:39-30:27"
        },
        {
            "Thithi": "Ekadashi 17:36",
            "Nakshatram": "Ardra 22:14",
            "Rahukalam": "08:11-09:51",
            "Durmuhurtam": "13:37-14:31, 16:18-17:11",
            "Varjam": ""
        },
        {
            "Thithi": "Dwadashi 20:00",
            "Nakshatram": "Punarvasu 25:09",
            "Rahukalam": "16:30-18:10",
            "Durmuhurtam": "09:11-10:04",
            "Varjam": "11:41-13:29"
        },
        {
            "Thithi": "Trayodashi 22:07",
            "Nakshatram": "Pushya 27:46",
            "Rahukalam": "13:10-14:50",
            "Durmuhurtam": "12:44-13:37",
            "Varjam": "10:01-11:48"
        },
        {
            "Thithi": "Chaturdashi 23:53",
            "Nakshatram": "Ashlesha 30:03",
            "Rahukalam": "14:49-16:28",
            "Durmuhurtam": "10:58-11:51",
            "Varjam": "17:47-19:32"
        },
        {
            "Thithi": "Amavasya 25:16",
            "Nakshatram": "Magha Full Night",
            "Rahukalam": "11:31-13:10",
            "Durmuhurtam": "09:12-10:05",
            "Varjam": "18:59-20:43"
        },
        {
            "Thithi": "Bhadrapada Shukla, Prathama 26:15",
            "Nakshatram": "Magha 07:56",
            "Rahukalam": "09:52-11:31",
            "Durmuhurtam": "06:35-08:20",
            "Varjam": "16:26-18:08"
        },
        {
            "Thithi": "Dwitiya 26:50",
            "Nakshatram": "Purvaphalguni 09:26",
            "Rahukalam": "18:04-19:43",
            "Durmuhurtam": "17:58-18:50",
            "Varjam": "16:59-18:39"
        },
        {
            "Thithi": "Tritiya 27:03",
            "Nakshatram": "Uttara 10:34",
            "Rahukalam": "08:14-09:53",
            "Durmuhurtam": "13:35-14:27",
            "Varjam": "19:14-20:53"
        },
        {
            "Thithi": "Chaturthi 26:52",
            "Nakshatram": "Hasta 11:20",
            "Rahukalam": "16:24-18:02",
            "Durmuhurtam": "09:14-10:06",
            "Varjam": "19:27-21:05"
        },
        {
            "Thithi": "Panchami 26:19",
            "Nakshatram": "Chitra 11:42",
            "Rahukalam": "13:08-14:46",
            "Durmuhurtam": "12:42-13:34",
            "Varjam": "17:18-18:54"
        }
    ],
    "panchangam_sep": [{
            "Thithi": "Shashti 25:21",
            "Nakshatram": "Swathi 11:42",
            "Rahukalam": "14:45-16:22",
            "Durmuhurtam": "10:58-11:50",
            "Varjam": "17:12-18:47"
        },
        {
            "Thithi": "Saptami 23:58",
            "Nakshatram": "Vishakha 11:17",
            "Rahukalam": "11:31-13:08",
            "Durmuhurtam": " 09:15-10:07",
            "Varjam": "15:09-16:42"
        },
        {
            "Thithi": "Ashtami 22:09",
            "Nakshatram": "Anuradha 10:27",
            "Rahukalam": "09:54-11:31",
            "Durmuhurtam": "06:41-08:24",
            "Varjam": "15:46-17:17"
        },
        {
            "Thithi": "Navami 19:57",
            "Nakshatram": "Jyeshta 09:13",
            "Rahukalam": "17:56-19:06",
            "Durmuhurtam": "17:50-18:41",
            "Varjam": "16:40-18:10"
        },
        {
            "Thithi": "Dashami 17:24",
            "Nakshatram": "Mula 07:36",
            "Rahukalam": "08:18-09:54",
            "Durmuhurtam": "13:32-14:23",
            "Varjam": "16:25-17:57"
        },
        {
            "Thithi": "Ekadashi 14:34",
            "Nakshatram": "Uttarashada 27:30",
            "Rahukalam": "16:18-17:54",
            "Durmuhurtam": "09:55-11:30",
            "Varjam": "12:56-14:24"
        },
        {
            "Thithi": "Dwadashi 11:34",
            "Nakshatram": "Shravana 25:16",
            "Rahukalam": "13:06-14:41",
            "Durmuhurtam": "12:40-13:31",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 08:32, Chaturdashi 29:37",
            "Nakshatram": "Dhanishta 23:05",
            "Rahukalam": "14:41-16:16",
            "Durmuhurtam": "10:59-11:49",
            "Varjam": "0"
        },
        {
            "Thithi": "Purnima 26:58",
            "Nakshatram": "Sathabhisha 21:07",
            "Rahukalam": "11:30-13:05",
            "Durmuhurtam": "09:17-10:08, 13:31-14:21",
            "Varjam": ""
        },
        {
            "Thithi": "Prathama 24:44",
            "Nakshatram": "Purvabhadra 19:32",
            "Rahukalam": "09:56-11:30",
            "Durmuhurtam": "06:46-08:27",
            "Varjam": "28:43-30:15"
        },
        {
            "Thithi": "Dwitiya 23:05",
            "Nakshatram": "Uttarabhadra 18:29",
            "Rahukalam": "17:48-19:22",
            "Durmuhurtam": "17:41-18:32",
            "Varjam": ""
        },
        {
            "Thithi": "Tritiya 22:07",
            "Nakshatram": "Revati 18:06",
            "Rahukalam": "08:22-09:56",
            "Durmuhurtam": "13:29-14:19, 16:00-16:50",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturthi 21:55",
            "Nakshatram": "Ashwini 18:28",
            "Rahukalam": "16:11-17:45",
            "Durmuhurtam": "09:19-10:09",
            "Varjam": "14:24-16:24"
        },
        {
            "Thithi": "Panchami 22:30",
            "Nakshatram": "Bharani 19:35",
            "Rahukalam": "13:03-14:37",
            "Durmuhurtam": "",
            "Varjam": ""
        },
        {
            "Thithi": "Shashti 23:49",
            "Nakshatram": "Krittika 21:26",
            "Rahukalam": "14:36-16:09",
            "Durmuhurtam": "10:59-11:49",
            "Varjam": "08:30-10:14"
        },
        {
            "Thithi": "Saptami 25:44",
            "Nakshatram": "Rohini 23:51",
            "Rahukalam": "11:30-13:03",
            "Durmuhurtam": "09:20-10:09",
            "Varjam": "15:03-16:48"
        },
        {
            "Thithi": "Ashtami 28:02",
            "Nakshatram": "Mrigashira 26:41",
            "Rahukalam": "09:57-11:30",
            "Durmuhurtam": "06:52-08:31",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 30:31",
            "Nakshatram": "Aardra 29:41",
            "Rahukalam": "17:39-19:11",
            "Durmuhurtam": "17:33-18:22",
            "Varjam": "12:08-13:56"
        },
        {
            "Thithi": "Dashami Full Night",
            "Nakshatram": "Punarvasu Full Night",
            "Rahukalam": "08:26-09:58",
            "Durmuhurtam": "13:26-14:15",
            "Varjam": "19:09-16:42"
        },
        {
            "Thithi": "Dashami 08:56",
            "Nakshatram": "Punarvasu 08:37",
            "Rahukalam": "16:05-17:36",
            "Durmuhurtam": "09:21-10:10",
            "Varjam": "17:30-19:17"
        },
        {
            "Thithi": "Ekadashi 11:04",
            "Nakshatram": "Pushya 11:17",
            "Rahukalam": "13:01-14:32",
            "Durmuhurtam": "12:37-13:25",
            "Varjam": "25:18-27:03"
        },
        {
            "Thithi": "Dwadashi 12:47",
            "Nakshatram": "Ashlesha 13:33",
            "Rahukalam": "14:32-16:03",
            "Durmuhurtam": "10:59-11:48, 15:51-16:39",
            "Varjam": ""
        },
        {
            "Thithi": "Trayodashi 14:00",
            "Nakshatram": "Magha 15:21",
            "Rahukalam": "11:29-13:00",
            "Durmuhurtam": "09:22-10:11, 13:24-14:13",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturdashi 14:42",
            "Nakshatram": "Purvaphalguni 16:38",
            "Rahukalam": "09:59-11:29",
            "Durmuhurtam": "06:58-08:34",
            "Varjam": "24:04-25:43"
        },
        {
            "Thithi": "Amavasya 14:53",
            "Nakshatram": "Uttara 17:25",
            "Rahukalam": "17:30-19:00",
            "Durmuhurtam": "17:24-18:12",
            "Varjam": "25:27-27:34"
        },
        {
            "Thithi": "Ashwija Shukla, Prathama 14:38",
            "Nakshatram": "Hasta 17:46",
            "Rahukalam": "08:30-09:59",
            "Durmuhurtam": "13:23-14:11, 15:47-16:35",
            "Varjam": ""
        },
        {
            "Thithi": "Dwitiya 13:58",
            "Nakshatram": "Chitra 17:44",
            "Rahukalam": "15:58-17:28",
            "Durmuhurtam": "09:24-10:12",
            "Varjam": "23:15-24:50"
        },
        {
            "Thithi": "Tritiya 12:57",
            "Nakshatram": "Swathi 17:22",
            "Rahukalam": "12:59-14:28",
            "Durmuhurtam": "12:35-13:22",
            "Varjam": "22:49-24:22"
        },
        {
            "Thithi": "Chaturthi 11:38",
            "Nakshatram": "Vishakha 16:43",
            "Rahukalam": "14:27-15:56",
            "Durmuhurtam": "11:00-11:47, 15:44-16:32",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 10:04",
            "Nakshatram": "Anuradha 15:49",
            "Rahukalam": "11:29-12:58",
            "Durmuhurtam": "09:25-10:12",
            "Varjam": "21:09-22:41"
        }
    ],
    "panchangam_oct": [{
            "Thithi": "Shashti 08:16",
            "Nakshatram": "Saptami 30:17",
            "Rahukalam": "10:01-11:29",
            "Durmuhurtam": "07:04-07:51",
            "Varjam": "22:15-23:46"
        },
        {
            "Thithi": "Ashtami 28:07",
            "Nakshatram": "Mula 13:23",
            "Rahukalam": "17:22-18:50",
            "Durmuhurtam": "17:16-18:03",
            "Varjam": "11:52-13:23"
        },
        {
            "Thithi": "Navami 25:50",
            "Nakshatram": "Purvashada 11:55",
            "Rahukalam": "08:33-10:01",
            "Durmuhurtam": "13:20-14:07",
            "Varjam": "19:24-20:53"
        },
        {
            "Thithi": "Dashami 23:30",
            "Nakshatram": "Uttarashada 10:21",
            "Rahukalam": "15:52-17:19",
            "Durmuhurtam": "09:27-10:13",
            "Varjam": "14:05-15:35"
        },
        {
            "Thithi": "Ekadashi 21:10",
            "Nakshatram": "Shravana 08:45",
            "Rahukalam": "12:56-14:24",
            "Durmuhurtam": "12:33-13:20",
            "Varjam": "12:30-13:59"
        },
        {
            "Thithi": "Dwadashi 18:56",
            "Nakshatram": "Dhanishta 07:12, Shatabhisha 29:47",
            "Rahukalam": "14:23-15:50",
            "Durmuhurtam": "11:00-11:46",
            "Varjam": "13:58-15:29"
        },
        {
            "Thithi": "Trayodashi 16:54",
            "Nakshatram": "Purvabhadra 28:38",
            "Rahukalam": "11:29-12:56",
            "Durmuhurtam": "09:28-10:14",
            "Varjam": "11:53-13:24"
        },
        {
            "Thithi": "Chaturdashi 15:11",
            "Nakshatram": "Uttarabhadra 27:51",
            "Rahukalam": "10:03-11:29",
            "Durmuhurtam": "07:10-08:42",
            "Varjam": "13:55-15:28"
        },
        {
            "Thithi": "Purnima 13:54",
            "Nakshatram": "Revathi 27:32",
            "Rahukalam": "17:13-18:39",
            "Durmuhurtam": "17:08-17:53",
            "Varjam": "15:41-17:16"
        },
        {
            "Thithi": "Prathama 13:08",
            "Nakshatram": "Ashwini 27:47",
            "Rahukalam": "08:38-10:03",
            "Durmuhurtam": "13:18-14:03, 15:35-16:21",
            "Varjam": ""
        },
        {
            "Thithi": "Dwitiya 12:59",
            "Nakshatram": "Bharani 28:40",
            "Rahukalam": "15:46-17:11",
            "Durmuhurtam": "09:29-10:15",
            "Varjam": "13:44-15:24"
        },
        {
            "Thithi": "Tritiya 13:29",
            "Nakshatram": "Krittika 30:11",
            "Rahukalam": "12:54-14:20",
            "Durmuhurtam": "12:32-13:17",
            "Varjam": "17:26-19:08"
        },
        {
            "Thithi": "Chaturthi 14:38",
            "Nakshatram": "Rohini Full Night",
            "Rahukalam": "14:19-15:44",
            "Durmuhurtam": "11:01-11:46, 15:33-16:18",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 16:22",
            "Nakshatram": "Rohini 08:17",
            "Rahukalam": "11:29-12:54",
            "Durmuhurtam": "09:31-10:16",
            "Varjam": "14:29-16:16"
        },
        {
            "Thithi": "Shashti 18:33",
            "Nakshatram": "Mrigashira 10:52",
            "Rahukalam": "10:05-11:29",
            "Durmuhurtam": "07:16-08:46",
            "Varjam": "20:16-22:04"
        },
        {
            "Thithi": "Saptami 20:59",
            "Nakshatram": "Aardra 13:45",
            "Rahukalam": "17:06-18:30",
            "Durmuhurtam": "17:00-17:45",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 23:27",
            "Nakshatram": "Punarvasu 16:43",
            "Rahukalam": "08:42-10:06",
            "Durmuhurtam": "13:16-14:00, 15:30-16:14",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 25:43",
            "Nakshatram": "Pushya 19:32",
            "Rahukalam": "15:40-17:03",
            "Durmuhurtam": "09:33-10:17",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 27:34",
            "Nakshatram": "Ashlesha 22:00",
            "Rahukalam": "12:53-14:16",
            "Durmuhurtam": "12:31-13:15",
            "Varjam": "09:39-11:25"
        },
        {
            "Thithi": "Ekadashi 28:52",
            "Nakshatram": "Magha 23:58",
            "Rahukalam": "14:16-15:38",
            "Durmuhurtam": "11:02-11:46",
            "Varjam": "10:59-12:43"
        },
        {
            "Thithi": "Dwadashi 29:32",
            "Nakshatram": "Purvaphalguni 25:20",
            "Rahukalam": "11:30-12:52",
            "Durmuhurtam": "09:34-10:18",
            "Varjam": "08:26-10:07"
        },
        {
            "Thithi": "Trayodashi 29:33",
            "Nakshatram": "Uttaraphalguni 26:04",
            "Rahukalam": "10:08-11:30",
            "Durmuhurtam": "07:23-08:51",
            "Varjam": "08:46-10:25"
        },
        {
            "Thithi": "Chaturdashi 28:57",
            "Nakshatram": "Hasta 26:12",
            "Rahukalam": "16:58-18:20",
            "Durmuhurtam": "16:53-17:37",
            "Varjam": "10:31-12:08"
        },
        {
            "Thithi": "Amavasya 27:48",
            "Nakshatram": "Chitra 25:47",
            "Rahukalam": "08:47-10:09",
            "Durmuhurtam": "13:14-13:57",
            "Varjam": "10:03-11:38"
        },
        {
            "Thithi": "Karthika Shukla, Prathama 26:12",
            "Nakshatram": "Swathi 24:54",
            "Rahukalam": "15:35-16:56",
            "Durmuhurtam": "09:36-10:20",
            "Varjam": ""
        },
        {
            "Thithi": "Dwitiya 24:15",
            "Nakshatram": "Vishakha 23:41",
            "Rahukalam": "12:52-14:13",
            "Durmuhurtam": "12:30-13:13",
            "Varjam": "27:26-28:56"
        },
        {
            "Thithi": "Tritiya 22:03",
            "Nakshatram": "Anuradha 22:12",
            "Rahukalam": "14:13-15:34",
            "Durmuhurtam": "11:04-11:47, 15:23-16:06",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturthi 19:43",
            "Nakshatram": "Jyeshta 20:36",
            "Rahukalam": "11:31-12:52",
            "Durmuhurtam": "09:38-10:21, 13:13-13:56",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 17:19",
            "Nakshatram": "Mula 18:56",
            "Rahukalam": "10:11-11:31",
            "Durmuhurtam": "07:30-08:56",
            "Varjam": "17:26-18:56"
        },
        {
            "Thithi": "Shashti 14:57",
            "Nakshatram": "Purvashada 17:18",
            "Rahukalam": "16:52-18:12",
            "Durmuhurtam": "16:47-17:29",
            "Varjam": "24:47-26:17"
        },
        {
            "Thithi": "Saptami 12:41",
            "Nakshatram": "Uttarashada 15:45",
            "Rahukalam": "08:52-10:12",
            "Durmuhurtam": "13:13-13:55",
            "Varjam": "19:32-21:02"
        }
    ],
    "panchangam_nov": [{
            "Thithi": "Ashtami 10:34",
            "Nakshatram": "Shravana 14:23",
            "Rahukalam": "15:31-16:50",
            "Durmuhurtam": "09:40-10:23",
            "Varjam": "18:11-19:43"
        },
        {
            "Thithi": "Navami 08:39, Dashami 31:00",
            "Nakshatram": "Dhanishta 13:13",
            "Rahukalam": "12:51-14:11",
            "Durmuhurtam": "12:30-13:13",
            "Varjam": "20:09-21:41"
        },
        {
            "Thithi": "Ekadashi 29:38",
            "Nakshatram": "Satabhisha 12:19",
            "Rahukalam": "14:11-15:30",
            "Durmuhurtam": "11:06-11:48",
            "Varjam": "18:33-20:06"
        },
        {
            "Thithi": "Dwadashi 28:36",
            "Nakshatram": "Purvabhadra 11:42",
            "Rahukalam": "11:33-12:51",
            "Durmuhurtam": "09:42-10:24",
            "Varjam": "21:12-22:47"
        },
        {
            "Thithi": "Trayodashi 26:58",
            "Nakshatram": "Uttarabhadra 11:26",
            "Rahukalam": "10:14-11:33",
            "Durmuhurtam": "07:37-09:01",
            "Varjam": "23:30-25:07"
        },
        {
            "Thithi": "Chaturdashi 26:45",
            "Nakshatram": "Revathi 10:34",
            "Rahukalam": "15:47-17:05",
            "Durmuhurtam": "15:41-16:23",
            "Varjam": "27:45-29:24"
        },
        {
            "Thithi": "Purnima 27:01",
            "Nakshatram": "Ashwini 11:07",
            "Rahukalam": "07:57-09:15",
            "Durmuhurtam": "12:12-12:54",
            "Varjam": "07:02-08:40"
        },
        {
            "Thithi": "Prathama 27:46",
            "Nakshatram": "Bharani 12:09",
            "Rahukalam": "14:27-15:45",
            "Durmuhurtam": "08:45-09:26",
            "Varjam": "24:54-26:36"
        },
        {
            "Thithi": "Dwitiya 29:02",
            "Nakshatram": "Krittika 13:39",
            "Rahukalam": "11:52-13:09",
            "Durmuhurtam": "11:31-12:12",
            "Varjam": ""
        },
        {
            "Thithi": "Tritiya Full Night",
            "Nakshatram": "Rohini 15:38",
            "Rahukalam": "13:09-14:27",
            "Durmuhurtam": "10:09-10:50",
            "Varjam": "06:58-08:42"
        },
        {
            "Thithi": "Tritiya 06:47",
            "Nakshatram": "Mrigashira 18:03",
            "Rahukalam": "10:35-11:52",
            "Durmuhurtam": "08:47-09:28, 12:12-12:54",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturthi 08:55",
            "Nakshatram": "Aardra 20:48",
            "Rahukalam": "09:18-10:35",
            "Durmuhurtam": "06:44-08:064",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 11:21",
            "Nakshatram": "Punarvasu 23:45",
            "Rahukalam": "15:42-16:59",
            "Durmuhurtam": "15:37-16:18",
            "Varjam": "10:17-12:04"
        },
        {
            "Thithi": "Shashti 13:53",
            "Nakshatram": "Pushya 26:43",
            "Rahukalam": "08:03-09:19",
            "Durmuhurtam": "12:13-12:54",
            "Varjam": "08:44-10:32"
        },
        {
            "Thithi": "Saptami 16:19",
            "Nakshatram": "Ashlesha 29:29",
            "Rahukalam": "14:25-15:41",
            "Durmuhurtam": "08:50-09:30",
            "Varjam": "16:59-18:46"
        },
        {
            "Thithi": "Ashtami 18:27",
            "Nakshatram": "Magha Full Night",
            "Rahukalam": "11:53-13:09",
            "Durmuhurtam": "11:32-12:13",
            "Varjam": "18:40-20:25"
        },
        {
            "Thithi": "Navami 20:03",
            "Nakshatram": "Magha 07:51",
            "Rahukalam": "13:09-14:25",
            "Durmuhurtam": "10:12-10:52",
            "Varjam": "16:27-18:10"
        },
        {
            "Thithi": "Dashami 20:59",
            "Nakshatram": "Purvaphalguni 09:38",
            "Rahukalam": "10:38-11:53",
            "Durmuhurtam": "08:52-09:32",
            "Varjam": "17:10-18:51"
        },
        {
            "Thithi": "Ekadashi 21:11",
            "Nakshatram": "Uttara 10:44",
            "Rahukalam": "09:23-10:38",
            "Durmuhurtam": "06:52-08:12",
            "Varjam": "19:16-20:53"
        },
        {
            "Thithi": "Dwadashi 20:37",
            "Nakshatram": "Hasta 11:06",
            "Rahukalam": "15:39-16:54",
            "Durmuhurtam": "15:34-16:14",
            "Varjam": "18:59-20:33"
        },
        {
            "Thithi": "Trayodashi 19:19",
            "Nakshatram": "Chitra 10:44",
            "Rahukalam": "08:09-09:24",
            "Durmuhurtam": "12:14-12:54",
            "Varjam": "16:06-17:37"
        },
        {
            "Thithi": "Chaturdashi 17:23",
            "Nakshatram": "Swathi 09:42",
            "Rahukalam": "14:24-15:39",
            "Durmuhurtam": "08:55-09:34",
            "Varjam": "14:56-16:26"
        },
        {
            "Thithi": "Amavasya 14:56",
            "Nakshatram": "Vishakha 08:07",
            "Rahukalam": "11:54-13:09",
            "Durmuhurtam": "11:34-12:14",
            "Varjam": "11:47-13:15"
        },
        {
            "Thithi": "Margashira Shukla, Prathama 12:07",
            "Nakshatram": "Jyeshta 27:51",
            "Rahukalam": "13:09-14:24",
            "Durmuhurtam": "10:15-10:55, 14:14-14:53",
            "Varjam": "11:11-12:38"
        },
        {
            "Thithi": "Dwitiya 09:05, Tritiya 29:58",
            "Nakshatram": "Mula 25:28",
            "Rahukalam": "10:41-11:55",
            "Durmuhurtam": "08:57-09:36",
            "Varjam": "11:04-12:30"
        },
        {
            "Thithi": "Chaturthi 26:55",
            "Nakshatram": "Purvashada 23:08",
            "Rahukalam": "09:27-10:41",
            "Durmuhurtam": "06:59-08:18",
            "Varjam": "10:08-11:35"
        },
        {
            "Thithi": "Panchami 24:05",
            "Nakshatram": "Uttarashada 20:59",
            "Rahukalam": "15:37-16:51",
            "Durmuhurtam": "15:32-16:12",
            "Varjam": "24:41-26:09"
        },
        {
            "Thithi": "Shashti 21:34",
            "Nakshatram": "Shravana 19:08",
            "Rahukalam": "08:15-09:28",
            "Durmuhurtam": "12:16-12:55, 14:14-14:53",
            "Varjam": ""
        },
        {
            "Thithi": "Saptami 19:28",
            "Nakshatram": "Dhanishta 17:41",
            "Rahukalam": "14:24-15:37",
            "Durmuhurtam": "09:00-09:39",
            "Varjam": "24:36-26:08"
        },
        {
            "Thithi": "Ashtami 17:51",
            "Nakshatram": "Sathabhisha 16:42",
            "Rahukalam": "11:57-13:10",
            "Durmuhurtam": "11:37-12:16",
            "Varjam": "22:59-24:33"
        }
    ],
    "panchangam_dec": [{
            "Thithi": "Navami 16:44",
            "Nakshatram": "Purvabhadra 16:14",
            "Rahukalam": "13:10-14:24",
            "Durmuhurtam": "10:19-10:58, 14:14-14:53",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 16:09",
            "Nakshatram": "Uttarabhadra 16:15",
            "Rahukalam": "10:44-11:57",
            "Durmuhurtam": "09:02-09:41, 12:17-12:56",
            "Varjam": ""
        },
        {
            "Thithi": "Ekadashi 16:04",
            "Nakshatram": "Revathi 16:46",
            "Rahukalam": "09:32-10:45",
            "Durmuhurtam": "Sunrise 07:06",
            "Varjam": "07:06-08:23"
        },
        {
            "Thithi": "Dwadashi 16:27",
            "Nakshatram": "Ashwini 17:45",
            "Rahukalam": "15:37-16:50",
            "Durmuhurtam": "15:32-16:11",
            "Varjam": "13:35-15:15"
        },
        {
            "Thithi": "Trayodashi 17:17",
            "Nakshatram": "Bharani 19:08",
            "Rahukalam": "08:20-09:33",
            "Durmuhurtam": "12:18-12:57, 14:15-14:53",
            "Varjam": ""
        },
        {
            "Thithi": "Chaturdashi 18:31",
            "Nakshatram": "Krittika 20:55",
            "Rahukalam": "14:25-15:37",
            "Durmuhurtam": "09:05-09:43",
            "Varjam": "08:02-09:45"
        },
        {
            "Thithi": "Purnima 20:07",
            "Nakshatram": "Rohini 23:03",
            "Rahukalam": "12:00-13:12",
            "Durmuhurtam": "11:40-12:19",
            "Varjam": "14:20-16:05"
        },
        {
            "Thithi": "Prathama 22:04",
            "Nakshatram": "Mrigashira 25:29",
            "Rahukalam": "13:12-14:25",
            "Durmuhurtam": "10:23-11:02, 14:15-14:54",
            "Varjam": ""
        },
        {
            "Thithi": "Dwitiya 24:17",
            "Nakshatram": "Aardra 28:12",
            "Rahukalam": "10:48-12:00",
            "Durmuhurtam": "09:07-09:45",
            "Varjam": "10:50-12:37"
        },
        {
            "Thithi": "Tritiya 26:44",
            "Nakshatram": "Punarvasu 31:06",
            "Rahukalam": "09:36-10:49",
            "Durmuhurtam": "07:11-08:29",
            "Varjam": "17:39-19:27"
        },
        {
            "Thithi": "Chaturthi 29:18",
            "Nakshatram": "Pushya Full Night",
            "Rahukalam": "15:38-16:50",
            "Durmuhurtam": "15:33-16:12",
            "Varjam": "16:06-17:54"
        },
        {
            "Thithi": "Panchami Full Night",
            "Nakshatram": "Pushya 10:06",
            "Rahukalam": "08:25-09:37",
            "Durmuhurtam": "12:21-13:00, 14:17-14:55",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 07:51",
            "Nakshatram": "Ashlesha 13:03",
            "Rahukalam": "14:27-15:39",
            "Durmuhurtam": "09:09-09:48",
            "Varjam": "26:24-28:11"
        },
        {
            "Thithi": "Shashti 10:12",
            "Nakshatram": "Magha 15:46",
            "Rahukalam": "12:03-13:15",
            "Durmuhurtam": "11:44-12:22",
            "Varjam": "24:32-26:18"
        },
        {
            "Thithi": "Saptami 12:09",
            "Nakshatram": "Purvaphalguni 18:05",
            "Rahukalam": "13:15-14:27",
            "Durmuhurtam": "10:27-11:06, 14:18-14:56",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 13:32",
            "Nakshatram": "Uttara 19:48",
            "Rahukalam": "10:52-12:04",
            "Durmuhurtam": "09:11-09:49, 12:23-13:01",
            "Varjam": ""
        },
        {
            "Thithi": "Navami 14:11",
            "Nakshatram": "Hasta 20:48",
            "Rahukalam": "09:40-10:52",
            "Durmuhurtam": "07:16-08:33",
            "Varjam": ""
        },
        {
            "Thithi": "Dashami 14:02",
            "Nakshatram": "Chitra 21:01",
            "Rahukalam": "15:41-16:52",
            "Durmuhurtam": "15:36-16:14",
            "Varjam": "26:28-28:02"
        },
        {
            "Thithi": "Ekadashi 13:02",
            "Nakshatram": "Swathi 20:25",
            "Rahukalam": "08:29-09:41",
            "Durmuhurtam": "12:24-13:03, 14:19-14:58",
            "Varjam": ""
        },
        {
            "Thithi": "Dwadashi 11:15",
            "Nakshatram": "Vishakha 19:03",
            "Rahukalam": "14:30-15:41",
            "Durmuhurtam": "09:13-09:51",
            "Varjam": "22:43-24:11"
        },
        {
            "Thithi": "Trayodashi 08:46, Chaturdashi 29:43",
            "Nakshatram": "Anuradha 17:03",
            "Rahukalam": "12:06-13:18",
            "Durmuhurtam": "11:47-12:25",
            "Varjam": "22:04-23:30"
        },
        {
            "Thithi": "Amavasya 26:16",
            "Nakshatram": "Jyeshta 14:33",
            "Rahukalam": "13:19-14:31",
            "Durmuhurtam": "10:31-11:09",
            "Varjam": "21:36-23:01"
        },
        {
            "Thithi": "Pausha Shukla, Prathama 22:36",
            "Nakshatram": "Mula 11:43",
            "Rahukalam": "10:55-12:07",
            "Durmuhurtam": "09:15-09:53, 12:26-13:05",
            "Varjam": "10:18-11:43"
        },
        {
            "Thithi": "Dwitiya 18:54",
            "Nakshatram": "Purvashada 08:45",
            "Rahukalam": "09:44-10:56",
            "Durmuhurtam": "07:20-08:37",
            "Varjam": "15:47-17:12"
        },
        {
            "Thithi": "Tritiya 15:21",
            "Nakshatram": "Shravana 27:12",
            "Rahukalam": "15:44-16:56",
            "Durmuhurtam": "15:39-16:18",
            "Varjam": "09:25-10:50"
        },
        {
            "Thithi": "Chaturthi 12:07",
            "Nakshatram": "Dhanishta 24:57",
            "Rahukalam": "08:33-09:45",
            "Durmuhurtam": "12:28-13:06, 14:23-15:01",
            "Varjam": ""
        },
        {
            "Thithi": "Panchami 09:22",
            "Nakshatram": "Shashti 31:14",
            "Rahukalam": "14:33-15:45",
            "Durmuhurtam": "09:16-09:55",
            "Varjam": "07:39-09:08"
        },
        {
            "Thithi": "Saptami 29:47",
            "Nakshatram": "Purvabhadra 22:14",
            "Rahukalam": "12:10-13:22",
            "Durmuhurtam": "11:50-12:29",
            "Varjam": ""
        },
        {
            "Thithi": "Ashtami 29:03",
            "Nakshatram": "Uttarabhadra 21:54",
            "Rahukalam": "13:22-14:34",
            "Durmuhurtam": "10:34-11:13",
            "Varjam": "07:42-09:17"
        },
        {
            "Thithi": "Navami 29:03",
            "Nakshatram": "Revathi 22:17",
            "Rahukalam": "10:59-12:11",
            "Durmuhurtam": "09:17-09:56",
            "Varjam": "10:06-11:43"
        },
        {
            "Thithi": "Dashami 29:41",
            "Nakshatram": "Ahwini 23:18",
            "Rahukalam": "09:47-10:59",
            "Durmuhurtam": "07:22-08:39",
            "Varjam": "19:08-20:48"
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
                if(r_date[2] != '2022'):
                   res_text = 'I can only give you 2022 details'
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
            res_text = '\nI give the Tithi,  Nakshatra and other details for the given date of the current year(2022).\n To request send a command as /tithi <mm-dd-yyyy> \n If no date is provided, it will use current date in PST zone.\n\n All the times mentioned are in PST'
        else:
            res_text = 'Invalid command entered, please use /help'
            
        bot.sendMessage(chat_id=chat_id,text=res_text)
    return f'ok'
