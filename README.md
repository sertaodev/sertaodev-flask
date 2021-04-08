![Alt Text](https://cdn.discordapp.com/attachments/340263600142942209/829135878420299776/bg_white.png)

## Criando api usando flaska

Notion [link](https://www.notion.so/Flask-26f75ac67a69497eaf24f9d29a2797dc)

Run project

Install dependencies from poetry

```sh
poetry install
```

- Windowns (cmd)

```sh
set FLASK_APP=src\app.py

set FLASK_ENV=development
```

Run database

```sh
flask db upgrade
```

Run app

```sh
flask run
```

Routes

```sh
/ -> Hello word
/prod -> List products
/prod/add -> Add products
/prod/delete/<gtin> -> Remove products
/prod/update/<gtin> -> Update products
```
