Links:
- https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
- https://pydantic.dev/docs/validation/latest/concepts/pydantic_settings/
- https://alembic.sqlalchemy.org/en/latest/cookbook.html

### alembic install
poetry add alembic
alembic init -t async alembic
poetry add --group dev black