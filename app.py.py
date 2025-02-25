import streamlit as st

def load_tasks():
    return st.session_state.get("tasks", [])

def save_tasks(tasks):
    st.session_state["tasks"] = tasks

def main():
    st.title("📝 To-Do List")
    
    tasks = load_tasks()
    
    new_task = st.text_input("Add a new task:", "")
    if st.button("Add Task") and new_task:
        tasks.append({"task": new_task, "completed": False})
        save_tasks(tasks)
    
    st.subheader("Your Tasks:")
    
    updated_tasks = []
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            completed = st.checkbox(task["task"], value=task["completed"])
        with col2:
            if st.button("❌", key=f"del_{i}"):
                continue  # Skip adding this task to updated list
        updated_tasks.append({"task": task["task"], "completed": completed})
    
    save_tasks(updated_tasks)

if __name__ == "__main__":
    main()
