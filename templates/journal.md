# Kelly's Technical Journal

## Week Two (1/30 to 2/6)

This week, I reminded myself that I'm likely to forget what we learn in class if I don't practice it every day. So, I took a few minutes every morning when I first logged on to review the command line, navigating around my computer.

Hour 1: I spread this hour over the course of the week, reviewing the basic command line commands of pwd, cd (with specific directory names, / , and ~), ls, and the handy tab and up arrow shortcuts every day, just so they became habit.

Hours 2 and 3: Learned new command line commands using the "Learn Python the Hard Way" appendix. Mkdir (including directory names with spaces and nested directories), rmdir, cd with the relative up (../), cp, mv, less, cat. All made tons of sense. Tried pushd and popd. I need practice with it. I get it intellectually, but not deeply, as I get the other commands so far. Same with recursive commands.

Hours 4 and 5: Played around with Git, using the resource Patrick gave us (so, Virtual Studio Code and checking to see that I had Git still from the DH Field Kit). Did a little markup in Virtual Studio Code. Tried the challenges and made up some of my own.

Hours 6: Reviewed everything to see what I could do from memory and what needed extra practice. Getting faster, which feels good. Still ignoring pushd and popd. Often forgetting to push files to my Github repository.

Hour 7ish: Getting to Carnegie Hall: practice, practice, practice


## Week Three (2/7 to 2/12)

Overall: This week was great fun, aside from a git error that had me banging my head against a wall for quite some time. Exploring python was pretty thrilling, especially as I learned some tricks to coding more efficiently (such as using %s to insert strings into strings rather than "" + x + ""). I created a few programs that used user input in some really basic ways--evaluating them with elif statements. I'm continuing to add comments to my work after playing, just to review and try to make concepts stick. 



<font style="color:pink;">Hour 1+</font>: As was the case last week, I spread this hour over the course of the week, reviewing the basic and new command line commands, VS Code, and the git commit and push processes. Even played around with some HTML in markdown (see red text below).

Hour 2: Installed Anaconda and began the Python tutorial on the syllabus to the first three exercises. Wonderered if I should heed the author's constant plea not to use Python 3, which came with the Anaconda download. As I played, I was reminded of how much proofreading goes into programming. AND, the difference between an expression to be solved (5 + 2) and one to be evaluated as true or false (5 > 2) is significant, as is every single keystroke.

Hours 3, 4, and 5: Played around the with program in exercise 3 to satisfy my curiosity. Did exercise 4 and 5 on creating variables to hold strings, numbers, and expressions. Errors were mostly typos. Had fun with exercise 6 learning how to use the %r, %d, and %s. Did exercise 7, which generated a question below. I came up with a work-around, but one of my goals is to write lean code, so I'd love to know how to concatenate print lines as simply as the author did (with a ,). The free tutorial ends at exercise 8.

Hour 6: AARRRRRGGGHHHH!!! Thought I'd just practice my basics by git commiting my new python files (using -a) and pushing them to git hub. Kept getting a swap error message. Tried everything to solve it: reopening termnal, resaving my docs, renaming one of my files that had a dash in the file name, quiting VS Code, uploading files one at a time, looking up the error on the internet, trying some of the suggestions to remove the file via the error path. THEN, I took time to read the *entire* error message. I had just forgotten to include the -m message describing the commit. Good Lord!

Hour 7: Found a bit on defining functions on the web and tried some. Very cool. Tried the second source that Patrick shared and found it fascinating. Tried some programs that stored user input in a variable to be printed out in a responsive string. Terminal prompts you to save the back and forth!

Hour 8 and a little: Using the wiki lessons Patrick linked on the syllabus, I learned a little about getting user input and how to think through formats. So fun! I continued annotating my programs as I had been prompted in the "Learn Python the Hard Way" exercises, and it really helped me think through the why behind the code, so I'll keep that up. (It may help me with my goal of programming cleanly, since I've noticed it gives me the time and processing space to think of and try alternatives.) 

Hour 9+: Challenged myself to create a new program that required user input and manipulated it in different ways, including amassing data from the user, and then providing some conversational response incorporating it and comparing it to mine. Poked around for the ability to provide pauses between print lines and found "import sleep" and "time.sleep(sec)" where sec is the number of seconds (or milliseconds if you input a decimal less than 1) that the program will wait before executing the next line, which, in my case, was another line of dialogue. It's easy to see how this function could provide a pacing mechanism for a program that is text-based play, like a Twine or RPG game.

Hour 10: Continued the wiki exercises to learn about the five fundamentals of python. Played with slicing strings into substrings, making and messing with lists. Stopped at Tuples, as my brain was getting quite full. Quickly previewed the other topics for upcoming class: Boolean logic, conditionals. Did not investigate or play with iteration.

Hour 11: After a day off, practiced python in termal, including variable use, basic math operations, rounding (new!), and list manipulation 



## Week Four (2/13 to 2/20)

Overall: The work we did in class made me eager to explore lists futher. I'd been trying to create a program to mimic a Starbucks receipt, and lists seemed to be the key. Appending user input to lists via a loop made it work pretty well. Switched gears to preview next week's material and loved customizing web pages. The reading really helped me frame my HTML and CSS tinkering as a chance to increase accessibility through consistent, thoughtful coding.

Hour 1: Added comments to talk myself through the hello.py file we created in class. Practiced (in postclass_practice.py) using three single quotes to extend the print command across several lines, using a for loop to print list items. Included in my program some of the techniques I found on my own last week: using %s to insert a variable string within an invariable string, appending a list with user input. Really fun. Continued to try to imitate some of the code that I think is behind a Starbucks receipt I got last week. Was less successful there.

Hour 2: Got the Starbucks program to work! Limited functionality, as it just asks the user what they want to order over and over and then prints the order when they are done. Took me awhile to figure out that a while loop would allow the user to add infinite items. So fun. Annotated my code to solify my understanding.

Hour 3: Added a random feature to print at the bottom of the "receipt" a send-off. Tried unsuccessfully to include a string in those random message strings. Answered a question I've been wondering about: does it matter if I choose to use single quotes or double quotes around strings. My instinct was to use doubles, but singles take one fewer keystroke. However, my thanks strings included contractions, so I had to use doubles. (Technically, I suppose I could try a " in the contraction, but since one of my goals is to be effcient, and I type quickly and automatically, I will lose less time if I just stick to "" for strings.) 

Hour 4: Updated my postclass_practice.py document to include a while loop that prompts the user to name as many poets as they can, appending it to a list of poets. The program then gets the length of the list (minus the prepopulated items) and uses an if, elif series of conditionals to provide feedback on how many poets the user could name. This took longer than it sounds because I wrongfully thought that len() would correspond to the numbering of items in a list, which starts with 0. So, I had an if number <=0 line if the user couldn't name any additional poets, but I needed to change it to if number <=1. It took me awhile to figure that out.

Hours 5 & 6: After doing the reading (which I am not including in these hours, of course), I decided to preview next week's content on HTML and CSS with a real eye toward accessibility. It's one of my course goals anyway, as is understanding CSS with less of a tinkerer's mindset. I know a little HTML, so I am already kicking myself for not getting how important it is to include alt tags. Did the first 9 chapters of the w3schools tutorial (see my Preview.html doc in the HTML and CSS folders). Highlighted in orange in my notes tags or techniques that would clearly impact accessibility, such as using headings just for headings (rather than for emphasis) to create an apt page outline or using relative font sizes rather than fixed ones.

Hour 7: Practiced as much HTML as I could without looking at my notes. Accidentally found the awesome color prompts and color picker in VS Code to choose background and font colors. Then did the next four chapters in w3schools, playing with formatting, quotations, comments, and colors. Saved CSS for the next day, as my brain was fried.

Hour 8: Did a quick python refresher in terminal, creating lists and playing with them, running python programs I created, and quitting and clearing. Continued the HTML tutorial reading and practicing the HTML CSS, Links, and half of the Images sections. I see some issues of responsive design here--specifying body padding, for example, in percents rather than pixels, and being sure to set image sizes to avoid browser or stylesheet overrides. I got stuck on a couple of items and never figured out why my image link's border could not be overridden by the border:0 style attribute.

Hour 9: Did 43 of the 90 exercises (just questions really) on W3schools for practice. 





<font style="color:blue;">**Questions for Patrick**</font>

- While html tags seem to work in VS Code, they don't seem to work when uploaded to git hub. Thoughts?
- What do you call using %d or %s in a string? (I'd just like to know how to talk about what I know how to do.)
- In exercise 7, the author used a comma after the first of two print commands to concatenate them. It doesn't work in Python 3 (and I tried the comma inside and out of the parens). Instead, I have to add a third print line that explicitly concatenates them. Thoughts?
- The first time I ran a program with user input, Terminal prompted me to save the output. It did not on subsequent user-input programs. Do you know why?



