# HomeGenerator

## Project Details
Home Generator uses Google's OR-Tools CP-SAT solver to generate random tile-based house layouts that adhere to certain constraints. Tiles (such as floor, wall, and door pieces) must adhere to adjacency constraints and other constraints across the entire layout. Tiles and layouts are created with the [Furniture Kit assets by Kenney](https://www.kenney.nl/assets/furniture-kit) and rendered in Unity.

## Platform
Currently the project build is only working for macOS.

## How to Run
We have plans to streamline the process of running the code; for now the process is not super user-friendly and is as follows for macOS with python 3.
1. Setup a pipenv with ortools installed (for CIS 189, just open the project within the pipenv we created for class)
    1. Open the main project folder in terminal
    2. Run `pipenv --three`
    3. Run `pipenv install ortools`
    4. Run `pipenv shell` if you are not in the pipenv
2. Generate a new layout
    1. Run the python file `start.py`: if you are in the root project directory, this will be `python3 python_scripts/start.py`
    2. Follow the command line prompts to choose layout features (this is somewhat limited at the moment)
3. Run HomeGenerator application
    1. If HomeGenerator.app is present in the root project directory, run this application to see the generated layout!
    2. If HomeGenerator.app is not present (not included on GitHub), you can run the `GeneratorScene` in the Unity Editor or create the project build in Unity yourself.
    3. Type cmd+q to exit the application

## Future Plans
We are proud of the project and that we were able to get these multiple technologies working together. In the future we would like to make the process more streamlined. We'd like to be able to get the C# version of OR-Tools working so we can genereate layouts directly in the application, and we'd also like to add more support for constraints such as defining rooms to make the layouts resemble real houses more. We ended up running out of time for this feature and others but hope to tackle them in the future!