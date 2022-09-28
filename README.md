# dajana
a programming language with good UX


## My Goal
I wanna design a programming language with good UX. This means a few things :
 - listing a few important use cases
 - reading over pros and cons of multiple langages solution (if any) to those use cases
 - evaluating the UX of those solutions
 - designing my own solution, based on what i learnt (and evaluating it too).
 
I will mostly back my UX evaluation based on this [french resource](https://www.usabilis.com/le-guidage-criteres-ergonomiques-de-bastien-et-scapin/#:~:text=Quatre%20sous%2Dcrit%C3%A8res%20participent%20au,d%C3%A9finition%20de%20l'ergonomie).
which in english translates to this list or criteria (translated on reverso):
1. Guidance
   1. Inducement
   2. Grouping / Distinction between Items
      1. Grouping / Distinction by location
      2. Grouping / Distinction by format
   3. Immediate Feedback
   4. Readability

2. Workload
   1. Brevity
      1. Conciseness
      2. Minimum Actions
   2. Information Density

3. Explicit Control
   1. Explicit Actions
   2. User control

4. Adaptability
   1. Flexibility
   2. Consideration of User Experience

5. Error Management
   1. Protection against Errors
   2. Quality of Error Messages
   3. Correction of Errors

6. Homogeneity / Coherence

7. Meaning of Codes and Denominations

8. Compatibility


I will also mostly back my listing of use cases on my real life experience as a developper, using knowledge managment interview techniques.


## The use case i'm faced with as a web developper, or the things i do and how i go about it

 - add / remove / modify some behavior of the program i'm writing, by adding, removing, modifying code, or adding appropriate libraries
 - try to understand what the code does today, by reading it, running it myself, or asking coworker to explain their codes
 - try to make sure i don't accidentally remove features / reintroduce bugs, by adding automated tests on those features and bugs (the behavior of the program i know i want or don't want), when i work on those bug / features
 - catch bugs, by adding tools such as sentry to collect and display crash reports
 - git
 - ensure everyone (even new hires) could read / understand my code, with minimal interaction on my part, by refactoring my code, meaning, in this order :
   - properly naming variables / functions / objects in a way that explains what they do or don't. Hopefully, this means when someone else tries to understand my code, they can read it, and it's enough. No need to run the code (or the tests), or to ask me what it means.
   - adding comments (even tho it's easy to forget to update those once the feature changes, so they aren't 100% accurate)
   - writing docs (even tho, not everyone always read it or know where to find it)
 - refactor so i can add features / reove bugs in the future
 - allow myself to work and break everything without breaking anything for users
 - try to reduce time and effort needed to do any common and repeatable tasks (install the program, run it, test it, and so on) by scripting those actions.
