image=jupyter/tensorflow-notebook
docker run -ti --rm -p 8888:8888 --volume=$(pwd):/home/jovyan/work ${image} jupyter lab 
