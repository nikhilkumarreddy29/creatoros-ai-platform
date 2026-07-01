from uuid import uuid4
from backend.graph.kg_store import GRAPH_NODES, GRAPH_RELATIONSHIPS


def create_node(node_type: str, name: str, properties: dict = None):
    node = {
        "id": str(uuid4()),
        "type": node_type,
        "name": name,
        "properties": properties or {}
    }

    GRAPH_NODES.append(node)
    return node


def create_relationship(source_name: str, target_name: str, relationship_type: str):
    relationship = {
        "source": source_name,
        "target": target_name,
        "type": relationship_type
    }

    GRAPH_RELATIONSHIPS.append(relationship)
    return relationship


def build_creator_graph():
    creator = create_node("Creator", "CreatorOS Demo Creator")
    platform_youtube = create_node("Platform", "YouTube")
    platform_linkedin = create_node("Platform", "LinkedIn")
    topic = create_node("Topic", "AI Agents for Creators")
    genre = create_node("Genre", "Tech")
    persona = create_node("Audience Persona", "Technical Builder")

    create_relationship(creator["name"], platform_youtube["name"], "CREATOR_USES_PLATFORM")
    create_relationship(creator["name"], platform_linkedin["name"], "CREATOR_USES_PLATFORM")
    create_relationship(topic["name"], genre["name"], "TOPIC_BELONGS_TO_GENRE")
    create_relationship(topic["name"], persona["name"], "TOPIC_TARGETS_PERSONA")

    return {
        "agent": "Knowledge Graph Agent",
        "message": "Local knowledge graph created",
        "nodes": GRAPH_NODES,
        "relationships": GRAPH_RELATIONSHIPS
    }


def get_graph():
    return {
        "nodes": GRAPH_NODES,
        "relationships": GRAPH_RELATIONSHIPS
    }
def query_related_entities(name: str):
    related = []

    for rel in GRAPH_RELATIONSHIPS:
        if rel["source"].lower() == name.lower():
            related.append({
                "entity": rel["target"],
                "relationship": rel["type"],
                "direction": "outgoing"
            })

        if rel["target"].lower() == name.lower():
            related.append({
                "entity": rel["source"],
                "relationship": rel["type"],
                "direction": "incoming"
            })

    return {
        "agent": "Knowledge Graph Query Agent",
        "query": name,
        "related_entities": related,
        "count": len(related)
    }
def add_draft_to_graph(draft_data: dict):
    topic_name = draft_data["topic"]
    genre_name = draft_data["genre"]
    platform_name = draft_data["platform"]
    workflow_id = draft_data["workflow_id"]

    create_node("Topic", topic_name)
    create_node("Genre", genre_name)
    create_node("Platform", platform_name)
    create_node("Draft", workflow_id)

    create_relationship(topic_name, genre_name, "TOPIC_BELONGS_TO_GENRE")
    create_relationship(topic_name, workflow_id, "TOPIC_GENERATED_DRAFT")
    create_relationship(workflow_id, platform_name, "DRAFT_TARGETS_PLATFORM")

    return {
        "message": "Draft added to knowledge graph",
        "workflow_id": workflow_id
    }