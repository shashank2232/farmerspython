--
-- PostgreSQL database dump
--

-- Dumped from database version 13.16 (Debian 13.16-1.pgdg120+1)
-- Dumped by pg_dump version 13.16 (Debian 13.16-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO shashank;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.countries (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.countries OWNER TO shashank;

--
-- Name: countries_id_seq; Type: SEQUENCE; Schema: public; Owner: shashank
--

CREATE SEQUENCE public.countries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.countries_id_seq OWNER TO shashank;

--
-- Name: countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shashank
--

ALTER SEQUENCE public.countries_id_seq OWNED BY public.countries.id;


--
-- Name: farmers; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.farmers (
    id integer NOT NULL,
    phone_number character varying NOT NULL,
    name character varying NOT NULL,
    language character varying,
    country_id integer
);


ALTER TABLE public.farmers OWNER TO shashank;

--
-- Name: farmers_id_seq; Type: SEQUENCE; Schema: public; Owner: shashank
--

CREATE SEQUENCE public.farmers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.farmers_id_seq OWNER TO shashank;

--
-- Name: farmers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shashank
--

ALTER SEQUENCE public.farmers_id_seq OWNED BY public.farmers.id;


--
-- Name: farms; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.farms (
    id integer NOT NULL,
    area character varying NOT NULL,
    village character varying NOT NULL,
    crop_grown character varying NOT NULL,
    sowing_date date NOT NULL,
    farmer_id integer,
    country_id integer
);


ALTER TABLE public.farms OWNER TO shashank;

--
-- Name: farms_id_seq; Type: SEQUENCE; Schema: public; Owner: shashank
--

CREATE SEQUENCE public.farms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.farms_id_seq OWNER TO shashank;

--
-- Name: farms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shashank
--

ALTER SEQUENCE public.farms_id_seq OWNED BY public.farms.id;


--
-- Name: schedules; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.schedules (
    id integer NOT NULL,
    days_after_sowing integer NOT NULL,
    fertiliser character varying NOT NULL,
    quantity integer NOT NULL,
    quantity_unit character varying NOT NULL,
    price_per_unit double precision NOT NULL,
    farm_id integer
);


ALTER TABLE public.schedules OWNER TO shashank;

--
-- Name: schedules_id_seq; Type: SEQUENCE; Schema: public; Owner: shashank
--

CREATE SEQUENCE public.schedules_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedules_id_seq OWNER TO shashank;

--
-- Name: schedules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shashank
--

ALTER SEQUENCE public.schedules_id_seq OWNED BY public.schedules.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: shashank
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(80) NOT NULL,
    password_hash character varying NOT NULL,
    roles character varying[] NOT NULL
);


ALTER TABLE public.users OWNER TO shashank;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: shashank
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO shashank;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shashank
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: countries id; Type: DEFAULT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.countries ALTER COLUMN id SET DEFAULT nextval('public.countries_id_seq'::regclass);


--
-- Name: farmers id; Type: DEFAULT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farmers ALTER COLUMN id SET DEFAULT nextval('public.farmers_id_seq'::regclass);


--
-- Name: farms id; Type: DEFAULT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farms ALTER COLUMN id SET DEFAULT nextval('public.farms_id_seq'::regclass);


--
-- Name: schedules id; Type: DEFAULT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.schedules ALTER COLUMN id SET DEFAULT nextval('public.schedules_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.alembic_version (version_num) FROM stdin;
04ebfd4d77b8
\.


--
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.countries (id, name) FROM stdin;
1	India
2	France
3	USA
4	USSR
5	SriLanka
6	Chile
\.


--
-- Data for Name: farmers; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.farmers (id, phone_number, name, language, country_id) FROM stdin;
1	9991110001	Farmer One	Hindi	1
3	9991110003	Farmer Three	English	3
4	9991110004	Farmer Four	Russian	4
5	9991110005	Farmer Five	Sinhala	5
6	9991110006	Farmer Six	Spanish	6
7	9991110007	Farmer Seven	Hindi	1
8	9991110008	Farmer Eight	French	2
9	9991110009	Farmer Nine	English	3
10	9991110010	Farmer Ten	Russian	4
11	9991110011	Farmer Eleven	Sinhala	5
12	9991110012	Farmer Twelve	Spanish	6
13	9991110013	Farmer Thirteen	Hindi	1
14	9991110014	Farmer Fourteen	French	2
15	9991110015	Farmer Fifteen	English	3
\.


--
-- Data for Name: farms; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.farms (id, area, village, crop_grown, sowing_date, farmer_id, country_id) FROM stdin;
1	5 hectares	Village A	Wheat	2024-01-15	1	1
3	8 hectares	Village C	Corn	2024-03-20	3	3
4	12 hectares	Village D	Soybean	2024-04-25	4	4
5	15 hectares	Village E	Barley	2024-05-30	5	5
6	20 hectares	Village F	Sugarcane	2024-06-10	6	6
7	25 hectares	Village G	Potato	2024-07-15	7	1
8	18 hectares	Village H	Cotton	2024-08-20	8	2
9	30 hectares	Village I	Tomato	2024-09-25	9	3
10	22 hectares	Village J	Peanut	2024-10-30	10	4
\.


--
-- Data for Name: schedules; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.schedules (id, days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id) FROM stdin;
1	30	Urea	50	kg	15.75	1
3	60	NPK	55	kg	18.5	3
4	75	Potash	40	kg	22	4
5	90	Calcium	65	kg	25	5
6	30	Urea	70	kg	16	6
7	60	DAP	45	kg	21	7
9	120	Potash	60	kg	23	9
10	150	Calcium	75	kg	26	10
8	1	NPK	50	kg	19	8
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: shashank
--

COPY public.users (id, username, password_hash, roles) FROM stdin;
1	superuser	$2b$12$RDRTsqfo7A/sYy/u4qedmu1Zgib3jAV7bHg9KRPAorhG9V5UDdZGa	{superuser}
2	venkat	$2b$12$C0inPxAwq5TIert3I0RRFOtDkyPSUC5kZ5.iBoEm4WJWnHKTCCxwS	{viewer,admin}
3	venkatesh	$2b$12$TZ4QRdL0wrtwYJOYWQGo7ePDLAJLHU/oxAKkktFXXqO9QmPXh7J2i	{viewer}
\.


--
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shashank
--

SELECT pg_catalog.setval('public.countries_id_seq', 6, true);


--
-- Name: farmers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shashank
--

SELECT pg_catalog.setval('public.farmers_id_seq', 15, true);


--
-- Name: farms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shashank
--

SELECT pg_catalog.setval('public.farms_id_seq', 10, true);


--
-- Name: schedules_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shashank
--

SELECT pg_catalog.setval('public.schedules_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shashank
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: countries countries_name_key; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_name_key UNIQUE (name);


--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (id);


--
-- Name: farmers farmers_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farmers
    ADD CONSTRAINT farmers_phone_number_key UNIQUE (phone_number);


--
-- Name: farmers farmers_pkey; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farmers
    ADD CONSTRAINT farmers_pkey PRIMARY KEY (id);


--
-- Name: farms farms_pkey; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farms
    ADD CONSTRAINT farms_pkey PRIMARY KEY (id);


--
-- Name: schedules schedules_pkey; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: farmers farmers_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farmers
    ADD CONSTRAINT farmers_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: farms farms_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farms
    ADD CONSTRAINT farms_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: farms farms_farmer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.farms
    ADD CONSTRAINT farms_farmer_id_fkey FOREIGN KEY (farmer_id) REFERENCES public.farmers(id);


--
-- Name: schedules schedules_farm_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shashank
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_farm_id_fkey FOREIGN KEY (farm_id) REFERENCES public.farms(id);


--
-- PostgreSQL database dump complete
--
