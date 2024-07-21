## Running the Project

### Questions 1-4

For questions 1-4, you need to run `main.py`. This script handles the necessary setup and execution for these questions.

1. Ensure you are in the project directory.
2. Run the script:

    ```bash
    python main.py
    ```

### Question 5

For question 5, you need to run the Django server. This part involves creating, listing, updating, and deleting school data using Django's REST framework.

1. Ensure you are in the project directory.
2. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```


### API Endpoints

- **Schools**
  - `GET /api/v1/schools/`: List all schools
  - `POST /api/v1/schools/`: Create a new school
  - `GET /api/v1/schools/<id>/`: Retrieve a specific school
  - `PUT /api/v1/schools/<id>/`: Update a specific school
  - `DELETE /api/v1/schools/<id>/`: Delete a specific school

- **Classrooms**
  - `GET /api/v1/classrooms/`: List all classrooms
  - `POST /api/v1/classrooms/`: Create a new classroom
  - `GET /api/v1/classrooms/<id>/`: Retrieve a specific classroom
  - `PUT /api/v1/classrooms/<id>/`: Update a specific classroom
  - `DELETE /api/v1/classrooms/<id>/`: Delete a specific classroom

- **Teachers**
  - `GET /api/v1/teachers/`: List all teachers
  - `POST /api/v1/teachers/`: Create a new teacher
  - `GET /api/v1/teachers/<id>/`: Retrieve a specific teacher
  - `PUT /api/v1/teachers/<id>/`: Update a specific teacher
  - `DELETE /api/v1/teachers/<id>/`: Delete a specific teacher

- **Students**
  - `GET /api/v1/students/`: List all students
  - `POST /api/v1/students/`: Create a new student
  - `GET /api/v1/students/<id>/`: Retrieve a specific student
  - `PUT /api/v1/students/<id>/`: Update a specific student
  - `DELETE /api/v1/students/<id>/`: Delete a specific student