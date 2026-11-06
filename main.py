import tasks_function as tf
def main():
    # Load any existing tasks at startup
    tasks = tf.load_tasks()

    print("Welcome to Personal Task Manager!")

    while True:
        print("\n ======================== ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("=============================")

        choice = input("Choose an option (1-5: )").strip()
        if choice =='1':
            tf.view_tasks(tasks)
        elif choice == '2':
            tf.add_task(tasks)
        elif choice == '3':
            tf.complete_task(tasks)
        elif choice == '4':
            tf.delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()