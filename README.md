# PW_lab2026 - Product Management Web Application

Applicazione web per la gestione di prodotti costruita con **FastAPI**, realizzata come laboratorio di programmazione web.

## Descrizione

Questa applicazione fornisce un'interfaccia web per visualizzare e gestire un catalogo di prodotti. Utilizza FastAPI come framework backend con template HTML renderizzati tramite Jinja2 e validazione dei dati con Pydantic.

## Tecnologie

- **FastAPI** - Framework web moderno e performante per Python
- **Jinja2** - Motore di template per il rendering HTML
- **Pydantic** - Validazione e serializzazione dei dati
- **CSS** - Styling dell'interfaccia

## Requisiti

- Python 3.7+
- Dipendenze indicate in `requirements.txt`

## Installazione

1. **Clonare il repository:**
   ```bash
   git clone <repository-url>
   cd PW_lab2026
   ```

2. **Creare un ambiente virtuale (opzionale ma consigliato):**
   
   **Con conda:**
   ```bash
   conda create --name pw_lab python=3.10
   conda activate pw_lab
   ```

   **Con venv:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # su macOS/Linux
   # oppure
   venv\Scripts\activate  # su Windows
   ```

3. **Installare le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

### Avviare il server di sviluppo:

```bash
fastapi dev main.py
```
*(In alternativa è possibile continuare a usare `uvicorn main:app --reload`)*

L'applicazione sarà disponibile su `http://localhost:8000`

### Accedere all'API interattiva:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Struttura del Progetto

```
PW_lab2026/
├── main.py                 # Applicazione principale FastAPI
├── typing_esempio.py       # Esempio di type hints in Python
├── requirements.txt        # Dipendenze del progetto
├── static/                 # File statici (CSS, JS)
│   └── styles.css         # Foglio di stile
├── templates/             # Template HTML Jinja2
│   ├── base.html          # Template base
│   ├── home.html          # Pagina home
│   ├── products.html      # Elenco prodotti
│   ├── product_form.html  # Form per aggiungere prodotto
│   └── success.html       # Pagina di successo
└── README.md              # Questo file
```

## API Endpoints

| Metodo | Endpoint | Descrizione |
|--------|----------|-------------|
| `GET` | `/` | Pagina home |
| `GET` | `/products` | Elenco di tutti i prodotti |
| `GET` | `/product_form` | Form per aggiungere un nuovo prodotto |
| `POST` | `/insert_product` | Inserire un prodotto tramite form HTML |
| `POST` | `/insert_product_json` | Inserire un prodotto tramite JSON |

## Modello Dati

### Product
```python
{
    "name": "string",      # Lunghezza: 3-30 caratteri
    "price": "float",      # Valore > 0
    "location": "string"   # Lunghezza: 3-30 caratteri
}
```

## Funzionalità

- ✅ Visualizzazione catalogo prodotti
- ✅ Aggiunta di nuovi prodotti tramite interfaccia web
- ✅ Validazione dati con Pydantic
- ✅ API REST con documentazione interattiva
- ✅ Template HTML responsive con Jinja2
- ✅ Styling CSS personalizzato

## Note per lo Sviluppo

- I prodotti vengono mantenuti in memoria durante l'esecuzione dell'applicazione
- Per una soluzione di produzione, integrarsi con un database (PostgreSQL, MongoDB, ecc.)
- La modalità `--reload` ricarica automaticamente il server al salvataggio dei file

## Autore

Laboratorio di Programmazione Web - 2026
