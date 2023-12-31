# DOG ADOPTION CLI APP (PHASE-3-FINAL-PROJECT)

The dog adoption app is a command-line interface application designed to simplify the dog adoption
process for anyone willing to have one.

### Problem Statement:

Stray dogs, that continue to live on streets, even if they are sterilized, will still bite, chase people and vehicles, get into accidents, suffer from hunger and disease, and remain in conflict with people. Therefore, the dog adoption app enables people with or without dogs to adopt them and minimize the effect.

## APlications Models:

**Facility**

- Stores all `facilities` that keep dogs for adoption

**Adopters**

- This model keeps records of all `users` who adopt dogs in different facilities.

**Dogs**

- This model keeps all records of stray `dogs`

## Application Key Features

**Managing Facilities**

- Viewing all facilities in the system
- View facility details
- Creating a new facility in the system
- Updating facility details
- Removing facilities from the system
- List all dogs in the facility
- List all users(adopters) under that facility

**Managing Adopters**

- Viewing all adopters in the system
- Registering a new user(adopter) in the system
- Updating adopters details
- List all adopter dogs
- List facilities associated with adopters

**Managing Dogs**

- Viewing all dogs in the system
- Registering a new stray dog in the system
- Updating dogs details
- Removing dogs from the system

## Technologies Used

The following have been used on this project:

- [Python3](https://docs.python.org/3.10/)
- [Pytest](https://docs.pytest.org/en/latest/contents.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Faker](https://faker.readthedocs.io/en/master/)

## Project Setup

- Clone the repository: `git clone <repository-url>`
- Navigate to cloned repository: `cd phase-3-final-project`
- Create pipenv environment and Install dependencies: `pipenv install`
- Activate environment: ` pipenv install`
- Run test using pytest: `pytest`

## Create database migrations

- create db from migrations with alembic: `cd app/db && alembic updgrade heads`
- populate db with `seed.py`: `python3 seed.py`

## Testing manually with debug file (ipdb)

- Navigate to `app/db` directory: ` cd app/db`
- Run `seed.py` file to populate db with fake data: ` python3 seed.py`
- Run `debug.py` file to get ipdb terminal: ` python3 debug.py`

## How to run App

After cloning project and seeding data:

- Navigate to `phase-3-final-project/app`
- Run application: `python3 main.py`

## Authors

- [John Maluki](https://github.com/john-maluki)

## Copyright

Released under the MIT License. See the [LICENSE](https://github.com/john-maluki/phase-3-final-project/blob/main/LICENSE) file.
