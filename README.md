Fuckbrain - The Reverse Brainfucking
===========

I was learning *brainfuck*, an esoteric programming language which only accepts the following characters: `+-><[],.`.

Basically, it's a fairly simple language. It can write ASCII characters to stdout by using `.`, read from stdin by `,`, other characters handle those computatoional stuff. To learn it, I suggest [Learn brainfuck in Y minutes](https://learnxinyminutes.com/docs/brainfuck/).

Apparently, it's not an easy job to write a piece of brainfuck code, and it hurts. So I found [this](https://copy.sh/brainfuck/text.html), a text-to-brainfuck code generator, which makes life easier.

The code generator application was written in JavaScript, but ported from Java, [here](http://codegolf.stackexchange.com/a/5440/3428) is the original Java code. I came up with an idea of building a Jupyter kernel for it, named it "fuckbrain". Basically, you enter some text, and it'll spit out some brainfuck code that you won't understand.

Usage
-----
You can use the kernel with any Jupyter frontends, including console, qtconsole and notebook.  
For console, use `jupyter console --kernel fuckbrain` to run a Jupyter Console with fuckbrain kernel.  
For notebook users, select "Fuckbrain" kernel when you create a new notebook, then you'll have it.

Type in any text you want into the code cell, then execute it, you'll see some brainfuck code in the output, that's the code which outputs the text you've entered.

There's one magic command in this kernel that you can use: `%%beautiful`. Enter `%%beautiful` in the beginning of code cell, then type in any text you want after that, you'll see the output code with character-to-code mapping comments (oh by the way, any letters except `+-><[],.` are ignored).

Installation
------------

### Install Package
Since the package hasn't submitted to PyPI yet, you'll have to clone the source and run `python setup.py install`, or use `pip install -e git+https://github.com/adrianliaw/fuckbrain.git`.

### Install Jupyter Kernel
After installing package, run `python -m fuckbrain install`, then you'll see the "Fuckbrain" kernel option showing up in your kernel list.