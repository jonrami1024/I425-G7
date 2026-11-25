![mk8-api](logo.png)


# Group 7

> To get calculated stats, do:
> `/combinations?driver_id=1&body_id=1&tire_id=1&glider_id=1`

## Setup (Lab 4)

1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and put a secret key in it
   (make one with `python -c "import secrets; print(secrets.token_urlsafe(64))"`).
3. `uvicorn main:app --reload`
4. Log in with `POST /auth/login` and send the token as `Authorization: Bearer <jwt>`.

Test logins: Toadsworth / TallyHoPassword (Admin), ProfessorEGadd / Poltergust3000 (User Manager),
Starlow / HelloYello (Advanced User), Goomba / EliteTrio (Basic User).


## Team Responsibilities

## Lab 5
#### Jonathan Ramirez-Molina
- Created visual design, layout, header, footer, the application routes, navigation, and the not-found page
- Created Logo

#### Daniel Shin
- k

#### Angel Avila
- Worked on incorporating step 3 of lab 5
  - Added src/config/settings.jsx
  - Added src/hooks/useAxios.jsx
- Worked on character and builds for step 4 of lab 5
  - List, detail, and related data:
    - Files are in src/pages/character and src/pages/builds. Routes are in src/routes, and CSS's are in src/assets/css
  - Pagination and sorting:
      - File is in src/pages/builds 
- Revised AppRoutes to incorporate character and build routes
- Disabled authentication for driver and builds routes in mk8api-api for them to display the information

### -----------------

## Lab 4

#### Jonathan Ramirez-Molina
- Added roles table and added password row to users table
- Started adding the create and delete users

#### Daniel Shin
- Fixed POST /users and PUT /users so passwords are always hashed and never saved as plain text
- Fixed the .sql script and database so the roles and users tables rebuild correctly
- Switched the read-only routers to `get_current_user` and kept role checks on create, update, and delete
- Added CORS for http://localhost:3000 and moved the secret key to a .env file (.env.example included)
- Updated requirements.txt, the API documentation, the Postman collection, and the testing document

#### Angel Avila
- Created the authentication (auth) folder
  - Added routes.py 
  - Added schemas.py
  - Added services.py
- Modified the users services.py
  - Added fetch_user_by_username to authenticate the users username
- Created config.py
- Modified dependencies.py
  - Stores code for JWT token and roles authorization
- Modified the routes files for all folders:
  - build_ratings and builds can only authorize advance users to create, update, and delete
  - users only authorizes roles 1 and 2
  - body, bodyTypeGroup, calculateStats, driver, driverSize, glider, tire, tireGroup, users is authorized to every role
- Created the I425-G7 Lab 4 Documentation docx.
  - Stores the screenshots as well as the user logins.
- Modified Postman collection
  - Added Auth folder for User Registration and User Login
  - Added child inheritance of parent token to every folder

### -----------------

## Lab 3

#### Jonathan Ramirez-Molina
- Added pagination to users, build_ratings, and builds (/users/?limit=2&offset=3)
- Added Sorting to users, build_ratings, and builds
- Added searching to users and builds

#### Daniel Shin
- Fixed the issues from the Lab 2 feedback
- Added create, update, and delete endpoints for users, builds, and ratings
- Added input validation for creating and updating data
- Wrote the API documentation and the Postman collection

#### Angel Avila
- Created the I425-G7_Postman_Screenshots.docx
  - Stores screenshots of every API request
  - Added missing "Saved responses" to requests
- Ensured every API request worked
- Revised Postman Collection JSON

### -----------------

## Lab 2

#### Daniel Shin
- Reviewed the project against the Lab 2 requirements and fixed the issues found
- Removed the old glider group code and table, fixed the builds foreign key, and added `glider_id` to build responses
- Added relationships on both sides (builds with each part, users with ratings) and the related-data endpoints
- Added a summary to every endpoint and readable tags for `/docs`
- Applied the Lab 1 feedback to the database: group labels, `build_name` and `username` checks, and the rule against rating your own build
- Updated the `.sql` script, ER diagram, API documentation (changes highlighted), Postman collection, and endpoint screenshots

#### Angel Avila
- Created the `Lab 2 Changes Documentation`. This docx contains the changes I have made within the files of our project to 
match the endpoint document and incorporate the Lab 1 feedback. Below are changes made, in the document it'll specify more of what changed.
  - Revised Database
  - Revised root file (I425-G7)
  - Revised body
  - Revised bodyTypeGroup
  - Revised calculateStats
  - Revised driver
  - Revised driverSize
  - Revised glider
  - Revised gliderGroup
  - Revised tire
  - Revised tireGroup
  - Revised users
  - Revised builds
  - Revised build_ratings
- Created the Postman collection for our project, `I425-G7 local`. Each response came back as 200 OK. Every model is included, with it's endpoints.
