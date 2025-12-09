# Student_Hub
A simple CRUD application using Postgres, FastAPI, SQLAlchemy, and React.js

The first step from this application work is to set up Postgres. After that, I modeled the ER to guide me through the configuration of the database, as shown in the image below

<img width="948" height="641" alt="image" src="https://github.com/user-attachments/assets/ddbd365f-4f59-4445-9ceb-d143e41e80b8" />

After that, the database was configured with simple parameters, since the goal is to achieve an MVP. As shown in the huge code image below.

<img width="767" height="828" alt="image" src="https://github.com/user-attachments/assets/38448cb8-5639-4166-9bfd-0f30b46ae5e3" />

FastAPI and SQLAlchemy were installed in a venv and run with uvicorn to update synchronously with the changes made in the source code

The next steps are to configure the models with SQLAlchemy and then configure the roots
