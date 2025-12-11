from engine.workflow_engine import WorkflowEngine

def main():
    print("Starting Workflow Engine...\n")

    engine = WorkflowEngine()

    
    tasks = [
        {"id": 1, "name": "Data Ingestion"},
        {"id": 2, "name": "Data Cleaning"},
        {"id": 3, "name": "Feature Engineering"},
        {"id": 4, "name": "Model Training"},
        {"id": 5, "name": "Model Evaluation"}
    ]

    engine.load_tasks(tasks)
    engine.execute()

if __name__ == "__main__":
    main()
