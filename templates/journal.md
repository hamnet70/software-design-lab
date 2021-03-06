# Kelly's Technical Journal

## Week Two (1/30 to 2/6)

Overall: This week, I reminded myself that I'm likely to forget what we learn in class if I don't practice it every day. So, I took a few minutes every morning when I first logged on to review the command line, navigating around my computer.

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


## Week Five (2/21 to 2/27)

Overall: I tried this week to balance review (terminal, python), deeper exploration (html, css), and preview (bootstrap). I'm starting to see the pyramid relationship between the strong, unmistakable base of html, the quirkier css, and (because some of the w3schools exercises included it) the far more error-prone javascript. Bootstrap is really cool, and I can see how it jumpstarts responsive websites already, but I also see how tricky it is (at least for me at this early stage) to design well, with blocks aligning. The mini-boostrap page I created looks great stacked, but looks terrible full screen! 

Hour 1: Reviewed the HTML and CSS work from class, adding comments to what we did to refresh my memory. Learned that CSS sheets use /* and */ for comments. Tried setting up a new site on the Oscars from scratch. Did well on the HMTL, did abysmally on the CSS stylesheet.

Hour 2: Given the trouble with CSS, I took the Khan Academy lessons on CSS. HUGE help. The most important take-away is that the CSS that you can put inside a style tag on an individual webpage is the same code you put in a style sheet. It's just that the former just treats the content on that page, and the latter can apply to multiple pages. (I don't know why I thought the syntax was different.) Got some good practice with ids, and restyled my Oscars website stylesheet from scratch, including ids in my bulleted lists to single out my personal favorites. Learned about classes. (Interestingly, the narrator of the Khan lessons said that every id had to be unique, and that you should use classes for multiple instances of the same id, but I found that multiple ids worked anyway. Still, I'll use classes, so I can chip away at my goal of being a lean programmer.)

Hour 3: Trying to keep my fragile, new python skills sharp, I created a python script to calculate hotel bills based on user input on the type of room they had and the length of their stay. Got stuck for a bit on how to distinguish user data as a string or a float decimal. Because the decimal was part of a multi-pronged formula, it took me awhile to realize that not only was my data type off, but I was missing a parenthesis. Turning half the program into comments while I debugged line by line really helped.

Hour 4: Now with a greater handle on CSS from Khan Academy, I returned to the W3Schools tutorials, doing the first six lessons and exercises. In addition to marking notes in orange that address accessibility, I have started marking notes in green that chip away at another of my class goals: coding efficiently. In these lessons, for example, I learned two ways to code CSS more efficiently: 1) grouping selectors that get the same treatment, and 2) using background shorthand to cover all of the properties of the background with one line.

Hour 5: Continued the CSS W3Schools tutorial doing the next six lessons and their exercises. Again, found shorthand code for a host of declarations. Played with borders, margins, padding, height/widgth, and outlining. Learned the box model, which helped me visualize sections of web pages. Applied some of the techniques to my Oscars page. It looks garish, but displays a lot of CSS!

Hour 6: Started to preview Bootstrap using W3Schools. Cool, but I realized that I hadn't learned about divisions and tables in HTML yet, and both showed up immediately (along with classes), so I headed back to the HTML tutorial. Played with tables and made a kinda cool one for my hideous Oscars website, with alternating background colors for every even row.

Hour 7: Returned to the HTML lessons to tackle lists and, more importantly, divisions and classes/ids. Here's where I really started to see how a website can start to be designed, thinking in terms of blocks of information that get styled in ways that cue the user. Also checked out iframes (very cool). I transferred all the lessons to my now super-garish Oscars page. (Wasn't able to embed in an iframe external webpages, but was able to embed my own--perhaps because my site is currently still local?)

Hour 8: Went back to preview bootstrap with some success. Created a new folder to house my bootstrap play. Created a simple site with one banner container, three 4-col span columns set to default for a tablet, and added a table. Only the table class worked. Table-striped and table-hover did not.

First half of hour 9: Challenged myself in python again to update my Starbucks receipt program to mimic the sticker that was on my coffee. Was not successful, though I made the program a little more elegant with delayed responses (thanks to time.sleep(1)) and presenting a number of total items ordered to the user by getting the length of the list. Learned the hard way that variables in python can't have dashes, so swapped to underscores. (Id names in CSS can, though, so I'd gotten in a bad habit!)



## Week Six (2/28 to 3/6)

Overall: This week, I explored Jekyll a little, and in doing so, realized I was becoming a bit of a make-it-do-something-cool junkie. After all, in just six weeks, we've been introduced to command line, markdown, python, HTML (which I knew a little of), CSS, and now liquid. And even though I've practiced every week, I've been practicing what I <i>already</i> know rather than deepening and testing my programming agility. So, this week brought back to me the line of Shakespeare's Friar Lawrence who says something like, "Wise and slow, they stumble that run fast."

Hour 1: Intrigued by Jekyll, I found a series of video tutorials by Mike Dane and watched the first ten. They assumed the Jekyll themes, not the blank site we created, so I didn't get to try much. Still--very helpful, as the videos explained the importance of naming post files YYYY-MM-DD-title.md and how Jekyll translates that into subfolders. They also demystified the config file that others in class mentioned they had accidentally downloaded by creating a themed Jekyll site.

Hours 2 and 3: Found some liquid code similar to what Patrick did in class--a for loop that, for every post in the posts folder, provided a link to that post. It worked. Watched five more tutorials from Mike Dane about getting Jekyll themes and customizing them, creating and using includes, and creating variables. Practiced creating my own theme and displaying variables such as the post title and author. Took me forever, but I got it, though I never managed to create a customized layout that referenced my stylesheet. Learned about passing variables to includes, though!

Hours 4 and 5: Decided to review python, and found a real weakness in my manipulation of variable types. Did some digging to learn the term "casting," which I guess I've done in the past, but didn't truly understand. I went to w3schools to practice working with data types and lists, doing the exercises provided. Then, I found practicepython.org (really), and found a host of beginner challenges and did 6 of the first 7. Looking at their solutions helped me see where I was over coding and where I was coding leanly, which is one of my course goals, so that was helpful. In fact, I'm most proud of my list-compare.py program, which compared two lists and printed the shared, nonredundant elements, which I managed in just seven lines of code. (Maybe there's a shorter way, but it felt pretty lean. There is no solution posted for that one, so I can't check.) I learned that I need, now, to focus on list comprehension for next time.

Hour 6: Continued to work through the extra python exercises, creating a truly lame (but working!) two-player rock-paper-scissors game, then adapted it so the user can play against the computer. Worked on a number guessing game and missed some obvious errors, like a missing end parenthesis that took forever to find. Then, realized that my loop included the randomizer, so every guess, the number changed. Still working on it. I refuse to look at the solution!

Hour 7: Victory! After lots of truly stupid mistakes, I not only got the number guessing game to work, but I extended the range (so easy with the list(range(x, y)) feature), tracked and printed the number of guesses, and gave the option of continuing indefinitely. I'm learning that reading the code out loud to myself really helps. For example, I had the random number chosen outside of the "play again" loop, so the number was the same every time--something I didn't notice when the range was 1 to 9 and I was tweaking after each try, but it was painfully obvious when the range was 1 to 100 and the first three "random" numbers were 20. I'm eager to get better at predicting. My code is staying pretty lean, but when I looked at the solution the site proposes (after making my own working version), I do see that Boolean logic could have combined a few of my if and elif statements.

Hour 8: Worked on a very clunky python program to determin if a user-provided number was a prime number. Very inelegant, unlean coding, and I continue to make really stupid data type assumptions and other little errors. I am getting better, though, at taking the time to read and think through the error messages, which is helping. I looked at a possible solution, which was far more thorough (mine just checked if there was at least one more factor other than 1 and the number) using list comprehension, which I clearly need to coninute to...you know...comprehend.

Hour 9ish: Worked on a python program to print the first and last items of a given list. I challenged myself and allowed the user to add as many items to the list as she cared to. It worked with far less troubleshooting than I've needed in the past, which is good, because it required list comprehension. 


## Week Seven (3/7 to 3/13)

Overall: 

Hour 1: I loved working with more complex functions in class this week, so I wanted to practice. I found a few challenges on practicepython.com that included the keyword of working with functions. My first was to create a program that displayed as many numbers in the Fibonacci sequence that they desired--really fun, as it required the list comprehension I'd been working on last week in addition to thinking in terms of functions. The hardest part was conceptualizing the function--the "Fibonacci-fying" machine that could extract the last two numbers in a list of unknown size to add them together and then append them to the list. Great fun. The toughest part was figuring out what to do if they asked for 0 numbers, but I learned that you code a function to return a string, so I returned, "Then why'd you run this program?" :) Better yet, my solution was shorter than either of the two offered on the solutions page (minus my comments to myself), so I feel as though I'm continuing to chip away at my goal to code efficiently. (And yes, I know that efficeint != short.)

Hour 2: I returned to our "Magic Nine Ball" program (which I just called 8ball). I edited it so that the user posed the question (as our "client" had originally indicated), which was easy. But, I had trouble formatting that user-generated question with our html function, finally figuring out (and remembering Patrick's explanation that you can call functions that call functions or write functions that write functiosn), I realized I needed: print(format_answer(answer_question(input("Ask a question.  ")))). The line runs a function with the argument of another called function. Cool. I also created a program from pythonpractice.org that reverses the order of a user-provided multi-word string.

Hour 3: I continued python lessons at w3schools, learning about tuples, sets, and, most awesomely, dictionaries, doing all of the tiny exercises to practice. I made a birthdays program that stores a dictioanry of birthdays, allows the user to add birthdays, retrieve them, or exit. It works really well! It also works hard (unlike some of my other programs) to anticipate and address user errors.

Hour 4: Refreshed and learned new things from w3schools about conditionals, loops, and functions. Found some lean coding approches, such as putting single-line conditionals on the same line. Struggled with the concept of lambda functions, so I'll need practical experience there. Finished all the python exercises they had and took the simple but satisfying 25-question quiz.

Hour 5: Took some more online python quizzes and did fairly well. Tried to learn about classes in python, but realized my brain was too full of new things. Looked at pythonpractice.org's solution for the reverse string program and learned a new method for lists: " ".join(list_name)

Hour 6: Got way ahead of myself trying to play around with excel data saved in csv format. (Seemed an easy fit for dictionaries.) Got home to realize that new homework had been put up over the weekend--what I really need, which is to figure out when/how to use functions and when not to. Replicated the imperative and functional programs. I don't see how the first function is used, since no unwanted characters list is defined. Had some small and stupid glitches, like indentation errors, typos, and missed parentheticals. Argh. (Do these start to go away???)

Hour 7: Classes became a bit of a leap for me, and it had been on w3 schools, so I found this handy video: https://www.youtube.com/watch?v=ZDa-Z5JzLYM. After watching it, I created a program that defined a "student" class, with methods and attributes. Student attributes included first and last names, section, and emails. And the method of being able to print the full name with a space in between. Very helpful video, as I finally understand the presence of the world "self" and the __init__.

Hour 8: After a night's sleep, reviewed my program defining the "student" class of objects, using comments to explain the seconds of the cass, its methods, and its attributes. I watched the second tutorial on class variables and instance variables and found that inordinately helpful. Applied what I saw to my student program, adding a gpa, a class variable for extra credit work, and a method for calculating the new gpa if a student did extra credit. I also included a class variable "total" that increments every time a new instance of the class "student" is initiated. As always--stupid errors, such as not recognizing gpa as a float value and spelling students without the first t in only one instance of my program. I also reviewed the function and object-oriented vocabulary to preview this week's class.

Hour 9 (well, almost): Looking for more ideas for ways to use challenges, I found the Python Practice Book online and reviewed their bank account program. I recreated it (mostly without looking), with a few extra twists. In addition to creating a BankAccount class with an initial balance value of 0 and the methods for withdrawal and deposit, I added a name attribute and included personalized overdraft messages and fees.



## Week Eight (3/14 to 3/20)

Overall: I think this week, starting in hour six, I reached a significant milestone: I am now spending more time thinking than coding. I am starting to see how functions can allow programs to scale far bigger and more flexibly than the imperative method that feels more comfortable to me. And, more exciting still, I can also see how classes are useful (though without being able to read and write to a database, my vision outstrips my current capacity). I'm certainly pacing a lot more and I'm jotting outlines down on paper. (I'm considering smoking a pipe, growing a beard to stroke, or writing on my windows John Nash style.) I'm currently working on a simple theater-ticketing program, with two iterations--one that relies solely on functions and one that uses classes and subclasses. In this case, the OOP iteration is seeming the best fit. Very fun.

Hour 1: Played with our Cafe program a bit to try to create pricing and bill-totalling functionality by turning our menu list into a dictionary with price values. Realized that the architecture of programs is tricky: since our menu existed only within the is_on_menu function, I couldn't pull the prices from the dictionary into another function. However, I think I will return to it and try creating a function that takes a function as its argument. I also rewatched the video on class variables and then reviewed the comments I had created in my student database program that took classes. I updated the program to include the formatting function (f...{}) that we learned this week. Watched another video by the same guy on class methods.

Hour 2: Ooh! While watching the class methods video I learned that you can define multiple variables at once. What!?!? Wrote a tiny program (called string_split in my python folder) to prove it to myself--one that took a three-term hyphenated string and broke it up into three variables. This seems to be what Marie was looking for with the file names. Talk about sleek code! Got ahead of myself by thinking I could read csv files. I figured out how to read and print them via w3schools, but then realized there's a whole nother set of steps to read files line by line. So, knowing that Cory Schafer had a tutorial on that coming up, I went back to his videos. 

Hour 3: Through continued videos, I learned about static methods and created a quick program to see if a given day was a workday or a weekend. (Worked like a charm and allowed me to add a timestamp to our cafe program!) I ventured into subclasses and created a subclass of "academic workshop" students in my playing-with-classes.py program whose objects received additional extra credit when the class method of extra credit was called for. Worked great! Note to self: rewatch the Python OOP Tutorial 4 on Inheritance.

Hour 4: Rewatched the Cory Schafer video on inheritance and then commented out my program where I used the material, just to make sure I could recall what every component meant. I found that simple functions, like running up a student counter, continue to work in the inherited init method. Sweet. Started to watch the tutorial on special methods, but realized it might be a little beyond what I need right now.

Hour 5: Watched the Schafer video on File Objects. The videos are getting longer (this one is 25 minutes), but the concepts are now starting to feel truly real-world. I used the tutorial to create a file_play.py document that reads the contents of a file and copies it to another. The video highlighted parsing files in chunks to save memory--another lean-coding technique that can help me with two of my course goals: coding efficiently and being more aware of accessibility, as big memory is a luxury. The video also covered working in binary to parse image files. I am eager, now, to add roster-generation functionality to my playing-with-classes program that created a student class.

Hour 6: In an attempt to stretch (that is to say, break) me, I decided to see what I could do with a big idea: to create a program that books theater tickets. I spent a half-hour just trying to imagine the components--to flesh out the architecture of such a program. My big hurdle at this stage in our course is in understanding the upsides and downsides to the paradigm choice, at that stumped me here. I could totally imagine a class-based program, with attributes (level, seat, row, price). I could also imagine purely functions-based program with "is_available," "purchase," and "suggest_alternatives." Sadly, because I don't know enough yet about working with files, I settled for building the program in small iterative chunks first, to see where functions might save me time. The upside to this sad approach? I found that I knew more than I thought, such as knowing to evaluate characters in a string (x[0]) to determine if the seat was a "premium" seat or not. 

Hour 7: Reworked the nascent theater program creating two small functions: one that generates the possible seats in a user-defined, one-story theater (levels to come later), and one that determines if any given seat is a "premium" seat (first two rows or any aisle seat). A lot less trial and error than I'd imagined. Still a lot of head-banging as I wrote = instead of == in one Boolean phrase and as I continue to forget about evaluating data types. 

Hour 8: Tried to convert my functions-based simple theater seating program to a class-based one, so that I could have a class of seats with subclasses for different seating tiers and pricing. Struggled with the implementation, though I was able to instantiate an orchestra and mezzanine seat. I'm floundering a bit with what pieces of data should be variables and what should be attributes.

Hours 9 and 10: Eager to understand how to instantiate objects from user-driven parameters, I looked for real-world examples of object instantiation and found https://realpython.com/python3-object-oriented-programming/. While it didn't answer my question, it certainly helped me move my program forward. I realized that I had mis-conceptualized my base class as an orchestra seat. Instead, I changed it to seats and included the subclasses of orchestra, mezzanine and balcony. That change allowed me to really think about what attributes and methods should be true for any seat in a theater, which helped me radically streamline my code (one of my goals!). So, in addition to the attributes of seat_no, row, and location, and in addition to the subclass variables of price and name, I created a class method for marking seats as available and purchased (including returning tickets). I am also still very much in the thinking stage of how I can create the parameters for each level of possible row and seat count. Next go-round, I'll try to build in that functionality myself before asking for those limits from the user.


## Week Nine (3/21 to 3/27)

Overall: For the first time in this course, I found myself completely lost this week. Part of that was because I was juggling family obligations and my technical hours, but most of it was because I radically misunderstood the big-picture architecture of SQL. In lab hour 4, I finally figured out the root of my misconception, and SQL started not only to make real sense but to promise significant power. 

Hour 1: Returning to my theater program, I began to work on the ability for the user to specify the seating capacity of each level of her theater, wishing I knew how to make a small program to create the possible seats and then my class-oriented program to assign those possible seats to users who purchased them. Fortunately, I looked at what was on deck for this upcoming week, SQL, and it seemed to be the missing link (literally and figuratively). 

Hour 2: Dove into SQL. Oy. For the first time in this course, my brain (and Zed Shaw!) let me down. I couldn't deduce the logic of the language, and it took me a while to simply figure out where I was working. Surprisingly, the Shaw didn't cover initially some of the essentials of the big picture of SQL -- for example, it seems as though the .db files I create are the architecture, or ".schema," of the database, but that ultimately those files get translated to a .sql file. Still not really sure what I mean by that, but two files seem to be required. So far, I have created a few databases and have learned to use the insert command to add data. I've also explored the five data types (or, storage types) for SQL, and am wondering if BLOB can hold images?

Hour 3: Don't laugh, but it took me about a half hour to figure out in GitHub how to add you as a collaborator. I also found that I had to reread all the Shaw introductory material on SQL. I'm finding it really hard to work with data that I can't "see," and, frustratingly, he continues to omit important practice steps such as how to get back into a database and the difference between the .db and .sql files. (I think the former stores the data and the other "runs" the executable action you've prompted in SQLite3???)

Hour 4: Turns out I am an idiot. After my hour+ of frustration with first few chapters of the Zed Shaw book, I decided to watch the videos. I had no idea that all the coding was done in a text editor. Doh! I thought it was all done in bash. REALLY embarassing. 

Hour 5: SQL is going very slowly. While I'm thrilled, now, that I have the easy editable environment of the text editor, I still find it very hard not to see the data in the database other than through selecting it in terninal. However, I can see how incredibly searchable data gets, just through the select command and some boolean operators or sub-selections. Further, the table output in terminal (when formatted with -column -headings) throws me back to printouts I'd seen from decades back--not of my work, but here and there. Cool. I've made it to exercise 7, finally, but I am still relying a bit too heavily on the videos to surpass my weak understanding of the slowly emerging big picture. 

Note: I traveled to help my family this week, so I only managed half of my technical hours. I will make it up over the remaining weeks, indicating them with "Make-Up" before the hour.

Make-up Hour 6: Had a jolt of energy after our class, so I decided to see if I could build a sql database from memory. Did pretty well, creating (no surprise) a database with a table of a few of my students (id, first and last name, and section), a smattering of assignments (id, date due, title, possible points), and what I think Shaw called a "relation" table linking the kid to the assignment AND providing the points possible. I was able to make it run after fixing some syntax errors and learned that thinking through the title of a table really matters. (For example, I called the first table students, plural, and then kept trying to retrieve student.id or student.name, thinking only of a singular student. Argh.) I was able to CR of CRUD pretty well, which felt pretty good, pulling, for example, the student name, assignment title, and grade of any piece of work earning above a 65. 

Make-up Hour 7 and 8: (Occurred 4/28, so I am now well into my client project.) Applied the new homepage CSS to the second image library of NYC pics, updated the picture links (what a fool I was to create this before we decided on a homepage design). Created a new page (so easy with CSS!) for Accessibility and Safety info for Sabina's review. Skype call with Quinn and then Quinn and Sabina.

Make-up Hour 9: Made corrections to the pages based on our Skype call: adding an explicit home button, changing the Why This Class to Why DH button. 
What a total pain in the ass that turned out to be, since Sabina and Quinn wanted to go with buttons rather than a horizontal nav bar.

Make-up Hour 10: Created the Peek at the Code page and had fun adding comments and figuring out why the < pre > tags wouldn't work to render the html. Exciting to learn about & l t ; work around. Uploaded all to the live site for review.


## Week Ten (3/28 to 4/3)

Overall: Dove into Flask this week. Loved seeing the fuctionality. It's easy to connect how the small projects I was led to create could scale to the types of web apps I use regularly. I did find it incredibly hard to troubleshoot, since the tutorial I started with relied on a "just type it and you'll learn about it later" approach. On a side note, I was thrilled to find that my brain must have been processing SQL in the background. I found creating my own database even after over a week's gap, seemed wonderfully logical.

Hour 1: Dove into Flask using Corey Schafer's intro video. Was able to successfully run and alter the simple sample code Flask provides on its website. (See the FlaskBlog folder for the work.) Really enjoyed the speed of generating the pages, though I'll admit that I am simply trusting (without understanding) code phrases such as __name__ and @app... Learned a little about local hosting and running a server in debugging mode. 

Hour 2: Continued to work building in greater complexity with templates. Nice to see that our HTML and CSS practice will still be useful here. Played around with the Jinja2 code that is like liquid in Jekyll to create loops to display blog posts. Watched Corey Schafer's second video (a half hour long), taking notes and replicating his actions. 

Hour 3: Continued with Flask to build in forms. I'm continuing to do more dictation than actual learning, since much of what I'm doing is importing capabilities rather than creating them myself. Further, Corey Schafer (whose videos I've enjoyed until now) keeps saying that I don't have to understand a given concept (like a secret key), but I should just put it in for now. Still, it is satisfying to see the forms and the CSS working smoothly, and I can at least figure out on my own how to create slightly modified pages.

Hour 4: More Flask. Continued to work through the forms tutorial, creating a registration and login page, adding validation and error messages. All is well except for ONE DAMN THING, which I can't figure out. Registration is not successful. I get "invalid field name 'Password' when I try to register. All other fields work great--cuing entry errors. And, I can't figure it out, even though I've compared my code LINE BY LINE to Schafer's (he posts the code for his projects in a GitHub repository). Aaaaaaaaaaaaaaaaaaaaaaargh! Zounds! Egad! This is madness! (No, this is Sparta.)

Hour 5: Still trouble shooting, for the love of God. After a good night's sleep I went through Schafer's code again, line by line. EUREKA!!! I had capitalized the variable password in one instance in the dang code. Geesh.

Hour 6: Started to watch the next Schafer video about setting up a SQLAlchemy database for the site, but ultimately decided that I was getting in over my head without understanding the foundations of Flask. (Though I will say that I'm starting to be able to predict structures a little ahead of the tutorials.) Started the Programming Historian tutorial on building a distant reading API. LOVED it! Much simpler, and I appreciate the line-by-line explanations after each bit of additional functionality. Embarassed that I hadn't realized that I could make a list of dictionaries, and that dictionaries can represent data from a single item. 

Hour 7: Continued working with the Programming Historian tutorial and looked into RESTful architecture a little. Super helpful to think through designing with an eye toward expansion and maintenance of a resource--will help me with my goal to code leanly. I'm thrilled to see the SQL get syntax that I learned last week.

Hour 8: Finished the tutorial. And hey! Patrick! You are the programming historian? Go you! Moved to another Patrick resource -- the "Prototype Twitter Clone."  Did the reading there (and think the pun of Chirper is hilarious), but aside from the three text pages, I didn't find tutorial text to run me through the process. Clearly, I'm missing something obvious. So, I went back to my sci-fi first-sentence API to review and reinforce what I learned. 

Hour 9: Tried to apply what I'd learned by creating from scratch a web app that allows users to search a database of American presidents. Successfully (though peeking at old code) created the .sql code and generated the database. Successfully queried the database in terminal with simple commands such as SELECT * from presidents. Was not successful with the .py code, though I mimicked line-by-line the successful sci-fi archive. Tried troubleshooting by chaning file names (for example, I didn't know if the folder had to be named api and if the python script had to be titled api.py), but no manipulation of those variables ran the app. I can think of only two differences between my version and the tutorials: file structure (my folders don't mimic nesting suggested by the slashes in the app.routes) and the number of filter variables. But, it's too late in the evening for me to continue to troubleshoot.

Hour 10: I don't know if this is good news or bad news, but now my sci-fi archive doesn't work. The app runs (which isn't true for the presidential app), but the database isn't getting accessed, as a query yeilds no jsonified results. Oddly, this is comforting, as at least two apps with nearly identical code almost identically don't work. 


## Week Eleven (4/4 to 4/10)

Overall: This week was split between flask and our software development project. This week was deeply satisfying as I made some breakthroughs and got my presidents web app working. Hooray!

Hour 1: I decided that rather than continue to debug my presidents program, I'd create a second from scratch following the Chirper model we saw in class: starting with the simple API and adding increased functionality. Trying as much as I could not to look, I got tripped up by some mistakes that I'm glad I've seen now (such as using double quotes in an img src tag that was inside double quotes of a return statement). Hopefully, that'll increase my ability to debug my own stuff.

Hour 2: Was really happy about the refresher on template use, as inheritance makes instantiating new pages so much more efficient. Was also really happy working with the list of dictionaries (president entries). Even though I know that the approach isn't robust (and that a SQL database will be the way to go), it allowed me to play with jinja syntax, as I created not only the for loop that ran through the dictionaries, but also conditionals such as the use of the singular "term" if the president served only one term. I also got to play with embedding html in and around the jinja syntax, since i wanted each president to get his own paragraph on the home page. Of course, throughout, I continued to make rookie mistakes, like forgetting a percent sign before a curly bracket or forgetting a comma in my dictionary list.

Hour 3: Spent hour three trying to make step 5 (working with database data) work. I was unsuccessful, despite doing some significant troubleshooting, including checking the schema's of your Chirper database against the schema of my presidents database. VICTORY IS MINE!!!!!!! I'm so fricking proud. I had two problems. First, I forgot that the key words in my practice dictionary did not match the terms in my sql database. So, I changed my sql script to generate a table with the terms that matched my jinja code (such as presidents.wife or presidents.terms). Then, though the colorcoding in Visual Studio did not indicate it, an error message had me hunting for why my new sql file was generating errors, and it turns out that first, last, and order are all special coding terms. So, I changed those to firstname, lastname, and o (I was tired on that last one since I hunted for it for a really long time), et voila! It worked beautifully! Pumped, I am ready to move on.

Hour 4: With the adreneline rush of hour 3, I dove headlong into using the Chirper model to add blog functionality to my president database. I started to create a separate database to handle the posts, but realized that I could simply add a table to my presidents database, so that in the future, if I wanted to search for posts connected to certain presidents, I could create a joining table. (Well, I'd need to add a line on the form to reference a president or search the database for the presidents, but I'm getting ahead of myself.) Had to tweak the Chirper code, as VS didn't like time or post as column names. Successfully created a blog section and posted two posts (one from me and one from Bob Costas). Hooray! 

Hour 5: Successfully finished step 7 -- adding bootstrap to my presidential database and blog. I'll admit, I mostly just copied and adapted rather than coding line for line. I'm eager to improve it, creating a sign-up page with a users table in my database. I'd also like to fix the way the text box appears on the posting page and create a title box. 

Hour 6: I turned to our software development project, reviewing the guest speakers' presentation, getting the ball rolling, creating a company name and logo, and doing some early research on ways to link computers without internet access. Quinn and I broke Sabina's proposal into big-picture questions to prepare for the interview.

Hour 7: Interviewed Sabina with Quinn. The method was super informative, as it turns out that what Sabina thought she wanted isn't really what she wants. 

Hour 8: Quinn and I laid out our next steps divvying up the work. She created a great wireframe using an online service called Freehand. I did research on the emotions generated by colors and web-friendly palettes that both will address some accessibility issues (from color blindness to low-res screens) and should elicit the emotions Sabina wants her students to have--a sense of safety as well as possibility. 

Hour 9: Continued research into web design and learned a ton. My favorite was the line "scrolling is a conversation, clicking is a decision." Helped me give good feedback on Quinn's wireframe--we are simplifying and flattening the heirarchy. 

Hour 10: Reviewed Quinn's wireframe revisions and am eager to hear Sabina's thoughts this weekend. Continued my research on accessibility. This was not a full hour.


## Week Twelve (4/11 to 4/17)

Overall: This week was devoted to targeting my exploration and practice toward my software project, though I did practice my SQL skills to keep them sharp. I am finding that, as I work on my software project, I am beginning to conceptualize well--imagining which tools we've learned so far that will work and won't work. But, I'm also finding that I am overthinking the content of the project rather than focusing on MVP functionality.

Hour 1: Scoured the web for HTML emulators and used the inspect element to deconstruct w3school's version so I could begin to imagine what creating such an emulator might do for our software project. With Sabina's choice of web palette, I was able to start to put together background/text combos that would stay WCAG AAA compliant--a goal of mine.

Hour 2: Took a break from the project to practice SQL using the DHRI tutorial you provided. LOVED hooking up the NYPL's csv data to a SQL database. Got a little overwhelmed thinking about tidying data.

Hour 3: Returned to the software project to review Quinn's wireframe edits and make more suggestions. Also broke down our work from this week into a script through which to walk Sabina. Worked to define two layers of the project--one that can exist purely on a USB stick with minimal features and one that could work if certain factors are in place.

Hours 4 and 5: Videoconferenced with Sabina and Quinn to review the wireframe, get feedback, and discuss next steps. Stayed on with Quinn to divvy up this week's workload, then collected images for the library component of the website.

Hour 6: Began coding the CSS for the gallery. Adapting code from w3schools to keep the design responsive, since we have no idea at this point what hardware Sabina's students will be using. Already 14 pics in, and there's lots of work to do, though the page functionality is pretty good.

Hour 7: Continuing to alter the code. Accidentally learned that cmd+z after pasting code will unindent! Super helpful. Learned that for this particular gallery, the images needed to be all the same aspect ratio, so I thinned the collection. I commented out a few of the deleted images so students to explore. Added teaching text to help students use the site. 

Hour 8: Still customizing the image gallery. I'm learning a lot and rejecting a lot. For example, I made up my own div class for the first time, which I called a vis_block. Ultimately thought it looked bad, both combined with the responsive class and on its own. Also learned html for an emdash, which is satisfying. I'm not terribly pleased with how things look, but the fuctionality is there. I also see that things could be significantly more efficient if we were using Jeckyll, but we had a good reason not to use it: the course this page will be used in is focusing on HTML and CSS, so we wanted to model the tools.

Hour 9: Finished the gallery, and got to play around with horizontal nav bar CSS. Realized that my current structure wasn't scalable, so created a second gallery to figure out how I might best streamline. Downloaded additional royalty/credit-free images for a new "people" gallery, in addition to the NYC one. 

Hour 10: Read w3c


## Week Thirteen (4/18 to 5/1)

Overall: This week was all about html and CSS, and I found that a lot of our early instruction returned to me or at least grounded me to make sense out of the sites I consulted. I was pleased that I could mimic nearly flawlessly Quinn's mock-up illustration of the homepage. CSS is truly a lifesaver, and while I've just used it for two pages, any others of the same type (such as additional image libraries) should be both easy and less error prone. Despite all of these successes, I continue to make some dumb mistakes, like using a colon instead of a semicolon to end a CSS style attribute or like making a link to a file that isn't in the folder my page is in. Just reminds me what a rookie I still am, despite my significantly expanding toolbox! Feel free to visit the site as it is thus far: http://u777316952.hostingerapp.com/Unbarred/

Hour 1: Eager to make the galleries accessible, I reviewed and tried tests from w3c's Accessibility page. Missed some obvious things (I had not included a title in my <head> section), and really struggled to get accustomed to the Voice Over options. I have huge respect for your patience Patrick! Found that my titles were not consistently descriptive, so I altered them.

Hour 2: Eager to modernize the gallery pages, I found a customizable svg background generator and created a few options using Sabina's chosen color palette. Tried to set up some hosting so Quinn (and eventually Sabina) can preview and give feedback. Took awhile. I had an old account at Hostinger which I bought and fumbled with for a project last semester. I think I let something lapse.

Hour 3: Skype call with Quinn to review her homepage protoype and my image galleries. Updated the image galleries (now called image libraries) tbased on our conversation and emailed Sabina with the three pieces to review: our updated wireframe, my image libraries, and Quinn's homepage prototype. I see now why fleshing things out on paper is important: I will have to rename my files and hyperlinks to reflect the changes we are making now.

Hour 4: Per client feedbac, added language to image libraries to indicate that they are, indeed, royalty- and credit-free. Client Skype call to refine design and set next steps, followed by team meeting to decide next steps.

Hour 5: Started coding the homepage HTML and CSS. Sabina's choices (such as separate nav buttons instead of a bar) make this a challenge, but thanks to w3schools, I am able to find and adapt a lot of code. I recreated Quinn's word art to have it sync with the color palatte Sabina chose. I am also learning to come up with creative solutions, for example, creating a separate row for the dang buttons so that I can use margins to space them out.

Hour 6: Loving CSS, as it allows me to change looks quickly without doing a lot of coding. I'm also starting to think through file structure for the webpage--what needs to be in separate folders for easy, scalable change out. Again, the design choices Sabina has made complicate all of this, and I'll need to find a solution for the typewriter font she wants. My background gradients aren't working for the headers and footers, so I'll need to figure that out in Hour 7.

Hour 7: Played around with Adobe Illustrator to learn how to make the gradient graphics, then added them to the style sheet as the header and footer backgrounds.

Hour 8: Worked on the final column of the homepage with the vertical nav bar that takes students to the syllabus, readings, and lessons. Very satisfying to be able to manipulate backgrounds, padding, and margins to make the element seem complete and well designed. While I'm not fond of the look of the design, I am pleased that I've been able to duplicate nearly flawlessly the mock-up Quinn provided that Sabina loved.

Hour 9: Per Sabina's request, I applied the CSS stylesheet of the homepage to the image libraries (which broke my heart a bit, since I loved the original design and the new one doesn't match my aesthetic). Had to reorganize the file structure so that the stylesheet and main pages all lived in the same folder, which required updating the photos with relative links that pointed to the image folder for that category. Painstaking.

Hour 10: Uploaded the site and wrote to Quinn for feedback. My folder structure on Hostinger didn't match the rearranged folder structure on my laptop, so it took lots of fixing relative links and reloading. We were forced to stick with html and CSS because the site has to work with no internet and because Sabina wants the students to be able to decode the code. But, I am truly understanding the genius of Jeckyll and Bootstrap, since we could go so far so fast with content holders and templates! Dang you prison!


## Week Fourteen (5/1 to 5/8)

Overall: This week was devoted to finishing my software project and exploring some of the list comprehension techniques we explored in class during our penultimate meeting.

Hour 1: Attended to Sabina's most recent requests: coding our About Us page, making changes to the home page buttons, editing the text on the Access and Safety page. Uploaded the finished work to the live site on Hostinger and, of course, found little things I had to change, such as the dash Sabina had included in her profile.

Hour 2: Tried a list comprehension video tutorial from Real Python. 

Hour 3: Skype call with Sabina and Quinn to review new additions.

Hour 4: Created About Us page with Quinn's avatars. Working with homemade graphics was more challenging than I'd imagined, because the files needed to
be resized and the resolution needed to be altered. With a self-imposed deadline of Wednesday for delivering the project to Sabina on Wednesday on a USB, I found myself MacGuyvering some code to make things look right. (For example, in order to get a div class container to recognize the end of 
content, I had to place an invisible a after the ending div tag.) I also messed around with our CSS, creating a new class called "main" and futzing
with margins and padding. The design, outside of the galleries, is not 100% responsive. I'll clean up all of these work-arounds later in the summer, but I can really see my inexperience shining through in moments like these. 

Hour 5: Proofed the site to fix the many inconsistencies, such as button links and subtitles. Also replaced characters that HTML doesn't recognize as
we've pasted Sabina's text into Visual Studio Code. Read an interesting debate on whether to use names or numbers for these special characters. 

Hour 6: Uploaded the myriad new and fixed pages to Hostinger. Exciting to see the site grow.

Hour 7: Tested the site on two ten-year-old laptops--a 2009 Toshiba Portege and a 2009 iBook--all from a USB stick to simulate how Sabina would be uploading the site. Don't laugh that this took long. It took quite a long time for each laptop to boot up, which I had to do twice so that I could record the browser operating systems for Sabina. 








