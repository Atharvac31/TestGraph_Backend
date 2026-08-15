from app.database.connection import driver


def create_projects():
    query = """
    UNWIND $projects AS project

    MERGE (p:Project {id: project.id})
    SET
        p.name = project.name,
        p.description = project.description,
        p.status = project.status
    """

    projects = [
        {
            "id": "PRJ-001",
            "name": "E-Commerce Platform",
            "description": "Online shopping platform for customers and administrators.",
            "status": "active",
        }
    ]

    with driver.session() as session:
        session.run(query, projects=projects)


def create_services():
    query = """
    UNWIND $services AS service

    MERGE (s:Service {id: service.id})
    SET
        s.name = service.name,
        s.description = service.description
    """

    services = [
        {
            "id": "SVC-001",
            "name": "Identity Service",
            "description": "Handles authentication, authorization and account security.",
        },
        {
            "id": "SVC-002",
            "name": "Catalog Service",
            "description": "Handles product search and product information.",
        },
        {
            "id": "SVC-003",
            "name": "Order Service",
            "description": "Handles shopping carts, checkout and order processing.",
        },
    ]

    with driver.session() as session:
        session.run(query, services=services)


def create_components():
    query = """
    UNWIND $components AS component

    MERGE (c:Component {id: component.id})
    SET
        c.name = component.name,
        c.technology = component.technology
    """

    components = [
        {
            "id": "COMP-001",
            "name": "Authentication API",
            "technology": "FastAPI",
        },
        {
            "id": "COMP-002",
            "name": "User Database",
            "technology": "PostgreSQL",
        },
        {
            "id": "COMP-003",
            "name": "Search API",
            "technology": "FastAPI",
        },
        {
            "id": "COMP-004",
            "name": "Cart API",
            "technology": "FastAPI",
        },
        {
            "id": "COMP-005",
            "name": "Payment API",
            "technology": "FastAPI",
        },
        {
            "id": "COMP-006",
            "name": "Order API",
            "technology": "FastAPI",
        },
    ]

    with driver.session() as session:
        session.run(query, components=components)


def create_requirements():
    query = """
    UNWIND $requirements AS requirement

    MERGE (r:Requirement {id: requirement.id})
    SET
        r.title = requirement.title,
        r.description = requirement.description,
        r.priority = requirement.priority,
        r.status = requirement.status
    """

    requirements = [
        {
            "id": "REQ-001",
            "title": "User Registration",
            "description": "Users shall be able to create an account using their email address and password.",
            "priority": "high",
            "status": "implemented",
        },
        {
            "id": "REQ-002",
            "title": "User Login",
            "description": "Users shall be able to log in using their registered email address and password.",
            "priority": "high",
            "status": "implemented",
        },
        {
            "id": "REQ-003",
            "title": "Product Search",
            "description": "Users shall be able to search for products by name or keyword.",
            "priority": "medium",
            "status": "implemented",
        },
        {
            "id": "REQ-004",
            "title": "Shopping Cart",
            "description": "Users shall be able to add products to a shopping cart and modify quantities.",
            "priority": "high",
            "status": "implemented",
        },
        {
            "id": "REQ-005",
            "title": "Checkout",
            "description": "Users shall be able to review their cart and complete the checkout process.",
            "priority": "high",
            "status": "implemented",
        },
        {
            "id": "REQ-006",
            "title": "Payment Processing",
            "description": "The system shall securely process payments during checkout.",
            "priority": "critical",
            "status": "implemented",
        },
        {
            "id": "REQ-007",
            "title": "Order Tracking",
            "description": "Users shall be able to view the status of their orders.",
            "priority": "medium",
            "status": "implemented",
        },
        {
            "id": "REQ-008",
            "title": "Account Lockout",
            "description": "The system shall temporarily lock an account after repeated failed login attempts.",
            "priority": "high",
            "status": "implemented",
        },
    ]

    with driver.session() as session:
        session.run(query, requirements=requirements)


def create_test_cases():
    query = """
    UNWIND $test_cases AS test_case

    MERGE (t:TestCase {id: test_case.id})
    SET
        t.title = test_case.title,
        t.type = test_case.type,
        t.status = test_case.status
    """

    test_cases = [
        {
            "id": "TC-001",
            "title": "Register with valid credentials",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-002",
            "title": "Register with invalid email",
            "type": "negative",
            "status": "passed",
        },
        {
            "id": "TC-003",
            "title": "Login with valid credentials",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-004",
            "title": "Login with invalid password",
            "type": "negative",
            "status": "passed",
        },
        {
            "id": "TC-005",
            "title": "Search product by keyword",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-006",
            "title": "Add product to cart",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-007",
            "title": "Modify cart quantity",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-008",
            "title": "Checkout with valid cart",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-009",
            "title": "Payment declined",
            "type": "negative",
            "status": "passed",
        },
        {
            "id": "TC-010",
            "title": "Track existing order",
            "type": "functional",
            "status": "passed",
        },
        {
            "id": "TC-011",
            "title": "Account lockout after failed attempts",
            "type": "security",
            "status": "failed",
        },
        {
            "id": "TC-012",
            "title": "Checkout without payment",
            "type": "negative",
            "status": "passed",
        },
    ]

    with driver.session() as session:
        session.run(query, test_cases=test_cases)


def create_defects():
    query = """
    UNWIND $defects AS defect

    MERGE (d:Defect {id: defect.id})
    SET
        d.title = defect.title,
        d.severity = defect.severity,
        d.status = defect.status
    """

    defects = [
        {
            "id": "BUG-001",
            "title": "Account lockout not triggered",
            "severity": "high",
            "status": "open",
        },
        {
            "id": "BUG-002",
            "title": "Payment timeout during checkout",
            "severity": "critical",
            "status": "open",
        },
        {
            "id": "BUG-003",
            "title": "Search returns incomplete results",
            "severity": "medium",
            "status": "resolved",
        },
        {
            "id": "BUG-004",
            "title": "Cart quantity resets after refresh",
            "severity": "medium",
            "status": "open",
        },
        {
            "id": "BUG-005",
            "title": "Order status update delayed",
            "severity": "low",
            "status": "resolved",
        },
    ]

    with driver.session() as session:
        session.run(query, defects=defects)


def create_relationships():
    queries = [
        # Project -> Requirements
        """
        MATCH (p:Project {id: "PRJ-001"})
        MATCH (r:Requirement)
        WHERE r.id IN $requirement_ids
        MERGE (p)-[:HAS_REQUIREMENT]->(r)
        """,

        # Requirements -> Test Cases
        """
        UNWIND $links AS link
        MATCH (r:Requirement {id: link.requirement_id})
        MATCH (t:TestCase {id: link.test_case_id})
        MERGE (r)-[:VALIDATED_BY]->(t)
        """,

        # Test Cases -> Components
        """
        UNWIND $links AS link
        MATCH (t:TestCase {id: link.test_case_id})
        MATCH (c:Component {id: link.component_id})
        MERGE (t)-[:TESTS_COMPONENT]->(c)
        """,

        # Components -> Services
        """
        UNWIND $links AS link
        MATCH (c:Component {id: link.component_id})
        MATCH (s:Service {id: link.service_id})
        MERGE (c)-[:PART_OF]->(s)
        """,

        # Requirement dependencies
        """
        UNWIND $links AS link
        MATCH (r1:Requirement {id: link.from_id})
        MATCH (r2:Requirement {id: link.to_id})
        MERGE (r1)-[:DEPENDS_ON]->(r2)
        """,

        # Test Cases -> Defects
        """
        UNWIND $links AS link
        MATCH (t:TestCase {id: link.test_case_id})
        MATCH (d:Defect {id: link.defect_id})
        MERGE (t)-[:CAUGHT]->(d)
        """,

        # Defects -> Components
        """
        UNWIND $links AS link
        MATCH (d:Defect {id: link.defect_id})
        MATCH (c:Component {id: link.component_id})
        MERGE (d)-[:AFFECTS]->(c)
        """,
    ]

    with driver.session() as session:

        session.run(
            queries[0],
            requirement_ids=[
                "REQ-001",
                "REQ-002",
                "REQ-003",
                "REQ-004",
                "REQ-005",
                "REQ-006",
                "REQ-007",
                "REQ-008",
            ],
        )

        session.run(
            queries[1],
            links=[
                {"requirement_id": "REQ-001", "test_case_id": "TC-001"},
                {"requirement_id": "REQ-001", "test_case_id": "TC-002"},
                {"requirement_id": "REQ-002", "test_case_id": "TC-003"},
                {"requirement_id": "REQ-002", "test_case_id": "TC-004"},
                {"requirement_id": "REQ-003", "test_case_id": "TC-005"},
                {"requirement_id": "REQ-004", "test_case_id": "TC-006"},
                {"requirement_id": "REQ-004", "test_case_id": "TC-007"},
                {"requirement_id": "REQ-005", "test_case_id": "TC-008"},
                {"requirement_id": "REQ-006", "test_case_id": "TC-009"},
                {"requirement_id": "REQ-007", "test_case_id": "TC-010"},
                {"requirement_id": "REQ-008", "test_case_id": "TC-011"},
                {"requirement_id": "REQ-005", "test_case_id": "TC-012"},
            ],
        )

        session.run(
            queries[2],
            links=[
                {"test_case_id": "TC-001", "component_id": "COMP-001"},
                {"test_case_id": "TC-002", "component_id": "COMP-001"},
                {"test_case_id": "TC-003", "component_id": "COMP-001"},
                {"test_case_id": "TC-004", "component_id": "COMP-001"},
                {"test_case_id": "TC-005", "component_id": "COMP-003"},
                {"test_case_id": "TC-006", "component_id": "COMP-004"},
                {"test_case_id": "TC-007", "component_id": "COMP-004"},
                {"test_case_id": "TC-008", "component_id": "COMP-005"},
                {"test_case_id": "TC-009", "component_id": "COMP-005"},
                {"test_case_id": "TC-010", "component_id": "COMP-006"},
                {"test_case_id": "TC-011", "component_id": "COMP-001"},
                {"test_case_id": "TC-012", "component_id": "COMP-005"},
            ],
        )

        session.run(
            queries[3],
            links=[
                {"component_id": "COMP-001", "service_id": "SVC-001"},
                {"component_id": "COMP-002", "service_id": "SVC-001"},
                {"component_id": "COMP-003", "service_id": "SVC-002"},
                {"component_id": "COMP-004", "service_id": "SVC-003"},
                {"component_id": "COMP-005", "service_id": "SVC-003"},
                {"component_id": "COMP-006", "service_id": "SVC-003"},
            ],
        )

        session.run(
            queries[4],
            links=[
                {"from_id": "REQ-002", "to_id": "REQ-001"},
                {"from_id": "REQ-008", "to_id": "REQ-002"},
                {"from_id": "REQ-004", "to_id": "REQ-003"},
                {"from_id": "REQ-005", "to_id": "REQ-004"},
                {"from_id": "REQ-005", "to_id": "REQ-006"},
                {"from_id": "REQ-007", "to_id": "REQ-005"},
            ],
        )

        session.run(
            queries[5],
            links=[
                {"test_case_id": "TC-011", "defect_id": "BUG-001"},
                {"test_case_id": "TC-009", "defect_id": "BUG-002"},
                {"test_case_id": "TC-005", "defect_id": "BUG-003"},
                {"test_case_id": "TC-007", "defect_id": "BUG-004"},
                {"test_case_id": "TC-010", "defect_id": "BUG-005"},
            ],
        )

        session.run(
            queries[6],
            links=[
                {"defect_id": "BUG-001", "component_id": "COMP-001"},
                {"defect_id": "BUG-002", "component_id": "COMP-005"},
                {"defect_id": "BUG-003", "component_id": "COMP-003"},
                {"defect_id": "BUG-004", "component_id": "COMP-004"},
                {"defect_id": "BUG-005", "component_id": "COMP-006"},
            ],
        )


def seed_database():
    print("Starting database seed...")

    create_projects()
    print("Projects created.")

    create_services()
    print("Services created.")

    create_components()
    print("Components created.")

    create_requirements()
    print("Requirements created.")

    create_test_cases()
    print("Test cases created.")

    create_defects()
    print("Defects created.")

    create_relationships()
    print("Relationships created.")

    print("Database seed completed successfully.")


if __name__ == "__main__":
    seed_database()
    driver.close()