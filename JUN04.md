# Summary, June 04

Ask most casual programmers for a function that squares a number, and they'll give you this simple implementation of $f(x)=x^2$:

```python
def f(x):
    y = x * x
    return y
```
or, more compactly:
```python
def f(x):
    return x * x
```

We do things a bit *less* casually. Here's a very rigorous implementation of the same function.

```python 
def f(x: int) -> int:
    """Squares a given number.
    
    Input
    -----
    x : int
      number to square 
    
    Returns
    -------
    x*x : int
      the number squared
    """
    return x*x
```
In the code above, everything between the tripple quotes `"""` is a comment. This particular block of comments is called *docstring* and it's meant to be a user manual for the function we write. Comments are ignored by the computer -- they are meant to help programmers understand better how the code works.

Of course we don't need 10 lines of comments to explain how this program works -- this is all for illustration purposes.

Focusing on the first line of the function -- called the *header* -- it's worth discussing some differences between a casual definition like `def f(x):` and ours:

```python 
def f(x: int) -> int:
```

* Both start with the *reserved word* `def` -- short for *define.*

* The first thing after `def` is the name of the function; here it is `f` but it can be any legitimate name, for example `pepperoni`.

* Then things get wildly different. 

  * The casual function has a simple list of parameters, just `(x)`. 
  
  * The more rigorous implementation has something more verbose: `(x: int)`. Both mean the same thing: the function takes one argument that we call `x` -- we could be calling it `mozerrela`. In the rigorous implementation the `: int` part is called a *type hint*. It suggests to users what kind of data we *wish* to pass to the function. Users should be asking the function to compute `f(2)` or `f(43)` not `f(4.3)`. Type hints do not stop a Python program from executing. They are there for quality control. And it's a good habit to learn how to use them.

* After the parameters of the function, the casual implementation ends with the *header delimiter* `:`. The more rigorous implementation has another type hint: `-> int` and then the header delimiter `:`. This second type hint reflects our intention that the function returns an integer number. Again, this is not enforced by Python. Someone can use the rigorous implementation to call `f(2.5)` and the program will return the value `6.25`.

If type hints do not affect the program, why use them? **Because it's professional level coding practice.** By using type hints you elevate your coding to the highest technical standard and that's good, right?