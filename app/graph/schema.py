from app.database.connection import driver


CONSTRAINTS = [
    """
    CREATE CONSTRAINT project_id_unique IF NOT EXISTS
    FOR (p:Project)
    REQUIRE p.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT requirement_id_unique IF NOT EXISTS
    FOR (r:Requirement)
    REQUIRE r.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT testcase_id_unique IF NOT EXISTS
    FOR (t:TestCase)
    REQUIRE t.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT component_id_unique IF NOT EXISTS
    FOR (c:Component)
    REQUIRE c.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT service_id_unique IF NOT EXISTS
    FOR (s:Service)
    REQUIRE s.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT defect_id_unique IF NOT EXISTS
    FOR (d:Defect)
    REQUIRE d.id IS UNIQUE
    """,
]


def create_schema():
    with driver.session() as session:
        for constraint in CONSTRAINTS:
            session.run(constraint)

    print("Graph schema created successfully.")


if __name__ == "__main__":
    create_schema()