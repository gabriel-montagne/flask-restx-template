# OGRE 

## WIND and SOLAR

### Prerequisites:
- Python 3.9
- [direnv](https://direnv.net/)

### Installation
- Clone the project:
    > git clone git@github.com:Ogre-AI/wind-solar-ref.git
- Change to the repo folder:
    > cd wind-solar-ref
- Install virtual environment:
    > make install
- Activate virtual environment:
    > . .venv/bin/activate
- Exit and reenter repo folder to allow direnv to export environment variables:


### Running
- development mode:
    > make dev       
    Project runs in docker environment and is used by **app-fe** project in development model
    To stop the containers use Ctrl+C and:
    > make stop_dev    
- tests:
    > make test   
- test PEP8:
    > make pep8  
                      
### DB migrations:
- create a new automated revision:
    > flask db migrate -m=_revision-name_
- create a new empty revision:
    > flask db revision
- migrate revision:
    > flask db upgrade
