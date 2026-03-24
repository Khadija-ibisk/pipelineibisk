# pipelineibisk

Plateforme Python avancee de traitement de donnees multi-format.

## Objectif metier
Traiter des donnees de commandes provenant de sources multiples (CSV, JSON, XML, Excel)
vers un format canonique unique stocke dans PostgreSQL.

## Fonctionnalites principales
- Ingestion automatique : CSV, JSON, XML, Excel, ZIP
- Validation via Pydantic
- Normalisation vers schema canonique
- Stockage PostgreSQL
- Export Parquet partitionne par pays + CSV consolide
- API FastAPI avec 5 endpoints
- Pipeline concurrent (ThreadPoolExecutor)
- Logging complet fichier + console
- 23 tests pytest

## Architecture du projet
## Architecture du projet
```
pipelineibisk/
├── data/
│   ├── raw/                    <- fichiers d'entree
│   │   ├── orders.csv
│   │   ├── orders.xlsx
│   │   ├── sales.json
│   │   └── ventes.xml
│   └── exports/                <- exports generes (gitignore)
├── sql/
│   └── seed.sql                <- creation des tables PostgreSQL
├── src/
│   └── datapipeline/
│       ├── analytics/
│       │   └── reports.py      <- requetes analytiques SQL
│       ├── api/
│       │   └── main.py         <- API FastAPI
│       ├── ingestion/
│       │   ├── detector.py     <- detection automatique du format
│       │   ├── csv_loader.py
│       │   ├── excel_loader.py
│       │   ├── json_loader.py
│       │   ├── xml_loader.py
│       │   └── archive_loader.py
│       ├── storage/
│       │   ├── postgres.py     <- connexion et insertion PostgreSQL
│       │   └── parquet_writer.py <- export Parquet partitionne
│       ├── transform/
│       │   └── normalize.py    <- normalisation vers schema canonique
│       ├── validation/
│       │   ├── models.py       <- modeles Pydantic
│       │   └── validators.py   <- validation des donnees
│       ├── cli.py              <- pipeline principal concurrent
│       ├── config.py           <- configuration centrale
│       ├── logging_config.py   <- systeme de logs
│       └── exceptions.py      <- exceptions personnalisees
├── tests/
│   ├── test_api.py
│   ├── test_csv_loader.py
│   ├── test_json_loader.py
│   ├── test_reports.py
│   ├── test_transform.py
│   └── test_validation.py
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```sts/            <- 23 tests pytest
```

## Technologies utilisees
- Python 3.11+
- FastAPI + Uvicorn
- Pydantic v2
- psycopg2 + PostgreSQL 15 (Docker)
- pandas + pyarrow + openpyxl
- pytest + httpx
- Docker + Docker Compose
- concurrent.futures (ThreadPoolExecutor)

## Installation
```bash
git clone https://github.com/TON_PSEUDO/pipelineibisk
cd pipelineibisk
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuration
Le fichier `.env` contient les parametres de connexion PostgreSQL :
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pipelineibisk
DB_USER=postgres
DB_PASSWORD=postgres
```

## Lancement de la base de donnees
```bash
docker compose up -d
```

## Lancement du pipeline
```bash
python -m src.datapipeline.cli
```

## Export analytique
```bash
python -c "from src.datapipeline.storage.parquet_writer import export_to_parquet; export_to_parquet()"
```

## Lancement de l'API
```bash
uvicorn src.datapipeline.api.main:app --reload
```
Swagger disponible sur : http://localhost:8000/docs

## Endpoints API
- GET /health
- GET /metrics/revenue-by-country
- GET /metrics/revenue-by-product
- GET /metrics/top-customers
- GET /metrics/revenue-over-time

## Execution des tests
```bash
pytest tests/ -v
```
Resultat : 23 tests passes

## Jeux de donnees
- `data/raw/orders.csv` - commandes CSV (5 lignes dont 1 invalide)
- `data/raw/sales.json` - ventes JSON (3 lignes dont 1 invalide)
- `data/raw/ventes.xml` - ventes XML (2 lignes)
- `data/raw/orders.xlsx` - ventes Excel (3 lignes)

## Limites connues
- Tests d'integration necessitent PostgreSQL actif via Docker
- Pas de pagination sur les endpoints API
- Pas de mecanisme de retry sur erreurs DB