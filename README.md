# Recommend System for Amazon Book Chatbot

This repository contains the code for the final project of GNG5125 Group 7. 

The project is a book recommendation chatbot that uses natural language processing techniques to suggest books to users based on their interests.

Group  members:

8795048 Yuting Cao

300254157 Manjie Hou

300250954 Haiwei Nan

300151213 Yunzhou Wang


## Getting Started

To get started with the project, you'll need to do the following:

1. Clone this repository to your local machine using `git clone https://github.com/GNG5125-Group7-Assignment/Final_Project.git`
2. Install the required packages by running `pip install -r requirements.txt`
3. Download the necessary data files and models by running `python download_data.py`
4. Run the training algorithm by `python Recommend_using_TFIDF.py` or `python Recommend_using_BERT.py`(Recommentd TFIDF since BERT need more time and processing ability of computer)
5. Run the `app.py` to connect to Dialogflow


## Usage

To use the book recommendation chatbot, you'll need to run the `app.py` file. You can do this by running the command `python app.py` in the terminal.

Once the chatbot is running, you can interact with it by opening a web browser and navigating to `http://localhost:5000`.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork this repository to your own account
2. Create a new branch with a descriptive name (`git checkout -b feature/add-new-functionality`)
3. Make your changes and commit them (`git commit -am 'Add new functionality'`)
4. Push your changes to your fork (`git push origin feature/add-new-functionality`)
5. Open a pull request on this repository and describe your changes

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
