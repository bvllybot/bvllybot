docker build -t bvllycommands -f Dockerfile.commands . &&
docker run -d -v $(pwd):/app --name bvllycommands bvllycommands &&
docker container ls