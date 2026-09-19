# dl_book: Deep Learning book structure viewer

A small Flask web app that renders the full table of contents of the textbook
*Deep Learning* (Goodfellow, Bengio, Courville, MIT Press, 2016) as one
readable page. It is meant as a study aid: it shows the whole book at a glance
(parts, chapters, sections and subsections), which helps when planning what to
read and seeing how the topics connect.

The book itself is free to read at <https://www.deeplearningbook.org/>. This
repository contains **only the outline** (titles and numbering), none of the
book's text.

## Features

- Book metadata at the top (title, authors, year, publisher, link to the free online edition).
- Front matter and back matter listed separately.
- 20 chapters grouped into 4 parts: an introduction, *Applied Math and ML
  Basics*, *Modern Practical Deep Networks* and *Deep Learning Research*.
- Each chapter is a collapsible `<details>` block, open by default. Sections are
  numbered (e.g. `8.5`), and subsections (e.g. `8.5.3 Adam`) are nested lists.
- A single page with inline CSS. No JavaScript, no database, no external assets.

## How it works

```
app.py                  BOOK dict (all book data) + one route "/"
templates/index.html    Jinja2 template that loops parts -> chapters -> sections -> subsections
```

- The whole outline is hard-coded in `app.py` as one Python dictionary, `BOOK`.
  Each chapter holds a list of `(number, title, [subsections])` tuples.
- `GET /` calls `render_template("index.html", book=BOOK)`. The template walks
  the nested structure with Jinja2 `for` loops.
- There is no state, no user input and no other route.

## Tech stack

- Python 3.11, Flask 3.0 (Jinja2 templating)
- Gunicorn 22 as the production WSGI server
- Docker (`python:3.11-slim` base image)

## Run it

All commands run from `dl_book_structure/`.

**Locally with the Flask dev server** (port 5050 by default, or `PORT` if set):

```bash
cd dl_book_structure
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5050/
```

**With Docker** (Gunicorn listens on `$PORT`, 10000 by default):

```bash
cd dl_book_structure
docker build -t dl-book .
docker run --rm -p 10000:10000 dl-book
# open http://127.0.0.1:10000/
```

The `PORT` variable and the `0.0.0.0` bind make the image ready for PaaS hosts
that set the port themselves, such as Render.

## Project layout

```
dl_book/
├── README.md
└── dl_book_structure/
    ├── app.py              Flask app + BOOK data
    ├── requirements.txt    flask, gunicorn
    ├── Dockerfile
    ├── .dockerignore
    └── templates/
        └── index.html      page template + inline CSS
```

## Limitations and status

- This is a small, finished personal tool. It is not an ongoing project.
- The outline is static data typed into `app.py`. To change it you edit the
  code; there is no import from a file or database.
- It has no search, no progress tracking and no links to individual chapters.
- `python app.py` starts Flask with `debug=True`. Use this only for local
  development. The Docker image runs Gunicorn instead.
- There are no automated tests.
