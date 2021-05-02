# The J Word

## Author

Joy Kirii

## Description

This is a flask application that allows users to create blog posts and read other writers blog posts. They can also give comments on other users' blogs.

## Behavour Driven Development

| Input                         | Behaviour                                                         | Output                                    |
| ----------------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| Add Post                      | Redirect to create_post page to fill in form with content         | Displays posts in index page              |
| User comment of the blog post | User fills form with feedback and post it                         | Comment will be displayed under blog post |
| User deletes a post           | Post deleted from database                                        | Post will no longer appear on page        |
| Update Post                   | Redirect to create_post page to fill in form with updated content | Displays updated post in index posts page |
| Delete Comment                | Comment is deleted from dateabase                                 | Comment no longer displayed on posts page |
| Subscribe to mail list        | Input user email                                                  | redirect to index page                    |

## Installation

### Requirements

-This program requires python3.+ (and pip) installed. Ensure you have this before proceeding with installation.

### Installlation and Set-up

- Step 1 : Clone this repository.
- Step 2 : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment.
- Step 3 : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.
  -Step 4 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt
- Step 5: Create a file in your root directory called start.sh and store a generated SECRET key like so `python export SECRET_KEY="<your-key>"`
  On the same file write down the command `python python3 manage.py server`
- Step 6 : On your terminal, run the following command, `python chmod a+x start.sh`

- You can now launch the application locally by running the command `python ./start.sh`

## Technology Used

- Python
- Flask
- Heroku
- HTML
- Bootstrap

## Known Bugs

Send email message function not working. Gives an Errno 61 error.

## Contact

For any comments,questions and concerns feel free to contact me via my email: joykirii@gmail.com.

## License

Copyright &Copy: 2020 Joy Kirii.
