# Small Library Project for PlateIQ

## Features

This project is composed of three main tables, **Author**, **Book** and **Stock**. And it's meant to be a mock up, meant to be done in ~2 or ~3 hours. When you run the website you can expect to be able to:

- See all books listed with the amount of books in stock
- You can search for books
- You can edit a book's title
- You can delete books and you can create them
- Book and Author lists have a *'load more'* option to demonstrate pagination on Django REST
- You can edit, delete and create authors as well
- There's an add on library called moment js that tells you the time since creation of an author's registry

## Pending Features

i.e features I couldn't fit in within the 3 hour-ish time frame.

- ISBN verification
- Stock update based on book lends
- Search with autocomplete
- Unit tests for the API (**feel bad about this one, got into jamming code too fast**)
- Modal for errors instead of console.log's

# How to Install

Once you have pulled the repo into the directory you are comfortable having the half-baked code in, you need to install the python dependencies.

```
pipenv install
```

Then install the node dependencies.

```
cd frontend
npm install
```

Once that's done you need to setup the databse, I used PostgreSQL (and you kinda needed for text search). So log into psql and create a database name **plateiq**.

The project takes the database configuration from your environment file, so if you use pipenv create a **.env** file and input your DB settings, the following are the default:

```
'RDS_DB_NAME', default='plateiq'
'RDS_USERNAME', default='dev')
'RDS_PASSWORD', default='developer'
'RDS_HOSTNAME', default='localhost'
'RDS_PORT', 5432
```

If you made it here you can migrate and add the example dataset:

```
python manage.py migrate
python manage.py loaddata dataset.json
```

Now, since this is a SPA you will need to run the frontend separately from the main server.

 1. Run the main server
  ```
  python manage.py runserver
  ```

 2. Run the frontend server
  ```
  cd frontend; npm run serve
  ```

Finally, got to [localhost](http://localhost:80000/)
