# This application is a calculator using python

# Was not able to automate build and deployment but still did it manually 
docker pull fmoralessandoval/finalproject

# for manual docker build and publish 
docker build -t fmoralessandoval/finalproject .

docker push fmoralessandoval/finalproject  

# to run testing coverage I used commands 
# although i did run into a bug where import error for report module but it is not a module its under coverage
# on my system i could not get just 'coverage report calculator.py test_calculator.py test_integrations' as that #was my original plan
python -m unittest coverage report calculator.py test_calculator.py test_integrations

I am running python 3.10.4 and Docker 20.10.13