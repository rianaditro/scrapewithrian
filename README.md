scrapewithrian/
├── api/
│   └── backend/
│       ├── __init__.py
│       ├── main.py
│       ├── db/
│       │   └── scrapewithrian.db
│       ├── routers/
│       │   ├── __init__.py
│       │   └── home.py
│       └── models/
│           └── __init__.py
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── public/
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       └── pages/
│           └── Home.jsx
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt


Create a folder structure like above
api/backend --> for routing on vercel
api/routers --> all endpoints
api/main --> main app

log_conf.yaml for logging with timestamp (TODO: no color in log levels)
Makefile for shorter execution from terminal:
    instead: uv run uvicorn api.backend.main:app --reload --log-config log_conf.yaml
    just: make dev
check if success

## preparing database
create mockup data from mockaroo in sql format, make sure to include CREATE TABLE and table name is match with sqlmodel object name
convert to db file using:
    sqlite3 scrapewithrian.db < data.sql
create the sqlmodel object to representing your table object in api/models/products.py
create connection with db file and yield session (so it closed after use)
create a temporary session for each request to interact with database (read), the session is temporary as long as the requests being processed and destroyed after it return the necassary value in deps.py

## pagination
add new routers for product pagination
query database based on offset and limit
check the total count of database by reading from app state instead of send new query every requests (initiate on app generation)
add handling if page requested is out of range

# frontend prep
install node.js 22, update the path and validate
create the frontend folder
    npm create vite@latest frontend --template react
choose react - javascript
cd folder, npm install, npm run dev
add allowed host (optional)
install dependencies
npm install react-router-dom axios tailwindcss
npx tailwindcss init -p

## add product page
create a product page that display all data by mapping the data
create product api handler using axios to comunicate with backend
update App.jsx to include link to product

