In this project we are planning to download(i/o bound) and resize(cpu bound) about 10-15 images of high resolution in two different ways: using threading and multiprocessing.
Each type is going to have its own container and one more container will make requests to them to get the information about time it took to download and resize the images.
So the project is going to consist of three parts:
- thread
- process
- result

I'm going to add one part at a time. The init commit will be together with the first part thread.
Just added the second part Process. Start working on result, where I plan to use matplotlib to make a histogram chart out of the results.

Right now you can clone the repo, run docker-compose up command and then visit two addresses: http://0.0.0.0:3010 for multiprocessing page and http://0.0.0.0:1010 for threading. You can also go /data each url and see json data.
Then you can open a new terminal, navigate into this repo and run python result.py to see how fast threading and multiprocessing downloaded and resized the images.

The final step I have to do is to configure the docker-compose file in such a way that result.py will run automatically.

