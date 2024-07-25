run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@$(pwd) alembic revision --autogenerate -m $(d) 

run-migrations:
	@$(pwd) alembic upgrade head