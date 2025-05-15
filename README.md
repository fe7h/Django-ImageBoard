# Django ImageBoard

Simple imageboard on Django with API on DRF.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fe7h/Django-ImageBoard.git
cd ImageBoard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Features

Users can:

- create threads with images

- post comments

- view the list of threads and posts

- all of the above, but using API

## Requirements

- Python 3.x

- Django

- Pillow (for image uploads)

- Django REST Framework
