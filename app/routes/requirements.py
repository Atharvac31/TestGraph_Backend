from fastapi import APIRouter, HTTPException

from app.graph.queries import (
    get_all_requirements,
    get_requirement,
    get_requirement_test_cases,
    get_requirement_components,
    get_requirement_services,
    get_requirement_defects,
    get_requirement_dependencies,
    get_requirement_impact,
    get_requirement_dependency_chain,
    get_dashboard_summary,
)


router = APIRouter(
    prefix="/api/requirements",
    tags=["Requirements"],
)


@router.get("/")
def list_requirements():
    """
    Return all requirements.
    """

    try:
        requirements = get_all_requirements()
        return {
            "count": len(requirements),
            "requirements": requirements,
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve requirements from the database.",
        )


@router.get("/{requirement_id}")
def retrieve_requirement(requirement_id: str):
    """
    Return a single requirement.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        return requirement

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve requirement from the database.",
        )


@router.get("/{requirement_id}/tests")
def requirement_tests(requirement_id: str):
    """
    Return test cases associated with a requirement.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        tests = get_requirement_test_cases(requirement_id)

        return {
            "requirement_id": requirement_id,
            "count": len(tests),
            "test_cases": tests,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve test cases.",
        )


@router.get("/{requirement_id}/components")
def requirement_components(requirement_id: str):
    """
    Return components associated with a requirement.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        components = get_requirement_components(requirement_id)

        return {
            "requirement_id": requirement_id,
            "count": len(components),
            "components": components,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve components.",
        )


@router.get("/{requirement_id}/services")
def requirement_services(requirement_id: str):
    """
    Return services reached through the requirement's
    test and component relationships.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        services = get_requirement_services(requirement_id)

        return {
            "requirement_id": requirement_id,
            "count": len(services),
            "services": services,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve services.",
        )


@router.get("/{requirement_id}/defects")
def requirement_defects(requirement_id: str):
    """
    Return defects associated with a requirement.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        defects = get_requirement_defects(requirement_id)

        return {
            "requirement_id": requirement_id,
            "count": len(defects),
            "defects": defects,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve defects.",
        )


@router.get("/{requirement_id}/dependencies")
def requirement_dependencies(requirement_id: str):
    """
    Return direct dependencies of a requirement.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        dependencies = get_requirement_dependencies(requirement_id)

        return {
            "requirement_id": requirement_id,
            "count": len(dependencies),
            "dependencies": dependencies,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve dependencies.",
        )


@router.get("/{requirement_id}/dependency-chain")
def requirement_dependency_chain(requirement_id: str):
    """
    Return the multi-hop requirement dependency chain.
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        chains = get_requirement_dependency_chain(requirement_id)

        return {
            "requirement_id": requirement_id,
            "chains": chains,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve dependency chain.",
        )


@router.get("/{requirement_id}/impact")
def requirement_impact(requirement_id: str):
    """
    Perform requirement impact analysis.

    Traverses the graph to identify:

    - Test cases
    - Components
    - Services
    - Defects
    - Affected components
    """

    try:
        requirement = get_requirement(requirement_id)

        if requirement is None:
            raise HTTPException(
                status_code=404,
                detail=f"Requirement '{requirement_id}' not found.",
            )

        impact = get_requirement_impact(requirement_id)

        return impact

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to perform impact analysis.",
        )

@router.get("/dashboard/summary")
def dashboard_summary():
    try:
        summary = get_dashboard_summary()

        if summary is None:
            raise HTTPException(
                status_code=404,
                detail="Dashboard data not available.",
            )

        return summary

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to retrieve dashboard data.",
        )