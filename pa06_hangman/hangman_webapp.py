"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_methods
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    state['word']=hangman_methods.generate_random_word()
    state['guesses'] = []
    word_so_far = hangman_methods.print_word(state)
    state['word_so_far'] = word_so_far
    print(state)
    return render_template("start.html",state=state)


@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state
    if request.method =='GET':
        return play()

    elif request.method == 'POST':
        letter = request.form['guess']
        guesses = []
        guesses.append(letter)
        guesses= "".join(guesses)
        length =len(state['word'])
        if letter in state['guesses']: # check if letter has already been guessed
            print("you already guessed that.")
            print("please guess again.") # and generate a response to guess again
        elif letter in state['word']: # else check if letter is in word
            print("Yay! The letter is in the word.")
        if length == 0: # then see if the word is complete
            done = True
            print('you won!')
        elif letter not in state['word']: # if letter not in word, then tell them
            print("that letter is not in the word. try again.")
        state['guesses'] += [letter]
        return render_template('play.html',state=state)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
