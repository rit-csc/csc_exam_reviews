This is a collection of practice exams for some of the intro-level Computer Science classes at RIT.

Right now, this includes:

- Intro to Computer Science (CSCI-141)
- Computer Science II (CSCI-142)
- Mechanics of Programming (CSCI-243)


### Building
To build the PDFs, you'll need LaTeX, TeXlive-extra, graphviz and PGF/Tikz installed.
You can generate the PDFs by executing ```make```.


### Adding Questions
To add a question to an existing exam, create a new .tex file in the appropriate /questions directory.
In the new .tex file, write the new question as usual.
Then place the solution to the question in an ```answer``` environment.

The answer environment is set up so that it *should* provide enough room for the students to write in their answers.
You can tailor how much space is given with ```\vspace{}```.

Here is an example of what the new question file should look like:

    What's the most exciting feature in Java?
        \begin{answer}
        Trick question: there's nothing exciting about Java.
        \end{answer}

Once that is done, you must add the new question file as input in the actual exam.
To do this, add an ```\item``` at the desired location within the ```enumerate``` environment.
Then include your questions as follows:

	\begin{enumerate}
		...
		\item \input{questions/your_new_question.tex}
		...
	\end{enumerate}

And that's it!


### Setting up a new exam
Use the [new-exam.sh script](new-exam.sh) with arguments: Class name, Exam Name.
The new template will be in the <Class name> directory.

### License
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
