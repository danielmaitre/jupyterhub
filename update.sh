images=$(docker ps -a | grep -o -e 'jupyter-.*')
for i in $images; do
    echo updating $i
    docker run --volumes-from=$i update
done
