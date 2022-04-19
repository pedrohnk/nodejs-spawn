## Execute another programming languages in Nodejs with Spawn method

Spawn is one method of child_process for interact with OS commands.

In this example, I created a Python file to read a CSV File and print the data of file in terminal (stdout).

In the same project, it was build a NodeJS server and inside this file a handler function that i used methods  ``pipeline from stream`` and ``createWriteStream from fs/promises`` for create a new CSV file from data that was printed on terminal by Python file (stdout).

In index.js, was created a function called ```requestPython``` and i've used ```spawn``` method to interact with OS commands and run my Python File with my local server.


## How to execute:

After cloning my code, its very simple:

Split two terminals and in one terminal, execute ```node server.js``` and up your local server.


```(if you need to change parameters, go to index.js file and change it!)```

In another terminal, execute ```node index.js ``` and thats it, You executed a Python file inside a NodeJS file!