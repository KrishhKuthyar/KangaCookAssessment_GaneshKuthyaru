# KangaCook_OA_GaneshKuthyaru
A Simple React and Django Website for Kangacook OA


Accessing and Setting Up the Movie Browser Project

Clone the Repository

Go to your GitHub repository page. Click the green “Code” button and copy the repository URL. Open your terminal or command prompt. Use the git clone command followed by the repository URL to clone the project to your local machine. Navigate into the project directory using the cd command.


2. Setting Up the Backend (Django)

Navigate to the backend directory within the project. Create a virtual environment (optional but recommended) to keep dependencies isolated. Activate the virtual environment. Install the required dependencies listed in the requirements.txt file. You can use a command to install these dependencies. Run database migrations to set up any necessary database tables. Start the Django development server, which will typically be accessible at http://127.0.0.1:8000/.

3. Setting Up the Frontend (React)

Navigate back to the main project directory, then go to the frontend directory. Install the Node.js dependencies required for the frontend. This can be done using a package manager command to install the dependencies. Start the React development server using the appropriate command. The frontend will typically be accessible at http://localhost:3000/.

4. Using the Application

Open a web browser and go to http://localhost:3000 to view the Movie Browser application. You will see a list of movies. Click on any movie title to view more detailed information about that movie. The frontend communicates with the backend using API endpoints, such as http://127.0.0.1:8000/api/movies/ for the list of movies, and http://127.0.0.1:8000/api/movies/<movie_id>/ for details about a specific movie.

![image](https://github.com/user-attachments/assets/cd0d667a-9ec7-45a8-964e-0a98da4c5879)
