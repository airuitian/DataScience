#docker run -ti --rm -p 10000:8888 --volume=$(pwd):/home/jovyan/work jupyter/pyspark-notebook jupyter lab 
docker run --rm -d  -p 10000:8888 --volume=$(pwd):/home/jovyan/work jupyter/pyspark-notebook jupyter lab  --no-browser --port=8888 --ip=0.0.0.0 --allow-root --NotebookApp.token='' 
