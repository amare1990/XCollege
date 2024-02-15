<a name="readme-top"></a>

<div align="center">

  <br/>

  <h3><b>College Management System</b></h3>

</div>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#triangular_flag_on_post-deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [⭐️ Show your support](#support)
- [📝 License](#license)


# 📖 College Management System <a name="about-project"></a>

> College Management System is a web application intended for the management of the college including teachers, students, course, and more. It is not just a web application but also a website. It is built with Django, bootstrap and JavaScript.

**College Management System** allows people who want to learn to view programs, important registration dates, program requirements, and more. It also allows each entity in the college to automate their responsibilities.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

- Developed with Django web, a Python web framework.

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="http://www.ecmascript.org/">JavaScript</a></li>
  </ul>
</details>

<details>
  <summary>Back-end</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.sqlite.org/index.html">SQLite</a></li>
  </ul>
</details>


## Key Features <a name="key-features"></a>


- **It is a website that incorporates web applications**
- **Allows users to create and edit their corresponding profile**
- **Allows admins to manage teachers, students, departments, courses, and more**
- **Allows students to register for courses, view courses they registered, view their result, manage leave requests, and more**
- **Allows department heads to offer course, view courses offered, evaluate and grade their students, and more**
- **Allows department heads to manage their leave requests (requested by themselves to the school dean)**
- **Allow department heads to manage leave requests by their corresponding department staffs and students**
- **Allows teachers to evaluate and grade their students for the course they are teaching**
- **Allows teachers to manage their leave requests (leave requests by themselves) and to manage leave requests (leave requests requested by their students)**

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🚀 Live Demo <a name="live-demo"></a>

> cooming soon!

- [Live Demo Link]().

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

Install python
```sh
  sudo apt-get update
  sudo apt install python3.8
```

### Setup

Clone this repository to your desired folder (e.g., my-folder):


```sh
  cd my-folder
  git clone https://github.com/amare1990/XCollege.git
```
### Install

Install this project with:

```sh
To activate the virtual environment (if you use Linux environment), run
source venv-college/bin/activate
```

Then run following commands to create migrations and databases
```sh
python manage makemigrations
python manage migrate

```

### Usage

To run the project, execute the following command:

```sh
  python manage runserver
```
To view the website, insert the following url in your browser's address bar

```sh
  localhost:8000
```

To create a user account, update profile, go to your dashboard, and more

Click the top right corner button (chiron) in the navbar

### Impportant notice!

- **Create super user (the college highest officials will have a super user status and will have the admin role) using the following command. You have to make the admin username to be 'admin' or update their profile role to be admin next in order to manage each staff with the highest privillege.**
```sh
  python manage.py createsuperuser
````

- **Create and update user profiles of which their role is a teacher before adding departments (as there is a OneToOne r/ship between a UserProfile model and department_head field in the Department model). Adding department requires to add a department name and a department head from the UserProfile of which their role is a teacher**
- **Create and update userprofiles of which their role is a student before using features**


### Run tests

To run tests, run the following command:

run the following command
```sh
Coming!
```

### Deployment

- Coming soon!


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 👥 Authors <a name="authors"></a>

👤 **Amare Kassa**

- GitHub: [@githubhandle](https://github.com/amare1990)
- Twitter: [@twitterhandle](https://twitter.com/amaremek)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/amaremek/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🔭 Future Features <a name="future-features"></a>

- **Add grade report management feature for both students and registrar**
- **Add class schedule application feature**
- **Implement notifications system for college community and to the users**
- **Add students monthly fee payment feature**
- **Add students' fee payment management feature**
- **Add staff salary and incentives management feature**


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/amare1990/XCollege/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## ⭐️ Show your support <a name="support"></a>


If you like this project, hit the ⭐️ button!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 📝 License <a name="license"></a>

This project is [MIT](https://github.com/amare1990/XCollege/commit/41d85d2dad7400a022d130fb5725970b5407b691) licensed.


<p align="right">(<a href="#readme-top">back to top</a>)</p>
