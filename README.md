<div align="center">
  <h1>HBNB - The Console <img src="https://i.imgur.com/elr4ah9.png" width=55 align=center> </h1>
</div>

![AirBnB Clone](https://camo.githubusercontent.com/0abfd1a3534470d279dd6eaca57e0b4b81e23fb77afd81483d470c2f63ab51d3/68747470733a2f2f692e696d6775722e636f6d2f4d5171334142632e706e67)

## Description

This is the first step towards building our first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management. This console will be used to manage the objects of our AirBnB clone project. The console will be a tool to validate and verify the functionality of the project.

## Usage

The console can be run both interactively and non-interactively. The console can be run by executing the following command:

```
./console.py
```

The console can also be run non-interactively by piping a command into the console. For example:

```
echo "help" | ./console.py
```

## Commands

The console supports the following commands:

-   `EOF` - Exits the console
-   `quit` - Exits the console
-   `help` - Displays the help message
-   `create` - Creates a new instance of a class
-   `show` - Displays the string representation of an instance
-   `destroy` - Deletes an instance
-   `all` - Displays all instances of a class
-   `update` - Updates an instance

## Examples

The following are examples of how to use the console:

```
(hbnb) create BaseModel
```

```
(hbnb) show BaseModel 1234-1234-1234
```

```
(hbnb) destroy BaseModel 1234-1234-1234
```

```
(hbnb) all BaseModel
```

```
(hbnb) update BaseModel 1234-1234-1234 name "John Doe"
```

## File Contents

The following are the contents of the project:

-   `console.py` - The console
-   `base_model.py` - The base model class
-   `user.py` - The user class
-   `state.py` - The state class
-   `city.py` - The city class
-   `amenity.py` - The amenity class
-   `place.py` - The place class
-   `review.py` - The review class
-   `__init__.py` - The initialization file
-   `file_storage.py` - The file storage class
-   `tests/` - The directory containing the unit tests
-   `models/` - The directory containing the classes

## Bugs

There are no known bugs at the time of release.

## Authors

-   [Ukeme Edet](https://github.com/Ukeme-Edet)
