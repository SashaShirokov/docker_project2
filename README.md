In this project we are planning to download(i/o bound) and resize(cpu bound) about 10-15 images of high resolution in two different ways: using threading and multiprocessing.
Each type is going to have its own container and one more container will make requests to them to get the information about time it took to download and resize the images.
So the project is going to consist of three parts:
- thread
- process
- result

I'm going to add one part at a time. The init commit will be together with the first part thread.
Just added the second part Process. Start working on result, where I plan to use matplotlib to make a histogram chart out of the results.
