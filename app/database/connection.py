from neo4j import GraphDatabase

from app.config import (
    COGNODB_URI,
    COGNODB_USERNAME,
    COGNODB_PASSWORD,
)


driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USERNAME, COGNODB_PASSWORD),
)


def verify_connection():
    with driver.session() as session:
        result = session.run("RETURN 1 AS number")
        record = result.single()

        return record["number"] == 1

def close_connection():
    driver.close()