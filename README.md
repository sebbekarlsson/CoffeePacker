# CoffeePacker
> Compile and execute Java programs with ease!

### Installing
> Clone down this repository and cd into it.
> execute:

        sudo python3 setup.py install

> python2 should work as well.

### How to use
> First of all, CoffeePacker requires that an 'src' folder with all your .java
> files exists. Not to mention the 'project.json' file which we will talk about
> soon.

> You need a "project.json" file inside your java project directory. It looks
> something like this:

        {
            "libraries":[
                "lib/jar/*",
                "lib/native"
            ],
            "class": "HelloWorld"
        }

> Inside of the "libraries" section, you put all required libraries that the
> project is using.
> The "class" is basically which class that is the starting-point of the
> program.
>
> #### Let's compile!
> cd into your project and execute:

        coffeepacker --path .

> If your "project.json" file is correct, all your code has now been compiled
> into a "bin" folder where you're standing.
> (Don't forget the "." after "--path")
>
> #### Let's Run!
> You can also compile your program and at the same time run it!
> Execute the following instead:

        cofffeepacker --path . --execute true
