# File Tree: pipelineibisk

**Generated:** 3/24/2026, 8:33:49 PM
**Root Path:** `c:\Users\DELL\Desktop\pipelineibisk`

```
├── 📁 .pytest_cache
│   ├── 📁 v
│   ├── ⚙️ .gitignore
│   ├── 📄 CACHEDIR.TAG
│   └── 📝 README.md
├── 📁 data
│   └── 📁 raw
│       ├── 📄 orders.csv
│       ├── 📄 orders.xlsx
│       ├── ⚙️ sales.json
│       └── ⚙️ ventes.xml
├── 📁 sql
│   └── 📄 seed.sql
├── 📁 src
│   └── 📁 datapipeline
│       ├── 📁 analytics
│       │   ├── 🐍 __init__.py
│       │   └── 🐍 reports.py
│       ├── 📁 api
│       │   ├── 🐍 __init__.py
│       │   └── 🐍 main.py
│       ├── 📁 ingestion
│       │   ├── 🐍 __init__.py
│       │   ├── 🐍 archive_loader.py
│       │   ├── 🐍 csv_loader.py
│       │   ├── 🐍 detector.py
│       │   ├── 🐍 excel_loader.py
│       │   ├── 🐍 json_loader.py
│       │   └── 🐍 xml_loader.py
│       ├── 📁 storage
│       │   ├── 🐍 __init__.py
│       │   ├── 🐍 parquet_writer.py
│       │   └── 🐍 postgres.py
│       ├── 📁 transform
│       │   ├── 🐍 __init__.py
│       │   └── 🐍 normalize.py
│       ├── 📁 validation
│       │   ├── 🐍 __init__.py
│       │   ├── 🐍 models.py
│       │   └── 🐍 validators.py
│       ├── 🐍 __init__.py
│       ├── 🐍 cli.py
│       ├── 🐍 config.py
│       ├── 🐍 exceptions.py
│       └── 🐍 logging_config.py
├── 📁 tests
│   ├── 🐍 __init__.py
│   ├── 🐍 test_api.py
│   ├── 🐍 test_csv_loader.py
│   ├── 🐍 test_json_loader.py
│   ├── 🐍 test_reports.py
│   ├── 🐍 test_transform.py
│   └── 🐍 test_validation.py
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 📝 README.md
├── ⚙️ docker-compose.yml
├── 🐍 generate_excel.py
└── 📄 requirements.txt
```

---
