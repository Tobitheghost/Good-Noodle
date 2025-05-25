# Good Noodle Chart by Tobi Ghost
This is the bones of a project to create a "Good Noodles" chart online in the fashion of Sponge Bob square pants. 

## Setup

1. **Getting the Files**
	Clone the repository.

        git clone https://github.com/Tobitheghost/Good-Noodle.git

	Or download the Zip file.


2. **Virtual Environment** 
	To create a virtual environment, go to the **/Games** folder and run the following command. This will create a new virtual environment in a folder named `.venv`:
	
    Windows: 

        py -m venv .venv
    
    Mac/Linux: 

        python3 -m venv .venv


    Next you will need to Activate the virtual environment. This will put the virtual environment-specific python and pip executables into your shell’s `PATH`.

    Windows:

        .venv\Scripts\activate
    
    Mac/Linux:

        source .venv/bin/activate

    <details>
        <summary>Tips</summary>
        If you want to switch projects or leave your virtual environment, deactivate the environment with the following command:

        deactivate
    </details>


    Lastly you will download the requirements.

    Windows: 

        py -m pip install -r requirements.txt
    
    Mac/Linux: 

        python3 -m pip install -r requirements.txt


3. **Running**
    You can now run the program from the **/Games** folder with the following command.

    Windows: 

        py app.py
    
    Mac/Linux: 

        python3 app.py

## Getting Started
#### Adding Stars.
In the `website\main\main.py` There is a dictionary that you can add entries to and they will be imported and injected into the app.

#### Tips.
the `app.py` is for debug mode, and the `wsgi.py` is meant for production.  

---