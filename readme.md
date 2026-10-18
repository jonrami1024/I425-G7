# Group 7

> To get calculated stats, do:
> `/combinations?driver_id=1&body_id=1&tire_id=1&glider_id=1`

## Team Responsibilities

### Daniel Shin
- Reviewed the project against the Lab 2 requirements and fixed the issues found
- Removed the old glider group code and table, fixed the builds foreign key, and added `glider_id` to build responses
- Added relationships on both sides (builds with each part, users with ratings) and the related-data endpoints
- Added a summary to every endpoint and readable tags for `/docs`
- Applied the Lab 1 feedback to the database: group labels, `build_name` and `username` checks, and the rule against rating your own build
- Updated the `.sql` script, ER diagram, API documentation (changes highlighted), Postman collection, and endpoint screenshots

### Jonathan Ramirez-Molina
- Added `users`, `builds`, and `build_ratings` to api
- Added relationships between builds and ratings

### Angel Avila
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






