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

        coffeepacker --path . --execute true

> #### Exporting
> You can also export the execution to an execution file, so that you won't
> need to run coffeepacker again.
> Use the "--export true" attribution like this:

        coffeepacker --path . --executre true --export true

> This will execute your java and and the same time generate an executable
> "execute.sh" file that you can run later. The cool thing is, "execute.sh"
> does not rely on coffeepacker in any way, so you can send everything to a
> friend and they won't even need coffeepacker!

        bash execute.sh

> Vola!
