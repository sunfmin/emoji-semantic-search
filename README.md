# Emoji Semantic Search

This version uses https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 to generate vectors, and for search

## Local test

Build embedding index:
```bash
python server/data/build.py
```

Start backend:
```bash
python server/app.py
```

Start frontend
```bash
cd client
npm install  # Run once
REACT_APP_SERVER_ADDRESS="http://localhost:8012" npm start
```

Changes to 8012 because seems default 5000 port is used by System AirPlay or something.
