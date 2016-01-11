# Crappy Product Generator

This code is the end result of a blog post, training a neural network on Amazon's lowest reviewed products and one star reviews. It uses char-rnn and torch-gan to generate text and images, respectively.

## Requirements

You'll need to have working installations of both [char-rnn](https://github.com/karpathy/char-rnn) and [torch-gan](https://github.com/skaae/torch-gan). You'll also need to have Python3 installed, in order to run the script that generates all the outputs you load.

## Usage

The socery.py file loads up all the text based char-rnn generators, and uses them to create a new set of products / reviews / prices. It uses the sample.lua script from the char-rnn repository, and includes the utils directory provided with that code. The sorcery.py assumes you've already trained and cleaned a set of images from the torch-gan separately. Refer to the blog post for the directory / image structure it assumes.

Then, to generate a new list of 50 products:

```bash
$ python3 sorcery.py 50
```

You'll notice that there will be times that the neural network won't generate a cohesive, finished review, and so the loop just keeps trying to generate product reviews until it gets finished.

Once that's done, you can view the generated projects in a web browser. Using Python3:

```bash
$ python3 -m http.server
```

Then, open your web browser to [http://localhost:8000](localhost:8000), and you should be able to see all of your generated products! The sky's the limit!

![gan trained on amazon crappy products](https://raw.githubusercontent.com/burningion/crappy-product-generator/master/images/out.gif)![gan trained on amazon crappy products](https://raw.githubusercontent.com/burningion/crappy-product-generator/master/images/out.gif)![gan trained on amazon crappy products](https://raw.githubusercontent.com/burningion/crappy-product-generator/master/images/out.gif)

## License

MIT
