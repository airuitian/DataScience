#
# This script is used to run jupyter lab on Deep Learning AMI(Amazon Linux)
#

# https://github.com/dunovank/jupyter-themes
# jt -t grade3 -T -N -ofs 11 -f inconsolata -tfs 11 -cellw 75%
jupyter  notebook --no-browser --port=8888 --ip=0.0.0.0 --allow-root --NotebookApp.token='' 


