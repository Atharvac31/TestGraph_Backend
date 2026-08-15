from app.database.connection import driver


def get_all_requirements():
    """
    Return all requirements in the project.
    """

    query = """
    MATCH (r:Requirement)
    RETURN
        r.id AS id,
        r.title AS title,
        r.description AS description,
        r.priority AS priority,
        r.status AS status
    ORDER BY r.id
    """

    with driver.session() as session:
        result = session.run(query)

        return [record.data() for record in result]


def get_requirement(requirement_id: str):
    """
    Return a single requirement by ID.
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
    RETURN
        r.id AS id,
        r.title AS title,
        r.description AS description,
        r.priority AS priority,
        r.status AS status
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        record = result.single()

        if record is None:
            return None

        return record.data()


def get_requirement_test_cases(requirement_id: str):
    """
    Return all test cases validating a requirement.
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
          -[:VALIDATED_BY]->
          (t:TestCase)

    RETURN
        t.id AS id,
        t.title AS title,
        t.type AS type,
        t.status AS status
    ORDER BY t.id
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]


def get_requirement_components(requirement_id: str):
    """
    Return components tested by test cases associated
    with a requirement.
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
          -[:VALIDATED_BY]->
          (t:TestCase)
          -[:TESTS_COMPONENT]->
          (c:Component)

    RETURN DISTINCT
        c.id AS id,
        c.name AS name,
        c.technology AS technology
    ORDER BY c.id
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]


def get_requirement_services(requirement_id: str):
    """
    Multi-hop traversal:

    Requirement
        -> TestCase
        -> Component
        -> Service
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
          -[:VALIDATED_BY]->
          (t:TestCase)
          -[:TESTS_COMPONENT]->
          (c:Component)
          -[:PART_OF]->
          (s:Service)

    RETURN DISTINCT
        s.id AS id,
        s.name AS name,
        s.description AS description
    ORDER BY s.id
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]


def get_requirement_defects(requirement_id: str):
    """
    Find defects associated with a requirement.

    Requirement
        -> TestCase
        -> Defect
        -> Component
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
          -[:VALIDATED_BY]->
          (t:TestCase)
          -[:CAUGHT]->
          (d:Defect)
          -[:AFFECTS]->
          (c:Component)

    RETURN DISTINCT
        d.id AS defect_id,
        d.title AS defect_title,
        d.severity AS severity,
        d.status AS status,
        c.id AS component_id,
        c.name AS component_name
    ORDER BY d.id
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]


def get_requirement_dependencies(requirement_id: str):
    """
    Return requirements directly depended upon by the
    selected requirement.
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})
          -[:DEPENDS_ON]->
          (dependency:Requirement)

    RETURN
        dependency.id AS id,
        dependency.title AS title,
        dependency.priority AS priority,
        dependency.status AS status
    ORDER BY dependency.id
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]

def get_requirement_impact(requirement_id: str):
    """
    Analyze the downstream impact of a requirement.

    Traverses:

    Requirement
        -> TestCase
        -> Component
        -> Service

    and:

    Requirement
        -> TestCase
        -> Defect
        -> Component
    """

    query = """
    MATCH (r:Requirement {id: $requirement_id})

    OPTIONAL MATCH
        (r)-[:VALIDATED_BY]->
        (t:TestCase)

    OPTIONAL MATCH
        (t)-[:TESTS_COMPONENT]->
        (c:Component)

    OPTIONAL MATCH
        (c)-[:PART_OF]->
        (s:Service)

    OPTIONAL MATCH
        (t)-[:CAUGHT]->
        (d:Defect)

    OPTIONAL MATCH
        (d)-[:AFFECTS]->
        (affected:Component)

    RETURN
        r.id AS requirement_id,
        r.title AS requirement_title,

        collect(DISTINCT {
            id: t.id,
            title: t.title,
            type: t.type,
            status: t.status
        }) AS test_cases,

        collect(DISTINCT {
            id: c.id,
            name: c.name,
            technology: c.technology
        }) AS components,

        collect(DISTINCT {
            id: s.id,
            name: s.name
        }) AS services,

        collect(DISTINCT {
            id: d.id,
            title: d.title,
            severity: d.severity,
            status: d.status
        }) AS defects,

        collect(DISTINCT {
            id: affected.id,
            name: affected.name
        }) AS affected_components
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        record = result.single()

        if record is None:
            return None

        return record.data()

def get_requirement_dependency_chain(requirement_id: str):
    """
    Find the dependency chain starting from a requirement.
    """

    query = """
    MATCH path =
        (r:Requirement {id: $requirement_id})
        -[:DEPENDS_ON*1..5]->
        (dependency:Requirement)

    RETURN
        [node IN nodes(path) | {
            id: node.id,
            title: node.title
        }] AS chain
    """

    with driver.session() as session:
        result = session.run(
            query,
            requirement_id=requirement_id,
        )

        return [record.data() for record in result]

def get_dashboard_summary():
    query = """
    MATCH (r:Requirement)
    WITH count(r) AS requirements

    MATCH (t:TestCase)
    WITH requirements, count(t) AS test_cases

    MATCH (c:Component)
    WITH requirements, test_cases, count(c) AS components

    MATCH (s:Service)
    WITH requirements, test_cases, components, count(s) AS services

    MATCH (d:Defect)
    RETURN
        requirements,
        test_cases,
        components,
        services,
        count(d) AS defects
    """

    with driver.session() as session:
        result = session.run(query)
        record = result.single()

        if record is None:
            return None

        return record.data()

if __name__ == "__main__":
    print("\n--- REQUIREMENTS ---")
    print(get_all_requirements())

    print("\n--- REQ-008 ---")
    print(get_requirement("REQ-008"))

    print("\n--- TEST CASES ---")
    print(get_requirement_test_cases("REQ-008"))

    print("\n--- COMPONENTS ---")
    print(get_requirement_components("REQ-008"))

    print("\n--- SERVICES ---")
    print(get_requirement_services("REQ-008"))

    print("\n--- DEFECTS ---")
    print(get_requirement_defects("REQ-008"))

    print("\n--- DEPENDENCIES ---")
    print(get_requirement_dependencies("REQ-008"))

    print("\n--- IMPACT ANALYSIS ---")
    print(get_requirement_impact("REQ-008"))

    print("\n--- DEPENDENCY CHAIN ---")
    print(get_requirement_dependency_chain("REQ-007"))

    driver.close()