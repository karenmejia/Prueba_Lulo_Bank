from enum import Enum
import os

class Constants(Enum):
    year = 2024
    month = 1
    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
    table_name = "January_series"
    fields_insert = (
    "id"
    ,"url"
    ,"name"
    ,"season"
    ,"number"
    ,"type"
    ,"airdate"
    ,"airtime"
    ,"airstamp"
    ,"runtime"
    ,"image"
    ,"summary"
    ,"rating_average"
    ,"_links_self_href"
    ,"_links_show_href"
    ,"_links_show_name"
    ,"_embedded_show_id"
    ,"_embedded_show_url"
    ,"_embedded_show_name"
    ,"_embedded_show_type"
    ,"_embedded_show_language"
    ,"_embedded_show_genres"
    ,"_embedded_show_status"
    ,"_embedded_show_runtime"
    ,"_embedded_show_averageRuntime"
    ,"_embedded_show_premiered"
    ,"_embedded_show_ended"
    ,"_embedded_show_officialSite"
    ,"_embedded_show_schedule_time"
    ,"_embedded_show_schedule_days"
    ,"_embedded_show_rating_average"
    ,"_embedded_show_weight"
    ,"_embedded_show_network"
    ,"_embedded_show_webChannel_id"
    ,"_embedded_show_webChannel_name"
    ,"_embedded_show_webChannel_country_name"
    ,"_embedded_show_webChannel_country_code"
    ,"_embedded_show_webChannel_country_timezone"
    ,"_embedded_show_webChannel_officialSite"
    ,"_embedded_show_dvdCountry"
    ,"_embedded_show_externals_tvrage"
    ,"_embedded_show_externals_thetvdb"
    ,"_embedded_show_externals_imdb"
    ,"_embedded_show_image_medium"
    ,"_embedded_show_image_original"
    ,"_embedded_show_summary"
    ,"_embedded_show_updated"
    ,"_embedded_show_links_self_href"
    ,"_embedded_show_links_previousepisode_href"
    ,"_embedded_show_links_previousepisode_name"
    ,"_embedded_show_image"
    ,"_embedded_show_links_nextepisode_href"
    ,"_embedded_show_links_nextepisode_name"
    ,"image_medium"
    ,"image_original"
    ,"_embedded_show_network_id"
    ,"_embedded_show_network_name"
    ,"_embedded_show_network_country_name"
    ,"_embedded_show_network_country_code"
    ,"_embedded_show_network_country_timezone"
    ,"_embedded_show_network_officialSite"
    ,"_embedded_show_webChannel"
    ,"_embedded_show_webChannel_country"
    ,"_embedded_show_dvdCountry_name"
    ,"_embedded_show_dvdCountry_code"
    ,"_embedded_show_dvdCountry_timezone")
    fields = """
    id TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    name TEXT NOT NULL,
    season TEXT NOT NULL,
    number TEXT,
    type TEXT NOT NULL,
    airdate TEXT NOT NULL,
    airtime TEXT NOT NULL,
    airstamp TEXT NOT NULL,
    runtime TEXT,
    image TEXT,
    summary TEXT,
    rating_average TEXT,
    _links_self_href TEXT NOT NULL,
    _links_show_href TEXT NOT NULL,
    _links_show_name TEXT NOT NULL,
    _embedded_show_id TEXT NOT NULL,
    _embedded_show_url TEXT NOT NULL,
    _embedded_show_name TEXT NOT NULL,
    _embedded_show_type TEXT NOT NULL,
    _embedded_show_language TEXT,
    _embedded_show_genres TEXT NOT NULL,
    _embedded_show_status TEXT NOT NULL,
    _embedded_show_runtime TEXT,
    _embedded_show_averageRuntime TEXT,
    _embedded_show_premiered TEXT NOT NULL,
    _embedded_show_ended TEXT,
    _embedded_show_officialSite TEXT,
    _embedded_show_schedule_time TEXT NOT NULL,
    _embedded_show_schedule_days TEXT NOT NULL,
    _embedded_show_rating_average TEXT,
    _embedded_show_weight TEXT NOT NULL,
    _embedded_show_network TEXT,
    _embedded_show_webChannel_id TEXT,
    _embedded_show_webChannel_name TEXT,
    _embedded_show_webChannel_country_name TEXT,
    _embedded_show_webChannel_country_code TEXT,
    _embedded_show_webChannel_country_timezone TEXT,
    _embedded_show_webChannel_officialSite TEXT,
    _embedded_show_dvdCountry TEXT,
    _embedded_show_externals_tvrage TEXT,
    _embedded_show_externals_thetvdb TEXT,
    _embedded_show_externals_imdb TEXT,
    _embedded_show_image_medium TEXT,
    _embedded_show_image_original TEXT,
    _embedded_show_summary TEXT,
    _embedded_show_updated TEXT NOT NULL,
    _embedded_show_links_self_href TEXT NOT NULL,
    _embedded_show_links_previousepisode_href TEXT NOT NULL,
    _embedded_show_links_previousepisode_name TEXT NOT NULL,
    _embedded_show_image TEXT,
    _embedded_show_links_nextepisode_href TEXT,
    _embedded_show_links_nextepisode_name TEXT,
    image_medium TEXT,
    image_original TEXT,
    _embedded_show_network_id TEXT,
    _embedded_show_network_name TEXT,
    _embedded_show_network_country_name TEXT,
    _embedded_show_network_country_code TEXT,
    _embedded_show_network_country_timezone TEXT,
    _embedded_show_network_officialSite TEXT,
    _embedded_show_webChannel TEXT,
    _embedded_show_webChannel_country TEXT,
    _embedded_show_dvdCountry_name TEXT,
    _embedded_show_dvdCountry_code TEXT,
    _embedded_show_dvdCountry_timezone TEXT
 """

    