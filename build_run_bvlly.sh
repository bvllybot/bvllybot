docker build -t bvlly .  &&
docker run -d -v $(pwd):/app --name bvlly bvlly &&
docker containter ls