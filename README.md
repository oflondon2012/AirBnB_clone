# AirBnB Clone - The Console

![AirBnB Clone - The Console](https://i.imgur.com/3v3v3zV.png)

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
