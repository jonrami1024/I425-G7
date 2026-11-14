# Group 7

> To get calculated stats, do:
> `/combinations?driver_id=1&body_id=1&tire_id=1&glider_id=1`

## Team Responsibilities

## Lab 4

#### Jonathan Ramirez-Molina
- k

#### Daniel Shin
- k

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
