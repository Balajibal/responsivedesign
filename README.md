# Design of Responsive Website
## AIM:
To design a responsive website with two break points.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:
### responsivewebsite.html
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>STARC FRUIT GALLERY</title>
</head>

<body>
    <div class="jumbotron jumbotron-fluid" style="background-color: aqua;"></div>
    <div class="container text-center">
        <h1 class="display-1">STARC FRUIT GALLERY</h1>
        <p class="lead">WE SHINE YOUR LIFE AND HEALTH</p>
    </div>
    <div class="container  text-center">
        <div class="col-12"><a href='#'>Home</a>
            <div class="col-12"><a href='#'>Seasonal Fruits</a>
                <div class="col-12"><a href='#'>Organic Fruits</a>
                    <div class="col-12"><a href='#'>Rare fruits</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="row text-center">
            <div class=" col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/img/j21.jpeg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">MANGO</h5>
                    <p class="card-text">RS:50</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/img/j22.jpeg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">GRAPES</h5>
                    <p class="card-text">RS:70</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
            <div class="row text-center"></div>
            <div class="col-12 col-md-3 col-sm-2">
                <img class="card-img-top" src="/static/img/j23.jpeg" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">APPLE</h5>
                    <p class="card-text">price:RS:80 per kg</p>
                    <a href="#" class="btn btn-primary">more info</a>
                </div>
            </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j24.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Banana</h5>
                <p class="card-text">RS:70</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j25.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">JACK FRIUT</h5>
                <p class="card-text">RS: 60</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j26.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">ORANGE</h5>
                <p class="card-text">RS:120</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j27.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">STRAWBERRY</h5>
                <p class="card-text">RS:70</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j28.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">GUAVA</h5>
                <p class="card-text">RS:130</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/blackberry.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">BLACKBERRY</h5>
                <p class="card-text">RS:50</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j30.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">PINEAPPLE</h5>
                <p class="card-text">RS:90</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j31.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">POMEGRANATE</h5>
                <p class="card-text">RS:80</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        <div class="row text-center"></div>
        <div class="col-12 col-md-3 col-sm-2">
            <img class="card-img-top" src="/static/img/j32.jpeg" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">KIWI</h5>
                <p class="card-text">RS:70</p>
                <a href="#" class="btn btn-primary">more info</a>
            </div>
        </div>
        
                </div>
            </div>



        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>
</body>

</html>
```
### Validation Report:
![output](./static/img/e04.png)

## OUTPUT:

![output](./static/img/e01.png)

![output](./static/img/eo2jpeg.jpeg)

![output](./static/img/e03.jpeg)

![output](./static/img/j21.jpeg)









## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the url http://balaji.student.saveetha.in:8000/responsivewebsite