# Nanodegree-Project1 
## Fresh Tomatoes Movie Trailers
(_This project is part of Udacity's FullStack web development Nanodegree_)
**Fresh Tomatoes Movie Trailers Website** Is a place where you can watch trailers of my favourite movies. To watch a trailer you need to click on _movie poster_ and the trailer for it will pop up right there.


## Includes
This project includes following python files:
- entertainment_center.py
- media.py
- fresh_tomatoes.py


## To add more movies to the website:

If you want to add new movies to this website follow the  steps below
- Goto entertainment_center.py
- Create new instance for Movie class as shown below

```
kingsman = media.Movie("Kingsman: The Golden Circle", <!-- Title for your movie -->
                       "It's James Bond On Laughing Gas.", <!-- Story line for your movie which appears right below the movie poster -->
                       "https://goo.gl/g3gh53",  # NOQA <!-- youtube trailer link for your movie -- >
                       "https://youtu.be/6Nxc-3WpMbg") <!-- poster image for your movie -->
```


## Requirements:

Thou the latest version of Python is _Python 3.6.4._ but since this website has been created in _Python2_ so for this website to run successfully you might need to instal [Python2](https://www.python.org/downloads/release/python-2715/) on your system if you never before installed any version of Python before.

## How To Run This Website:
To run _Fresh Tomatoes Movie Trailer Website_ Follow the steps below:
+ After Downloading and installing **Python** on your system.
+ Search for _IDLE_ from start menu (A GUI of an integrated development environment for Python).
+ Now when you are in Python shell, Goto File -> Open -> select entertainment_center.py -> and open it.
+ Now you will see entertainment_center.py file opened.
+ From inside entertainment_center.py file, **hit** `f5` key or **click on** `Run` and then **click on**  `Run Module`.
+ Now your website should be opened successfully in your web browser.
