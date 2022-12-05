# FastAPI-TDD-Docker

### Overview

An example of dockerized fastapi application developed using test-driven technology
This application will follow RESTful design principles, comprise docker configuration, use Tortoise ORM interacting with Postgres
Pytest will be used fod test-driven development
Application will be configured for deployment on Heroku

<hr>

### The application routes:

| Endpoint       | Method | CRUD Operation | Result                          |
| -------------- | ------ | -------------- | ------------------------------- |
| /summaries     | GET    | READ           | Retrieve all summaries          |
| /summaries/:id | GET    | READ           | Retrieve a single summary by id |
| /summaries     | POST   | CREATE         | Create a summary                |
| /summaries/:id | PUT    | UPDATE         | Update a summary by id          |
| /summaries:id  | DELETE | DELETE         | Delete a summary by id          |

<hr>

### Useful links

[FastAPI](https://fastapi.tiangolo.com)

[Pytest](https://docs.pytest.org/en/7.2.x)

[Docker](https://www.docker.com)

[Tortoise](https://tortoise.github.io)

[Postgres](https://www.postgresql.org)

[Heroku](https://devcenter.heroku.com)
