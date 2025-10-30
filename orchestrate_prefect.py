from prefect import flow, task, get_run_logger
from dotenv import load_dotenv
from src.extract import Extract
from src.transform import transform_universities
from src.load import Load


load_dotenv()


@task(retries=3, retry_delay_seconds=10)
def extract_task(country: str) -> list[dict]:
    logger = get_run_logger()
    extractor = Extract()
    data = extractor.extract_data(country)
    logger.info(f"{len(data)} registros extraídos de {country}")
    return data


@task
def transform_task(data: list[dict]) -> list[dict]:
    logger = get_run_logger()
    transformed = transform_universities(data)
    logger.info(f"{len(transformed)} registros transformados")
    return transformed


@task
def load_task(universities: list[dict]):
    logger = get_run_logger()
    loader = Load()
    db_name = "universidades_db"
    collection_name = "universidades"

    loader.load_data_atlas(universities, db_name, collection_name)
    logger.info(f"{len(universities)} registros inseridos em {db_name}.{collection_name}")


@flow(name="ETL Universities Prefect", log_prints=True)
def etl_universities_flow(country: str = "Brazil"):
    data = extract_task(country)
    transformed = transform_task(data)
    load_task(transformed)


if __name__ == "__main__":
    etl_universities_flow()
